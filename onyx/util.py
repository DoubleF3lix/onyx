<<<<<<< Updated upstream
import json
from typing import Union
from nbtlib.tag import *
from nbtlib import parse_nbt
=======
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
>>>>>>> Stashed changes

from .selector import selector
from .enums import item, action as action_enum, particles, item, block
from .handler import Handler, _buildable, _position

<<<<<<< Updated upstream

class SetFrom(_buildable):
    """Used with data.modify() when setting from an entity

    Args:
        target (Union[str, tuple, selector]): The entity that the data should be retrieved from
        path (str): The data location
        index (int, optional): [description]. The index of the data. Only use if the path is a list. Defaults to None.
        container_type (str, optional): Override for container type (entity, storage, or block). If unspecified, the container type will be assumed based off the value for ``target``. Defaults to None.
    """
    def __init__(self, target: Union[str, tuple, selector], path: str, index: int = None, container_type: str = None):
        if container_type:
            self.container_type = container_type
        else:
            if isinstance(target, str):
                self.container_type = "storage"
            elif isinstance(target, tuple):
                self.container_type = "block"
                self.target = ' '.join(target)
            elif isinstance(target, selector):
                self.container_type = "entity"
                self.target = target.build()

    def build(self):
        if self.index is not None:
            return f"{self.index} from {self.container_type} {self.target} {self.path}"
        else:
            return f"from {self.container_type} {self.target} {self.path}"


class SetTo(_buildable):
    """Used with data.modify() when setting to a value
=======
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
>>>>>>> Stashed changes

    Args:
        data (str): The value to be set.
        index (int, optional): The index of a list that should be modified. Only use if the path is a list. Defaults to None.
    """
    def __init__(self, data: str, index: int = None):
        self.data = data
        self.index = index

<<<<<<< Updated upstream
    def build(self):
        if self.index is not None:
            return f"{self.index} value {self.data}"
        else:
            return f"value {self.data}"


class Negate(_buildable):
    """Negates an argument
=======
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
>>>>>>> Stashed changes

    Args:
        arg: The argument to negate
    """
    def __init__(self, arg):
        self.arg = arg

<<<<<<< Updated upstream
    def build(self):
        return f"!{Handler._translate(self.arg)}"


class Range(_buildable):
    """Defines a scoreboard range
=======
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
        super().__init__("~", x, y)
>>>>>>> Stashed changes

    Args:
        min (int, optional): The minimum value the score should be (inclusive). If unspecified, the range will check for all scores equal to or below the maximum. Defaults to None.
        max (int, optional): The maximum value the score should be (inclusive). If unspecified, the range will check for all scores equal to or below the minimum. Defaults to None.
    """
    def __init__(self, min: int = None, max: int = None):
        if min is None and max is None:
            Handler._warn("'min' and 'max' were not assigned")
        self.min = min
        self.max = max

<<<<<<< Updated upstream
    def build(self):
        return f"{self.min or ''}..{self.max or ''}"


class ClickEvent(_buildable):
    """Used with JSON strings
=======
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
        super().__init__("~", x, y)
>>>>>>> Stashed changes

    Args:
        action (action_enum, optional): The action type.
        value (str, optional): The argument of the action.
    """
    def __init__(self, action: action_enum, value: str):
        # Check if an invalid action was used
        if Handler._translate(action) in {"show_text", "show_item"}:
            Handler._warn(f"{Handler._translate(action)} is exclusive to hover_event")

<<<<<<< Updated upstream
        self.action = Handler._translate(action)
        self.value = value

    def build(self):
        return {"action": self.action, "contents": self.value}


class HoverEvent(_buildable):
    """Used with JSON strings
=======
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
>>>>>>> Stashed changes

    Args:
        action (action_enum, optional): The action type. Defaults to None.
        text (str, optional): The text to show on hover. Only used if ``action`` is set to ``show_text``. Defaults to None.
        item_id (str, optional): The item to show on hover. Only used if ``action`` is set to ``show_item``. Defaults to None.
        item_tags (dict, optional): The tags the item should have. Defaults to None.
    """
    def __init__(self, action: action_enum = None, text: str = None, item_id: str = None, item_tags: dict = None):
        # Check if an invalid action was used
        if Handler._translate(action) not in {"show_text", "show_item"}:
            Handler._warn(f"{Handler._translate(action)} is exclusive to click_event")

