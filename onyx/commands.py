import os
import inspect
import enum
from .enum import advancement_action, selection, mode, difficulty, debug_mode
from .execute import execute
from .handler import Handler
from .selector import Selector
from .json_string import json_string

# Send any command
def send(cmd:str) -> None:
    if not isinstance(cmd, str):
        raise ValueError(f"Expected string for 'cmd', got {type(cmd)}")
    Handler._write(inspect.stack()[1][3], cmd)

def advancement(action:advancement_action, targets:Selector, advancement_selection:selection, advancement:str) -> None:
    if not isinstance(targets, Selector):
        raise ValueError(f"Expected selector object for 'targets', got {type(targets)}")
    if not isinstance(advancement, str):
        raise ValueError(f"Expected string for 'advancement', got {type(advancement)}")
    Handler._write(inspect.stack()[1][3], f"advancement {action.value} {targets.build()} {advancement_selection.value} {advancement}")
    
def ban(player:str, reason:str=None, ip:bool=False):
    if not isinstance(player, str):
        raise ValueError(f"Expected string for 'player', got {type(player)}")
    if reason:
        if not isinstance(reason, str):
            raise ValueError(f"Expected string for 'reason', got {type(reason)}")

    # Write "ban-ip" if ip == True, otherwise just write "ban"
    nothing, ip_txt = "", "-ip"
    Handler._write(f"ban{nothing if ip else ip_txt} {player} {reason or ''}")

def clear(targets:Selector, item:str, count:int=None, auto_namespace:bool=True) -> None:
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
    Handler._write(inspect.stack()[1][3], f"clear {targets.build()} {item} {count or ''}")

# Adds a comment to the function file with a custom amount of blank lines before and after
def comment(text:str, preline:int=1, postline:int=0) -> None:
    for x in range(preline):
        Handler._write(inspect.stack()[1][3], "")
    Handler._write(inspect.stack()[1][3], f"# {text}")
    for x in range(postline):
        Handler._write(inspect.stack()[1][3], "")	
    return preline + postline + 1

# Writes "function <datapack name>:<path>"" to the working path
def call(function:callable) -> None:
    # Get the function path, split it, and then keep only everything past /data/namespace/functions/
    function_path = Handler._get_function_path(function.__name__)
    Handler._write(inspect.stack()[1][3], f"function {Handler._datapack_name}:{function_path}") 

def debug(mode:debug_mode):
    Handler._write(inspect.stack()[1][3], f"debug {mode.value}")

def defaultgamemode(gamemode:mode):
    Handler._write(inspect.stack()[1][3], f"defaultgamemode {gamemode.value}")

def difficulty(level:difficulty):
    Handler._write(inspect.stack()[1][3], f"difficulty {level.value}")

# Execute presets (everyone for /execute except if, unless, and store)
def using(execute_preset:execute, cmds:tuple) -> None:
    # Type checking
    if not isinstance(execute_preset, execute):
        raise ValueError(f"Expected execute object, got {type(execute_preset)}")

    # Count the commands inside the block (so it works for things like effects)
    command_count = 0
    for command in cmds:
        if command:
            command_count += command
        else:
            command_count += 1

    # Get the file contents and seperate the commands and everything else
    with open(os.path.join(Handler._working_path, inspect.stack()[1][3] + ".mcfunction"), "r") as _file:
        contents = _file.readlines()
        contents_without_commands = contents[:-command_count]
        commands = contents[-command_count:]

    # Remove the commands that are part of the execute block
    with open(os.path.join(Handler._working_path, inspect.stack()[1][3] + ".mcfunction"), "w") as _file:
        _file.write(''.join(contents_without_commands))
    
    # Make the generated folder if it doesn't exist
    os.makedirs(os.path.join(Handler._working_path, "generated"), exist_ok=True)

    # Find the number to put at the end of the mcfunction name by looping through all numbers and checking if it exists
    for differentiator in range(1, 1000000):
        # Keep searching for a new differentiator until one that is not in use is found
        if os.path.exists(os.path.join(Handler._working_path, "generated", f"{inspect.stack()[1][3]}{differentiator}.mcfunction")):
            continue
        # The loop will only exit if it finds a differentiator that isn't in use
        break

    # Write the seperated commands to the other file
    with open(os.path.join(Handler._working_path, "generated", f"{inspect.stack()[1][3]}{differentiator}.mcfunction"), "w") as _file:
        _file.write(''.join(commands))

    # Get the function path and write the function call to the file
    function_path = Handler._get_function_path(inspect.stack()[1][3])  
    Handler._write(inspect.stack()[1][3], f"{execute_preset.output}run function {Handler._datapack_name}:{function_path}/generated/{inspect.stack()[1][3]}{differentiator}")

    Handler._status(f"Generated new function: {Handler._datapack_name}:{function_path}/generated/{inspect.stack()[1][3]}{differentiator}")

def tellraw(targets:Selector, text:json_string) -> None:
    if not isinstance(targets, Selector):
        raise ValueError(f"Expected selector object for 'targets', got {type(targets)}")
    if not isinstance(text, json_string):
        raise ValueError(f"Expected json_string object for 'text', got {type(text)}")
    Handler._write(inspect.stack()[1][3], f"tellraw {targets.build()} {text.output}")

def say(text:str) -> None:
    Handler._write(inspect.stack()[1][3], f"say {text}")