import json
import math
from typing import Union
from onyx.handler import Handler
from onyx.selector import selector
from onyx.json_string import json_string
from onyx.enums import lib, scoreboard_trait, rendertype


def resetPlayer(name: Union[selector, str]):
    """Resets all scores for a player

    Args:
        name (Union[selector, str]): The player to reset
    """
    Handler._cmds.append(f"scoreboard players reset {Handler._translate(name)}")


def setdisplay(scoreboard_name: Union["Scoreboard", str], location: str = "sidebar"):
    """
    Args:
        scoreboard_name (Union[Scoreboard, str]): The scoreboard name
        location (str, optional): Where the scoreboard should be displayed. Defaults to "sidebar".
    """
    if isinstance(scoreboard_name, Scoreboard):
        scoreboard_name = scoreboard_name.name
    Handler._cmds.append(f"scoreboard objectives setdisplay {Handler._translate(location)} {scoreboard_name}")


def list():
    """Returns the amount of scoreboards
    """
    Handler._cmds.append("scoreboard objectives list")


class Scoreboard:
    """Scoreboard objective object

    Args:
        name (str): The scoreboard name
        create (bool, optional): Whether or not the scoreboard should be created. Defaults to False.
        critera (str, optional): The scoreboard critera. Should only be specified if ``create`` is ``True``. Defaults to ``dummy``.
        display_name (json_string, optional): How the scoreboard should be displayed. Should only be specified if ``create`` is ``True``. Defaults to None.
    """
    def __init__(self, name: str, create: bool = False, critera: str = "dummy", display_name: json_string = None):
        self.name = Handler._translate(name)
        self.create = create
        self.critera = Handler._translate(critera)
        if display_name is None:
            display_name = Handler._translate(name, convert=True)
        self.display_name = Handler._translate(display_name, convert=True)

        if create:
            if self.display_name is None:
                self.display_name = name
            Handler._add_to_init(f"scoreboard objectives add {self.name} {self.critera} {self.display_name}")

    def delete(self):
        """Deletes the scoreboard
        """
        Handler._cmds.append(f"scoreboard objectives remove {self.name}")

    def modify(self, trait: scoreboard_trait, value: Union[json_string, rendertype]):
        """Change the display name or render type
        Args:
            trait (scoreboard_trait): The attribute to change
            value (Union[json_string, rendertype]): The value of the new attribute
        """
        Handler._cmds.append(f"scoreboard objectives modify {self.name} {Handler._translate(trait)} {Handler._translate(value)}")

    def remove_allPlayers(self):
        """Remove all players from a scoreboard
        """
        Handler._cmds.append(f"scoreboard objectives remove {self.name}")
        Handler._cmds.append(f"scoreboard objectives add {self.name} {self.critera} {self.display_name}")

    def player(self, name: Union[selector, str]):
        """
        Args:
            name (Union[selector, str]): The selector/name of the player

        Returns:
            Player: A new player object
        """
        return Player(name, self.name, self.create, self.critera)


