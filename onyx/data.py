from typing import Union
from .handler import Handler, _position
from .enums import data_operator
from .selector import selector
from .util import AbsPos, RelPos, LocPos, CurrentPos


def get(target: Union[str, AbsPos, RelPos, LocPos, CurrentPos, selector], path: str = None, scale: Union[float, int] = None):
    """Get data from the target specified

    Args:
        target (Union[str, AbsPos, RelPos, LocPos, CurrentPos, selector]): The target(s) to get the data from.
        path (str, optional): The data to retrieve. By default, this will get everything. Defaults to None.
        scale (Union[float, int], optional): The scale in which to retrieve the data (With a scale of 0.01, 100 => 1). Defaults to None.
    """
    if isinstance(target, str):
        container_type = "storage"
    if isinstance(target, _position):
        container_type = "block"
    elif isinstance(target, selector):
        container_type = "entity"
    else:
        container_type = "storage"
    Handler._cmds.append(f"data get {Handler._translate(container_type)} {Handler._translate(target)} {Handler._translate(path) or ''} {Handler._translate(scale) or ''}")


def merge(target: Union[str, AbsPos, RelPos, LocPos, CurrentPos, selector], nbt: str):
    """Merge a piece of data with a target

    Args:
        target (Union[str, AbsPos, RelPos, LocPos, CurrentPos, selector]): The target(s) to modify the data of.
        nbt (str): The data to merge.
    """
    if isinstance(target, str):
        container_type = "storage"
    elif isinstance(target, _position):
        container_type = "block"
    elif isinstance(target, selector):
        container_type = "entity"
    else:
        container_type = "storage"

    Handler._cmds.append(f"data merge {Handler._translate(container_type)} {Handler._translate(target)} {Handler._translate(nbt)}")


def modify(target: Union[str, AbsPos, RelPos, LocPos, CurrentPos, selector], path: str, operation: data_operator, data_location: dict):
    """Directly modify a specific element of the target

    Args:
        target (Union[str, AbsPos, RelPos, LocPos, CurrentPos, selector]): The target(s) to modify the data of.
        path (str): The name of the data location that should be modified.
        operation (data_operator): How the data should be modified.
        data_location (dict): The data that should be set.
    """
    if isinstance(target, str):
        container_type = "storage"
    elif isinstance(target, _position):
        container_type = "block"
    elif isinstance(target, selector):
        container_type = "entity"
    else:
        container_type = "storage"

    Handler._cmds.append(f"data modify {Handler._translate(container_type)} {Handler._translate(target)} {Handler._translate(path)} {Handler._translate(operation)} {Handler._translate(data_location)}")


def remove(target: Union[str, AbsPos, RelPos, LocPos, CurrentPos, selector], path: str):
    """Remove a piece of data from the target(s)

    Args:
        target (Union[str, AbsPos, RelPos, LocPos, CurrentPos, selector]): The target(s) to remove the entity from.
        path (str): The piece of data to remove.
    """
    if isinstance(target, str):
        container_type = "storage"
    elif isinstance(target, _position):
        container_type = "block"
    elif isinstance(target, selector):
        container_type = "entity"
    else:
        container_type = "storage"

    Handler._cmds.append(f"data remove {Handler._translate(container_type)} {Handler._translate(target)} {Handler._translate(path)}")
