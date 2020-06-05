import inspect
from .handler import Handler
from .selector import Selector
from .enum import trait as trait_enum, style as style_enum, color as color_enum
from .json_string import json_string

# "id" has strange highlighting, so I used "bossbar_id"
# "name" was changed for consistency
def create(bossbar_id:str, bossbar_name:json_string) -> None:
	if not isinstance(bossbar_name, json_string):
		raise ValueError("'bossbar_name' must be a json_string object")
	Handler._write(inspect.stack()[1][3], f"bossbar add {bossbar_id} {bossbar_name.output}")

def delete(bossbar_id:str):
	Handler._write(inspect.stack()[1][3], f"bossbar remove {bossbar_id}")

def list():
	Handler._write(inspect.stack()[1][3], f"bossbar list")

# "property" has weird highlighting, so I used "attribute" instead
def get_trait(bossbar_id:str, attribute:trait_enum=trait_enum.progress):
	if attribute.name in {"color", "name", "players", "style"}:
		raise ValueError(f"'{attribute.name}' is exclusive to 'set_trait'")
	Handler._write(inspect.stack()[1][3], f"bossbar get {bossbar_id} {attribute.value}")

def set_trait(bossbar_id:str, color:color_enum=None, max:int=None, name:json_string=None, players:Selector=None, style:style_enum=None, value:int=None, visible:bool=None):
	# -1 accounts for itself
	cmd_count = -1
	# Iterate through each of the default arguments (required arguments won't fail since they behave like default arguments)
	for key, arg in locals().items():
		# Filter out the args that were not assigned
		if arg is not None:
			if key == "color":
				# Check if the provided color is supported by bossbars
				if arg.value not in {"blue", "green", "pink", "purple", "yellow", "white"}:
					raise ValueError(f"Unknown value for 'color': {arg} (Did you set it to an incompatible color?)")
				Handler._write(inspect.stack()[1][3], f"bossbar set minecraft:{bossbar_id} color {arg.value}")
			elif key == "max":
				if not isinstance(arg, int):
					raise ValueError("'max' must be an int")
				Handler._write(inspect.stack()[1][3], f"bossbar set {bossbar_id} max {arg}")
			elif key == "name":
				if not isinstance(arg, json_string):
					raise ValueError("'name' must be a json_string object")
				Handler._write(inspect.stack()[1][3], f"bossbar set minecraft:{bossbar_id} name {arg.output}")
			elif key == "players":
				if not isinstance(arg, Selector):
					raise ValueError("'players' must be a selector object")
				Handler._write(inspect.stack()[1][3], f"bossbar set minecraft:{bossbar_id} players {arg.build()}")
			elif key == "style":
				Handler._write(inspect.stack()[1][3], f"bossbar set minecraft:{bossbar_id} style {arg.value}")
			elif key == "value":
				if not isinstance(arg, int):
					raise ValueError("'max' must be an int")
				Handler._write(inspect.stack()[1][3], f"bossbar set minecraft:{bossbar_id} value {arg}")
			elif key == "visible":
				if not isinstance(arg, bool):
					raise ValueError("'visible' must be True or False")
				# str(arg).lower() is used to turn it from "True" to "true" or "False" to "false"
				Handler._write(inspect.stack()[1][3], f"bossbar set minecraft:{bossbar_id} max {str(arg).lower()}")
			cmd_count += 1
	return cmd_count