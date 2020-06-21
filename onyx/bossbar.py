import enum
from typing import Union
from .handler import Handler
from .selector import Selector
from .enum import trait as trait_enum, style as style_enum, color as color_enum
from .json_string import json_string


# "id" has strange highlighting, so I used "bossbar_id"
# "name" was changed for consistency
def create(bossbar_id: str, bossbar_name: json_string):
    """create - Creates a bossbar.
    Args:
        bossbar_id (str): The bossbar ID.
        bossbar_name (json_string): The name of the bossbar. Must be a json_string.

    Raises:
        ValueError: Raised if the name is not a json_string object

    Returns:
        str: The command to be written.
    """
    if not isinstance(bossbar_name, json_string):
        raise ValueError("'bossbar_name' must be a json_string object")
    Handler._write(f"bossbar add {bossbar_id} {bossbar_name.output}")
    return f"bossbar add {bossbar_id} {bossbar_name.output}"


def delete(bossbar_id: str):
    """delete - Deletes a bossbar.

    Args:
        bossbar_id (str): The ID of the bossbar to delete.

    Returns:
        str: The command to be written.
    """
    Handler._write(f"bossbar remove {bossbar_id}")
    return f"bossbar remove {bossbar_id}"


def list():
    """list - Lists all the bossbars. Only useful with 'execute store'

    Returns:
        str: The command to be written.
    """
    Handler._write("bossbar list")
    return "bossbar list"


# "property" has weird highlighting, so I used "attribute" instead
def get_trait(bossbar_id: str, attribute: trait_enum = trait_enum.progress):
    """get_trait - Gets a bossbar element

    Args:
        bossbar_id (str): The ID of the bossbar containing the desired element.
        attribute (trait_enum, optional): The attribute to get. Must be an enum. Defaults to trait.progress.

    Raises:
        ValueError: Raised when the specified attribute is set to a "set_trait()" exclusive attribute.

    Returns:
        str: The command to be written.
    """
    if attribute.name in {"color", "name", "players", "style"}:
        raise ValueError(f"'{attribute.name}' is exclusive to 'set_trait'")
    Handler._write(f"bossbar get {bossbar_id} {attribute.value}")
    return f"bossbar get {bossbar_id} {attribute.value}"


def set_trait(bossbar_id: str, color: Union[color_enum, str] = None, max: int = None, name: json_string = None,
              players: Selector = None, style: style_enum = None, value: int = None, visible: bool = None):
    """set_trait - Sets a trait(s) of the bossbar

    Args:
        bossbar_id (str): The ID of the bossbar of the modified attribute.
        color (Union[color_enum, str], optional): The bossbar color. Defaults to None.
        max (int, optional): The maximum value of the bossbar. Defaults to None.
        name (json_string, optional): The bossbar name. Must be a json_string object. Defaults to None.
        players (Selector, optional): The players the bossbar is visible to. Must be a selector object. Defaults to None.
        style (style_enum, optional): The style of the bossbar. Defaults to None.
        value (int, optional): The value of the bossbar (how 'full' it is). Defaults to None.
        visible (bool, optional): Whether or not the bossbar is visible. Defaults to None.

    Raises:
        ValueError: Raised if the argument isn't the right type.

    Returns:
        list: The commands to be written.
    """
    cmds = []
    # Iterate through each of the default arguments
    # (required arguments won't fail since they behave like default arguments)
    for key, arg in locals().items():
        # Filter out the args that were not assigned
        if arg is not None:
            if key == "color":
                # Check if the provided color is supported by bossbars
                if isinstance(key, enum.Enum):
                    if arg.value not in {"blue", "green", "pink", "purple", "yellow", "white"}:
                        raise ValueError(f"Unknown value for 'color': {arg} (Did you set it to an incompatible color?")
                    Handler._write(f"bossbar set minecraft:{bossbar_id} color {arg.value}")
                    cmds.append(f"bossbar set minecraft:{bossbar_id} color {arg.value}")
                elif isinstance(key, str):
                    Handler._write(f"bossbar set minecraft:{bossbar_id} color {arg}")
                    cmds.append(f"bossbar set minecraft:{bossbar_id} color {arg}")
            elif key == "max":
                if not isinstance(arg, int):
                    raise ValueError("'max' must be an int")
                Handler._write(f"bossbar set {bossbar_id} max {arg}")
                cmds.append(f"bossbar set {bossbar_id} max {arg}")
            elif key == "name":
                if not isinstance(arg, json_string):
                    raise ValueError("'name' must be a json_string object")
                Handler._write(f"bossbar set minecraft:{bossbar_id} name {arg.output}")
                cmds.append(f"bossbar set minecraft:{bossbar_id} name {arg.output}")
            elif key == "players":
                if not isinstance(arg, Selector):
                    raise ValueError("'players' must be a selector object")
                Handler._write(f"bossbar set minecraft:{bossbar_id} players {arg.build()}")
                cmds.append(f"bossbar set minecraft:{bossbar_id} players {arg.build()}")
            elif key == "style":
                Handler._write(f"bossbar set minecraft:{bossbar_id} style {arg.value}")
                cmds.append(f"bossbar set minecraft:{bossbar_id} style {arg.value}")
            elif key == "value":
                if not isinstance(arg, int):
                    raise ValueError("'value' must be an int")
                Handler._write(f"bossbar set minecraft:{bossbar_id} value {arg}")
                cmds.append(f"bossbar set minecraft:{bossbar_id} value {arg}")
            elif key == "visible":
                if not isinstance(arg, bool):
                    raise ValueError("'visible' must be True or False")
                # str(arg).lower() is used to turn it from "True" to "true" or "False" to "false"
                Handler._write(f"bossbar set minecraft:{bossbar_id} max {str(arg).lower()}")
                cmds.append(f"bossbar set minecraft:{bossbar_id} max {str(arg).lower()}")
    return cmds
