from typing import Union
from .handler import Handler
from .pack_manager import Function
from .enums import schedule_mode


def clear(function: Function):
    Handler._cmds.append(f"schedule clear {Handler._translate(function)}")


def add(function: Function, time: Union[str, int], schedule_mode: schedule_mode = None):
    if isinstance(time, int):
        time = f"{time}t"
    elif time[-1] == "m":
        time = f"{int(time[:-1]) * 60}s"
    elif time[-1] == "h":
        time = f"{int(time[:-1]) * 3600}s"

    Handler._cmds.append(f"schedule function {Handler._translate(function)} {Handler._translate(time)} {Handler._translate(schedule_mode)}")
