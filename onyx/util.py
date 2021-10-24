import uuid
from typing import Union

from nbtlib.tag import *

from onyx.class_types import Buildable, Particle, Vector2, Vector3
from onyx.dev_util import dict_to_block_state, translate
from onyx.registries import (
    attribute_modifier_mode,
    bossbar_location,
    click_event_action,
    data_type,
    hover_event_action,
    slot,
    source_type,
)
from onyx.split_registries.block import block
from onyx.split_registries.item import item
from onyx.split_registries.particle import particle


class Range(Buildable):
    """
    Range - Represents a range between two values

    Args:
        min (int, optional): The minimum value. Defaults to None.
        max (int, optional): The maximum value. Defaults to None.
    """

    def __init__(self, min: int = None, max: int = None) -> None:
        self.min = min
        self.max = max

    def build(self) -> str:
        """
        build - Returns the built range

        Raises:
            ValueError: Neither ``min`` nor ``max`` are specified

        Returns:
            str: The built range
        """
        if not self.min and not self.max:
            raise ValueError("Range must have either a minimum or a maximum value")
        return f"{self.min or ''}..{self.max or ''}"


class AbsPos(Buildable, Vector3):
    """
    AbsPos - Represents an absolute position

    Args:
        x (int, optional): X coordinate. Defaults to None.
        y (int, optional): Y coordinate. Defaults to None.
        z (int, optional): Z coordinate. Defaults to None.
    """

    def __init__(self, x: int = None, y: int = None, z: int = None) -> None:
        super().__init__("", x, y, z)


class RelPos(Buildable, Vector3):
    """
    RelPos - Represents a relative position

    Args:
        x (int, optional): X coordinate. Defaults to None.
        y (int, optional): Y coordinate. Defaults to None.
        z (int, optional): Z coordinate. Defaults to None.
    """

    def __init__(self, x: int = None, y: int = None, z: int = None) -> None:
        super().__init__("~", x, y, z)


class LocPos(Buildable, Vector3):
    """
    LocPos - Represents a local position

    Args:
        left (int, optional): Direction to the left of the entities rotation. Defaults to None.
        up (int, optional): Direction above the entities rotation. Defaults to None.
        forward (int, optional): Direction toward the entities location. Defaults to None.
    """

    def __init__(self, left: int = None, up: int = None, forward: int = None) -> None:
        super().__init__("^", left, up, forward)


class AbsPos2D(Buildable, Vector2):
    """
    AbsPos2D - Represents an absolute position in 2D

    Args:
        x (int, optional): X coordinate. Defaults to None.
        y (int, optional): Y coordinate. Defaults to None.
    """

    def __init__(self, x: int = None, y: int = None) -> None:
        super().__init__("", x, y)


class RelPos2D(Buildable, Vector2):
    """
    RelPos2D - Represents a relative position in 2D

    Args:
        x (int, optional): X coordinate. Defaults to None.
        y (int, optional): Y coordinate. Defaults to None.
    """

    def __init__(self, x: int = None, y: int = None) -> None:
        super().__init__("", x, y)


class AbsRot(Buildable, Vector2):
    """
    AbsRot - Represents an absolute rotation

    Args:
        x (int, optional): X (vertical) coordinate. Defaults to None.
        y (int, optional): Y (horizontal) coordinate. Defaults to None.
    """

    def __init__(self, x: int = None, y: int = None) -> None:
        super().__init__("", x, y)


class RelRot(Buildable, Vector2):
    """
    RelRot - Represents a relative rotation

    Args:
        x (int, optional): X (vertical) coordinate. Defaults to None.
        y (int, optional): Y (horizontal) coordinate. Defaults to None.
    """

    def __init__(self, x: int = None, y: int = None) -> None:
        super().__init__("", x, y)


class ClickEvent(Buildable):
    """
    ClickEvent - Represents a click event for text components

    Args:
        action (click_event_action): The action to perform
        value (str): The value to pass to the action (url, command, etc.)
    """

    def __init__(self, action: click_event_action, value: str) -> None:
        self.action = translate(action)
        self.value = translate(value)

    def build(self) -> str:
        """
        build - Returns the built click event

        Returns:
            str: The built click event
        """
        return {"action": self.action, "value": self.value}


