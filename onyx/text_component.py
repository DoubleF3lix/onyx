import json
from onyx.dev_util import translate, camelify
from onyx.class_types import Buildable
from onyx.selector import Selector
from onyx.registries import keybind, color


class TextComponentPart(Buildable):
    def __init__(self, text: str = None, translate: str = None, with_: list = None, score: dict = None, selector: Selector = None,
            keybind: keybind = None, nbt: str = None, interpret: bool = None, block: tuple = None, entity: Selector = None,
            storage: str = None, extra: list = None, color: color = None, font: str = None, bold: bool = None,
            italic: bool = None, underlined: bool = None, strikethrough: bool = None, obfuscated: bool = None,
            insertion: str = None, click_event: dict = None, hover_event: dict = None, dict: dict = None):

        if dict is None:
            self.text = text
            self.translate = translate
            self.with_ = with_
            self.score = score
            self.selector = selector
            self.keybind = keybind
            self.nbt = nbt
            self.interpret = interpret
            self.block = block
            self.entity = entity
            self.storage = storage
            self.extra = extra
            self.color = color
            self.font = font
            self.bold = bold
            self.italic = italic
            self.underlined = underlined
            self.strikethrough = strikethrough
            self.obfuscated = obfuscated
            self.insertion = insertion
            self.click_event = click_event
            self.hover_event = hover_event
        else:
            for key, item in dict.items():
                setattr(self, key, item)

    def build(self):
        output = {}

        for key, item in vars(self).items():
            if item:
                if key == "color":
                    if translate(item) == "pink":
                        item = "light_purple"
                    elif translate(item) == "purple":
                        item = "dark_purple"
                elif key == "extra":
                    item = [q.build(is_extra=True) for q in self.extra]
                elif key in {"click_event", "hover_event"}:
                    key = camelify(key)
                elif key == "with_":
                    key = "with"

                output[key] = translate(item) if key not in {"extra", "with"} else item
        return output

class TextComponent(Buildable):
    def __init__(self):
        self.parts = []

    def __getitem__(self, index):
        return json.dumps(self.parts[index].build())

    def part(self, text: str = None, translate: str = None, with_: list = None, score: dict = None, selector: Selector = None,
            keybind: keybind = None, nbt: str = None, interpret: bool = None, block: tuple = None, entity: Selector = None,
            storage: str = None, extra: list = None, color: color = None, font: str = None, bold: bool = None,
            italic: bool = None, underlined: bool = None, strikethrough: bool = None, obfuscated: bool = None,
            insertion: str = None, click_event: dict = None, hover_event: dict = None, dict: dict = None):

        part = TextComponentPart(text, translate, with_, score, selector, keybind, nbt, interpret, block, entity, storage,
                                extra, color, font, bold, italic, underlined, strikethrough, obfuscated, insertion, click_event, hover_event, dict)
        self.parts.append(part)
        return self

    def build(self, is_extra: bool = False): 
        translated_parts = [part.build() for part in self.parts]
        if not is_extra:
            return json.dumps([""] + translated_parts)
        else:
            return translated_parts
