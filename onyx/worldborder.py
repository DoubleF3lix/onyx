from typing import Union
from .handler import Handler
from .util import Abs2DPos, Current2DPos
from .enums import border_damage, border_warning


def add(distance, time: int = None):
    Handler._cmds.append(f"worldborder add {Handler._translate(distance)} {Handler._translate(time)}")


def set_center(center: Union[Abs2DPos, Current2DPos]):
    Handler._cmds.append(f"worldborder center {Handler._translate(center)}")


def damage(damage_type: border_damage, distance: int):
    Handler._cmds.append(f"worldborder damage {Handler._translate(damage_type)} {Handler._cmds.append(distance)}")


def get():
    Handler._cmds.append("worldborder get")


def set(distance, time: int = None):
    Handler._cmds.append(f"worldborder set {Handler._translate(distance)} {Handler._translate(time)}")


def set_warning(warning_type: border_warning, value: int):
    Handler._cmds.append(f"worldborder warning {Handler._translate(set_warning)} {Handler._translate(value)}")
