from .selector import Selector
from .json_string import json_string
from .enum import action as action_enum
from typing import Union
import enum
import ast

def Negate(arg:str) -> str:
	if isinstance(arg, enum.Enum): 
		return f"!{str(arg.name)}"
	elif isinstance(arg, (int, float)): 
		return f"!{arg}"
	
def Range(min:Union[int, float]=None, max:Union[int, float]=None) -> str:
	return f"{min}..{max}"

def Scoreboard(player:Union[Selector, str]=None, objective:str=None) -> dict:
	# Type checking
	if not isinstance(player, (Selector, str)): 
		raise ValueError("'player' must be a string or selector object")
	if not isinstance(objective, str):
		raise ValueError("'objective' must be a string")
	
	# Check if "player" is a selector object, and if so, call build()
	if isinstance(player, Selector):
		return {"player": player.build(), "objective": objective, "signature18": 0}
	# This won't run if if "player" is a selector object
	return {"player": player, "objective": objective, "signature18": 0}

def click_event(action:action_enum=None, value:str=None):
	# Type checking
	if not isinstance(action, action_enum):
		raise ValueError(f"Unknown value for 'action': {action}")
	if not isinstance(value, str):
		raise ValueError(f"Expected string for 'value', got {type(value)}")

	# Check if an invalid action was used
	if action.value in {"show_text", "show_item", "show_entity"}:
		raise ValueError(f"{action.value} is exclusive to hover_event")
	return {"action": action.value, "value": value, "signature5": 0}

def hover_event(action:action_enum=None, contents:str=None):
	# Type checking
	if not isinstance(action, action_enum):
		raise ValueError(f"Unknown value for 'action': {action}")
	if action.value not in {"show_text", "show_item"}:
		raise ValueError(f"{action.value} is exclusive to click_event")

	if action.value == "show_text":
		# Type checking
		if not isinstance(contents, json_string):
			raise ValueError(f"Expected json_string object for 'contents', got {type(contents)}")
		return {"action": action.value, "contents": ast.literal_eval(contents.output), "signature42": 0}

	elif action.value == "show_item":
		# Type checking
		if not isinstance(contents, dict):
			raise ValueError(f"Expected dictionary for 'contents', got {type(contents)}")
		if "id" not in contents:
			raise ValueError(f"Missing 'id' in 'contents'")

		# Return the dict without the tag parameter if one isn't specified, otherwise, include it
		if not "tag" in contents:
			return {"action": action.value, "contents": {"id": contents["id"]}, "signature42": 0}
		return {"action": action.value, "contents": {"id": contents["id"], "tag": contents["tag"]}, "signature42": 0}

# Returns a tuple of 3 values as strings
def abs_pos(x:Union[int, float], y:Union[int, float], z:Union[int, float]) -> tuple:
	if not all(isinstance(arg, (int, float)) for arg in [x, y, z]):
		raise ValueError("You must supply 3 numbers")
	return (f"{x}", f"{y}", f"{z}")

# Returns a tuple of 3 values as strings
def rel_pos(x:Union[int, float], y:Union[int, float], z:Union[int, float]) -> tuple:
	if not all(isinstance(arg, (int, float)) for arg in [x, y ,z]):
		raise ValueError("You must supply 3 numbers")
	return (f"~{x or ''}", f"~{y or ''}", f"~{z or ''}")

# Returns a tuple of 3 values as strings
def loc_pos(left:Union[int, float], up:Union[int, float], forward:Union[int, float]) -> tuple:
	if not all(isinstance(arg, (int, float)) for arg in [left, up, forward]):
		raise ValueError("You must supply 3 numbers")
	return (f"^{left or ''}", f"^{up or ''}", f"^{forward or ''}")

# Returns a tuple of 2 values as strings
def abs_rot(y_rot:Union[int, float], x_rot:Union[int, float]) -> tuple:
	if not all(isinstance(arg, (int, float)) for arg in [y_rot, x_rot]):
		raise ValueError("You must supply 2 numbers")
	return (f"{y_rot}", f"{x_rot}")

# Returns a tuple of 2 values as strings
def rel_rot(y_rot:Union[int, float], x_rot:Union[int, float]) -> tuple:
	if not all(isinstance(arg, (int, float)) for arg in [y_rot, x_rot]):
		raise ValueError("You must supply 2 numbers")
	return (f"~{y_rot}", f"~{x_rot}")  