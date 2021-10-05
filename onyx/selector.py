from typing import Union
from onyx.registries import selector_type, gamemode, entity_sort
from onyx.util import Range
from onyx.dev_util import dict_to_score_selector, translate, dict_to_advancement_selector
from onyx.class_types import Buildable
from nbtlib.tag import Compound


class Selector(Buildable):
    def __init__(self, type: selector_type = selector_type.all_entities, advancements: dict = None, 
                       distance: Union[int, Range] = None, dx: int = None, dy: int = None, dz: int = None, 
                       gamemode: gamemode = None, level: int = None, limit: int = None, name: str = None,
                       nbt: Compound = None, predicate: Union[str, list] = None, scores: dict = None,
                       sort: entity_sort = None, tag: Union[str, list] = None, team: Union[str, list] = None,
                       x: int = None, y: int = None, z: int = None, x_rotation: Union[int, Range] = None,
                       y_rotation: Union[int, Range] = None):

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
        self.y_rotation = y_rotation

    def build(self):
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
