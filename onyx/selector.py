<<<<<<< Updated upstream
from .enums import at
from .handler import Handler, _buildable
=======
from typing import Union

from nbtlib.tag import Compound
>>>>>>> Stashed changes

from onyx.class_types import Buildable
from onyx.dev_util import (dict_to_advancement_selector,
                           dict_to_score_selector, translate)
from onyx.registries import entity_sort, gamemode, selector_type
from onyx.util import Range


<<<<<<< Updated upstream
class selector(_buildable):
    """Defines a selector
=======
class Selector(Buildable):
    """
    Selector - Represents a selector

    Args:
        type (selector_type, optional): The type of selector (``@e``, ``@s`, etc.). Defaults to selector_type.all_entities.
        advancements (dict, optional): The advancements of the entity. Defaults to None.
        distance (Union[int, Range], optional): The distance of the entity from a certain point. Defaults to None.
        dx (int, optional): How far away the entity can be from ``x`` in the positive X-axis. Defaults to None.
        dy (int, optional): How far away the entity can be from ``y`` in the positive Y-axis. Defaults to None.
        dz (int, optional): How far away the entity can be from ``z`` in the positive Z-axis. Defaults to None.
        gamemode (gamemode, optional): The gamemode of the entity. Defaults to None.
        level (int, optional): The experience points the entity must have. Defaults to None.
        limit (int, optional): The amount of entities that can be selected. Defaults to None.
        name (str, optional): The name of the entity. Defaults to None.
        nbt (Compound, optional): The NBT of the entity. Defaults to None.
        predicate (Union[str, list], optional): The predicates that must apply to the entity. Defaults to None.
        scores (dict, optional): The scores of the entity. Should be given as a dictionary with the keys being the objectives and the values being the values. Defaults to None.
        sort (entity_sort, optional): How the entities will be sorted if multiple are selected. Defaults to None.
        tag (Union[str, list], optional): The tags of the entity. If this is a list, then multiple ``tag`` entries will be created in the selector. Example: ``tag=["tag1", "tag2"]`` => ``tag=tag1, tag=2``. Defaults to None.
        team (Union[str, list], optional): The team of the entity. If this is a list, then multiple ``team`` entries will be created in the selector. Example: ``team=["team1", "team2"]`` => ``team=team1, team=team2``. However, this selector will always fail, since an entity can only be on one team. As such, a list should only be specified if you're negating multiple teams. Defaults to None.
        x (int, optional): The point on the X-axis of the entity. Defaults to None.
        y (int, optional): The point on the Y-axis of the entity. Defaults to None.
        z (int, optional): The point on the Z-axis of the entity. Defaults to None.
        x_rotation (Union[int, Range], optional): The rotation of the entity on the X-axis (vertical). Defaults to None.
        y_rotation (Union[int, Range], optional): The rotation of the entity on the Y-axis (horizontal). Defaults to None.
    """
    def __init__(self, type: selector_type = selector_type.all_entities, advancements: dict = None, 
                       distance: Union[int, Range] = None, dx: int = None, dy: int = None, dz: int = None, 
                       gamemode: gamemode = None, level: int = None, limit: int = None, name: str = None,
                       nbt: Compound = None, predicate: Union[str, list] = None, scores: dict = None,
                       sort: entity_sort = None, tag: Union[str, list] = None, team: Union[str, list] = None,
                       x: int = None, y: int = None, z: int = None, x_rotation: Union[int, Range] = None,
                       y_rotation: Union[int, Range] = None) -> None:
>>>>>>> Stashed changes

    Args:
        selector_type (at): The selector type (@a, @p, etc.).
        advancements (str, optional): Defaults to None.
        distance (Union[int, float], optional): Defaults to None.
        dx (Union[int, float], optional): Defaults to None.
        dy (Union[int, float], optional): Defaults to None.
        dz (Union[int, float], optional): Defaults to None.
        gamemode (mode, optional): Defaults to None.
        level (int, optional): Defaults to None.
        limit (int, optional): Defaults to None.
        name (str, optional): Defaults to None.
        nbt (str, optional): Defaults to None.
        predicate (str, optional): Defaults to None.
        scores (str, optional): Defaults to None.
        sort (sort, optional): Defaults to None.
        tag (str, optional): Defaults to None.
        team (str, optional): Defaults to None.
        type (str, optional): Defaults to None.
        x (int, optional): Defaults to None.
        y (int, optional): Defaults to None.
        z (int, optional): Defaults to None.
        x_rotation (Union[int, float], optional): Defaults to None.
        y_rotation (Union[int, float], optional): Defaults to None.
    """
    def __init__(self, selector_type: at, **kwargs):
        self._selector_type = Handler._translate(selector_type)
        self._args = {}
        self._change_args(kwargs)

<<<<<<< Updated upstream
    def _change_args(self, kwargs):
        for key, arg in kwargs.items():
            # Filter out the args that weren't assigned
            if arg is not None:
                # Skip over the "self" and "selector_type" arguments
                if key in {"self", "selector_type"}:
                    continue
                elif key == "name":
                    self._args[key] = f"'{arg}'"
                # Negated arguments, enum arguments, and any custom arguments are handled here
                else:
                    self._args[key] = Handler._translate(arg)
=======
    def build(self) -> str:
        """
        build - Returns the built selector

        Returns:
            str: The built selector
        """
        advancements, name, scores = None, None, None

        if self.advancements:
            advancements = dict_to_advancement_selector(self.advancements)
>>>>>>> Stashed changes

    # Merge the two dictionaries together, with the new one taking priority.
    def modify(self, **kwargs):
        """Modify arguments for an existing selector object.
        """
        self._args = {**self._args, **kwargs.items()}
        # Type checking isn't needed since _change_args already provides it
        self._change_args(self._args)

    # Remove an element. Default arguments aren't provided because then they'd have to specify a value
    def remove(self, *args):
        for arg in args:
            del self._args[arg]

    def build(self):
        _selector_args = []
        for key, value in self._args.items():
            if isinstance(value, tuple):
                for arg in value:
                    _selector_args.append(f"{key}={arg}")
            else:
                _selector_args.append(f"{key}={Handler._translate(value)}")

        # Don't include "[]" if no arguments were provided
        if len(_selector_args) > 0:
            return f"{self._selector_type}[{', '.join(_selector_args)}]"
        return f"{self._selector_type}"
