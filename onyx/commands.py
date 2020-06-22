import enum
import os
from typing import Union
from .enum import advancement_action, selection, mode, difficulty, debug_mode
from .execute import execute
from .handler import Handler
from .selector import Selector
from .json_string import json_string


# Send any command
def send(cmd: str):
    """send - Writes a raw commands to the function

    Args:
        cmd (str): The command to be written

    Raises:
        ValueError: Raised if the command specified is not a string.

    Returns:
        str: The command to be written.
    """
    if not isinstance(cmd, str):
        raise ValueError(f"Expected string for 'cmd', got {type(cmd)}")
    Handler._write(cmd)
    return cmd


def advancement(action: advancement_action, targets: Selector, advancement_selection: selection, advancement: str):
    """advancement - advancement command

    Args:
        action (advancement_action): The action to perform (grant / revoke).
        targets (Selector): The players to act upon.
        advancement_selection (selection): The advancements area to select (everything, from, etc.).
        advancement (str): The advancement itself.

    Raises:
        ValueError: Raised if the argument isn't the right type.

    Returns:
        str: The command to be written.
    """
    if not isinstance(targets, Selector):
        raise ValueError(f"Expected selector object for 'targets', got {type(targets)}")
    if not isinstance(advancement, str):
        raise ValueError(f"Expected string for 'advancement', got {type(advancement)}")
    Handler._write(f"advancement {action.value} {targets.build()} {advancement_selection.value} {advancement}")
    return f"advancement {action.value} {targets.build()} {advancement_selection.value} {advancement}"


def clear(targets: Selector, item: str, count: int = None, auto_namespace: bool = True):
    """clear - clear command

    Args:
        targets (Selector): The players to clear from.
        item (str): The item to clear.
        count (int, optional): The amount of items to clear. Clears all if unspecified. Defaults to None.
        auto_namespace (bool, optional): Whether or not 'minecraft:' should be prepended to the item name. Defaults to True.

    Raises:
        ValueError: Raised if the argument isn't the right type.

    Returns:
        str: The command to be written.
    """
    if not isinstance(targets, Selector):
        raise ValueError(f"Expected selector object for 'targets', got {type(targets)}")
    if not isinstance(item, str):
        raise ValueError(f"Expected string for 'item', got {type(item)}")
    if not count and not isinstance(count, int):
        raise ValueError(f"Expected None or integer for 'count', got {type(count)}")
    if not item.startswith("minecraft:"):
        if auto_namespace:
            item = f"minecraft:{item}"
            Handler._warn("'item' was not namespaced with 'minecraft:' so it has been done for you. You can disable this with 'auto_namespace=False'.")
    Handler._write(f"clear {targets.build()} {item} {count or ''}")
    return f"clear {targets.build()} {item} {count or ''}"


# Adds a comment to the function file with a custom amount of blank lines before and after
def comment(text: str, preline: int = 1, postline: int = 0):
    """comment - Adds a comment to the function file

    Args:
        text (str): The comment content.
        preline (int, optional): The amount of blank lines before the comment. Defaults to 1.
        postline (int, optional): The amount of blank lines after the comment. Defaults to 0.

    Returns:
        str: The comment to be written.
    """
    cmds = []
    for x in range(preline):
        Handler._write("")
        cmds.append("")
    Handler._write(f"# {text}")
    cmds.append(f"# {text}")
    for x in range(postline):
        Handler._write("")
        cmds.append("")
    return cmds


def call(function: callable):
    """call - Calls a function (the function must be declared before this function is run)

    Args:
        function (callable): The function to run.

    Returns:
        str: The command to be written.
    """
    # Get the function path, split it, and then keep only everything past /data/namespace/functions/
    function_path = Handler._get_function_path(function.__name__)
    Handler._write(f"function {Handler._datapack_name}:{function_path}")
    return f"function {Handler._datapack_name}:{function_path}"


def defaultgamemode(gamemode: mode):
    """defaultgamemode - defaultgamemode command

    Args:
        gamemode (mode): The gamemode to set to.

    Returns:
        str: The command to be written.
    """
    Handler._write(f"defaultgamemode {gamemode.value}")
    return f"defaultgamemode {gamemode.value}"


def difficulty(level: difficulty):
    """difficulty - difficulty command

    Args:
        level (difficulty): The difficulty to set to.

    Returns:
        str: The command to be written.
    """
    Handler._write(f"difficulty {level.value}")
    return f"difficulty {level.value}"


