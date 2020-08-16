import json
import math
from typing import Union
from onyx.handler import Handler
from onyx.selector import selector
from onyx.json_string import json_string
from onyx.enums import lib, scoreboard_trait, rendertype


def reset_player(name: str):
    Handler._cmds.append(f"scoreboard players reset {Handler._translate(name)}")


def setdisplay(name: Union["Scoreboard", str], location: str = "sidebar"):
    if isinstance(name, Scoreboard):
        name = Scoreboard.name
    Handler._cmds.append(f"scoreboard objectives setdisplay {Handler._translate(location)} {name}")


class Scoreboard:
    def __init__(self, name: str, create: bool = False, critera: str = "dummy", display_name: json_string = None):
        self.name = Handler._translate(name)
        self.critera = Handler._translate(critera)
        self.display_name = Handler._translate(display_name, convert=True)

        if create:
            if self.display_name is None:
                self.display_name = name
            Handler._add_to_init(f"scoreboard objectives add {self.name} {self.critera} {self.display_name}")

    def delete(self):
        Handler._cmds.append(f"scoreboard objectives remove {self.name}")

    def modify(self, trait: scoreboard_trait, value: Union[json_string, rendertype]):
        Handler._cmds.append(f"scoreboard objectives modify {self.name} {Handler._translate(trait)} {Handler._translate(value)}")

    def remove_all_players(self):
        Handler._cmds.append(f"scoreboard objectives remove {self.name}")
        Handler._cmds.append(f"scoreboard objectives add {self.name} {self.critera} {self.display_name}")

    def player(self, name: str):
        return _Player(name, self.name)


