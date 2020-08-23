from typing import Union

from .enums import (advancement_action, selection, mode, difficulty, rule, enchants, mask_mode, clone_mode, fill_mode,
                    forceload_mode, structure, biome, sound_channel, container_type, container_slot, block, setblock_mode,
                    weather, entity)

from .util import AbsPos, Current2DPos, RelPos, LocPos, CurrentPos, Abs2DPos, Rel2DPos, Item, Particle
from .handler import Handler

from .execute import execute
from .selector import selector
from .json_string import json_string
from .pack_manager import Function


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


def clone(corner1: Union[AbsPos, RelPos, LocPos, CurrentPos, tuple, list], corner2: Union[AbsPos, RelPos, LocPos, CurrentPos, tuple, list], location: Union[AbsPos, RelPos, LocPos, CurrentPos, tuple, list], mask_mode: mask_mode = None, block_filter: str = None, clone_mode: clone_mode = None):
    """
    Args:
        corner1 (Union[AbsPos, RelPos, LocPos, CurrentPos, tuple, list]): The first corner of the area to be cloned
        corner2 (Union[AbsPos, RelPos, CurrentPos, LocPos, tuple, list]): The second corner of the area to be cloned
        location (Union[AbsPos, RelPos, CurrentPos, LocPos, tuple, list]): The location where the first corner should be cloned to
        mask_mode (mask_mode, optional): The mask mode (filtered, masked, and replace)
        block_filter (str, optional): The blocks to clone if "mask_mode" is set to "filtered". Defaults to None.
        clone_mode (clone_mode, optional): The clone mode (force, move, and normal). Defaults to None.
    """
    if Handler._translate(mask_mode) == "filtered":
        if block_filter is None:
            Handler._warn("'filtered' mask mode specified but not 'block_filter'. Switching to 'replace' mode.")
            mask_mode = "replace"
        else:
            Handler._cmds.append(f"clone {Handler._translate(corner1)} {Handler._translate(corner2)} {Handler._translate(location)} {Handler._translate(mask_mode)} {Handler._translate(block_filter)} {Handler._translate(clone_mode)}")
    else:
        Handler._cmds.append(f"clone {Handler._translate(corner1)} {Handler._translate(corner2)} {Handler._translate(location)} {Handler._translate(mask_mode)} {Handler._translate(clone_mode)}")


def defaultgamemode(gamemode: mode):
    """
    Args:
        gamemode (mode): The gamemode to set to
    """
    Handler._cmds.append(f"defaultgamemode {gamemode.value}")


def difficulty(level: difficulty):
    """
    Args:
        level (difficulty): The difficulty to set to
    """
    Handler._cmds.append(f"difficulty {level.value}")


def enchant(targets: selector, enchant_list: Union[list, enchants], level: int = None):
    """
    Args:
        targets (selector): The players on whom the enchantment should be applied
        enchant_list (Union[list, enchants]): The enchantment to apply
        level (int, optional): The level of the enchantment. Defaults to None.
    """
    if isinstance(enchant_list, list):
        for enchant in enchant_list:
            Handler._cmds.append(f"enchant {Handler._translate(targets)} {enchant.value} {level or ''}")
    else:
        Handler._cmds.append(f"enchant {Handler._translate(targets)} {enchant_list.value} {level or ''}")


def fill(corner1: Union[AbsPos, RelPos, LocPos, CurrentPos, tuple, list], corner2: Union[AbsPos, RelPos, LocPos, CurrentPos, tuple, list], block: str, fill_mode: fill_mode = None, replace_block: str = None):
    """
    Args:
        corner1 (Union[AbsPos, RelPos, LocPos, CurrentPos, tuple, list]): The first corner of the area to fill
        corner2 (Union[AbsPos, RelPos, LocPos, CurrentPos, tuple, list]): The second corner of the area to fill
        block (str): The block to fill with
        fill_mode (fill_mode, optional): The fill mode (destroy, hollow, keep, outline, and replace). Defaults to None.
        replace_block (str, optional): The block to replace if "fill_mode" is set to "replace". Defaults to None.
    """
    if Handler._translate(fill_mode) == "replace" and replace_block is None:
        Handler._warn("'replace' fill mode specified but not 'replace_block'. Switching to 'normal' mode.")
        fill_mode = None
    Handler._cmds.append(f"fill {Handler._translate(corner1)} {Handler._translate(corner2)} {Handler._translate(fill_mode)} {Handler._translate(replace_block)}")


def forceload(mode: forceload_mode, chunk_pos1: Union[Abs2DPos, Rel2DPos], chunk_pos2: Union[Abs2DPos, Rel2DPos]):
    """
    Args:
        mode (forceload_mode): The forceload mode (add, query, and remove)
        chunk_pos1 (Union[AbsChunkPos, RelChunkPos]): The coordinates that the chunk contains
        chunk_pos2 (Union[AbsChunkPos, RelChunkPos]): The second set of coordinates that the chunk contains. Allows for forceloading an area of chunks.
    """
    Handler._cmds.append(f"forceload {Handler._translate(mode)} {Handler._translate(chunk_pos1)} {Handler._translate(chunk_pos2)}")


