from typing import Union
from .handler import Handler
from .selector import selector
from .json_string import json_string
from .enums import collision_rule, death_message_visibility, nametag_visibility, team_trait


def create(team_name: str, display_name: json_string = None):
    Handler._cmds.append(f"team add {Handler._translate(team_name)} {Handler._translate(display_name, convert=True)}")


def empty(team_name: str):
    Handler._cmds.append(f"team empty {Handler._translate(team_name)}")


def join(team_name: str, targets: selector):
    Handler._cmds.append(f"team join {Handler._translate(team_name)} {Handler._translate(targets)}")


def leave(targets: selector):
    Handler._cmds.append(f"team leave {Handler._translate(targets)}")


def list():
    Handler._cmds.append("team list")


def modify(team_name: str, attribute: team_trait, value: Union[bool, json_string, collision_rule, death_message_visibility, nametag_visibility]):
    Handler._cmds.append(f"team modify {Handler._translate(team_name)} {Handler._translate(attribute)} {Handler._translate(value)}")


def delete(team_name: str):
    Handler._cmds.append(f"team remove {Handler._translate(team_name)}")
