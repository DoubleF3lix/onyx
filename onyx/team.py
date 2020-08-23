from typing import Union
from .handler import Handler
from .selector import selector
from .json_string import json_string
from .enums import collision_rule, death_message_visibility, nametag_visibility, team_trait


def create(team_name: str, display_name: json_string = None):
    """
    Args:
        team_name (str): The team name
        display_name (json_string, optional): The display name of the team. If unspecified, the display name is set to the team name. Defaults to None.
    """
    if display_name is None:
        display_name = Handler._translate(team_name, convert=True)
    Handler._cmds.append(f"team add {Handler._translate(team_name)} {Handler._translate(display_name)}")


def empty(team_name: str):
    """
    Args:
        team_name (str): The team to empty
    """
    Handler._cmds.append(f"team empty {Handler._translate(team_name)}")


def join(team_name: str, targets: selector):
    """
    Args:
        team_name (str): The team to be joined
        targets (selector): The players who should join the team
    """
    Handler._cmds.append(f"team join {Handler._translate(team_name)} {Handler._translate(targets)}")


def leave(targets: selector):
    """
    Args:
        targets (selector): The players who should leave their current team
    """
    Handler._cmds.append(f"team leave {Handler._translate(targets)}")


def list():
    """Only useful with "execute store"
    """
    Handler._cmds.append("team list")


def modify(team_name: str, attribute: team_trait, value: Union[bool, json_string, collision_rule, death_message_visibility, nametag_visibility]):
    """
    Args:
        team_name (str): The team to modify
        attribute (team_trait): The attribute to modify
        value (Union[bool, json_string, collision_rule, death_message_visibility, nametag_visibility]): The new value of the attribute
    """
    Handler._cmds.append(f"team modify {Handler._translate(team_name)} {Handler._translate(attribute)} {Handler._translate(value)}")


def delete(team_name: str):
    """
    Args:
        team_name (str): The team to delete
    """
    Handler._cmds.append(f"team remove {Handler._translate(team_name)}")
