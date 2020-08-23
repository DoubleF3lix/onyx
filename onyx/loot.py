from typing import Union
from .handler import Handler
from .selector import selector
from .enums import loot_type, AbsPos, RelPos, LocPos, CurrentPos, item, container_type


def _multi_loot(command_name, targets, loot_type, loot_table, killed_entity, mined_block, item_used):
    if Handler._translate(loot_type) in {"fish", "loot"}:
        if loot_table is None:
            Handler._warn(f"'loot_table' not specified for loot type '{Handler._translate(loot_type)}'. Ignoring command.")
        else:
            Handler._cmds.append(f"loot {command_name} {Handler._translate(targets)} {Handler._translate(loot_type)} {Handler._translate(loot_table)}")
    elif Handler._translate(loot_type) == "kill":
        if killed_entity is None:
            Handler._warn("'killed_entity' not specified for loot type 'kill'. Ignoring command.")
        else:
            Handler._cmds.append(f"loot {command_name} {Handler._translate(targets)} kill {Handler._translate(killed_entity)}")
    elif Handler._translate(loot_type) == "mine":
        if mined_block is None:
            Handler._warn("'mined_block' not specified for loot type 'mine'. Ignoring command.")
        else:
            if item_used is None:
                Handler._warn("Loot type 'mine' specified but not 'item_used'. Assuming 'mainhand'.")
                item_used = "mainhand"
            Handler._cmds.append(f"loot {command_name} {Handler._translate(targets)} mine {Handler._translate(item_used)}")


def give(targets: selector, loot_type: loot_type, loot_table: str = None, killed_entity: selector = None, mined_block: Union[AbsPos, RelPos, LocPos, CurrentPos] = None, item_used: Union[item, str] = "mainhand"):
    """
    Args:
        targets (selector): The entities to give the loot to
        loot_type (loot_type): The loot type (fish, kill, loot, mine)
        loot_table (str, optional): The loot table to give. Only specify if "loot_type" is "fish" or "loot". Defaults to None.
        killed_entity (selector, optional): Only specify if "loot_table" is "kill". Defaults to None.
        mined_block (Union[AbsPos, RelPos, LocPos, CurrentPos], optional): Only specify if "loot_table" is "mine". Defaults to None.
        item_used (Union[item, str], optional): The item used to break the block. Only specify if "loot_type" is "mine". Defaults to mainhand.
    """
    _multi_loot("give", targets, loot_type, loot_table, killed_entity, mined_block, item_used)


def insert(block: Union[AbsPos, RelPos, LocPos, CurrentPos], loot_type: loot_type, loot_table: str = None, killed_entity: selector = None, mined_block: Union[AbsPos, RelPos, LocPos, CurrentPos] = None, item_used: Union[item, str] = None):
    """
    Args:
        block (Union[AbsPos, RelPos, LocPos, CurrentPos]): The block to insert the loot into
        loot_type (loot_type): The loot type (fish, kill, loot, mine)
        loot_table (str, optional): The loot table to give. Only specify if "loot_type" is "fish" or "loot". Defaults to None.
        killed_entity (selector, optional): Only specify if "loot_table" is "kill". Defaults to None.
        mined_block (Union[AbsPos, RelPos, LocPos, CurrentPos], optional): Only specify if "loot_table" is "mine". Defaults to None.
        item_used (Union[item, str], optional): The item used to break the block. Only specify if "loot_type" is "mine". Defaults to mainhand.
    """
    _multi_loot("insert", block, loot_type, loot_table, killed_entity, mined_block, item_used)


def spawn(location: Union[AbsPos, RelPos, LocPos, CurrentPos], loot_type: loot_type, loot_table: str = None, killed_entity: selector = None, mined_block: Union[AbsPos, RelPos, LocPos, CurrentPos] = None, item_used: Union[item, str] = None):
    """
    Args:
        location (Union[AbsPos, RelPos, LocPos, CurrentPos]): The coordinates to spawn the loot at
        loot_type (loot_type): The loot type (fish, kill, loot, mine)
        loot_table (str, optional): The loot table to give. Only specify if "loot_type" is "fish" or "loot". Defaults to None.
        killed_entity (selector, optional): Only specify if "loot_table" is "kill". Defaults to None.
        mined_block (Union[AbsPos, RelPos, LocPos, CurrentPos], optional): Only specify if "loot_table" is "mine". Defaults to None.
        item_used (Union[item, str], optional): The item used to break the block. Only specify if "loot_type" is "mine". Defaults to mainhand.
    """
    _multi_loot("spawn", location, loot_type, loot_table, killed_entity, mined_block, item_used)


def replace(target_type: container_type, target: Union[selector, AbsPos, RelPos, LocPos, CurrentPos], slot: container_type, loot_type: loot_type, loot_table: str = None, killed_entity: selector = None, mined_block: Union[AbsPos, RelPos, LocPos, CurrentPos] = None, item_used: Union[item, str] = None):
    """
    Args:
        target_type (container_type): The target type to replace the loot of (block, entity)
        target (Union[selector, AbsPos, RelPos, LocPos, CurrentPos]): The coordinates of the block or the selector of the entity
        slot (container_type): The slot to replace
        loot_type (loot_type): The loot type (fish, kill, loot, mine)
        loot_table (str, optional): The loot table to give. Only specify if "loot_type" is "fish" or "loot". Defaults to None.
        killed_entity (selector, optional): Only specify if "loot_table" is "kill". Defaults to None.
        mined_block (Union[AbsPos, RelPos, LocPos, CurrentPos], optional): Only specify if "loot_table" is "mine". Defaults to None.
        item_used (Union[item, str], optional): The item used to break the block. Only specify if "loot_type" is "mine". Defaults to mainhand.
    """
    if Handler._translate(target_type) == "storage":
        Handler._warn("Container type 'storage' isn't supported for 'target_type'")

    if Handler._translate(loot_type) in {"fish", "loot"}:
        if loot_table is None:
            Handler._warn(f"'loot_table' not specified for loot type '{Handler._translate(loot_type)}'. Ignoring command.")
        else:
            Handler._cmds.append(f"loot replace {Handler._translate(target_type)} {Handler._translate(target)} {Handler._translate(slot)} {Handler._translate(loot_type)} {Handler._translate(loot_table)}")
    elif Handler._translate(loot_type) == "kill":
        if killed_entity is None:
            Handler._warn("'killed_entity' not specified for loot type 'kill'. Ignoring command.")
        else:
            Handler._cmds.append(f"loot replace {Handler._translate(target_type)} {Handler._translate(target)} {Handler._translate(slot)} kill {Handler._translate(killed_entity)}")
    elif Handler._translate(loot_type) == "mine":
        if mined_block is None:
            Handler._warn("'mined_block' not specified for loot type 'mine'. Ignoring command.")
        else:
            if item_used is None:
                Handler._warn("Loot type 'mine' specified but not 'item_used'. Assuming 'mainhand'.")
                item_used = "mainhand"
            Handler._cmds.append(f"loot replace {Handler._translate(target_type)} {Handler._translate(target)} {Handler._translate(slot)} mine {Handler._translate(item_used)}")