class _Player:
    def __init__(self, name: selector, scoreboard):
        self.name = Handler._translate(name)
        self.scoreboard = scoreboard

    def set(self, value: Union[int, "_Player"]):
        self._multi_operator("=", value, "set")

    def add(self, value: Union[int, "_Player"]):
        self._multi_operator("+=", value, "add")

    def subtract(self, value: Union[int, "_Player"]):
        self._multi_operator("-=", value, "remove")

    def multiply(self, value: Union[int, "_Player"]):
        self._multi_operator("*=", value)

    def divide(self, value: Union[int, "_Player"]):
        self._multi_operator("/=", value)

    def modulo(self, value: Union[int, "_Player"]):
        self._multi_operator("%=", value)

    def reset(self):
        Handler._cmds.append(f"scoreboard players reset {self.name} {self.scoreboard}")

    def pow(self, value: int):
        if value == 2:
            Handler._cmds.append(f"scoreboard players operation {self.name} {self.scoreboard} *= {self.name} {self.scoreboard}")
        else:
            Handler.load_lib(lib.math)
            Handler._cmds.append(f"scoreboard players operation $input onyx.math = {self.name} {self.scoreboard}")
            Handler._cmds.append(f"scoreboard players set $exponent onyx.math {math.floor(value) - 1}")
            Handler._cmds.append(f"function {Handler._datapack_name}:lib/math/pow/main")
            Handler._cmds.append(f"scoreboard players operation {self.name} {self.scoreboard} = $output onyx.math")

        if value > 30:
            Handler._warn("An exponent higher than 30 will overflow")

    # NOTE Outputs to a scale of 10,000 (0.0197 => 197)
    def sin(self, value: Union[int, float] = None):
        self._multi_trig("sin", value)

    # NOTE Outputs to a scale of 10,000 (0.0197 => 197)
    def cos(self, value: Union[int, float] = None):
        self._multi_trig("cos", value)

    # NOTE Outputs to a scale of 1 (1.0105 => 1)
    def tan(self, value: Union[int, float] = None):
        self._multi_trig("tan", value)

    # NOTE Outputs to a scale of 1000. (-0.001 => -1)
    def asin(self, value: Union[int, float] = None):
        self._multi_trig("asin", value, inverse=True)

    # NOTE Outputs to a scale of 1000. (-0.001 => -1)
    def acos(self, value: Union[int, float] = None):
        self._multi_trig("acos", value, inverse=True)

    # NOTE Outputs to a scale of 1000. (-0.001 => -1)
    def atan(self, value: Union[int, float] = None):
        self._multi_trig("atan", value, inverse=True)

    def sqrt(self, value: int = None):
        Handler.load_lib(lib.math)

        if value is not None:
            value = math.floor(value)
            Handler._cmds.append(f"scoreboard players set $input onyx.math {value}")
        else:
            Handler._cmds.append(f"scoreboard players operation $input onyx.math = {self.name} {self.scoreboard}")
        Handler._cmds.append(f"function {Handler._datapack_name}:lib/math/sqrt/main")
        Handler._cmds.append(f"scoreboard players operation {self.name} {self.scoreboard} = $output onyx.math")

    def rand_int(self, lower_bound: int = None, upper_bound: int = None):
        Handler.load_lib(lib.rng)

        if lower_bound == upper_bound:
            Handler._cmds.append(f"scoreboard players set {self.name} {self.scoreboard} {upper_bound}")
        else:
            if lower_bound is not None:
                lower_bound = math.floor(lower_bound)
                Handler._cmds.append(f"scoreboard players set $min onyx.rng {lower_bound}")
            else:
                Handler._cmds.append("scoreboard players set $min onyx.rng -2147483648")

            if upper_bound is not None:
                upper_bound = math.floor(upper_bound)
                Handler._cmds.append(f"scoreboard players set $max onyx.rng {min(upper_bound, 2147483647)}")
            else:
                Handler._cmds.append("scoreboard players set $max onyx.rng 2147483647")

            Handler._cmds.append(f"function {Handler._datapack_name}:lib/rng/main")
            Handler._cmds.append(f"scoreboard players operation {self.name} {self.scoreboard} = $output onyx.rng")

    def NOT(self, value: int):
        Handler.load_lib(lib.bitwise)

        Handler._cmds.append(f"scoreboard players set $input_1 onyx.bitwise {value}")
        Handler._cmds.append(f"function {Handler._datapack_name}:lib/bitwise/not/main")
        Handler._cmds.append(f"scoreboard players operation {self.name} {self.scoreboard} = $output onyx.bitwise")

    def AND(self, value_1: int, value_2: int = None):
        self._multi_bitwise("and", value_1, value_2)

    def OR(self, value_1: int, value_2: int = None):
        self._multi_bitwise("or", value_1, value_2)

    def XOR(self, value_1: int, value_2: int = None):
        self._multi_bitwise("xor", value_1, value_2)

    def LEFT_SHIFT(self, value_1: int, value_2: int = None):
        self._multi_bitwise("left_shift", value_1, value_2)

    def RIGHT_SHIFT(self, value_1: int, value_2: int = None):
        self._multi_bitwise("right_shift", value_1, value_2)

    def _multi_operator(self, operator, value, operator_name=None):
        value = math.floor(value)
        if operator in {"=", "+=", "-="}:
            if isinstance(value, _Player):
                Handler._cmds.append(f"scoreboard players operation {self.name} {self.scoreboard} {operator} {value.name} {value.scoreboard}")
            else:
                Handler._cmds.append(f"scoreboard players {operator_name} {self.name} {self.scoreboard} {value}")
        elif operator in {"*=", "/=", "%="}:
            if isinstance(value, _Player):
                Handler._cmds.append(f"scoreboard players operation {self.name} {self.scoreboard} {operator} {value.name} {value.scoreboard}")
            else:
                Handler._add_scoreboard("onyx.const")
                Handler._add_to_init(f"scoreboard players set {value} onyx.const {value}")
                Handler._cmds.append(f"scoreboard players operation {self.name} {self.scoreboard} {operator} {value} onyx.const")

    def _multi_trig(self, trig_func, value, inverse=False):
        if inverse:
            if value > 1 or value < -1:
                raise ValueError("'value' must be between -1 and 1")

        Handler.load_lib(lib.math)

        if value is not None:
            Handler._cmds.append(f"scoreboard players set $input onyx.math {math.floor(value * 10)}")
        else:
            Handler._cmds.append(f"scoreboard players operation $input onyx.math = {self.name} {self.scoreboard}")
        Handler._cmds.append(f"function {Handler._datapack_name}:lib/math/{trig_func}/main")
        Handler._cmds.append(f"scoreboard players operation {self.name} {self.scoreboard} = $output onyx.math")

    def _multi_bitwise(self, operator_name, value_1, value_2):
        Handler.load_lib(lib.bitwise)

        if value_2 is None:
            Handler._cmds.append(f"scoreboard players operation $input_1 onyx.bitwise = {self.name} {self.scoreboard}")
            Handler._cmds.append(f"scoreboard players set $input_2 onyx.bitwise {value_1}")
        else:
            Handler._cmds.append(f"scoreboard players set $input_1 onyx.bitwise {value_1}")
            Handler._cmds.append(f"scoreboard players set $input_2 onyx.bitwise {value_2}")

        Handler._cmds.append(f"function {Handler._datapack_name}:lib/bitwise/{operator_name}/main")
        Handler._cmds.append(f"scoreboard players operation {self.name} {self.scoreboard} = $output onyx.bitwise")