<<<<<<< Updated upstream
        self.action = Handler._translate(action)
        self.text = text
        self.item_id = item_id
        self.item_tags = item_tags
=======
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
>>>>>>> Stashed changes

    def build(self) -> str:
        """
        build - Returns the built hover event

        Returns:
            str: The built hover event
        """
        if self.action == "show_text":
<<<<<<< Updated upstream
            return {"action": "show_text", "contents": Handler._translate(self.text)}
        elif self.action == "show_item":
            if self.item_tags is not None:
                return {"action": "show_item", "contents": ({"id": self.item_id, "count": Byte(1), "tag": Compound(self.item_tags).snbt()})}
=======
            return {"action": "show_text", "contents": self.text}
        elif self.action == "show_item":
            if self.item_tags:
                return {
                    "action": "show_item",
                    "contents": (
                        {"id": self.item_id, "count": Byte(1), "tag": self.item_tags}
                    ),
                }
>>>>>>> Stashed changes
            else:
                return {
                    "action": "show_item",
                    "contents": ({"id": self.item_id, "count": Byte(1)}),
                }


<<<<<<< Updated upstream
class AbsPos(_buildable, _position):
    """Defines an absolute position (exact coordinates)

    Args:
        x (Union[int, float])
        y (Union[int, float])
        z (Union[int, float])

    Raises:
        ValueError: Raised when any of the arguments is not a number
    """
    def __init__(self, x: Union[int, float], y: Union[int, float], z: Union[int, float]):
        if not all(isinstance(arg, (int, float)) for arg in [x, y, z]):
            raise ValueError("You must supply 3 numbers")

        self.x = x
        self.y = y
        self.z = z

    def build(self):
        return f"{self.x} {self.y} {self.z}"


class RelPos(_buildable, _position):
    """Defines a relative position (relative to an entity, block, etc.)

    Args:
        x (Union[int, float])
        y (Union[int, float])
        z (Union[int, float])
=======
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
>>>>>>> Stashed changes

    Raises:
        ValueError: Raised when any of the arguments is not a number
    """
    def __init__(self, x: Union[int, float], y: Union[int, float], z: Union[int, float]):
        if not all(isinstance(arg, (int, float)) for arg in [x, y, z]):
            raise ValueError("You must supply 3 numbers")

<<<<<<< Updated upstream
        self.x = x
        self.y = y
        self.z = z

    def build(self):
        return f"~{self.x} ~{self.y} ~{self.z}"


class LocPos(_buildable, _position):
    """Defines a local position (relatve to the direction an entity is facing)

    Args:
        left (Union[int, float])
        up (Union[int, float])
        forward (Union[int, float])

    Raises:
        ValueError: Raised when any of the arguments is not a number
    """
    def __init__(self, left: Union[int, float], up: Union[int, float], forward: Union[int, float]):
        if not all(isinstance(arg, (int, float)) for arg in [left, up, forward]):
            raise ValueError("You must supply 3 numbers")

        self.left = left
        self.up = up
        self.forward = forward

    def build(self):
        return f"^{self.left} ^{self.up} ^{self.forward}"


class CurrentPos(_buildable, _position):
    """
    Args:
        rotation (bool): Whether or not rotation should be included in this position (~ ~ ~ ~ ~). Defaults to False.
    """
    def __init__(self, rotation: bool = False):
        self.rotation = rotation

    def build(self):
        if self.rotation is True:
            return "~ ~ ~ ~ ~"
        return "~ ~ ~"


class AbsRot(_buildable, _position):
    """Defines an absolute rotation

    Args:
        y_rot (Union[int, float])
        x_rot (Union[int, float])

    Raises:
        ValueError: Raised when any of the arguments is not a number
        """
    def __init__(self, y_rot: Union[int, float], x_rot: Union[int, float]):
        if not all(isinstance(arg, (int, float)) for arg in [y_rot, x_rot]):
            raise ValueError("You must supply 2 numbers")

        self.y_rot = y_rot
        self.x_rot = x_rot

    def build(self):
        return f"{self.y_rot} {self.x_rot}"