def call(function: Function):
    Handler._cmds.append(f"function {function._mcfunction_path}")

def gamemode(targets: selector, mode: mode):
    """
    Args:
        targets (selector): The players whose gamemode should be set
        mode (mode): The gamemode that should be set
    """
    Handler._cmds.append(f"gamemode {Handler._translate(mode)} {Handler._translate(targets)}")


def gamerule(rule: rule, value: str):
    """
    Args:
        rule (rule): The gamerule that should be modified
        value (str): The value the gamerule should be set to
    """
    Handler._cmds.append(f"gamerule {Handler._translate(rule)} {value}")


def give(targets: selector, item: Item, count: int = 1):
    """
    Args:
        targets (selector): The players to give the item to
        item (Item): The item to be given
        count (int, optional): How much of the item (up to 64). Defaults to 1.
    """
    Handler._cmds.append(f"give {Handler._translate(targets)} {Handler._translate(item)} {Handler._translate(count)}")


def kill(targets: selector):
    """
    Args:
        targets (slector): The entities to kill
    """
    Handler._cmds.append(f"kill {Handler._translate(targets)}")


def locate(structure: structure):
    """
    Args:
        structure (structure): The structure to locate
    """
    Handler._cmds.append(f"locate {Handler._translate(structure)}")


def locatebiome(biome: biome):
    """
    Args:
        biome (biome): The biome to locate
    """
    Handler._cmds.append(f"locate {Handler._translate(biome)}")


def particle(particle: Particle, force: bool = False, targets: selector = None):
    """
    Args:
        particle (Particle): The particle itself and its attributes
        force (bool, optional): Defaults to False.
        targets (selector, optional): The player to display the particle to. Defaults to None.
    """
    Handler._cmds.append(f"particle {Handler._translate(particle)} {'force' if force else 'normal'} {Handler._translate(targets)}")


def playsound(sound: str, sound_channel: sound_channel, targets: selector, position: Union[AbsPos, RelPos, LocPos, CurrentPos], volume: int = 1, pitch: int = 1, min_volume: int = 1):
    """
    Args:
        sound (str): The sound to be played
        sound_channel (sound_channel): The channel the sound should be played through (music, neutral, ambient, etc.)
        targets (selector): The players the sound should be played to
        position (Union[AbsPos, RelPos, LocPos, CurrentPos]): Where the sound should be played
        volume (int, optional): How many blocks away from the position the sound should be audible. Defaults to None.
        pitch (int, optional): The pitch of the sound. Defaults to None.
        min_volume (int, optional): The minimum volume the sound should be played at. Defaults to None.
    """
    if Handler._translate(sound_channel) == "*":
        Handler._warn("'*' (any) sound channel is supported by playsound. Assuming 'master'.")
        sound_channel = sound_channel.master

    if pitch > 2 and pitch < 0:
        Handler._warn("'pitch' should be between 0 and 2")

    Handler._cmds.append(f"playsound {Handler._translate(sound)} {Handler._translate(sound_channel)} {Handler._translate(targets)} {Handler._translate(position)} {Handler._translate(volume)} {Handler._translate(pitch)} {Handler._translate(min_volume)}")


def replaceitem(container_type: container_type, container_location: Union[selector, AbsPos, LocPos, RelPos], slot: container_slot, item: Item):
    """
    Args:
        container_type (container_type): The container type (block or entity)
        container_location (Union[selector, AbsPos, LocPos, RelPos]): The selector of the entity or the coordinates of the block to modify
        slot (container_slot): The slot to modify
        item (Item): The item to be put into the slot
    """
    if Handler._translate(container_type) == "storage":
        Handler._warn("Container type 'storage' isn't supported for 'replaceitem'")

    Handler._translate(f"replaceitem {Handler._translate(container_type)} {Handler._translate(container_location)} {Handler._translate(slot)} {Handler._translate(item)}")


def say(text: str):
    """
    Args:
        text (str): The text to print.
    """
    Handler._cmds.append(f"say {text}")


def setblock(position: Union[AbsPos, RelPos, LocPos, CurrentPos], block: block, setblock_mode: setblock_mode = None):
    """
    Args:
        position (Union[AbsPos, RelPos, LocPos, CurrentPos]): The block position
        block (block): The block to place
        setblock_mode (setblock_mode, optional): The setblock mode (destroy, keep, replace). Defaults to None.
    """
    Handler._cmds.append(f"setblock {Handler._translate(position)} {Handler._translate(block)} {Handler._translate(setblock_mode)}")


