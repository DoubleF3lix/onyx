import inspect
import enum
from .handler import Handler
from .selector import Selector
from .enum import lib


def add(targets: Selector, amount: str):
    """add - Adds a certain amount of XP levels or points.

    Args:
        targets (Selector): The players to give the XP to.
        amount (str): The amount of XP. Append it with "P" for points or "L" for levels.

    Raises:
        ValueError: Raised when targets is not a selector object.

    Returns:
        str: The command to be written.
    """
    if not isinstance(targets, Selector):
        raise ValueError(f"Expected selector object for 'targets', got {type(targets)}")
    if amount.lower().startswith("p"):
        Handler._write(inspect.stack()[1][3], f"experience add {targets.build()} {amount[:-1]} points")
        return f"experience add {targets.build()} {amount[:-1]} points"
    elif amount.lower().startswith("l"):
        Handler._write(inspect.stack()[1][3], f"experience add {targets.build()} {amount[:-1]} levels")
        return f"experience add {targets.build()} {amount[:-1]} levels"
    else:
        Handler._warn("No valid suffix provided, assuming levels")
        Handler._write(inspect.stack()[1][3], f"experience add {targets.build()} {amount} levels")
        return f"experience add {targets.build()} {amount} levels"


# Removing levels or points is just adding negative levels or points
def remove(targets: Selector, amount: str):
    """remove - Removes a certain amount of XP levels or points.

    Args:
        targets (Selector): The players to remove the XP from.
        amount (str): The amount of XP. Append it with "P" for points or "L" for levels.

    Raises:
        ValueError: Raised when targets is not a selector object.

    Returns:
        str: The command to be written.
    """
    if not isinstance(targets, Selector):
        raise ValueError(f"Expected selector object for 'targets', got {type(targets)}")
    if amount.lower().startswith("p"):
        Handler._write(inspect.stack()[1][3], f"experience add {targets.build()} -{amount[:-1]} points")
        return f"experience add {targets.build()} -{amount[:-1]} points"
    elif amount.lower().startswith("l"):
        Handler._write(inspect.stack()[1][3], f"experience add {targets.build()} -{amount[:-1]} levels")
        return f"experience add {targets.build()} -{amount[:-1]} levels"
    else:
        Handler._warn("No valid suffix provided, assuming levels")
        Handler._write(inspect.stack()[1][3], f"experience add {targets.build()} -{amount} levels")
        return f"experience add {targets.build()} -{amount} levels"


def set(targets: Selector, amount: str):
    """set - Sets a certain amount of XP levels or points.

    Args:
        targets (Selector): The players to remove the XP from.
        amount (str): The amount of XP. Append it with "P" for points or "L" for levels.

    Raises:
        ValueError: Raised when targets is not a selector object.

    Returns:
        str: The command to be written.
    """
    if not isinstance(targets, Selector):
        raise ValueError(f"Expected selector object for 'targets', got {type(targets)}")
    if amount.lower().startswith("p"):
        Handler._write(inspect.stack()[1][3], f"experience set {targets.build()} {amount[:-1]} points")
        f"experience set {targets.build()} {amount[:-1]} points"
    elif amount.lower().startswith("l"):
        Handler._write(inspect.stack()[1][3], f"experience set {targets.build()} {amount[:-1]} levels")
        return f"experience set {targets.build()} {amount[:-1]} levels"
    else:
        Handler._warn("No valid suffix provided, assuming levels")
        Handler._write(inspect.stack()[1][3], f"experience set {targets.build()} {amount} levels")
        return f"experience set {targets.build()} {amount} levels"


# 2,147,483,647 is the max amount of XP levels a user can have, so just remove all of it
# (they can't have any more points if they have this many levels)
def reset(targets: Selector):
    """reset - Sets the targets XP to 0

    Args:
        targets (Selector): The players to reset the XP of.
    Raises:
        ValueError: Raised when targets is not a selector object.

    Returns:
        str: The command to be written.
    """
    if not isinstance(targets, Selector):
        raise ValueError(f"Expected selector object for 'targets', got {type(targets)}")
    Handler._write(f"experience add {targets.build()} -2147483647 levels")
    return f"experience add {targets.build()} -2147483647 levels"


# Also known as query
def get(targets: Selector, query_type: enum.Enum):
    """get - Gets the XP levels or points of the target

    Args:
        target (Selector): The player to get the XP of.
        query_type (enum.Enum): Whether the levels or the points should be retrieved.

    Raises:
        ValueError: Raised when target is not a selector object.

    Returns:
        str: The command to be written.
    """
    if not isinstance(targets, Selector):
        raise ValueError(f"Expected selector object for 'targets', got {type(targets)}")
    if not isinstance(query_type, enum.Enum):
        Handler._warn("Invalid query type provided, assuming levels")
        Handler._write(inspect.stack()[1][3], f"experience query {targets.build()} levels")
        return f"experience query {targets.build()} levels"
    Handler._write(inspect.stack()[1][3], f"experience query {targets.build()} {query_type.value}")
    return f"experience query {targets.build()} {query_type.value}"


def get_total_points(targets: Selector):
    """get_total_points - Loads the "calc_xp_points" library to calculate the total points of XP a player has.

    Args:
        targets (Selector): The players whose points should be calculated.

    Returns:
        str: The command to be written.
    """
    Handler._load_lib(lib.calc_xp_points)
    Handler._add_to_init([
        "scoreboard objectives add onyx.xp_points dummy",
        "scoreboard objectives add onyx.const dummy",
        "scoreboard players set $6 onyx.const 6",
        "scoreboard players set $10 onyx.const 10",
        "scoreboard players set $25 onyx.const 25",
        "scoreboard players set $45 onyx.const 45",
        "scoreboard players set $360 onyx.const 360",
        "scoreboard players set $405 onyx.const 405",
        "scoreboard players set $1625 onyx.const 1625",
        "scoreboard players set $2220 onyx.const 2220"
    ])
    Handler._write(inspect.stack()[1][3], f"function {Handler._datapack_name}:lib/calc_xp_points/main")
    return f"function {Handler._datapack_name}:lib/calc_xp_points/main"
