from typing import Union
from .handler import Handler
from .enum import data_operator
from .selector import Selector


def get(target: Union[str, tuple, Selector], path: str = None, scale: Union[float, int] = None):
    """get - Get data from the target specified

    Args:
        target (Union[str, tuple, Selector]): The target(s) to get the data from.
        path (str, optional): The data to retrieve. By default, this will get everything. Defaults to None.
        scale (Union[float, int], optional): The scale in which to retrieve the data (With a scale of 0.01, 100 => 1). Defaults to None.

    Returns:
        str: The command to be written.
    """
    if isinstance(target, str):
        container_type = "storage"
    if isinstance(target, tuple):
        container_type = "block"
        target = ' '.join(target)
    if isinstance(target, Selector):
        container_type = "entity"
        target = target.build()
    Handler._write(f"data get {container_type} {target} {path or ''} {scale or ''}")
    return f"data get {container_type} {target} {path or ''} {scale or ''}"


def merge(target: Union[str, tuple, Selector], nbt: str):
    """merge - Merge a piece of data with a target.

    Args:
        target (Union[str, tuple, Selector]): The target(s) to modify the data of.
        nbt (str): The data to merge.

    Returns:
        str: The command to be written.
    """
    if isinstance(target, str):
        container_type = "storage"
    if isinstance(target, tuple):
        container_type = "block"
        target = ' '.join(target)
    if isinstance(target, Selector):
        container_type = "entity"
        target = target.build()
    Handler._write(f"data merge {container_type} {target} {nbt}")
    return f"data merge {container_type} {target} {nbt}"


def modify(target: Union[str, tuple, Selector], path: str, operation: data_operator, data_location: dict):
    """modify - Directly modify a specific element of the target.

    Args:
        target (Union[str, tuple, Selector]): The target(s) to modify the data of.
        path (str): The name of the data location that should be modified.
        operation (data_operator): How the data should be modified.
        data_location (dict): The data that should be set.

    Raises:
        ValueError: Raised if the argument isn't the right type.

    Returns:
        str: The command to be written.
    """
    if isinstance(target, str):
        container_type = "storage"
    if isinstance(target, tuple):
        container_type = "block"
        target = ' '.join(target)
    if isinstance(target, Selector):
        container_type = "entity"
        target = target.build()

    if operation.value == "insert" and "signature1" in data_location:
        raise ValueError("Specified 'insert' operation but not 'index'")
    if operation.value == "insert" and "signature44" in data_location:
        raise ValueError("Specified 'insert' operation but not 'index'")
    if operation.value != "insert" and "signature7" in data_location:
        raise ValueError(f"Specified 'index' but the operation is {operation.value}, not 'insert'")
    if operation.value != "insert" and "signature33" in data_location:
        raise ValueError(f"Specified 'index' but the operation is {operation.value}, not 'insert'")

    if "signature44" or "signature33" in data_location:
        Handler._write(f"data modify {container_type} {target} {path} {operation.value} {data_location['output']}")
        return f"data modify {container_type} {target} {path} {operation.value} {data_location['output']}"
    elif "signature7" or "signature1" in data_location:
        Handler._write(f"data modify {container_type} {target} {path} {operation.value} {data_location['output']}")
        return f"data modify {container_type} {target} {path} {operation.value} {data_location['output']}"
    else:
        Handler._warn("Missing signature for 'data_location'. Consider using 'set_to()' or 'set_from()' to avoid errors.")
        Handler._write(f"data modify {container_type} {target} {path} {operation.value} {data_location['output']}")
        return f"data modify {container_type} {target} {path} {operation.value} {data_location['output']}"


def remove(target: Union[str, tuple, Selector], path: str):
    """remove - Remove a piece of data from the target(s).

    Args:
        target (Union[str, tuple, Selector]): The target(s) to remove the entity from.
        path (str): The piece of data to remove.

    Returns:
        str: The command to be written.
    """
    if isinstance(target, str):
        container_type = "storage"
    if isinstance(target, tuple):
        container_type = "block"
        target = ' '.join(target)
    if isinstance(target, Selector):
        container_type = "entity"
        target = target.build()
    Handler._write(f"data remove {container_type} {target} {path}")
    return f"data remove {container_type} {target} {path}"