class Player:
    def __init__(self, name, scoreboard, created, critera):
        self.name = Handler._translate(name)
        self.scoreboard = scoreboard
        self.is_created = created
        self.scoreboard_critera = critera

    def set(self, value: Union[int, "Player"]):
        """
        Args:
            value (Union[int, Player])
        """
        self._multi_operator("=", value, "set")

    def add(self, value: Union[int, "Player"]):
        """
        Args:
            value (Union[int, Player])
        """
        self._multi_operator("+=", value, "add")

    def subtract(self, value: Union[int, "Player"]):
        """
        Args:
            value (Union[int, Player])
        """
        self._multi_operator("-=", value, "remove")

    def multiply(self, value: Union[int, "Player"]):
        """
        Args:
            value (Union[int, Player])
        """
        self._multi_operator("*=", value)

    def divide(self, value: Union[int, "Player"]):
        """
        Args:
            value (Union[int, Player])
        """
        self._multi_operator("/=", value)

    def modulo(self, value: Union[int, "Player"]):
        """
        Args:
            value (Union[int, Player])
        """
        self._multi_operator("%=", value)

    def set_if_less(self, value: Union[int, "Player"]):
        """Sets the score to the value if the score is lower than the value
        Args:
            value (Union[int, Player])
        """
        self._multi_operator("<", value)

    def set_if_greater(self, value: Union[int, "Player"]):
        """Sets the score to the value if the score is greater than the value
        Args:
            value (Union[int, Player])
        """
        self._multi_operator(">", value)

    def swap(self, value: "Player"):
        """
        Args:
            value (Union[int, Player])
        """
        self._multi_operator("><", value)

    def reset(self):
        """Removes the player from the scoreboard
        """
        Handler._cmds.append(f"scoreboard players reset {self.name} {self.scoreboard}")

    def enable(self):
        """Enables the score to be used in the trigger command
        """
        if self.scoreboard_critera != "trigger" and self.is_created is True:
            Handler._warn(f"'{self.scoreboard}' should have 'trigger' critera")
        Handler._warn(f"scoreboard players enable {self.name} {self.scoreboard}")

    def pow(self, value: Union[int, "Player"]):
        """Raises the score to the exponent value
        Args:
            value (Union[int, Player])
        """
        if value == 2:
            Handler._cmds.append(f"scoreboard players operation {self.name} {self.scoreboard} *= {self.name} {self.scoreboard}")
        else:
            Handler.load_lib(lib.math)
            Handler._cmds.append(f"scoreboard players operation $input onyx.math = {self.name} {self.scoreboard}")
            if isinstance(value, int):
                Handler._cmds.append(f"scoreboard players set $exponent onyx.math {math.floor(value)}")
                if value > 30:
                    Handler._warn("An exponent higher than 30 will overflow")
            else:
                Handler._cmds.append(f"scoreboard players operation $exponent onyx.math = {value.name} {value.scoreboard}")
            Handler._cmds.append(f"function {Handler._datapack_name}:lib/math/pow/main")
            Handler._cmds.append(f"scoreboard players operation {self.name} {self.scoreboard} = $output onyx.math")

    def sin(self, value: Union[int, float] = None):
        """Input is taken to a scale of 1 (automatically scaled to 10). Outputs to a scale of 10,000 (0.0197 => 197).

        Args:
            value (Union[int, float], optional): The value of theta. If unspecified, the current value of the player is assigned to theta. Defaults to None.
        """
        self._multi_trig("sin", value)

    def cos(self, value: Union[int, float] = None):
        """Input is taken to a scale of 1 (automatically scaled to 10). Outputs to a scale of 10,000 (0.0197 => 197).

        Args:
            value (Union[int, float], optional): The value of theta. If unspecified, the current value of the player is assigned to theta. Defaults to None.
        """
        self._multi_trig("cos", value)

    def tan(self, value: Union[int, float] = None):
        """Input is taken to a scale of 1 (automatically scaled to 10). Outputs to a scale of 1 (1.0105 => 1).

        Args:
            value (Union[int, float], optional): The value of theta. If unspecified, the current value of the player is assigned to theta. Defaults to None.
        """
        self._multi_trig("tan", value)

    def asin(self, value: Union[int, float] = None):
        """Input is taken to a scale of 1 (automatically scaled to 10). Outputs to a scale of 1000 (-0.021 => -21)

        Args:
            value (Union[int, float], optional): The value of theta. Must be between -1 and 1. If unspecified, the current value of the player is assigned to theta. If the current value of the player is not between -1 and 1, the output will be set to the previous successful operation. Defaults to None.
        """
        self._multi_trig("asin", value, inverse=True)

    def acos(self, value: Union[int, float] = None):
        """Input is taken to a scale of 1 (automatically scaled to 10). Outputs to a scale of 1000 (-0.021 => -21)

        Args:
            value (Union[int, float], optional): The value of theta. Must be between -1 and 1. If unspecified, the current value of the player is assigned to theta. If the current value of the player is not between -1 and 1, the output will be set to the previous successful operation. Defaults to None.
        """
        self._multi_trig("acos", value, inverse=True)

    def atan(self, value: Union[int, float] = None):
        """Input is taken to a scale of 1 (automatically scaled to 10). Outputs to a scale of 1000 (-0.021 => -21)

        Args:
            value (Union[int, float], optional): The value of theta. Must be between -1 and 1. If unspecified, the current value of the player is assigned to theta. If the current value of the player is not between -1 and 1, the output will be set to the previous successful operation. Defaults to None.
        """
        self._multi_trig("atan", value, inverse=True)

    def sqrt(self, value: int = None):
        """Outputs to a precision of 1 decimal place.

        Args:
            value (int, optional): The value to take the square root of. May break with very large values. Defaults to None.
        """
        Handler.load_lib(lib.math)

        if value is not None:
            value = math.floor(value)
            Handler._cmds.append(f"scoreboard players set $input onyx.math {value}")
        else:
            Handler._cmds.append(f"scoreboard players operation $input onyx.math = {self.name} {self.scoreboard}")
        Handler._cmds.append(f"function {Handler._datapack_name}:lib/math/sqrt/main")
        Handler._cmds.append(f"scoreboard players operation {self.name} {self.scoreboard} = $output onyx.math")

    def rand_int(self, lower_bound: int = -2147483648, upper_bound: int = 2147483647):
        """Calculates a random number between the range specified.

        Args:
            lower_bound (int, optional): Defaults to -2147483648.
            upper_bound (int, optional): Defaults to 2147483647.
        """
        Handler.load_lib(lib.rng)

        if lower_bound == upper_bound:
            Handler._cmds.append(f"scoreboard players set {self.name} {self.scoreboard} {upper_bound}")
        else:
            lower_bound = math.floor(lower_bound)
            Handler._cmds.append(f"scoreboard players set $min onyx.rng {max(lower_bound, -2147483648)}")

            upper_bound = math.floor(upper_bound)
            Handler._cmds.append(f"scoreboard players set $max onyx.rng {min(upper_bound, 2147483647)}")

            Handler._cmds.append(f"function {Handler._datapack_name}:lib/rng/main")
            Handler._cmds.append(f"scoreboard players operation {self.name} {self.scoreboard} = $output onyx.rng")

    def NOT(self, value: Union[int, "Player"]):
        """
        Args:
            value (Union[int, Player]): The value to operaton on. If unspecified, the current value of the player is operated on.
        """
        Handler.load_lib(lib.bitwise)

        if isinstance(value, Player):
            Handler._cmds.append(f"scoreboard players operation $input_1 onyx.bitwise = {self.name} {self.scoreboard}")
        else:
            Handler._cmds.append(f"scoreboard players set $input_1 onyx.bitwise {value}")
        Handler._cmds.append(f"function {Handler._datapack_name}:lib/bitwise/not/main")
        Handler._cmds.append(f"scoreboard players operation {self.name} {self.scoreboard} = $output onyx.bitwise")

    def AND(self, value_1: Union[int, "Player"], value_2: int = None):
        """
        Args:
            value_1 (Union[int, Player]): The first value to operate on
            value_2 (int, optional): If unspecified, the value of ``value_1`` is moved to ``value_2``, and the value of the current player is assigned to ``value_1``. Defaults to None.
        """
        self._multi_bitwise("and", value_1, value_2)

    def OR(self, value_1: Union[int, "Player"], value_2: int = None):
        """
        Args:
            value_1 (Union[int, Player]): The first value to operate on
            value_2 (int, optional): If unspecified, the value of ``value_1`` is moved to ``value_2``, and the value of the current player is assigned to ``value_1``. Defaults to None.
        """
        self._multi_bitwise("or", value_1, value_2)

    def XOR(self, value_1: Union[int, "Player"], value_2: int = None):
        """
        Args:
            value_1 (Union[int, Player]): The first value to operate on
            value_2 (int, optional): If unspecified, the value of ``value_1`` is moved to ``value_2``, and the value of the current player is assigned to ``value_1``. Defaults to None.
        """
        self._multi_bitwise("xor", value_1, value_2)

    def LEFT_SHIFT(self, value_1: Union[int, "Player"], value_2: int = None):
        """
        Args:
            value_1 (Union[int, Player]): The value to shift.
            value_2 (int, optional): The amount of bits to shift by. If unspecified, the value of ``value_1`` is moved to ``value_2``, and the value of the current player is assigned to ``value_1``. Defaults to None.
        """
        self._multi_bitwise("left_shift", value_1, value_2)

    def RIGHT_SHIFT(self, value_1: Union[int, "Player"], value_2: int = None):
        """
        Args:
            value_1 (Union[int, Player]): The value to shift.
            value_2 (int, optional): The amount of bits to shift by. If unspecified, the value of ``value_1`` is moved to ``value_2``, and the value of the current player is assigned to ``value_1``. Defaults to None.
        """
        self._multi_bitwise("right_shift", value_1, value_2)

    def _multi_operator(self, operator, value, operator_name=None):
        # Ignore the flooring if the value passed isn't an integer
        if not isinstance(value, Player):
            value = math.floor(value)

        if operator in {"=", "+=", "-="}:
            if isinstance(value, Player):
                Handler._cmds.append(f"scoreboard players operation {self.name} {self.scoreboard} {operator} {value.name} {value.scoreboard}")
            else:
                Handler._cmds.append(f"scoreboard players {operator_name} {self.name} {self.scoreboard} {value}")
        elif operator in {"*=", "/=", "%=", "<", ">"}:
            if isinstance(value, Player):
                Handler._cmds.append(f"scoreboard players operation {self.name} {self.scoreboard} {operator} {value.name} {value.scoreboard}")
            else:
                Handler._add_scoreboard("onyx.const")
                Handler._add_to_init(f"scoreboard players set {value} onyx.const {value}")
                Handler._cmds.append(f"scoreboard players operation {self.name} {self.scoreboard} {operator} {value} onyx.const")
        elif operator == "><":
            Handler._cmds.append(f"scoreboard players operation {self.name} {self.scoreboard} >< {value.name} {value.scoreboard}")

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
        # Ignore the flooring if the value passed isn't an integer
        if not isinstance(value_1, Player):
            value_1 = math.floor(value_1)
        if not isinstance(value_2, Player):
            value_2 = math.floor(value_2)

        Handler.load_lib(lib.bitwise)

        if value_2 is None:
            Handler._cmds.append(f"scoreboard players operation $input_1 onyx.bitwise = {self.name} {self.scoreboard}")
            Handler._cmds.append(f"scoreboard players set $input_2 onyx.bitwise {value_1}")
        else:
            Handler._cmds.append(f"scoreboard players set $input_1 onyx.bitwise {value_1}")
            Handler._cmds.append(f"scoreboard players set $input_2 onyx.bitwise {value_2}")

        Handler._cmds.append(f"function {Handler._datapack_name}:lib/bitwise/{operator_name}/main")
        Handler._cmds.append(f"scoreboard players operation {self.name} {self.scoreboard} = $output onyx.bitwise")
