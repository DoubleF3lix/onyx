<<<<<<< Updated upstream
import enum
from typing import Union
from .selector import selector
from .enums import bossbar_trait as trait_enum, style as style_enum, color as color_enum
from .json_string import json_string
from .handler import Handler


def create(id: str, bossbar_name: json_string):
    """Creates a bossbar

    Args:
        id (str): The bossbar ID.
        bossbar_name (json_string): The name of the bossbar.
    """
    Handler._cmds.append(f"bossbar add {Handler._translate(id)} {Handler._translate(bossbar_name, convert=True)}")


def delete(id: str):
    """Deletes a bossbar

    Args:
        id (str): The ID of the bossbar to delete.
    """
    Handler._cmds.append(f"bossbar remove {Handler._translate(id)}")


def get_trait(id: str, attribute: trait_enum = trait_enum.value):
    """Gets a bossbar element

    Args:
        id (str): The ID of the bossbar containing the desired element.
        attribute (trait_enum, optional): The attribute to get. Defaults to trait.value.
    """
    if isinstance(attribute, enum.Enum) and attribute.name in {"color", "name", "players", "style"}:
        Handler._warn(f"'{attribute.value}' is exclusive to 'set_trait'")
    Handler._cmds.append(f"bossbar get {Handler._translate(id)} {Handler._translate(attribute)}")


def set_trait(id: str, color: Union[color_enum, str] = None, max: int = None, name: json_string = None,
              players: selector = None, style: style_enum = None, value: int = None, visible: bool = None):
    """Sets a trait(s) of the specified bossbar

    Args:
        id (str): The ID of the bossbar of the modified attribute.
        color (Union[color_enum, str], optional): The bossbar color. Defaults to None.
        max (int, optional): The maximum value of the bossbar. Defaults to None.
        name (json_string, optional): The bossbar name. Defaults to None.
        players (selector, optional): The players the bossbar is visible to. Defaults to None.
        style (style_enum, optional): The style of the bossbar. Defaults to None.
        value (int, optional): The value of the bossbar (how 'full' it is). Defaults to None.
        visible (bool, optional): Whether or not the bossbar is visible. Defaults to None.
    """
    if color is not None:
        if isinstance(color, enum.Enum) and color.value not in {"blue", "green", "pink", "purple", "yellow", "white"}:
            Handler._warn(f"'color' was set to an invalid color: {color.value}")
        Handler._cmds.append(f"bossbar set {Handler._translate(id)} color {Handler._translate(color)}")

    if max is not None:
        Handler._cmds.append(f"bossbar set {Handler._translate(id)} max {Handler._translate(max)}")

    if name is not None:
        Handler._cmds.append(f"bossbar set minecraft:{Handler._translate(id)} name {Handler._translate(name, convert=True)}")

    if players is not None:
        Handler._cmds.append(f"bossbar set minecraft:{Handler._translate(id)} players {Handler._translate(players)}")

    if style is not None:
        Handler._cmds.append(f"bossbar set minecraft:{Handler._translate(id)} style {Handler._translate(style)}")

    if value is not None:
        Handler._cmds.append(f"bossbar set minecraft:{Handler._translate(id)} value {Handler._translate(value)}")

    if visible is not None:
        Handler._cmds.append(f"bossbar set minecraft:{Handler._translate(id)} max {Handler._translate(visible)}")
=======
from onyx.class_types import Stringable
from onyx.commands import Commands
from onyx.dev_util import translate
from onyx.registries import bossbar_color, bossbar_query, bossbar_style
from onyx.selector import Selector
from onyx.text_component import TextComponent


class Bossbar(Stringable):
    """
    Bossbar - An object representing a bossbar

    Args:
        id (str): The ID of the bossbar
        display_name (TextComponent, optional): The display name of the bossbar. Defaults to None.
        create (bool, optional): Whether or not the bossbar should be created on initalization. Defaults to False.
    """

    def __init__(
        self, id: str, display_name: TextComponent = None, create: bool = False
    ) -> None:
        self.id = (
            f"minecraft:{translate(id)}" if ":" not in translate(id) else translate(id)
        )
        self.display_name = translate(display_name) if display_name else f'"{id}"'

        if create:
            Commands.push(f"bossbar add {self.id} {self.display_name}", init=True)

    def __str__(self) -> str:
        """
        __str__ - Returns the bossbar ID

        Returns:
            str: The ID of the bossbar
        """
        return self.id

    def get(self, query_type: bossbar_query) -> str:
        """
        get - Gets an attribute of the bossbar

        Args:
            query_type (bossbar_query): What attribute of the bossbar to get

        Returns:
            str: Command
        """
        return Commands.push(f"bossbar get {self.id} {translate(query_type)}")

    def remove(self) -> str:
        """
        remove - Deletes the bossbar

        Returns:
            str: Command
        """
        return Commands.push(f"bossbar remove {self.id}")

    def set_color(self, color: bossbar_color) -> str:
        """
        set_color - Set the color attribute of the bossbar

        Args:
            color (bossbar_color): The new color of the bossbar

        Returns:
            str: Command
        """
        return Commands.push(f"bossbar set {self.id} color {translate(color)}")

    def set_max_value(self, value: int) -> str:
        """
        set_max_value - Sets the max value attribute of the bossbar

        Args:
            value (int): The new max value of the bossbar

        Returns:
            str: Command
        """
        return Commands.push(f"bossbar set {self.id} max {translate(value)}")

    def set_name(self, display_name: TextComponent) -> str:
        """
        set_name - Sets the display name (the text at the top) of the bossbar

        Args:
            display_name (TextComponent): The new display name of the bossbar

        Returns:
            str: Command
        """
        return Commands.push(f"bossbar set {self.id} name {translate(display_name)}")

    def set_players(self, players: Selector) -> str:
        """
        set_players - Sets the players the bossbar is shown to

        Args:
            players (Selector): The players the bossbar is visible to

        Returns:
            str: Command
        """
        return Commands.push(f"bossbar set {self.id} players {translate(players)}")

    def set_style(self, style: bossbar_style) -> str:
        """
        set_style - Sets the style of the the bossbar

        Args:
            style (bossbar_style): The new style of the bossbar

        Returns:
            str: Command
        """
        return Commands.push(f"bossbar set {self.id} style {translate(style)}")

    def set_value(self, value: int) -> str:
        """
        set_value - Sets the value (how filled) of the bossbar

        Args:
            value (int): The new value

        Returns:
            str: Command
        """
        return Commands.push(f"bossbar set {self.id} value {translate(value)}")

    def __imatmul__(self, value: int) -> str:
        """
        __imatmul__ - Alias of set_value

        Args:
            value (int): The new value

        Returns:
            str: Command
        """
        return self.set_value(value)

    def set_visibility(self, visibility: bool) -> str:
        """
        set_visibility - Sets whether or not the bossbar can be seen at all

        Args:
            visibility (bool): Whether or not the bossbar is visible

        Returns:
            str: Command
        """
        return Commands.push(
            f"bossbar set {self.id} visible {translate(visibility, normalize_boolean=True)}"
        )
>>>>>>> Stashed changes
