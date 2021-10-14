from typing import Union
from .enums import color as color_enum, key
from .selector import selector
from .handler import Handler


class json_string:
    """Defines a json_string

    Args:
        text (str, optional): Defaults to None.
        translate (str, optional): Defaults to None.
        With (list, optional): Defaults to None.
        score (Player, dict, optional): Defaults to None.
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

    def component(self, text: str = None, translate: str = None, With: list = None, score: Union["Player", dict] = None, selector: selector = None,
                  keybind: key = None, nbt: str = None, interpret: bool = None, block: tuple = None, entity: selector = None,
                  storage: str = None, extra: list = None, color: color_enum = None, font: str = None, bold: bool = None,
                  italic: bool = None, underlined: bool = None, strikethrough: bool = None, obfuscated: bool = None,
                  insertion: str = None, clickEvent: dict = None, hoverEvent: dict = None):

        element = {}
        if text is not None:
            element["text"] = Handler._translate(text)

        if translate is not None:
            element["translate"] = Handler._translate(translate)

        if With is not None:
            if not translate:
                Handler._warn("Parameter 'With' specified without 'translate'")
            element["with"] = Handler._translate(With)

        if score is not None:
            if text:
                Handler._warn("'score' will not display with specified 'text' parameter")
            if isinstance(score, Player):
                element["score"] = {"name": score.name, "objective": score.scoreboard}
            else:
                element["score"] = {"name": score["player"], "objective": score["objective"]}

        if selector is not None:
            element["selector"] = Handler._translate(selector)

        if keybind is not None:
            element["key"] = Handler._translate(keybind)

        if nbt is not None:
            element["nbt"] = Handler._translate(nbt)

        if interpret is not None:
            if not nbt:
                Handler._warn("Parameter 'interpet' specified without 'nbt'")
            element["interpret"] = str(interpret).lower()

        if block is not None:
            if not nbt:
                Handler._warn("Parameter 'block' specified without 'nbt'")
            element["block"] = Handler._translate(block)

        if entity is not None:
            if not nbt:
                Handler._warn("Parameter 'entity' specified without 'nbt'")
            element["selector"] = Handler._translate(entity)

        if storage is not None:
            if not nbt:
                Handler._warn("Parameter 'storage' specified without 'nbt'")
            element["storage"] = Handler._translate(storage)

        if extra is not None:
            element["extra"] = Handler._translate(extra, convert=True)

        if color is not None:
            if Handler._translate(color) not in {"black", "dark_blue", "dark_green", "dark_aqua", "dark_red", "dark_purple", "gold", "gray", "dark_gray", "blue", "green", "aqua", "red", "light_purple", "yellow", "white", "reset"}:
                Handler._warn(f"'color' was set to an unsupported color: {Handler._translate(color)}")
            element["color"] = Handler._translate(color)

        if font is not None:
            element["font"] = Handler._translate(font)

        if bold is not None:
            element["bold"] = Handler._translate(bold)

        if italic is not None:
            element["italic"] = Handler._translate(italic)

        if underlined is not None:
            element["underlined"] = Handler._translate(underlined)

        if strikethrough is not None:
            element["strikrethrough"] = Handler._translate(strikethrough)

        if obfuscated is not None:
            element["obfuscated"] = Handler._translate(obfuscated)

        if insertion is not None:
            element["insertion"] = Handler._translate(insertion)

        if clickEvent is not None:
            element["clickEvent"] = Handler._translate(clickEvent)

        if hoverEvent is not None:
            element["hoverEvent"] = Handler._translate(hoverEvent)

        # Add the dictionary to a list element
        self.component_text.append(element)
        self.output = self.component_text
        return self
