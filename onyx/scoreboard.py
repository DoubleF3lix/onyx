<<<<<<< Updated upstream
import json
import math
from typing import Union
from onyx.handler import Handler
from onyx.selector import selector
from onyx.json_string import json_string
from onyx.enums import lib, scoreboard_trait, rendertype
=======
from typing import Union

from onyx.commands import Commands
from onyx.dev_util import add_scoreboard, convert_scoreboard_player_name, translate
from onyx.pack_manager import Stringable
from onyx.registries import scoreboard_display, scoreboard_render_type, scoreboard_trait
from onyx.text_component import TextComponent
from onyx.util import Range


class Expression(Stringable):
    """
    Expression - Represents a scoreboard check expression used for ``execute if/unless``. Do not create manually. Use the expression operators on a ``Player`` object instead.

    Args:
        left_side (str): A stringified ``Player`` object
        operator (str): A string containing the operator
        right_side (str): A stringified ``Player`` object

    Notes:
        Any function without an overridden operator can be added by doing the following:
>>>>>>> Stashed changes

        from onyx.scoreboard import Player
        # Overload an operator for swap
        Player.__ior__ = Player.swap

<<<<<<< Updated upstream
def reset_player(name: Union[selector, str]):
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
        self.display_name = display_name

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

    def remove_all_players(self):
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
    """
    """
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
=======
        A full list of potential operators to overload without breaking existing functionality is as follows:

        * ``__ipow__`` (**=)
        * ``__ilshift__`` (<<=)
        * ``__irshift__`` (>>=)
        * ``__iand__`` (&=)
        * ``__ior__`` (|=)
        * ``__ixor__`` (^=)

        This list may change at any time, and this functionality is not supported. Just replace the proper things in the above example and you're good to go.
    """

    def __init__(self, left_side: str, operator: str, right_side: str) -> None:
        self.left_side = left_side
        self.operator = operator
        self.right_side = right_side

    def __str__(self) -> str:
        """
        __str__ - Returns the complete expression

        Returns:
            str: The complete expression
        """
        return f"{self.left_side} {self.operator} {self.right_side}"


