from typing import Union
from onyx.class_types import Buildable, Vector3, Vector2, Particle
from onyx.registries import click_event_action, hover_event_action
from onyx.split_registries.block import block
from onyx.split_registries.item import item
from onyx.split_registries.particle import particle
from onyx.dev_util import dict_to_block_state, translate
import nbtlib
from nbtlib.tag import *
import json


class Range(Buildable):
    def __init__(self, min: int = None, max: int = None):
        self.min = min
        self.max = max

    def build(self):
        return f"{self.min or ''}..{self.max or ''}"


class AbsPos(Buildable, Vector3):
    def __init__(self, x: int = None, y: int = None, z: int = None):
        super().__init__("", x, y, z)


class RelPos(Buildable, Vector3):
    def __init__(self, x: int = None, y: int = None, z: int = None):
        super().__init__("~", x, y, z)


class LocPos(Buildable, Vector3):
    def __init__(self, x: int = None, y: int = None, z: int = None):
        super().__init__("^", x, y, z)


class AbsPos2D(Buildable, Vector2):
    def __init__(self, x: int = None, y: int = None):
        super().__init__("", x, y)


class RelPos2D(Buildable, Vector2):
    def __init__(self, x: int = None, y: int = None):
        super().__init__("~", x, y)


class AbsRot(Buildable, Vector2):
    def __init__(self, x: int = None, y: int = None):
        super().__init__("", x, y)


class RelRot(Buildable, Vector2):
    def __init__(self, x: int = None, y: int = None):
        super().__init__("~", x, y)


class ClickEvent(Buildable):
    def __init__(self, action: click_event_action, value: str):
        self.action = translate(action)
        self.value = value

    def build(self):
        return {"action": self.action, "value": self.value}


class HoverEvent(Buildable):
    def __init__(self, action: hover_event_action = None, text: str = None, item_id: item = None, item_tags: dict = None):
        self.action = translate(action)
        self.text = text
        self.item_id = item_id
        self.item_tags = item_tags

    def build(self):
        if self.action == "show_text":
            return {"action": "show_text", "contents": translate(self.text)}
        elif self.action == "show_item":
            if self.item_tags:
                return {"action": "show_item", "contents": ({"id": self.item_id, "count": Byte(1), "tag": Compound(self.item_tags).snbt()})}
            else:
                return {"action": "show_item", "contents": ({"id": self.item_id, "count": Byte(1)})}


class Item(Buildable):
    def __init__(self, item_type: item, item_name: "TextComponent" = None):
        self.type = item_type
        self.set_name(item_name)
        self.lore = None
        self.tags = None

    def set_name(self, item_name: "TextComponent"):
        if item_name:
            self.name = json.dumps(translate(item_name))
        else:
            self.name = None

    def set_lore(self, *lore_lines: "TextComponent"):
        self.lore = translate(lore_lines, json_dump_elements=True)

    def add_lore(self, *lore_lines: "TextComponent"):
        self.lore.extend(translate(lore_lines, json_dump_elements=True))

    def build(self):
        item_data = Compound({"display": Compound()})
        if self.name:
            item_name = nbtlib.parse_nbt(String(json.dumps(self.name)))
            item_data["display"]["Name"] = item_name
        if self.lore:
            item_lore = nbtlib.parse_nbt(str(self.lore))
            item_data["display"]["Lore"] = item_lore

        return f"{self.type}{item_data.snbt()}"


def verify_optional_argument(particle_type, optional_argument):
    if particle_type in {"dust", "minecraft:dust"}:
        if optional_argument is None or len(optional_argument) != 4:
            raise ValueError(f"'optional_particle_argument' must be set to a tuple of 4 elements with particle type '{particle_type}'")
    elif particle_type in {"block", "minecraft:block", "falling_dust", "minecraft:falling_dust"}:
        if optional_argument is None:
            raise ValueError(f"'optional_particle_argument' must be set to a block with particle type '{particle_type}'")
    elif particle_type in {"item", "minecraft:item"}:
        if optional_argument is None:
            raise ValueError(f"'optional_particle_argument' must be set to an item with particle type '{particle_type}'")


class ParticleNormal(Buildable, Particle):
    def __init__(self, particle_type: particle, position: Vector3, delta: tuple, speed: float, count: int, optional_particle_argument: Union[tuple, block, item] = None):
        self.particle_type = translate(particle_type)
        self.position = translate(position)
        self.delta = translate(delta)
        self.speed = translate(speed)
        self.count = translate(count)
        self.optional_particle_argument = translate(optional_particle_argument)

        verify_optional_argument(particle_type, optional_particle_argument)

        if self.position is None and self.delta:
            raise ValueError("'delta' was defined but 'position' was not")

    def build(self):
        if self.optional_particle_argument:
            return f"{self.particle_type} {self.optional_particle_argument} {self.position} {self.delta} {self.speed} {self.count}"
        return f"{self.particle_type} {self.position} {self.delta} {self.speed} {self.count}"


class ParticleEntityEffectModified(Buildable, Particle):
    def __init__(self, particle_type: particle, position: Vector3, RGB: tuple, brightness: int = 128):
        self.particle_type = translate(particle_type)
        if self.particle_type not in {"entity_effect", "minecraft:entity_effect", "ambient_entity_effect", "minecraft:ambient_entity_effect"}:
            raise ValueError("'particle_type' must be either 'entity_effect' or 'ambient_entity_effect'")
        self.position = translate(position)
        self.RGB = translate(RGB)
        self.brightness = translate(brightness)

    def build(self):
        return f"{self.particle_type} {self.position} {self.RGB} {self.brightness} 0" # count


class ParticleMotion(Buildable, Particle):
    def __init__(self, particle_type: particle, position: Vector3, motion: tuple, motion_multiplier: Union[int, float], optional_particle_argument: Union[tuple, block, item] = None):
        self.particle_type = translate(particle_type)
        self.position = translate(position)
        self.motion = translate(motion)
        self.motion_multiplier = translate(motion_multiplier)
        self.optional_particle_argument = translate(optional_particle_argument)

        verify_optional_argument(particle_type, optional_particle_argument)

    def build(self):
        if self.optional_particle_argument:
            return f"{self.particle_type} {self.optional_particle_argument} {self.position} {self.motion} {self.motion_multiplier} 0"
        return f"{self.particle_type} {self.position} {self.motion} {self.motion_multiplier} 0" # count


class ParticleNoteModified(Buildable, Particle):
    def __init__(self, position: Vector3, color_modifier: int, color_multiplier: int):
        self.position = translate(position)
        self.color_modifier = translate(color_modifier)
        self.color_multiplier = translate(color_multiplier)

    def build(self):
        return f"minecraft:note {self.position} {self.color_modifier} 0 0 {self.color_multiplier} 0" # dy, dz, and count


class BlockPredicate(Buildable):
    def __init__(self, type: block, block_states: dict = None, nbt: Compound = None):
        self.block = block
        self.block_states = block_states
        self.nbt = nbt

    def build(self):
        return f"{translate(block)}{translate(dict_to_block_state(self.block_states)) if self.block_states else ''}{translate(self.nbt) if self.nbt else ''}"
