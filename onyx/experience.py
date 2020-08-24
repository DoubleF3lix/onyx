import enum
from onyx.handler import Handler
from onyx.selector import selector
from onyx.enums import lib


def add(targets: selector, amount: str):
    """
    Args:
        targets (selector): The players to give the XP to.
        amount (str): The amount of XP. Append it with ``P`` for points or ``L`` for levels.
    """
    if amount.lower().startswith("p"):
        Handler._cmds.append(f"experience add {Handler._translate(targets)} {amount[:-1]} points")
    elif amount.lower().startswith("l"):
        Handler._cmds.append(f"experience add {Handler._translate(targets)} {amount[:-1]} levels")
    else:
        Handler._warn("No valid suffix provided, assuming levels")
        Handler._cmds.append(f"experience add {Handler._translate(targets)} {amount} levels")


# Removing levels or points is just adding negative levels or points
def remove(targets: selector, amount: str):
    """
    Args:
        targets (selector): The players to remove the XP from.
        amount (str): The amount of XP. Append it with ``P`` for points or ``L`` for levels.

    """
    if amount.lower().startswith("p"):
        Handler._cmds.append(f"experience add {Handler._translate(targets)} -{amount[:-1]} points")
    elif amount.lower().startswith("l"):
        Handler._cmds.append(f"experience add {Handler._translate(targets)} -{amount[:-1]} levels")
    else:
        Handler._warn("No valid suffix provided, assuming levels")
        Handler._cmds.append(f"experience add {Handler._translate(targets)} -{amount} levels")


def set(targets: selector, amount: str):
    """
    Args:
        targets (selector): The players to remove the XP from.
        amount (str): The amount of XP. Append it with ``P`` for points or ``L`` for levels.
    """
    if amount.lower().startswith("p"):
        Handler._cmds.append(f"experience set {Handler._translate(targets)} {amount[:-1]} points")
    elif amount.lower().startswith("l"):
        Handler._cmds.append(f"experience set {Handler._translate(targets)} {amount[:-1]} levels")
    else:
        Handler._warn("No valid suffix provided, assuming levels")
        Handler._cmds.append(f"experience set {Handler._translate(targets)} {amount} levels")


# 2,147,483,647 is the max amount of XP levels a user can have, so just remove all of it
# (they can't have any more points if they have this many levels)
def reset(targets: selector):
    """Sets the target(s) XP to 0

    Args:
        targets (selector): The players to reset the XP of.
    """
    Handler._cmds.append(f"experience add {Handler._translate(targets)} -2147483647 levels")


# Also known as query
def get(targets: selector, query_type: enum.Enum):
    """
    Args:
        target (selector): The player to get the XP of.
        query_type (enum.Enum): Whether the levels or the points should be retrieved.
    """
    if not isinstance(query_type, (enum.Enum, str)):
        Handler._warn("Invalid query type provided, assuming levels")
        Handler._cmds.append(f"experience query {Handler._translate(targets)} levels")
    else:
        Handler._cmds.append(f"experience query {Handler._translate(targets)} {Handler._translate(query_type)}")


def get_total_points(targets: selector):
    """Loads the ``calc_xp_points`` library to calculate the total points of XP a player has

    Args:
        targets (selector): The players whose points should be calculated.
    """
    Handler._add_scoreboard("onyx.xp_points")
    Handler._add_scoreboard("onyx.const")
    Handler.load_lib(lib.calc_xp_points)
    Handler._cmds.append(f"execute as {Handler._translate(targets)} run function {Handler._datapack_name}:lib/calc_xp_points/main")