class RelRot(_buildable, _position):
    """Defines a relative rotation (relative to the target's current rotation)
=======
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
>>>>>>> Stashed changes

    Args:
        y_rot (Union[int, float])
        x_rot (Union[int, float])

<<<<<<< Updated upstream
    Raises:
        ValueError: Raised when any of the arguments is not a number
    """
    def __init__(self, y_rot: Union[int, float], x_rot: Union[int, float]):
        if not all(isinstance(arg, (int, float)) for arg in [y_rot, x_rot]):
            raise ValueError("You must supply 2 numbers")

        self.y_rot = y_rot
        self.x_rot = x_rot

    def build(self):
        return f"~{self.y_rot} ~{self.x_rot}"


class Abs2DPos(_buildable, _position):
    """Defines an absolute position without a y-coordinate

    Args:
        x_pos (Union[int, float])
        y_pos (Union[int, float])
    """
    def __init__(self, x_pos: Union[int, float], z_pos: Union[int, float]):
        if not all(isinstance(arg, (int, float)) for arg in [x_pos, z_pos]):
            raise ValueError("You must supply 2 numbers")

        self.x_pos = x_pos
        self.z_pos = z_pos

    def build(self):
        return f"{self.x_pos} {self.z_pos}"


class Rel2DPos(_buildable, _position):
    """Defines an absolute position without a y-coordinate

    Args:
        x_pos (Union[int, float])
        y_pos (Union[int, float])
    """
    def __init__(self, x_pos: Union[int, float], z_pos: Union[int, float]):
        if not all(isinstance(arg, (int, float)) for arg in [x_pos, z_pos]):
            raise ValueError("You must supply 2 numbers")

        self.x_pos = x_pos
        self.z_pos = z_pos

    def build(self):
        return f"~{self.x_pos} ~{self.z_pos}"


class Current2DPos(_buildable, _position):
    @staticmethod
    def build():
        return "~ ~"


class Item(_buildable):
    """Item builder

    Args:
        item_type (item): The item name (stone, brick, etc.)
        item_name (json_string): The custom name of the item. Defaults to None.
    """
    def __init__(self, item_type: item, item_name: "json_string" = None):
        self.type = item_type
        self.set_name(item_name)
        self.lore = None
        self.tags = None

    def set_name(self, item_name: "json_string"):
        """Set the name of the item

        Args:
            item_name (json_string): The custom name of the item.
        """
        if item_name is not None:
            self.name = json.dumps(Handler._translate(item_name))
        else:
            self.name = None

    def set_lore(self, *lore_lines: "json_string"):
        """Overwrites all the old lore and replaces it with new lore

        Args:
            *lore_lines (json_string): The new lore to set
        """
        self.lore = Handler._translate(lore_lines, item=True)

    def add_lore(self, *lore_lines: "json_string"):
        """Adds to the existing item lore

        Args:
            *lore_lines (json_string): The new lore to add
        """
        self.lore.extend(Handler._translate(lore_lines, item=True))

    def build(self):
        item_data = Compound({"display": Compound()})
        if self.name is not None:
            item_name = parse_nbt(String(json.dumps(self.name)))
            item_data["display"]["Name"] = item_name
        if self.lore is not None:
            item_lore = parse_nbt(str(self.lore))
            item_data["display"]["Lore"] = item_lore

        return f"{self.type}{item_data.snbt()}"
