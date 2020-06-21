import enum
from typing import Union
from .selector import Selector
from .handler import Handler


def clear(targets: Selector, effects_to_remove: Union[list, enum.Enum]):
    """clear - Clears an effect from the targets.

    Args:
        targets (Selector): The entities to clear the effect from.
        effects_to_remove (Union[list, enum.Enum]): The effects to remove. If a list is provided, it will remove them all.

    Raises:
        ValueError: Raised if targets is not a selector object.

    Returns:
        list: The commands to be written.
    """
    cmds = []
    if not isinstance(targets, Selector):
        raise ValueError(f"Expected selector object for 'targets', got {type(targets)}")
    if isinstance(effects_to_remove, enum.Enum):
        if effects_to_remove.value == "all":
            Handler._write(f"effect clear {targets.build()}")
            return f"effect clear {targets.build()}"
        else:
            Handler._write(f"effect clear {targets.build()} {effects_to_remove.value}")
            return f"effect clear {targets.build()} {effects_to_remove.value}"
    elif isinstance(effects_to_remove, list):
        for effect in effects_to_remove:
            Handler._write(f"effect clear {targets.build()} {effect.value}")
            cmds.append(f"effect clear {targets.build()} {effect.value}")
        return cmds


def give(targets: Selector, effects: Union[list, enum.Enum], amplifier: int = None, length: int = None):
    """give [summary]

    Args:
        targets (Selector): The entities to apply the effect to.
        effects (Union[list, enum.Enum]): The effect(s) to add.
        amplifier (int, optional): The level of the effect. Defaults to None.
        length (int, optional): The amount of seconds the effect should last for. Defaults to None.

    Raises:
        ValueError: Raised if targets is not a selector object.

    Returns:
        list: The commands to be written.
    """
    cmds = []
    if not isinstance(targets, Selector):
        raise ValueError(f"Expected selector object for 'targets', got {type(targets)}")
    if isinstance(effects, enum.Enum):
        if effects.value == "all":
            Handler._write(f"effect give {targets.build()}")
            return f"effect give {targets.build()}"
        else:
            Handler._write(f"effect give {targets.build()} {effects.value} {length or ''} {amplifier or ''}")
            return f"effect give {targets.build()} {effects.value} {length or ''} {amplifier or ''}"
    elif isinstance(effects, list):
        for effect in effects:
            Handler._write(f"effect give {targets.build()} {effect.value} {length or ''} {amplifier or ''}")
            cmds.append(f"effect give {targets.build()} {effect.value} {length or ''} {amplifier or ''}")
        return cmds
