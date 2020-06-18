import inspect
from .handler import Handler
from .enum import position


def disable(datapack_name: str):
    """disable - Disables a datapack

    Args:
        datapack_name (str): The name of the datapack to disable.

    Raises:
        ValueError: Raised when datapack_name is not a string.

    Returns:
        str: The command to be written.
    """
    if not isinstance(datapack_name, str):
        raise ValueError(f"Expected string for 'datapack_name', got {type(datapack_name)}")
    Handler._write(inspect.stack()[1][3], f"datapack disable \"file/{datapack_name}\"")
    return f"datapack disable \"file/{datapack_name}\""


def enable(datapack_name: str, datapack_pos: position = None, relative_to: str = None):
    """enable - Enables a datapack.

    Args:
        datapack_name (str): The name of the datapack to enable.
        datapack_pos (position, optional): Where the datapack should be enabled (before, first, etc.). Defaults to None.
        relative_to (str, optional): The datapack that datapack_name should be enabled relative to. Only specify with "datapack_pos". Defaults to None.

    Raises:
        ValueError: Raised if datapack_name is not a string.
        ValueError: Rasied if relative_to is not a string.

    Returns:
        [type]: [description]
    """
    if not isinstance(datapack_name, str):
        raise ValueError(f"Expected string for 'datapack_name', got {type(datapack_name)}")
    if datapack_pos:
        if datapack_pos.value in {"before", "after"}:
            if not relative_to:
                Handler._warn("Specified 'datapack_pos' but not 'relative_to' so it was ignored")
                Handler._write(inspect.stack()[1][3], f"datapack enable \"file/{datapack_name}\"")
                return f"datapack enable \"file/{datapack_name}\""
            else:
                if not isinstance(relative_to, str):
                    raise ValueError(f"Expected string for 'relative_to', got {type(relative_to)}")
                Handler._write(inspect.stack()[1][3], f"datapack enable \"file/{datapack_name}\" {datapack_pos.value} \"file/{relative_to}\"")
                return f"datapack enable \"file/{datapack_name}\" {datapack_pos.value} \"file/{relative_to}\""

        Handler._write(inspect.stack()[1][3], f"datapack enable \"file/{datapack_name}\" {datapack_pos.value}")
        return f"datapack enable \"file/{datapack_name}\" {datapack_pos.value}"
    Handler._write(inspect.stack()[1][3], f"datapack enable \"file/{datapack_name}\"")
    return f"datapack enable \"file/{datapack_name}\""
