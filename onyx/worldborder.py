from typing import Union
from .handler import Handler
from .util import Abs2DPos, Current2DPos
from .enums import border_damage, border_warning


def add(distance: int, time: int = None):
    """
    Args:
        distance (int): The distance to increase the worldborder by
        time (int, optional): How long it should take the worldborder to resize in size in seconds. Defaults to None.
    """
    Handler._cmds.append(f"worldborder add {Handler._translate(distance)} {Handler._translate(time)}")


def set_center(center: Union[Abs2DPos, Current2DPos]):
    """
    Args:
        center (Union[Abs2DPos, Current2DPos]): The center of the worldborder
    """
    Handler._cmds.append(f"worldborder center {Handler._translate(center)}")


def damage(damage_type: border_damage, distance: int):
    """
    Args:
        damage_type (border_damage): (amount, buffer)
        distance (int): How far from the worldborder players should be before they start being damaged
    """
    Handler._cmds.append(f"worldborder damage {Handler._translate(damage_type)} {Handler._cmds.append(distance)}")


def get():
    """Should only be used with ``execute store``
    """
    Handler._cmds.append("worldborder get")


def set(distance, time: int = None):
    """
    Args:
        distance ([type]): The size of the worldborder
        time (int, optional): How long it should take the worldborder to resize. Defaults to None.
    """
    Handler._cmds.append(f"worldborder set {Handler._translate(distance)} {Handler._translate(time)}")


def set_warning(warning_type: border_warning, value: int):
    """
    Args:
        warning_type (border_warning): (distance, time)
        value (int): How many blocks away the player should be to display the warning or how long before the screen tints red if the moving worldborder is at the players position
    """
    Handler._cmds.append(f"worldborder warning {Handler._translate(set_warning)} {Handler._translate(value)}")