class HoverEvent(Buildable):
    """
    HoverEvent - Represents a hover event for text components

    Args:
        action (hover_event_action): The action to perform (``show_text`` or ``show_item``)
        text (str, optional): The text to show. Only used if ``action`` is ``show_text``. Defaults to None.
        item_id (item, optional): The ID of the item to show. Only used if ``action`` is ``show_item``. Defaults to None.
        item_tags (dict, optional): The data value of the item to show. Only used if ``action`` is ``show_item``. Defaults to None.
    """

    def __init__(
        self,
        action: hover_event_action = None,
        text: str = None,
        item_id: item = None,
        item_tags: Compound = None,
    ) -> None:
        self.action = translate(action)
        self.text = translate(text)
        self.item_id = translate(item_id)
        self.item_tags = translate(item_tags)

    def build(self) -> str:
        """
        build - Returns the built hover event

        Returns:
            str: The built hover event
        """
        if self.action == "show_text":
            return {"action": "show_text", "contents": self.text}
        elif self.action == "show_item":
            if self.item_tags:
                return {
                    "action": "show_item",
                    "contents": (
                        {"id": self.item_id, "count": Byte(1), "tag": self.item_tags}
                    ),
                }
            else:
                return {
                    "action": "show_item",
                    "contents": ({"id": self.item_id, "count": Byte(1)}),
                }


class Item(Buildable):
    """
    Item - Defines an item with name, lore, and NBT tags

    Args:
        type (item): The ID of the item
        name (TextComponent, optional): The item name. Defaults to None.
        lore (list, optional): The lore of the item. Each item of the list should be its own text component. Defaults to None.
        tags (Compound, optional): The tags of the item. You must use an ``nbtlib.Compound`` object. Defaults to None.
    """

    def __init__(
        self,
        type: item,
        name: "TextComponent" = None,
        lore: list = None,
        tags: Compound = None,
    ) -> None:
        self.type = type
        self.name = translate(name)
        self.lore = translate(lore, keep_list=True)
        self.tags = tags

    def build(self) -> str:
        """
        build - Returns the built item

        Returns:
            str: The built item
        """
        item_data = self.tags or Compound({})
        if self.name:
            item_data["display"] = Compound({})
            item_data["display"]["Name"] = String(
                self.name
            )  # Convert to a string since that's what parse_nbt takes. We use parse_nbt to turn it into a format suitable for item data.
        if self.lore:
            item_data["display"] = Compound({})
            item_data["display"]["Lore"] = List[String](self.lore)

        return f"{self.type}{translate(item_data)}"


def _verify_optional_argument(
    particle_type: particle, optional_argument: Union[tuple, block, item]
):
    """
    _verify_optional_argument - Private method. Do not used. Used to check if an optional argument is valid for a particle type.

    Args:
        particle_type (particle)): The particle type
        optional_argument (Union[tuple, block, item]): The optional argument

    Raises:
        ValueError: Raised if type is ``dust`` and the optional argument is not a tuple of 4 elements or an optional argument was not supplied
        ValueError: Raised if type is ``block`` or ``falling_dust`` and an optional argument was not supplied
        ValueError: Raised if type is ``item`` and an optional argument was not supplied
    """
    if particle_type in {"dust", "minecraft:dust"}:
        if optional_argument is None or len(optional_argument) != 4:
            raise ValueError(
                f"'optional_particle_argument' must be set to a tuple of 4 elements with particle type '{particle_type}'"
            )
    elif particle_type in {
        "block",
        "minecraft:block",
        "falling_dust",
        "minecraft:falling_dust",
    }:
        if optional_argument is None:
            raise ValueError(
                f"'optional_particle_argument' must be set to a block with particle type '{particle_type}'"
            )
    elif particle_type in {"item", "minecraft:item"}:
        if optional_argument is None:
            raise ValueError(
                f"'optional_particle_argument' must be set to an item with particle type '{particle_type}'"
            )


