import json
import enum
from .enums import color as color_enum, key
from .selector import selector
from .handler import Handler
from .util import HoverEvent, ClickEvent


class json_string:
    """Defines a json_string

    Args:
        text (str, optional): Defaults to None.
        translate (str, optional): Defaults to None.
        With (list, optional): Defaults to None.
        score (tuple, optional): Defaults to None.
        selector (selector, optional): Defaults to None.
        keybind (key, optional): Defaults to None.
        nbt (str, optional): Defaults to None.
        interpret (bool, optional): Defaults to None.
        block (tuple, optional): Defaults to None.
        entity (selector, optional): Defaults to None.
        storage (str, optional): Defaults to None.
        extra (list, optional): Defaults to None.
        color (color_enum, optional): Defaults to None.
        font (str, optional): Defaults to None.
        bold (bool, optional): Defaults to None.
        italic (bool, optional): Defaults to None.
        underlined (bool, optional): Defaults to None.
        strikethrough (bool, optional): Defaults to None.
        obfuscated (bool, optional): Defaults to None.
        insertion (str, optional): Defaults to None.
        clickEvent (dict, optional): Defaults to None.
        hoverEvent (dict, optional): Defaults to None.
    """
    def __init__(self):
        self.component_text = [""]

    def component(self, text: str = None, translate: str = None, With: list = None, score: tuple = None, selector: selector = None,
                  keybind: key = None, nbt: str = None, interpret: bool = None, block: tuple = None, entity: selector = None,
                  storage: str = None, extra: list = None, color: color_enum = None, font: str = None, bold: bool = None,
                  italic: bool = None, underlined: bool = None, strikethrough: bool = None, obfuscated: bool = None,
                  insertion: str = None, clickEvent: dict = None, hoverEvent: dict = None):

        element = {}
        if text is not None:
            if not isinstance(text, str):
                Handler._warn("'text' should be a string")
            element["text"] = Handler._translate(text)

        if translate is not None:
            if not isinstance(translate, str):
                Handler._warn("'translate' should be a string")
            element["translate"] = translate

        if With is not None:
            if not isinstance(With, list):
                Handler._warn("'With' should be a list")
            if not translate:
                Handler._warn("Parameter 'With' specified without 'translate'")
            element["with"] = With

        if score is not None:
            if text:
                Handler._warn("'score' will not display with specified 'text' parameter")
            if not isinstance(score, dict):
                raise ValueError(f"Expected dictionary for 'score', got {type(score)}")
            if "signature18" not in score:
                Handler._warn("'score' is missing siganture. Consider using 'Scoreboard()' to avoid errors.")
                if isinstance(score["player"], selector):
                    score["player"] = score["player"].build()
            element["score"] = {"name": score["player"], "objective": score["objective"]}

        if selector is not None:
            if not isinstance(selector, selector):
                Handler._warn("'selector' should be a selector object")
            element["selector"] = Handler._translate(selector)

        if keybind is not None:
            element["key"] = Handler._translate(keybind)

        if nbt is not None:
            if not isinstance(nbt, str):
                Handler._warn("'nbt' should be a string")
            element["nbt"] = nbt

        if interpret is not None:
            if not isinstance(interpret, bool):
                Handler._warn("'interpret' should be a boolean")
            if not nbt:
                Handler._warn("Parameter 'interpet' specified without 'nbt'")
            element["interpret"] = str(interpret).lower()

        if block is not None:
            if not isinstance(block, tuple) or len(tuple) != 3:
                Handler._warn("'block' should be an absolute position object")
            if not nbt:
                Handler._warn("Parameter 'block' specified without 'nbt'")
            element["block"] = Handler._translate(block)

        if entity is not None:
            if not isinstance(entity, selector):
                Handler._warn("'entity' should be a selector object")
            if not nbt:
                Handler._warn("Parameter 'entity' specified without 'nbt'")
            element["selector"] = Handler._translate(entity)

        if storage is not None:
            if not isinstance(storage, str):
                Handler._warn("'storage' should be a string")
            if not nbt:
                Handler._warn("Parameter 'storage' specified without 'nbt'")
            element["storage"] = Handler._translate(storage)

        if extra is not None:
            if not isinstance(extra, list):
                Handler._warn("'extra' should be a list}")
            element["extra"] = Handler._translate(extra, convert=True)

        if color is not None:
            if isinstance(color, enum.Enum) and color.value not in {"black", "dark_blue", "dark_green", "dark_aqua", "dark_red", "dark_purple", "gold", "gray", "dark_gray", "blue", "green", "aqua", "red", "light_purple", "yellow", "white", "reset"}:
                Handler._warn(f"'color' was set to an invalid color: {color.value}")
            element["color"] = Handler._translate(color)

        if font is not None:
            if not isinstance(font, str):
                Handler._warn("'font' should be a string")
            element["font"] = Handler._translate(font)

        if bold is not None:
            if not isinstance(bold, bool):
                Handler._warn("'bold' should be a boolean")
            element["bold"] = Handler._translate(bold)

        if italic is not None:
            if not isinstance(italic, bool):
                Handler._warn("'italic' should be a boolean")
            element["italic"] = Handler._translate(italic)

        if underlined is not None:
            if not isinstance(underlined, bool):
                Handler._warn("'underlined' should be a boolean")
            element["underlined"] = Handler._translate(underlined)

        if strikethrough is not None:
            if not isinstance(strikethrough, bool):
                Handler._warn("'strikethrough' should be a boolean")
            element["strikrethrough"] = Handler._translate(strikethrough)

        if obfuscated is not None:
            if not isinstance(obfuscated, bool):
                Handler._warn("'obfuscated' should be a boolean")
            element["obfuscated"] = Handler._translate(obfuscated)

        if insertion is not None:
            if not isinstance(insertion, str):
                Handler._warn("'insertion' should be a string")
            element["insertion"] = Handler._translate(insertion)

        if clickEvent is not None:
            if not isinstance(clickEvent, ClickEvent):
                Handler._warn("'clickEvent' should be a ClickEvent object")
            element["clickEvent"] = Handler._translate(clickEvent)

        if hoverEvent is not None:
            if not isinstance(hoverEvent, HoverEvent):
                Handler._warn("'hoverEvent' should be a HoverEvent object")
            element["hoverEvent"] = Handler._translate(hoverEvent)

        # Add the dictionary to a list element
        self.component_text.append(element)
        self.output = self.component_text
        return self