class Player(Stringable):
    """
    Player - Represents a player on a scoreboard. Do not create manually. Use the ``Scoreboard.player`` method instead.

    Args:
        parent (Scoreboard): The parent ``Scoreboard`` object
        name (str): The player name. Automatically converted. A prefix of ``player_`` is interpreted as a plain string. A prefix of `_` is interpreted as a hidden player. Anything else is interpreted as a non-player player. Example: ``player_DoubleF3lix`` => ``DoubleF3lix``, ``_DoubleF3lix`` => ``#DoubleF3lix``, and ``DoubleF3lix`` => ``$DoubleF3lix``.
    """

    def __init__(self, parent: "Scoreboard", name: str) -> None:
        self.parent = parent
        self.name = convert_scoreboard_player_name(name)

    def __str__(self) -> str:
        """
        __str__ - Returns the player name followed by the scoreboard name

        Returns:
            str: The player name and the scoreboard name
        """
        return f"{self.name} {self.parent.name}"

    # Operators and their overloaded counterparts
    def __imatmul__(self, value: int) -> "Player":
        """
        __imatmul__ - Alias of ``set``

        Args:
            value (int): The value to set

        Returns:
            str: Command
        """
        return self.set(value)

    def set(self, value: int) -> "Player":
        """
        set - Sets the value of the scoreboard player

        Args:
            value (int): The value to set

        Returns:
            str: Command
        """
        self.parent.operator = "="
        return self.parent.handle_operator(self.name, value)

    def __iadd__(self, value: int) -> "Player":
        """
        __iadd__ - Alias of ``add``

        Returns:
            str: Command
        """
        return self.add(value)

    def add(self, value: int) -> "Player":
        """
        add - Adds the value to the scoreboard player

        Args:
            value (int): The value to add

        Returns:
            str: Command
        """
        self.parent.operator = "+="
        return self.parent.handle_operator(self.name, value)

    def __isub__(self, value: int) -> "Player":
        """
        __isub__ - Alias of ``subtract``

        Args:
            value (int): The value to subtract

        Returns:
            str: Command
        """
        return self.subtract(value)

    def subtract(self, value: int) -> "Player":
        """
        subtract - Subtracts the value from the scoreboard player

        Args:
            value (int): The value to subtract

        Returns:
            str: Command
        """
        self.parent.operator = "-="
        return self.parent.handle_operator(self.name, value)

    def __imul__(self, value: int) -> "Player":
        """
        __imul__ - Alias of ``multiply``

        Args:
            value (int): The value to multiply

        Returns:
            str: Command
        """
        return self.multiply(value)

    def multiply(self, value: int) -> "Player":
        """
        multiply - Multiplies a number or another players score to the scoreboard player. If an integer is specified, a constant player will be created and that will be multiplied.

        Args:
            value (int): The value to multiply

        Returns:
            str: Command
        """
        self.parent.operator = "*="
        return self.parent.handle_operator(self.name, value)

    def __idiv__(self, value: int) -> "Player":
        """
        __idiv__ - Alias of ``divide``

        Args:
            value (int): The value to divide

        Returns:
            str: Command
        """
        return self.divide(value)

    def divide(self, value: int) -> "Player":
        """
        divide - Divides a number or another players score to the scoreboard player. If an integer is specified, a constant player will be created and that will be divided.

        Args:
            value (int): The value to divide

        Returns:
            str: Command
        """
        self.parent.operator = "/="
        return self.parent.handle_operator(self.name, value)

    def __imod__(self, value: int) -> "Player":
        """
        __imod__ - Alias of ``modulo``

        Args:
            value (int): The value to apply a modulo with

        Returns:
            str: Command
        """
        return self.modulo(value)

    def modulo(self, value: int) -> "Player":
        """
        modulo - Applies a modulo a number or another players score to the scoreboard player. If an integer is specified, a constant player will be created and that will have the modulo applied. Essentially, this is ``self % value``.

        Args:
            value (int): The value to apply a modulo with

        Returns:
            str: Command
        """
        self.parent.operator = "%="
        return self.parent.handle_operator(self.name, value)

    def swap(self, value: "Player") -> "Player":
        """
        swap - Swaps the value of the scoreboard player with another player

        Args:
            value (Player): The player to swap with

        Returns:
            str: Command
        """
        self.parent.operator = "><"
        return self.parent.handle_operator(self.name, value)

    def set_if_less(self, value: "Player") -> "Player":
        """
        set_if_less - Sets the scoreboard player to the value if it is less than it

        Args:
            value (Player): The value to compare against and set if it is less

        Returns:
            str: Command
        """
        self.parent.operator = "<"
        return self.parent.handle_operator(self.name, value)

    def set_if_greater(self, value: "Player") -> "Player":
        """
        set_if_greater - Sets the scoreboard player to the value if it is greater than it

        Args:
            value (Player): The value to compare against and set if it is greater

        Returns:
            str: Command
        """
        self.parent.operator = ">"
        return self.parent.handle_operator(self.name, value)

    def enable(self) -> str:
        """
        enable - Enables the scoreboard player for ``trigger``

        Returns:
            str: Command
        """
        return Commands.push(
            f"scoreboard players enable {translate(self.name)} {self.parent.name}"
        )

    def get(self) -> str:
        """
        get - Gets the value of the scoreboard player. Only useful with ``execute store``.

        Returns:
            str: Command
        """
        return Commands.push(
            f"scoreboard players get {translate(self.name)} {self.parent.name}"
        )

    def reset(self) -> str:
        """
        reset - Removes the player from its parent scoreboard

        Returns:
            str: Command
        """
        return Commands.push(
            f"scoreboard players reset {translate(self.name)} {self.parent.name}"
        )

    # Expression operators (for execute)
    def __eq__(self, value: Union["Player", int, Range]) -> Expression:
        """
        __eq__ - Alias of ``if_equal``

        Args:
            value (Union[Player, int, Range]): The value to compare against

        Returns:
            Expression: An expression object representing the comparison
        """
        return self.if_equal(value)

    def if_equal(self, value: Union["Player", int, Range]) -> Expression:
        """
        if_equal - Checks if the scoreboard player is equal to the given player. Used in ``execute if/unless``.

        Args:
            value (Union[Player, int, Range): The scoreboard player or value to compare against

        Returns:
            Expression: An expression object representing the comparison
        """
        if isinstance(value, Player):
            return Expression(str(self), "=", str(value))
        # Handles Range object as well
        else:
            return Expression(str(self), "matches", translate(value))

    def __lt__(self, value: "Player") -> Expression:
        """
        __lt__ - Alias of ``if_less_than``

        Args:
            value (Player): The scoreboard player to compare against. For checking numbers, use ``if_equal`` with a ``Range`` object.

        Returns:
            Expression: An expression object representing the comparison
        """
        return self.if_less_than(value)

    def if_less_than(self, value: "Player") -> Expression:
        """
        if_less_than - Checks if the scoreboard player is less than the given player. Used in ``execute if/unless``.

        Args:
            value (Player): The scoreboard player to compare against. For checking numbers, use ``if_equal`` with a ``Range`` object.

        Returns:
            Expression: An expression object representing the comparison
        """
        return Expression(str(self), "<", str(value))

    def __gt__(self, value: "Player") -> Expression:
        """
        __gt__ - Alias of ``if_greater_than``

        Args:
            value (Player): The scoreboard player to compare against. For checking numbers, use ``if_equal`` with a ``Range`` object.

        Returns:
            Expression: An expression object representing the comparison
        """
        return self.if_greater_than(value)

    def if_greater_than(self, value: "Player") -> Expression:
        """
        if_greater_than - Checks if the scoreboard player is greater than the given player. Used in ``execute if/unless``.

        Args:
            value (Player): The scoreboard player to compare against. For checking numbers, use ``if_equal`` with a ``Range`` object.

        Returns:
            Expression: An expression object representing the comparison
        """
        return Expression(str(self), ">", str(value))

    def __le__(self, value: "Player") -> Expression:
        """
        __le__ - Alias of ``if_less_than_or_equal``

        Args:
            value (Player): The scoreboard player to compare against. For checking numbers, use ``if_equal`` with a ``Range`` object.

        Returns:
            Expression: An expression object representing the comparison
        """
        return self.if_less_than_or_equal(value)

    def if_less_than_or_equal(self, value: "Player") -> Expression:
        """
        if_less_than_or_equal - Checks if the scoreboard player is less than or equal to the given player. Used in ``execute if/unless``.

        Args:
            value (Player): The scoreboard player to compare against. For checking numbers, use ``if_equal`` with a ``Range`` object.

        Returns:
            Expression: An expression object representing the comparison
        """
        return Expression(str(self), "<=", str(value))

    def __ge__(self, value: "Player") -> Expression:
        """
        __ge__ - Alias of ``if_greater_than_or_equal``

        Args:
            value (Player): The scoreboard player to compare against. For checking numbers, use ``if_equal`` with a ``Range`` object.

        Returns:
            Expression: An expression object representing the comparison
        """
        return self.if_greater_than_or_equal(value)

    def if_greater_than_or_equal(self, value: "Player") -> Expression:
        """
        if_greater_than_or_equal - Checks if the scoreboard player is greater than or equal to the given player. Used in ``execute if/unless``.

        Args:
            value (Player): The scoreboard player to compare against. For checking numbers, use ``if_equal`` with a ``Range`` object.

        Returns:
            Expression: An expression object representing the comparison
        """
        return Expression(str(self), ">=", str(value))
