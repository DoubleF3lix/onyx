from typing import Union

from onyx.enums import advancement_action, selection, mode, difficulty, rule, enchants
from onyx.handler import Handler

from onyx.execute import execute
from onyx.selector import selector
from onyx.json_string import json_string


def send(cmd: str):
    """Writes a raw commands to the function

    Args:
        cmd (str): The command to be written
    """
    Handler._cmds.append(cmd)


def advancement(action: advancement_action, targets: selector, advancement_selection: selection, advancement: str):
    """
    Args:
        action (advancement_action): The action to perform (grant / revoke).
        targets (selector): The players to act upon.
        advancement_selection (selection): The advancements area to select (everything, from, etc.).
        advancement (str): The advancement itself.
    """
    Handler._cmds.append(f"advancement {action.value} {Handler._translate(targets)} {advancement_selection.value} {advancement}")


def clear(targets: selector, item: str, count: int = None, auto_namespace: bool = True):
    """
    Args:
        targets (selector): The players to clear from.
        item (str): The item to clear.
        count (int, optional): The amount of items to clear. Clears all if unspecified. Defaults to None.
        auto_namespace (bool, optional): Whether or not 'minecraft:' should be prepended to the item name. Defaults to True.
    """
    if auto_namespace and not item.startswith("minecraft:"):
        item = f"minecraft:{item}"
        Handler._warn("'item' was not namespaced with 'minecraft:' so it has been done for you. You can disable this with 'auto_namespace=False'.")
    Handler._cmds.append(f"clear {Handler._translate(targets)} {item} {count or ''}")


# Adds a comment to the function file with a custom amount of blank lines before and after
def comment(text: str, preline: int = 1, postline: int = 0):
    """Adds a comment to the function file

    Args:
        text (str): The comment content.
        preline (int, optional): The amount of blank lines before the comment. Defaults to 1.
        postline (int, optional): The amount of blank lines after the comment. Defaults to 0.
    """
    for x in range(preline):
        Handler._cmds.append("")
    Handler._cmds.append(f"# {text}")
    for x in range(postline):
        Handler._cmds.append("")


def defaultgamemode(gamemode: mode):
    """
    Args:
        gamemode (mode): The gamemode to set to.
    """
    Handler._cmds.append(f"defaultgamemode {gamemode.value}")


def difficulty(level: difficulty):
    """
    Args:
        level (difficulty): The difficulty to set to.
    """
    Handler._cmds.append(f"difficulty {level.value}")


def enchant(targets: selector, enchant_list: Union[list, enchants], level: int = None):
    """
    Args:
        targets (selector): The players on whom the enchantment should be applied.
        enchant_list (Union[list, enchants]): The enchantment to apply.
        level (int, optional): The level of the enchantment. Defaults to None.
    """
    if isinstance(enchant_list, list):
        for enchant in enchant_list:
            Handler._cmds.append(f"enchant {Handler._translate(targets)} {enchant.value} {level or ''}")
    else:
        Handler._cmds.append(f"enchant {Handler._translate(targets)} {enchant_list.value} {level or ''}")


def using(execute_preset: execute, cmds: list):
    """execute

    Args:
        execute_preset (execute): The preset to be used. Generated with 'execute()'
        cmds (list): A list of commands that should be run when the condition is met.
    """
    Handler._move_commands(execute_preset, cmds)


def gamemode(targets: selector, mode: mode):
    """
    Args:
        targets (selector): The players whose gamemode should be set.
        mode (mode): The gamemode that should be set.
    """
    Handler._cmds.append(f"gamemode {Handler._translate(mode)} {Handler._translate(targets)}")


def gamerule(rule: rule, value: str):
    """
    Args:
        rule (rule): The gamerule that should be modified.
        value (str): The value the gamerule should be set to.
    """
    Handler._cmds.append(f"gamerule {Handler._translate(rule)} {value}")


def kill(targets: selector):
    """
    Args:
        targets (slector): The entities to kill.
    """
    Handler._cmds.append(f"kill {Handler._translate(targets)}")


def say(text: str):
    """
    Args:
        text (str): The text to print.
    """
    Handler._cmds.append(f"say {text}")


def spectate(target: selector, source: selector = "@s"):
    """
    Args:
        target (selector): The entity to be spectated
        source (selector, optional): The entity that should spectate. Defaults to "@s".
    """
    Handler._cmds.append(f"spectate {Handler._translate(target)} {Handler._translate(source)}")


def tellraw(targets: selector, text: json_string):
    """
    Args:
        targets (selector): The players to print the text to.
        text (json_string): The text to print.
    """
    Handler._cmds.append(f"tellraw {Handler._translate(targets)} {Handler._translate(text, convert=True)}")
