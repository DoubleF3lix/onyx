from typing import Union

from onyx.commands import Commands
from onyx.dev_util import (add_scoreboard, convert_scoreboard_player_name,
                           translate)
from onyx.pack_manager import Stringable
from onyx.registries import (scoreboard_display, scoreboard_render_type,
                             scoreboard_trait)
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

        from onyx.scoreboard import Player
        # Overload an operator for swap
        Player.__ior__ = Player.swap

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
        self.name = name

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

    def set(self, value: int, init: bool = False) -> "Player":
        """
        set - Sets the value of the scoreboard player

        Args:
            value (int): The value to set
            init (bool, optional): Whether or not this command should be put in the init function. Defaults to ``False``.

        Returns:
            str: Command
        """
        if init:
            return Commands.push(
                f"scoreboard players set {self.name} {self.parent.name} {value}",
                init=True,
            )
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


class Scoreboard(Stringable):
    """
    Scoreboard - Represents a scoreboard objective.

    Args:
        name (str): The name of the scoreboard
        create (bool, optional): Whether or not the scoreboard should be created. Defaults to False.
        criteria (str, optional): The criteria of the scoreboard. Only used if ``create`` is ``True``. Defaults to "dummy".
        display_name (TextComponent, optional): The display name of the scoreboard. Only used if ``create`` is ``True``. Defaults to None.
        players (dict, optional): A dictionary of players to values. Only used if ``create`` is ``True``. Defaults to None.
    """

    def __init__(
        self,
        name: str,
        create: bool = False,
        criteria: str = "dummy",
        display_name: TextComponent = None,
        players: dict = None,
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

        if players:
            for name, value in players.items():
                self.player(name).set(value, init=True)

    def player(self, name: str) -> Player:
        """
        player - Returns a player object representing the given player. See documentation for ``Player`` for more information. If an object with the same name already exists, it will be returned instead.

        Args:
            name (str): The player name. The player name. Automatically converted. A prefix of ``player_`` is interpreted as a plain string. A prefix of `_` is interpreted as a hidden player. Anything else is interpreted as a non-player player. Example: ``player_DoubleF3lix`` => ``DoubleF3lix``, ``_DoubleF3lix`` => ``#DoubleF3lix``, and ``DoubleF3lix`` => ``$DoubleF3lix``.

        Returns:
            Player: A player object representing the given player.
        """
        name = convert_scoreboard_player_name(name)
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