>>>>>>> Stashed changes

        Args:
            lower_bound (int, optional): Defaults to -2147483648.
            upper_bound (int, optional): Defaults to 2147483647.
        """
        Handler.load_lib(lib.rng)

<<<<<<< Updated upstream
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
=======
class Scoreboard(Stringable):
    """
    Scoreboard - Represents a scoreboard objective.

    Args:
        name (str): The name of the scoreboard
        create (bool, optional): Whether or not the scoreboard should be created. Defaults to False.
        criteria (str, optional): The criteria of the scoreboard. Only used if ``create`` is ``True``. Defaults to "dummy".
        display_name (TextComponent, optional): The display name of the scoreboard. Only used if ``create`` is ``True``. Defaults to None.
    """

    def __init__(
        self,
        name: str,
        create: bool = False,
        criteria: str = "dummy",
        display_name: TextComponent = None,
    ) -> None:
        self.name = name
        self.criteria = criteria
        self.display_name = translate(display_name)

        if create:
            Commands.push(
                f"scoreboard objectives add {self.name} {self.criteria} {self.display_name}",
                init=True,
            )

        # self.operator is overwritten if anything except "=" is used
        self.operator = "="

        # Used to keep track of existing players to de-dupe stuff
        self.players = {}

    def player(self, name: str) -> Player:
        """
        player - Returns a player object representing the given player. See documentation for ``Player`` for more information. If an object with the same name already exists, it will be returned instead.

        Args:
            name (str): The player name. The player name. Automatically converted. A prefix of ``player_`` is interpreted as a plain string. A prefix of `_` is interpreted as a hidden player. Anything else is interpreted as a non-player player. Example: ``player_DoubleF3lix`` => ``DoubleF3lix``, ``_DoubleF3lix`` => ``#DoubleF3lix``, and ``DoubleF3lix`` => ``$DoubleF3lix``.

        Returns:
            Player: A player object representing the given player.
        """
        if name not in self.players:
            self.players[name] = Player(self, name)
        return self.players[name]

    def __str__(self) -> str:
        """
        __str__ - Returns the scoreboard name

        Returns:
            str: The scoreboard name
        """
        return self.name

    def handle_operator(self, name: str, value: Union[Player, int]) -> str:
        """
        handle_operator - Handles are player operators (except expression)

        Args:
            name (str): The player name
            value (Union[Player, int]): The value passed as the right side of the operator (with the player being the left)

        Raises:
            ValueError: Swap operator was used with a number

        Returns:
            str: Command
        """
        if isinstance(value, int):
            if self.operator in {"=", "+=", "-="}:
                operator_name = {"=": "set", "+=": "add", "-=": "remove"}[self.operator]
                return Commands.push(
                    f"scoreboard players {operator_name} {translate(name)} {self.name} {value}"
                )
            elif self.operator in {"*=", "/=", "%=", "<", ">"}:
                add_scoreboard("onyx.const"),
                Commands.push(
                    f"scoreboard players set ${value} onyx.const {value}", init=True
                ),
                return Commands.push(
                    f"scoreboard players operation {translate(name)} {self.name} {self.operator} ${value} onyx.const"
                )
            elif self.operator == "><":
                raise ValueError("Cannot swap between player score and integer")
        elif self.operator in {"=", "+=", "-=", "*=", "/=", "%=", "<", ">", "><"}:
            return Commands.push(
                f"scoreboard players operation {translate(name)} {self.name} {self.operator} {value.name} {value.parent.name}"
            )

    def delete(self) -> str:
        """
        delete - Deletes the scoreboard objective

        Returns:
            str: Command
        """
        return Commands.push(f"scoreboard objectives remove {self.name}")

    def reset(self) -> str:
        """
        reset - Resets all players on the scoreboard

        Returns:
            str: Command
        """
        return Commands.push(f"scoreboard players reset * {self.name}")

    def setdisplay(self, display: scoreboard_display) -> str:
        """
        setdisplay - Sets this scoreboard on a display

        Args:
            display (scoreboard_display): The display to set this scoreboard on

        Returns:
            str: Command
        """
        return Commands.push(
            f"scoreboard objectives setdisplay {translate(display)} {self.name}"
        )

    def modify(
        self,
        trait: scoreboard_trait,
        value: Union[TextComponent, scoreboard_render_type],
    ) -> str:
        """
        modify - Modifies a scoreboard trait

        Args:
            trait (scoreboard_trait): Either ``display_name`` or ``render_type``
            value (Union[TextComponent, scoreboard_render_type]): The new value of the attribute

        Returns:
            str: Command
        """
        return Commands.push(
            f"scoreboard objectives modify {self.name} {translate(trait)} {translate(value)}"
        )

    def create(self, overwrite: bool = False) -> str:
        """
        create - Creates the scoreboard

        Args:
            overwrite (bool, optional): If ``True``, the scoreboard is deleted and then recreated. Defaults to False.

        Returns:
            str: Command
        """
        if overwrite:
            Commands.push(f"scoreboard objectives remove {self.name}")
        return Commands.push(
            f"scoreboard objectives add {self.name} {self.criteria} {self.display_name}"
        )
>>>>>>> Stashed changes
