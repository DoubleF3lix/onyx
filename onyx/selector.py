from typing import Union

from nbtlib.tag import Compound

from onyx.class_types import Buildable
from onyx.dev_util import (dict_to_advancement_selector,
                           dict_to_score_selector, translate)
from onyx.registries import entity_sort, gamemode, selector_type
from onyx.util import Range


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

        self.type = type
        self.advancements = advancements
        self.distance = distance
        self.dx = dx
        self.dy = dy
        self.dz = dz
        self.gamemode = gamemode
        self.level = level
        self.limit = limit
        self.name = name
        self.nbt = nbt
        self.predicate = predicate
        self.scores = scores
        self.sort = sort
        self.tag = tag
        self.team = team
        self.x = x
        self.y = y
        self.z = z
        self.x_rotation = x_rotation


    def build(self) -> str:
        """
        build - Returns the built selector

        Returns:
            str: The built selector
        """
        advancements, name, scores = None, None, None

        if self.advancements:
            advancements = dict_to_advancement_selector(self.advancements)

        if self.name:
            name = f"'{self.name}'"

        if self.scores:
            scores = dict_to_score_selector(self.scores)

        output = []
        for key, item in vars(self).items():
            if item and key != "type":
                if key in {"gamemode", "level", "name", "tag", "team", "predicate"} and isinstance(item, list):
                    for arg in item:
                        output.append(f"{translate(key)}={translate(arg)}")
                # This awful special case needs to exist because overwriting the class attributes makes building the selector more than once error out, and copying, overwriting, appending to output, and rewriting the copy back to the class attribute is even worse
                elif key == "advancements" and advancements:
                    output.append(f"{translate(key)}={translate(advancements)}")
                elif key == "name" and name:
                    output.append(f"{translate(key)}={translate(name)}")
                elif key == "scores" and scores:
                    output.append(f"{translate(key)}={translate(scores)}")
                else:
                    output.append(f"{translate(key)}={translate(item)}")

        if output:
            return f"{translate(self.type)}[{', '.join(output)}]"
        else:
            return translate(self.type)
