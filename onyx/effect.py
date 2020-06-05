import inspect
import enum
from typing import Union
from .selector import Selector
from .handler import Handler

def clear(targets:Selector, effects_to_remove:Union[list, enum.Enum]):
    if not isinstance(targets, Selector):
        raise ValueError(f"Expected selector objective for 'targets', got {type(targets)}")
    if isinstance(effects_to_remove, enum.Enum):
        if effects_to_remove.value == "all":
            Handler._write(inspect.stack()[1][3], f"effect clear {targets.build()}")
        else:
            Handler._write(inspect.stack()[1][3], f"effect clear {targets.build()} {effects_to_remove.value}")
    elif isinstance(effects_to_remove, list):
        for effect in effects_to_remove:
            Handler._write(inspect.stack()[1][3], f"effect clear {targets.build()} {effect.value}")
        return len(effects_to_remove)

def give(targets:Selector, effects:Union[list, enum.Enum], amplifier:int=None, length:int=None):
    if not isinstance(targets, Selector):
        raise ValueError(f"Expected selector objective for 'targets', got {type(targets)}")
    if isinstance(effects, enum.Enum):
        if effects.value == "all":
            Handler._write(inspect.stack()[1][3], f"effect give {targets.build()}")
        else:
            Handler._write(inspect.stack()[1][3], f"effect give {targets.build()} {effects.value} {length or ''} {amplifier or ''}")
    elif isinstance(effects, list):
        for effect in effects:
            Handler._write(inspect.stack()[1][3], f"effect give {targets.build()} {effect.value} {length or ''} {amplifier or ''}")
        return len(effects)