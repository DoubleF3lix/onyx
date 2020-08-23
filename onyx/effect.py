import enum
from typing import Union
from onyx.selector import selector
from onyx.handler import Handler


def clear(targets: selector, effects_to_remove: Union[list, enum.Enum]):
    """
    Args:
        targets (selector): The entities to clear the effect from.
        effects_to_remove (Union[list, enum.Enum]): The effects to remove. If a list is provided, it will remove them all.
    """
    if Handler._translate(effects_to_remove) == "all":
        effects_to_remove = ""
    if isinstance(effects_to_remove, list):
        for effect in effects_to_remove:
            Handler._cmds.append(f"effect clear {Handler._translate(targets)} {Handler._translate(effect)}")
    else:
        Handler._cmds.append(f"effect clear {Handler._translate(targets)} {Handler._translate(effects_to_remove)}")


def give(targets: selector, effects: Union[list, enum.Enum], amplifier: int = None, length: int = None):
    """
    Args:
        targets (selector): The entities to apply the effect to.
        effects (Union[list, enum.Enum]): The effect(s) to add.
        amplifier (int, optional): The level of the effect. Defaults to None.
        length (int, optional): The amount of seconds the effect should last for. Defaults to None.
    """
    if isinstance(effects, list):
        for effect in effects:
            Handler._cmds.append(f"effect give {Handler._translate(targets)} {Handler._translate(effect)} {length or ''} {amplifier or ''}")
    else:
        Handler._cmds.append(f"effect give {Handler._translate(targets)} {Handler._translate(effects)} {length or ''} {amplifier or ''}")
