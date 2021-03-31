from onyx.class_types import Buildable, Pos, Rot
from onyx.registries import click_event_action, hover_event_action
from onyx.dev_util import translate
from nbtlib.tag import *


class Range(Buildable):
    def __init__(self, min: int = None, max: int = None):
        self.min = min
        self.max = max

    def build(self):
        return f"{self.min or ''}..{self.max or ''}"


class Position(Buildable, Pos):
    def __init__(self, x: int = None, y: int = None, z: int = None):
        self.x = x
        self.y = y
        self.z = z

    def build(self):
        return f"{self.x or ''} {self.y or ''} {self.z or ''}"


class LocalPosition(Buildable, Pos):
    def __init__(self, x: int = None, y: int = None, z: int = None):
        self.x = x
        self.y = y
        self.z = z

    def build(self):
        return f"{self.x or ''} {self.y or ''} {self.z or ''}"


class Rotation(Buildable, Rot):
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def build(self):
        return f"{self.x} {self.y}"


class ClickEvent(Buildable):
    def __init__(self, action: click_event_action, value: str):
        self.action = translate(action)
        self.value = value

    def build(self):
        return {"action": self.action, "value": self.value}


class HoverEvent(Buildable):
    def __init__(self, action: hover_event_action = None, text: str = None, item_id: str = None, item_tags: dict = None):
        self.action = translate(action)
        self.text = text
        self.item_id = item_id
        self.item_tags = item_tags

    def build(self):
        if self.action == "show_text":
            return {"action": "show_text", "contents": translate(self.text)}
        elif self.action == "show_item":
            if self.item_tags is not None:
                return {"action": "show_item", "contents": ({"id": self.item_id, "count": Byte(1), "tag": Compound(self.item_tags).snbt()})}
            else:
                return {"action": "show_item", "contents": ({"id": self.item_id, "count": Byte(1)})}
