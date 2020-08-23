from onyx.handler import Handler
from onyx.enums import position


def disable(datapack_name: str):
    """
    Args:
        datapack_name (str): The name of the datapack to disable.
    """
    Handler._cmds.append(f"datapack disable \"file/{Handler._translate(datapack_name)}\"")


def enable(datapack_name: str, datapack_pos: position = None, relative_to: str = None):
    """
    Args:
        datapack_name (str): The name of the datapack to enable.
        datapack_pos (position, optional): Where the datapack should be enabled (before, first, etc.). Defaults to None.
        relative_to (str, optional): The datapack that datapack_name should be enabled relative to. Only specify with "datapack_pos". Defaults to None.
    """
    if datapack_pos is not None:
        # Other options are first and last
        if Handler._translate(datapack_pos) in {"before", "after"}:
            if relative_to is None:
                Handler._warn("Specified 'datapack_pos' but not 'relative_to' so it was ignored")
                Handler._cmds.append(f"datapack enable \"file/{datapack_name}\"")
            else:
                Handler._cmds.append(f"datapack enable \"file/{datapack_name}\" {Handler._translate(datapack_pos)} \"file/{relative_to}\"")
        else:
            Handler._cmds.append(f"datapack enable \"file/{datapack_name}\" {Handler._translate(datapack_pos)}")
    else:
        Handler._cmds.append(f"datapack enable \"file/{datapack_name}\"")