def enchant(targets: Selector, enchant_list: Union[list, enum.Enum], level: int = None):
    """enchant [summary]

    Args:
        targets (Selector): The players on whom the enchantment should be applied.
        enchant_list (Union[list, enum.Enum]): The enchantment to apply.
        level (int, optional): The level of the enchantment. Defaults to None.

    Raises:
        ValueError: Raised when targets is not a selector object.

    Returns:
        list: The commands to be written.
    """
    cmds = []
    if not isinstance(targets, Selector):
        raise ValueError(f"Expected selector object for 'targets', got {type(targets)}")
    if isinstance(enchant_list, enum.Enum):
        Handler._write(f"enchant {targets.build()} {enchant_list.value} {level or ''}")
        return f"enchant {targets.build()} {enchant_list.value} {level or ''}"
    elif isinstance(enchant_list, list):
        for enchant in enchant_list:
            Handler._write(f"enchant {targets.build()} {enchant.value} {level or ''}")
            cmds.append(f"enchant {targets.build()} {enchant.value} {level or ''}")
        return cmds


# Execute presets (everyone for /execute except if, unless, and store)
def using(execute_preset: execute, cmds: list):
    """using - execute (except for if / unless and store)

    Args:
        execute_preset (execute): The preset to be used. Generated with 'execute()'
        cmds (list): A list of commands that should be run when the condition is met.

    Raises:
        ValueError: Raised when the preset is not an execute object.
    """
    # Type checking
    if not isinstance(execute_preset, execute):
        raise ValueError(f"Expected execute object, got {type(execute_preset)}")

    Handler._move_commands(execute_preset, cmds)


def gamemode(targets: Selector, mode: mode):
    """gamemode - gamemode command

    Args:
        targets (Selector): The players whose gamemode should be set.
        mode (mode): The gamemode that should be set.

    Raises:
        ValueError: Raised when targets is not a selector object
    """
    if not isinstance(targets, Selector):
        raise ValueError(f"Expected selector object for 'targets', got {type(targets)}")
    Handler._write(f"gamemode {mode.value} {targets.build()}")


def gamerule(rule: enum.Enum, value: str):
    """gamerule - gamerule command

    Args:
        rule (enum.Enum): The gamerule that should be modified.
        value (str): The value the gamerule should be set to.

    Returns:
        str: The command to be written.
    """
    Handler._write(f"gamerule {rule.value} {value}")
    return f"gamerule {rule.value} {value}"


def if_block(block: str, position: tuple = None, cmds: tuple = None, radius: int = 0):
    if radius > 16:
        raise ValueError("'radius' cannot exceed 16")
    cmd_list = []
    Handler._status(f"Generating {(radius * 2 + 1) ** 3} commands for 'if_block' with a radius of {radius}.")
    pos = f"positioned {position[0]} {position[1]} {position[2]} " if position else ""


def kill(targets: Selector):
    """kill - kill command

    Args:
        targets (Selector): The entities to kill.

    Raises:
        ValueError: Raised when targets is not a selector object.

    Returns:
        str: The command to be written.
    """
    if not isinstance(targets, Selector):
        raise ValueError(f"Expected selector object for 'targets', got {type(targets)}")
    Handler._write(f"kill {targets.build()}")
    return f"kill {targets.build()}"


def say(text: str):
    """say - say command

    Args:
        text (str): The text to print.

    Returns:
        str: The command to be written.
    """
    Handler._write(f"say {text}")
    return f"say {text}"


def tellraw(targets: Selector, text: json_string):
    """tellraw - tellraw command

    Args:
        targets (Selector): The players to print the text to.
        text (json_string): The text to print.

    Raises:
        ValueError: Raised if the argument isn't the right type.

    Returns:
        str: The command to be written.
    """
    if not isinstance(targets, Selector):
        raise ValueError(f"Expected selector object for 'targets', got {type(targets)}")
    if not isinstance(text, json_string):
        raise ValueError(f"Expected json_string object for 'text', got {type(text)}")
    Handler._write(f"tellraw {targets.build()} {text.output}")
    return f"tellraw {targets.build()} {text.output}"


def wait(length: str):
    lookup_table = {"t": 1, "s": 20, "m": 1200, "h": 72000}
    if str(length)[-1] in lookup_table:
        length = int(str(length)[:-1]) * int(lookup_table[length[-1]])

    # Add to the working path
    differentiator = Handler._get_differentiator()
    Handler._write(f"schedule function {Handler._datapack_name}:{Handler._get_function_path(Handler._current_func, keep_function_name=False)}/generated/{Handler._current_func}{differentiator} {length}t")
    Handler._working_path = os.path.join(Handler._working_path, "generated")
    Handler._current_func = Handler._current_func + differentiator

    # Register the new path in the list
    Handler._path_list[Handler._current_func] = Handler._working_path

    return f"schedule function {Handler._datapack_name}:{Handler._get_function_path(Handler._current_func, keep_function_name=False)}/generated/{Handler._current_func}{differentiator} {length}t"
