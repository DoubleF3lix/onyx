import json
from typing import Union
from nbtlib.tag import *
from nbtlib import parse_nbt

from .selector import selector
from .enums import item, action as action_enum
from .handler import Handler, _buildable, _position


class SetFrom(_buildable):
    """Used with data.modify() when setting from an entity

    Args:
        target (Union[str, tuple, selector]): The entity that the data should be retrieved from
        path (str): The data location
        index (int, optional): [description]. The index of the data. Only use if the path is a list. Defaults to None.
        container_type (str, optional): Override for container type (entity, storage, or block). If unspecified, the container type will be assumed based off the value for "target". Defaults to None.
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

    Args:
        data (str): The value to be set.
        index (int, optional): The index of a list that should be modified. Only use if the path is a list. Defaults to None.
    """
    def __init__(self, data: str, index: int = None):
        self.data = data
        self.index = index

    def build(self):
        if self.index is not None:
            return f"{self.index} value {self.data}"
        else:
            return f"value {self.data}"


class Negate(_buildable):
    """Negates an argument

    Args:
        arg: The argument to negate
    """
    def __init__(self, arg):
        self.arg = arg

    def build(self):
        return f"!{Handler._translate(self.arg)}"


class Range(_buildable):
    """Defines a scoreboard range

    Args:
        min (int, optional): The minimum value the score should be (inclusive). If unspecified, the range will check for all scores equal to or below the maximum. Defaults to None.
        max (int, optional): The maximum value the score should be (inclusive). If unspecified, the range will check for all scores equal to or below the minimum. Defaults to None.
    """
    def __init__(self, min: int = None, max: int = None):
        if min is None and max is None:
            Handler._warn("'min' and 'max' were not assigned")
        self.min = min
        self.max = max

    def build(self):
        return f"{self.min}..{self.max}"


class ClickEvent(_buildable):
    """Used with JSON strings

    Args:
        action (action_enum, optional): The action type.
        value (str, optional): The argument of the action.
    """
    def __init__(self, action: action_enum, value: str):
        # Check if an invalid action was used
        if Handler._translate(action) in {"show_text", "show_item"}:
            Handler._warn(f"{Handler._translate(action)} is exclusive to hover_event")

        self.action = Handler._translate(action)
        self.value = value

    def build(self):
        return {"action": self.action, "contents": self.value}


class HoverEvent(_buildable):
    """Used with JSON strings

    Args:
        action (action_enum, optional): The action type. Defaults to None.
        text (str, optional): The text to show on hover. Only used if "action" is set to "show_text". Defaults to None.
        item_id (str, optional): The item to show on hover. Only used if "action" is set to "show_item". Defaults to None.
        item_tags (dict, optional): The tags the item should have. Defaults to None.
    """
    def __init__(self, action: action_enum = None, text: str = None, item_id: str = None, item_tags: dict = None):
        # Check if an invalid action was used
        if Handler._translate(action) not in {"show_text", "show_item"}:
            Handler._warn(f"{Handler._translate(action)} is exclusive to click_event")

        self.action = Handler._translate(action)
        self.text = text
        self.item_id = item_id
        self.item_tags = item_tags

    def build(self):
        if self.action == "show_text":
            return {"action": "show_text", "contents": Handler._translate(self.text)}
        elif self.action == "show_item":
            if self.item_tags is not None:
                return {"action": "show_item", "contents": ({"id": self.item_id, "count": Byte(1), "tag": Compound(self.item_tags).snbt()})}
            else:
                return {"action": "show_item", "contents": ({"id": self.item_id, "count": Byte(1)})}


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
        return f"~{self.x} ~{self.y} ~{self.z}"


class LocPos(_buildable, _position):
    """Defines a local position (relatve to the direction an entity is facing)

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
        return f"^{self.x} ^{self.y} ^{self.z}"


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