=======
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
>>>>>>> Stashed changes

        Returns:
            str: The built particle
        """
        return f"minecraft:note {self.position} {self.color_modifier} 0 0 {self.color_multiplier} 0"  # dy, dz, and count

<<<<<<< Updated upstream
class Particle(_buildable):
    """Defines a particle for use in particle command

    Args:
        particle_name (particle): The particle type (cloud, barrier, etc.)
        position (AbsPos, optional): The position of the particle. Defaults to None.
        delta (AbsPos, optional): The size of the particle area. Defaults to None.
        speed (int, optional): How quickly the particle vanishes. Defaults to None.
        count (int, optional): How many particles. Defaults to None.
        motion (AbsPos, optional): The motion of a particle. Sets the count to 0 and nullifies the ``delta`` parameter. Defaults to None.
        RGB (tuple, optional): Used for particle ``entity_effect`` and ``ambient_entity_effect``. Defaults to None.
        dust_color (tuple, optional): The color of the ``dust`` particle. Only specify if ``particle_name`` is set to ``dust``. Defaults to None.
        dust_size (int, optional): The size of the ``dust`` particle. Only specify if ``dust_color`` is also specified. Defaults to None.
        block_particle (block, optional): Only specify if ``particle_name`` is ``block``. Defaults to None.
        item_particle (item, optional): Only specify if ``particle_name`` is ``item``. Defaults to None.
        note_color (int, optional): Only specify if "``article_name`` is set to ``note``. Defaults to None.
        color_multiplier (int, optional): Used as an extra modifier for ``RGB`` and ``note_color``. Defaults to None.
    """
    def __init__(self, particle_name: particles, position: Union[AbsPos, CurrentPos] = None, delta: AbsPos = None, speed: int = None, count: int = None, motion: AbsPos = None,
                 RGB: tuple = None, dust_color: tuple = None, dust_size: int = None, block_particle: block = None, item_particle: item = None,
                 note_color: int = None, color_multiplier: int = None):
        self.particle_name = Handler._translate(particle_name)
        self.position = Handler._translate(position)
        self.delta = Handler._translate(delta)
        self.speed = Handler._translate(speed)
        self.count = Handler._translate(count)
        self.motion = Handler._translate(motion)
        self.RGB = Handler._translate(RGB)
        self.dust_color = Handler._translate(dust_color)
        self.dust_size = Handler._translate(dust_size)
        self.block_particle = Handler._translate(block_particle)
        self.item_particle = Handler._translate(item_particle)
        self.note_color = Handler._translate(note_color)
        self.color_multiplier = Handler._translate(color_multiplier)

    def build(self):
        if not Handler._is_none(self.motion):
            self.count = 0
            self.delta = self.motion

        if self.particle_name in {"entity_effect", "ambient_entity_effect"} and not Handler._is_none(self.RGB):
            if self.color_multiplier is None:
                Handler._warn("'color_multiplier' not specified with 'RGB'. Assuming value of '1'")
                self.color_multiplier = 1
            # <particle> <position> <R> <G> <B> <E> <count>
            output = f"{self.particle_name} {self.position} {self.RGB} {self.color_multiplier} 0"
        elif not Handler._is_none(self.block_particle):
            # <particle> <block> <position> <dx> <dy> <dz> <speed> <count>
            output = f"{self.particle_name} {self.block_particle} {self.position} {self.delta} {self.speed} {self.count}"
        elif not Handler._is_none(self.item_particle):
            # <particle> <item> <position> <dx> <dy> <dz> <speed> <count>
            output = f"minecraft:item {self.item_particle} {self.position} {self.delta} {self.speed} {self.count}"
        elif not Handler._is_none(self.dust_color):
            if self.dust_size is None:
                self.dust_size = 1.0
            # <particle> <color> <particle_size> <position> <dx> <dy> <dz> <speed> <count>
            output = f"minecraft:dust {self.dust_color} {self.dust_size} {self.position} {self.delta} {self.speed} {self.count}"
        elif not Handler._is_none(self.note_color):
            if Handler._is_none(self.color_multiplier):
                Handler._warn("'color_multiplier' not specified with 'note_color'. Assuming value of '1'")
                self.color_multiplier = 1
            # <particle> <position> <note_color> <dy(0)> <dz(0)> <speed> <count(0)>
            output = f"minecraft:note {self.position} {self.note_color} {self.color_multiplier} 0"
        else:
            if Handler._is_none(self.position):
                Handler._warn("'position' was not specified")
            if Handler._is_none(self.delta):
                Handler._warn("'delta' was not specified")
            if Handler._is_none(self.speed):
                Handler._warn("'speed' was not specified")
            if Handler._is_none(self.count):
                Handler._warn("'count' was not specified")
            output = f"{self.particle_name} {self.position} {self.delta} {self.speed} {self.count}"

        return output
=======

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
>>>>>>> Stashed changes
