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