def setworldspawn(position: Union[AbsPos, RelPos, LocPos, CurrentPos], angle: Union[int, float] = None):
    """
    Args:
        position (Union[AbsPos, RelPos, LocPos, CurrentPos]): The coordinates of the new spawn
        angle (Union[int, float], optional): The Y axis the player should be facing on spawn. Defaults to None.
    """
    Handler._cmds.append(f"setworldspawn {Handler._translate(position)} {Handler._translate(angle)}")


def spawnpoint(targets: selector, position: Union[AbsPos, RelPos, LocPos, CurrentPos], angle: Union[int, float] = None):
    """
    Args:
        targets (selector): The players whose spawn should be set
        position (Union[AbsPos, RelPos, LocPos, CurrentPos]): The coordinates of the new spawn
        angle (Union[int, float], optional): The Y axis the player should be facing on spawn. Defaults to None.
    """
    Handler._cmds.append(f"spawnpoint {Handler._translate(targets)} {Handler._translate(position)} {Handler._translate(angle)}")


def spectate(target: selector, source: selector = "@s"):
    """
    Args:
        target (selector): The entity to be spectated
        source (selector, optional): The entity that should spectate. Defaults to "@s".
    """
    Handler._cmds.append(f"spectate {Handler._translate(target)} {Handler._translate(source)}")


def spreadplayers(center: Union[Abs2DPos, Rel2DPos, Current2DPos], spread_distance: int, max_spread: int, targets: selector, respect_teams: bool = False, max_height: int = None):
    if max_height is not None:
        Handler._cmds.append(f"spreadplayers {Handler._translate(center)} {Handler._translate(spread_distance)} {Handler._translate(max_spread)} under {Handler._translate(max_height)} {Handler._translate(respect_teams)} {Handler._translate(targets)}")
    else:
        Handler._cmds.append(f"spreadplayers {Handler._translate(center)} {Handler._translate(spread_distance)} {Handler._translate(max_spread)} {Handler._translate(respect_teams)} {Handler._translate(targets)}")


def stopsound(targets: selector, sound_channel: sound_channel = None, sound: str = None):
    if sound_channel is not None and sound is None:
        Handler._warn("'sound_channel' specified but not 'sound'. Ignoring.")
        sound_channel = None

    if sound_channel is None and sound is not None:
        Handler._warn("'sound' specified but not 'sound_channel'. Assuming 'master' for 'sound_channel'.")
        sound_channel = "master"

    Handler._cmds.append(f"stopsound {Handler._translate(targets)} {Handler._translate(sound_channel)} {Handler._translate(sound)}")


def summon(entity: entity, position: Union[selector, AbsPos, RelPos, LocPos, CurrentPos], nbt: str = None):
    Handler._cmds.append(f"summon {Handler._translate(entity)} {Handler._translate(position)} {Handler._translate(nbt)}")


def teleport(targets: selector, destination: Union[selector, AbsPos, RelPos, LocPos, CurrentPos], facing: Union[selector, AbsPos, RelPos, LocPos, CurrentPos] = None, facing_type: container_type = container_type.entity):
    if facing is None:
        Handler._cmds.append(f"teleport {Handler._translate(targets)} {Handler._translate(destination)}")
    else:
        # Get the container type
        if Handler._translate(facing_type) == "storage":
            Handler._warn("Container type 'storage' is not supported for 'teleport'. Assuming 'block'.")
            facing = container_type.block
        elif Handler._translate(facing).startswith("@"):
            facing_type = container_type.entity
        elif isinstance(facing, (AbsPos, RelPos, LocPos, CurrentPos)):
            facing_type = container_type.block

        # Modify the end of the command depending on whether or not the facing type is an entity
        if Handler._translate(facing_type) == "entity":
            cmd_suffix = f"facing entity {Handler._translate(facing)}"
        else:
            cmd_suffix = f"facing {Handler._translate(facing)}"

        # Allows for facing a block or entity if the destination is a selector
        if Handler._translate(destination).startswith("@"):
            Handler._cmds.append(f"execute as {Handler._translate(targets)} at {Handler._translate(destination)} run tp @s ~ ~ ~ {cmd_suffix}")
        else:
            Handler._cmds.append(f"teleport {Handler._translate(targets)} {Handler._translate(destination)} {cmd_suffix}")


def tellraw(targets: selector, text: json_string):
    """
    Args:
        targets (selector): The players to print the text to.
        text (json_string): The text to print.
    """
    Handler._cmds.append(f"tellraw {Handler._translate(targets)} {Handler._translate(text, convert=True)}")


def weather(weather_mode: weather):
    """
    Args:
        weather_mode (weather): The weather type (clear, rain, thunder)
    """
    Handler._cmds.append(f"weather {Handler._translate(weather_mode)}")
