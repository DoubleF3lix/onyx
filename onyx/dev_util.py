import json
import re
from typing import Any

import nbtlib


def convert_resource_path(resource_path: str) -> dict:
    """
    convert_resource_path - Converts a pack resource path into different parts

    Args:
        mcfunction_path (str): The path to split

    Returns:
        dict: The split parts
    """
    path = resource_path.split(":")
    namespace = path[0]
    namespace_removed_path = path[1].split("/")

    return {
        "namespace": namespace,
        "path": "/".join(namespace_removed_path[:-1]),
        "name": namespace_removed_path[-1],
    }


def snakify(text: str) -> str:
    """
    snakify - Converts a string to snake case

    Args:
        text (str): The string to convert

    Returns:
        str: The snake cased string
    """
    return "_".join(re.sub(r"[^a-zA-Z0-9_]", "", q.lower()) for q in text.split(" "))


def camelify(text: str) -> str:
    """
    camelify - Converts a string to camel case

    Args:
        text (str): The text to convert

    Returns:
        str: The camel cased string
    """
    return "".join(
        q.lower().capitalize() if i != 0 else q.lower()
        for i, q in enumerate(
            re.sub("[^a-z0-9 ]", "", text.replace("_", " ").lower()).split(" ")
        )
    )


def dict_to_advancement_selector(arg: dict) -> str:
    """
    dict_to_advancement_selector - Converts a dictionary into an advancement selector

    Args:
        arg (dict): The dictionary to convert

    Returns:
        str: The advancement selector
    """
    # {"thing/1": {"thing/12": True}, "thing/2": False}
    q = []
    for key, item in arg.items():
        if isinstance(item, bool):
            q.append(f"{key}={json.dumps(item)}")
        # Assume type is dictionary
        else:
            # Grab only the first key and its value (stored in a tuple, key is 0, value is 1)
            first_dict_pair = list(item.items())[0]
            q.append(f"{key}={{{first_dict_pair[0]}={json.dumps(first_dict_pair[1])}}}")

    return f"{{{', '.join(q)}}}"


def dict_to_score_selector(arg: dict) -> str:
    """
    dict_to_score_selector - Converts a dictionary into a score selector

    Args:
        arg (dict): The dictionary to convert

    Returns:
        str: The score selector
    """
    # {scoreboardObj1: 3, scoreboardObj2: 4}
    q = [f"{key}={translate(item)}" for key, item in arg.items()]
    return f"{{{', '.join(q)}}}"


def translate(
    obj: Any,
    json_dump_elements: bool = False,
    normalize_boolean: bool = False,
    just_uuid: bool = False,
    keep_list: bool = False,
) -> Any:
    """
    translate - Translates an object into something useable. The parameters for this function are highly specialized to meet the needs of various objects.

    Args:
        json_dump_elements (bool): Whether or not to json dump elements if ``obj`` is a list or tuple
        normalize_boolean (bool): Whether or not json dump booleans
        just_uuid (bool): Whether or not to just return the uuid of the attribute modifier
        keep_list (bool): Whether or not to keep the list structure of ``obj`` and just translate the individual parts
    """
    import enum

    from onyx.class_types import Buildable
    from onyx.pack_manager import Stringable

    if isinstance(obj, Buildable):
        if just_uuid:
            return obj.build(just_uuid=True)
        return obj.build()
    elif isinstance(obj, enum.Enum):
        return obj.value
    elif isinstance(obj, (list, tuple)):
        if json_dump_elements:
            return [json.dumps(translate(element)) for element in obj]
        elif keep_list:
            return [translate(element) for element in obj]
        else:
            return " ".join(str(translate(element)) for element in obj)
    elif obj is None:
        return ""
    elif isinstance(obj, Stringable):
        return str(obj)
    elif isinstance(obj, bool) and normalize_boolean:
        return json.dumps(obj)
    elif isinstance(obj, nbtlib.Base):
        return obj.snbt()
    else:
        return obj


def convert_experience_amount(amount: str) -> tuple:
    """
    convert_experience_amount - Converts a string into a tuple of amount and type

    Args:
        amount (str): The string to convert

    Returns:
        tuple: Index 0 is the amount and index 1 is the type
    """
    xp_type = "levels"
    if isinstance(amount, str):
        amount = amount.lower()
        if amount.endswith("p"):
            xp_type = "points"
        if not amount.isdigit():
            amount = amount[:-1]
    return (amount, xp_type)


def add_scoreboard(objective, criteria="dummy"):
    """
    add_scoreboard - Adds a scoreboard if it does not already exist

    Args:
        objective (str): The objective name
        criteria (str, optional): The objective criteria. Defaults to "dummy".

    Returns:
        str: Command
    """
    from onyx.commands import Commands

    if objective not in Commands.added_scoreboards:
        Commands.added_scoreboards.append(objective)
        return Commands.push(
            f"scoreboard objectives add {objective} {criteria}", init=True
        )


def convert_scoreboard_player_name(name: str) -> str:
    """
    convert_scoreboard_player_name - Converts a scoreboard player name indicated by the documentation for ``Player`` and ``Scoreboard``

    Args:
        name (str): The player name to convert

    Returns:
        str: The converted player name
    """
    from onyx.scoreboard import Player

    if isinstance(name, Player):
        name = name.name

    if isinstance(name, str):
        if name.startswith("player_"):
            name = name[7:]
        elif name.startswith("_"):
            name = f"#{name[1:]}"
        else:
            name = f"${name}"
    return translate(name)


def get_integer_count_at_string_end(string: str) -> int:
    """
    get_integer_count_at_string_end - Gets the amount of numbers at the end of a string

    Args:
        string (str): The string to check

    Returns:
        int: The amount of numbers at the end of the string
    """
    string = str(string)[::-1]
    for char_index in range(len(string)):
        if not string[char_index].isdigit():
            return char_index


def dict_to_block_state(dict: dict) -> str:
    """
    dict_to_block_state - Converts a dictionary into a block state

    Args:
        dict (dict): The dictionary to convert

    Returns:
        str: The block state
    """
    return f"[{','.join([f'{key}={value}' for key, value in dict.items()])}]"


def convert_schedule_time(string: str) -> str:
    """
    convert_schedule_time - Provides extra time types for schedule times

    Args:
        string (str): The string to convert

    Returns:
        str: The converted string
    """
    # ticks, seconds, and days are included
    if isinstance(string, int):
        return f"{string}t"
    elif string.endswith("m"):
        return f"{int(string[:-1]) * 60}s"
    elif string.endswith("h"):
        return f"{int(string[:-1]) * 3600}s"
    elif string.endswith("w"):
        return f"{int(string[:-1]) * 7}d"
    else:
        return string


def convert_day_time(string: str) -> str:
    """
    convert_day_time - Provides a conversion to turn schedule-like times into day time

    Args:
        string (str): The string to convert

    Returns:
        str: The converted string
    """
    if isinstance(string, int):
        return string
    elif string.endswith("s"):
        return int(string[:-1]) * 0.27777777
    elif string.endswith("m"):
        return int(string[:-1]) * 16.6666666
    elif string.endswith("h"):
        return int(string[:-1]) * 1000
    elif string.endswith("d"):
        return int(string[:-1]) * 24000
    elif string.endswith("w"):
        return int(string[:-1]) * 168000
    else:
        return string
