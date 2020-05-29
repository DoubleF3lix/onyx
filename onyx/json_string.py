import json
import traceback
from .enum import color as color_enum
from .enum import action, key
from .selector import Selector
from .commands import Commands

class json_string:
	def __init__(self):
		self.component_text = [""]

	# "with" is a reserved keyword
	def component(self, text:str=None, translate:str=None, With:list=None, score:tuple=None, selector:Selector=None, keybind:key=None, nbt:str=None, interpret:bool=None, block:tuple=None, entity:Selector=None, storage:str=None, extra:list=None, color:color_enum=None, font:str=None, bold:bool=None, italic:bool=None, underlined:bool=None, strikethrough:bool=None, obfuscated:bool=None, insertion:str=None, clickEvent:dict=None, hoverEvent:dict=None) -> "json_string":
		element = {}
		if text:
			if not isinstance(text, str):
				raise ValueError(f"Expected string for 'text', got {type(text)}")
			element["text"] = text

		if translate:
			if not isinstance(translate, str):
				raise ValueError(f"Expected string for 'translate', got {type(translate)}")
			element["translate"] = translate

		if With:
			if not isinstance(With, list):
				raise ValueError(f"Expected list for 'with', got {type(With)}")
			if not translate:
				Commands._warn("Parameter 'with' specified without 'translate'")
			element["with"] = With

		if score:
			if text:
				Commands._warn(f"'score' will not display with specified 'text' parameter")
			if not isinstance(score, dict):
				raise ValueError(f"Expected dictionary for 'score', got {type(score)}")
			if not "signature18" in score:
				Commands._warn("'score' is missing siganture. Consider using 'Scoreboard()' to avoid errors.")
				if isinstance(score["player"], Selector):
					score["player"] = score["player"].build()
			element["score"] = {"name": score["player"], "objective": score["objective"]}

		if selector:
			if not isinstance(selector, Selector):
				raise ValueError(f"Expected Selector object, got {type(selector)}")
			element["selector"] = selector.build()

		if keybind:
			if not isinstance(keybind, key):
				raise ValueError(f"Unknown value for 'keybind': {keybind}")
			element["key"] = key.value

		if nbt:
			if not isinstance(nbt, str):
				raise ValueError(f"Expected string for 'nbt', got {type(nbt)}")
			element["nbt"] = nbt

		if interpret:
			if not isinstance(interpret, bool):
				raise ValueError(f"Expected boolean for 'interpret', got {type(interpret)}")
			if not nbt:
				Commands._warn("Parameter 'interpet' specified without 'nbt'")
			element["interpret"] = str(interpret).lower()
		
		if block:
			if not isinstance(block, tuple) or len(tuple) != 3:
				raise ValueError("'block' must be a tuple with 3 elements")
			if not nbt:
				Commands._warn("Parameter 'block' specified without 'nbt'")
			element["block"] = " ".join(block)

		if entity:
			if not isinstance(entity, Selector):
				raise ValueError(f"Expected Selector object, got {type(entity)}")
			if not nbt:
				Commands._warn("Parameter 'entity' specified without 'nbt'")
			element["selector"] = entity.build()

		if storage:
			if not isinstance(storage, str):
				raise ValueError(f"Expected string for 'storage', got {type(storage)}")
			if not nbt:
				Commands._warn("Parameter 'storage' specified without 'nbt'")
			element["storage"] = storage

		if extra:
			if not isinstance(extra, list):
				raise ValueError(f"Expected list for 'extra', got {type(extra)}")
			element["extra"] = extra

		if color:
			if not isinstance(color, color_enum):
				raise ValueError(f"Unknown value for 'color': {color}")
			if color.value not in {"black", "dark_blue", "dark_green", "dark_aqua", "dark_red", "dark_purple", "gold", "gray", "dark_gray", "blue", "green", "aqua", "red", "light_purple", "yellow", "white", "reset"}:
				raise ValueError(f"Color {color.value} is exclusive to bossbars")
			element["color"] = color.value

		if font:
			if not isinstance(font, str):
				raise ValueError(f"Expected string for 'font', got {type(font)}")
			element["font"] = font

		if bold:
			if not isinstance(bold, bool):
				raise ValueError(f"Expected boolean for 'bold', got {type(bold)}")
			element["bold"] = str(bold).lower()

		if italic:
			if not isinstance(italic, bool):
				raise ValueError(f"Expected boolean for 'italic', got {type(italic)}")
			element["italic"] = str(italic).lower()

		if underlined:
			if not isinstance(underlined, bool):
				raise ValueError(f"Expected boolean for 'underlined', got {type(underlined)}")
			element["underlined"] = str(underlined).lower()

		if strikethrough:
			if not isinstance(strikethrough, bool):
				raise ValueError(f"Expected boolean for 'strikethrough', got {type(strikethrough)}")
			element["strikrethrough"] = str(strikethrough).lower()

		if obfuscated:
			if not isinstance(obfuscated, bool):
				raise ValueError(f"Expected boolean for 'obfuscated', got {type(obfuscated)}")
			element["obfuscated"] = str(obfuscated).lower()

		if insertion:
			if not isinstance(insertion, str):
				raise ValueError(f"Expected string for 'insertion', got {type(insertion)}")
			element["insertion"] = insertion

		if clickEvent:
			# Type checking
			if not isinstance(clickEvent, dict):
				raise ValueError(f"Expected dict for 'clickEvent', got {type(clickEvent)}")
			
			# Check if clickEvent has all the elements
			if "action" not in clickEvent:
				raise ValueError("Missing 'action' in 'clickEvent'")
			if "value" not in clickEvent:
				raise ValueError("Missing 'value' in 'clickEvent'")

			# Warn the user if it's missing a signature, otherwise remove it
			if "signature5" not in clickEvent:
				Commands._warn("'clickEvent' is missing siganture. Consider using 'click_event()' to avoid errors.")
			else:
				del clickEvent["signature5"]
			if not text and not score:
				Commands._warn("Parameter 'clickEvent' specified without 'text' or 'score'")
			element["clickEvent"] = clickEvent

		if hoverEvent:
			# Type checking
			if not isinstance(hoverEvent, dict):
				raise ValueError(f"Expected dict for 'hoverEvent', got {type(hoverEvent)}")
			
			# Check if clickEvent has all the elements
			if "action" not in hoverEvent:
				raise ValueError("Missing 'action' in 'hoverEvent'")
			if "contents" not in hoverEvent:
				raise ValueError("Missing 'contents' in 'hoverEvent'")

			# Warn the user if it's missing a signature, otherwise remove it
			if "signature42" not in hoverEvent:
				Commands._warn("'hoverEvent' is missing siganture. Consider using 'hover_event()' to avoid errors.")
			else:
				del hoverEvent["signature42"]
			if not text and not score:
				Commands._warn("Parameter 'hoverEvent' specified without 'text' or 'score'")
			element["hoverEvent"] = hoverEvent

		# Add the dictionary to a list element
		self.component_text.append(element)
		# Turn ' into "
		self.output = json.dumps(self.component_text)
		return self