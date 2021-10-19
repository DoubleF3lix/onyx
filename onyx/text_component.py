import json

from onyx.class_types import Buildable
from onyx.dev_util import camelify, translate
from onyx.registries import color, keybind
from onyx.selector import Selector
from onyx.util import ClickEvent, HoverEvent


class TextComponentPart(Buildable):
    """
    TextComponentPart - Do not create manually. Instead, use the ``TextComponent.part()`` method. Defines an element in a text component.

    Args:
        text (str, optional): The text of the text component. Defaults to None.
        translate (str, optional): A translation identifier. Defaults to None.
        with_ (list, optional): A list of text components to be inserted into the translation text. Defaults to None.
        score (dict, optional): Displays the score holder's current score in an objective. Defaults to None.
        selector (Selector, optional): Displays all entities matched from a selector. Defaults to None.
        keybind (keybind, optional): Displays a keybind. Defaults to None.
        nbt (str, optional): The NBT path to look for when using ``block``, ``entity``, or ``storage``. Defaults to None.
        interpret (bool, optional): Whether or not each NBT value should be parsed as a text component. Defaults to None.
        block (tuple, optional): The coordinates of a block to get the NBT from. Defaults to None.
        entity (Selector, optional): The selector matching an entity to get the NBT from. Defaults to None.
        storage (str, optional): The storage ID to get the NBT from. Defaults to None.
        extra (list, optional): A list of child text components. Defaults to None.
        color (color, optional): The color of ``text``. Defaults to None.
        font (str, optional): The font used by ``text``. Defaults to None.
        bold (bool, optional): Whether or not ``text`` should be bold. Defaults to None.
        italic (bool, optional): Whether or not ``text`` should be italic. Defaults to None.
        underlined (bool, optional): Whether or not ``text`` should be underlined. Defaults to None.
        strikethrough (bool, optional): Whether or not ``text`` should be stricken. Defaults to None.
        obfuscated (bool, optional): Whether or not ``text`` should be obfuscated. Defaults to None.
        insertion (str, optional): The text to be inserted into the chat when the text is shift clicked. Defaults to None.
        click_event (ClickEvent, optional): Defines an event to run when the text is clicked on. Defaults to None.
        hover_event (HoverEvent, optional): Defines a tooltip to be display when the text is hovered over. Defaults to None.
        dict (dict, optional): Import a text component directly into an object without using other parameters. Defaults to None.
    """

    def __init__(
        self,
        text: str = None,
        translate: str = None,
        with_: list = None,
        score: dict = None,
        selector: Selector = None,
        keybind: keybind = None,
        nbt: str = None,
        interpret: bool = None,
        block: tuple = None,
        entity: Selector = None,
        storage: str = None,
        extra: list = None,
        color: color = None,
        font: str = None,
        bold: bool = None,
        italic: bool = None,
        underlined: bool = None,
        strikethrough: bool = None,
        obfuscated: bool = None,
        insertion: str = None,
        click_event: ClickEvent = None,
        hover_event: HoverEvent = None,
        dict: dict = None,
    ) -> None:

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

    def build(self) -> str:
        """
        build - Returns the built text component part

        Returns:
            str: The built text component part
        """
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
    """
    TextComponent - Defines a text component array
    """

    def __init__(self) -> None:
        self.parts = []

    def __getitem__(self, index: int) -> TextComponentPart:
        """
        __getitem__ - Gets a specific part from the text component by index

        Args:
            index (int): The index of the text component part

        Returns:
            TextComponentPart: The text component part at the index
        """
        return json.dumps(translate(self.parts[index]))

    def part(
        self,
        text: str = None,
        translate: str = None,
        with_: list = None,
        score: dict = None,
        selector: Selector = None,
        keybind: keybind = None,
        nbt: str = None,
        interpret: bool = None,
        block: tuple = None,
        entity: Selector = None,
        storage: str = None,
        extra: list = None,
        color: color = None,
        font: str = None,
        bold: bool = None,
        italic: bool = None,
        underlined: bool = None,
        strikethrough: bool = None,
        obfuscated: bool = None,
        insertion: str = None,
        click_event: dict = None,
        hover_event: dict = None,
        dict: dict = None,
    ) -> "TextComponent":
        """
        part - See TextComponentPart documentation for more info

        Returns:
            self - The current TextComponent object. Allows for method chaining.
        """

        part = TextComponentPart(
            text,
            translate,
            with_,
            score,
            selector,
            keybind,
            nbt,
            interpret,
            block,
            entity,
            storage,
            extra,
            color,
            font,
            bold,
            italic,
            underlined,
            strikethrough,
            obfuscated,
            insertion,
            click_event,
            hover_event,
            dict,
        )
        self.parts.append(part)
        return self

    def build(self, is_extra: bool = False) -> str:
        """
        build - Returns a built text component

        Args:
            is_extra (bool, optional): Whether or not the text component should be put inside an ``extra`` list. Defaults to False.

        Returns:
            str: The built text component
        """
        translated_parts = [translate(part) for part in self.parts]
        if not is_extra:
            return json.dumps([""] + translated_parts)
        else:
            return translated_parts