class ParticleNormal(Buildable, Particle):
    """
    ParticleNormal - Represents a normal particle class

    Args:
        particle_type (particle): The type of particle
        position (Vector3): The position of the particle
        delta (tuple): The spread of the particle
        speed (float): How fast the particle moves
        count (int): How many particles there are
        optional_particle_argument (Union[tuple, block, item], optional): Any optional particle arguments. Should only be used with particle types ``dust``, ``block``, ``falling_dust``, or ``item``. If ``dust``, should be a tuple of 4 items representing RGBS (red, green, blue, size). If ``block`` or ``faling_dust``, should be a block ID. If ``item``, should be an item ID. Defaults to None.

    Raises:
        ValueError: Raised if an invalid optional argument is used
    """

    def __init__(
        self,
        particle_type: particle,
        position: Vector3,
        delta: tuple,
        speed: float,
        count: int,
        optional_particle_argument: Union[tuple, block, item] = None,
    ) -> None:
        self.particle_type = translate(particle_type)
        self.position = translate(position)
        self.delta = translate(delta)
        self.speed = translate(speed)
        self.count = translate(count)
        self.optional_particle_argument = translate(optional_particle_argument)

        _verify_optional_argument(particle_type, optional_particle_argument)

    def build(self) -> str:
        """
        build - Returns the built particle

        Returns:
            str: The built particle
        """
        if self.optional_particle_argument:
            return f"{self.particle_type} {self.optional_particle_argument} {self.position} {self.delta} {self.speed} {self.count}"
        return f"{self.particle_type} {self.position} {self.delta} {self.speed} {self.count}"


class ParticleEntityEffectModified(Buildable, Particle):
    """
    ParticleEntityEffectModified - Represents a particle with a modified entity effect (delta and speed act like RGBE values with a count of ``0``)

    Args:
        particle_type (particle): The particle type. Either ``entity_effect`` or ``ambient_entity_effect``.
        position (Vector3): The position of the particle
        RGB (tuple): The RGB color of the particle
        brightness (int, optional): The brightness of the particle. Defaults to 128.

    Raises:
        ValueError: Raised when particle type is not ``entity_effect`` or ``ambient_entity_effect``
    """

    def __init__(
        self,
        particle_type: particle,
        position: Vector3,
        RGB: tuple,
        brightness: int = 128,
    ) -> None:
        self.particle_type = translate(particle_type)
        if self.particle_type not in {
            "entity_effect",
            "minecraft:entity_effect",
            "ambient_entity_effect",
            "minecraft:ambient_entity_effect",
        }:
            raise ValueError(
                "'particle_type' must be either 'entity_effect' or 'ambient_entity_effect'"
            )
        self.position = translate(position)
        self.RGB = translate(RGB)
        self.brightness = translate(brightness)

    def build(self) -> str:
        """
        build - Returns the built particle

        Returns:
            str: The built particle
        """
        return f"{self.particle_type} {self.position} {self.RGB} {self.brightness} 0"  # count is 0


class ParticleMotion(Buildable, Particle):
    """
    ParticleMotion - Represents a particle with motion

    Args:
        particle_type (particle): The particle type
        position (Vector3): The position of the particle
        motion (tuple): The motion of the particle
        motion_multiplier (Union[int, float]): The motion multiplier of the particle
        optional_particle_argument (Union[tuple, block, item], optional): Any optional particle arguments. Should only be used with particle types ``dust``, ``block``, ``falling_dust``, or ``item``. If ``dust``, should be a tuple of 4 items representing RGBS (red, green, blue, size). If ``block`` or ``faling_dust``, should be a block ID. If ``item``, should be an item ID. Defaults to None.
    """

    def __init__(
        self,
        particle_type: particle,
        position: Vector3,
        motion: tuple,
        motion_multiplier: Union[int, float],
        optional_particle_argument: Union[tuple, block, item] = None,
    ) -> None:
        self.particle_type = translate(particle_type)
        self.position = translate(position)
        self.motion = translate(motion)
        self.motion_multiplier = translate(motion_multiplier)
        self.optional_particle_argument = translate(optional_particle_argument)

        _verify_optional_argument(particle_type, optional_particle_argument)

    def build(self) -> str:
        """
        build - Returns the built particle

        Returns:
            str: The built particle
        """
        if self.optional_particle_argument:
            return f"{self.particle_type} {self.optional_particle_argument} {self.position} {self.motion} {self.motion_multiplier} 0"
        return f"{self.particle_type} {self.position} {self.motion} {self.motion_multiplier} 0"  # count


class ParticleNoteModified(Buildable, Particle):
    """
    ParticleNoteModified - Represents a note particle with a custom color

    Args:
        position (Vector3): The position of the particle
        color_modifier (float): The color modifier of the particle. Should be from 0 to 1.
        color_multiplier (int): The color multiplier of the particle.
    """

    def __init__(
        self, position: Vector3, color_modifier: float, color_multiplier: int
    ) -> None:
        self.position = translate(position)
        self.color_modifier = translate(color_modifier)
        self.color_multiplier = translate(color_multiplier)

    def build(self) -> str:
        """
        build - Returns the built particle

        Returns:
            str: The built particle
        """
        return f"minecraft:note {self.position} {self.color_modifier} 0 0 {self.color_multiplier} 0"  # dy, dz, and count


class Block(Buildable):
    """
    Block - Defines a block with block states and NBT

    Args:
        type (block): The type of the block
        block_states (dict, optional): Block states. Should be given as a dictionary with keys being block state names and values being values. Defaults to None.
        nbt (Compound, optional): Any NBT on the block. Defaults to None.
    """

    def __init__(
        self, type: block, block_states: dict = None, nbt: Compound = None
    ) -> None:
        self.type = type
        self.block_states = block_states
        self.nbt = nbt

    def build(self) -> str:
        return f"{translate(self.type)}{translate(dict_to_block_state(self.block_states))}{translate(self.nbt)}"


# TODO implement UUID tracking and keep UUID for same attribute and value
class AttributeModifier(Buildable):
    """
    AttributeModifier - Defines an attribute modifier

    Args:
        name (str): The name of the attribute modifier
        value (Union[int, float]): The value of the attribute modifier
        mode (attribute_modifier_mode): How the attribute modifier will affect the modifier. Either ``add``, ``multiply``, or ``multiply_base``.
        uuid_override (str, optional): Override for the automatically generated UUID. Defaults to None.
    """

    def __init__(
        self,
        name: str,
        value: Union[int, float],
        mode: attribute_modifier_mode,
        uuid_override: str = None,
    ) -> None:
        self.name = name
        self.value = value
        self.mode = mode
        self.uuid = uuid_override or uuid.uuid4()

    def build(self, just_uuid: bool = False) -> str:
        """
        build - Returns the built attribute modifier

        Args:
            just_uuid (bool, optional): Whether or not just the UUID of the attribute modifier should be returned. Defaults to False.

        Returns:
            str: The built attribute modifier
        """
        if just_uuid:
            return translate(self.uuid)
        return f"{translate(self.uuid)} {translate(self.name)} {translate(self.value)} {translate(self.mode)}"


class DataSource(Buildable):
    """
    DataSource - Defines an NBT data location

    Args:
        source_type (source_type): The type of the location (``storage``, ``entity``, or ``block``)
        location (Union[Vector3, Selector, str): The data location
        path (Union[slot, str], optional): The data path. Defaults to None.
    """

    def __init__(
        self,
        source_type: source_type,
        location: Union[Vector3, "Selector", str],
        path: Union[slot, str] = None,
    ) -> None:
        self.source_type = source_type
        self.location = location
        self.path = path

    def build(self) -> str:
        """
        build - Returns the built data source

        Returns:
            str: The built data source
        """
        return f"{translate(self.source_type)} {translate(self.location)}{' ' + translate(self.path) if self.path else ''}"


class StoreTarget(Buildable):
    """
    StoreTarget - Defines a target for storing data

    Args:
        location (Union[Vector3, Selector, str, Bossbar): The location where the data should be stored
        path (Union[str, bossbar_location]): The path where the data should be stored
        data_type (data_type, optional): The data type of the location. Defaults to None.
        scale (Union[int, float], optional): The scale to store the data at. Defaults to None.
    """

    def __init__(
        self,
        location: Union[Vector3, "Selector", str, "Bossbar"],
        path: Union[str, bossbar_location],
        data_type: data_type = None,
        scale: Union[int, float] = None,
    ) -> None:
        self.location = location
        self.path = path
        self.data_type = data_type
        self.scale = scale

    def build(self) -> str:
        """
        build - Returns the built store target

        Returns:
            str: The built store target
        """
        return f"{translate(self.location)} {translate(self.path)}{' ' + translate(self.data_type) if self.data_type else ''}{' ' + str(translate(self.scale)) if self.scale else ''}"
