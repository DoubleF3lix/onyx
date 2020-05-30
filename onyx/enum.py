import enum

# Gamemodes
class mode(enum.Enum):
	survival = 0
	creative = 1
	adventure = 2
	spectator = 3

# Used for "sort" property of selectors
class sort(enum.Enum):
	arbitrary = 0
	furthest = 1
	nearest = 2
	random = 3

# Used for selector types
class at(enum.Enum):
	all_players = "@a"
	all_entities = "@e"
	nearest_player = "@p"
	random_player = "@r"
	selected_entity = "@s"

# Used for execute align
class axis(enum.Enum):
	x = "x"
	y = "y"
	z = "z"

# Used for execute anchored
class anchor(enum.Enum):
	feet = "feet"
	eyes = "eyes"

# Used for execute in
class dimension(enum.Enum):
	overworld = "overworld"
	nether = "the_nether"
	end = "the_end"

# Used for bossbars
# "property" has special highlighting in VSCode and attribute is used to refer to another command, so I used trait
class trait(enum.Enum):
	color = "color"         		# set
	max_value = "max"       		# set and get
	name = "name"           		# set
	players = "players"     		# set (get is only useful when run from chat)
	style = "style"         		# set
	progress = "value"      		# set and get ("value" is used to access enum values, so I used "progress")

# Used for bossbars
class style(enum.Enum):
	six_segments = "notched_6" 
	ten_segments = "notched_10" 
	twelve_segments = "notched_12"
	twenty_segments = "notched_20" 
	solid = "progress"

class color(enum.Enum):
	black = "black"
	dark_blue = "dark_blue"
	dark_green = "dark_green"
	dark_aqua = "dark_aqua"
	dark_red = "dark_red"
	dark_purple = "dark_purple"     
	gold = "gold"
	gray = "gray"
	dark_gray = "dark_gray"
	blue = "blue"                   # bossbar compatible
	green = "green"                 # bossbar compatible
	pink = "pink"                   # bossbar exclusive
	purple = "purple"               # bossbar exclusive
	aqua = "aqua"
	red = "red"                     # bossbar compatible
	light_purple = "light_purple"   
	yellow = "yellow"               # bossbar compatible
	white = "white"                 # bossbar compatible
	reset = "reset"

# Used for text component "clickEvent" and "hoverEvent"
# show_entity is not supported since it requires an external generate to convert the UUIDs, and it's just a broken mess all around.
class action(enum.Enum):
	change_page = "change_page"		# clickEvent exclusive
	copy = "copy_to_clipboard"    	# clickEvent exclusive
	open_url = "open_url"           # clickEvent exclusive
	run_cmd = "run_command"         # clickEvent exclusive
	suggest_cmd = "suggest_command"	# clickEvent exclusive
	show_text = "show_text"			# hoverEvent exclusive
	show_item = "show_item"			# hoverEvent exclusive

# Used for text component "keybind"
class key(enum.Enum):
	jump = "jump"
	sneak = "sneak"
	sprint = "sprint"
	left = "left"
	right = "right"
	back = "back"
	forward = "forward"
	attack = "attack"
	pick_item = "pick_item"
	use = "use"
	drop = "drop"
	hotbar_one = "hotbar.1"
	hotbar_two = "hotbar.2"
	hotbar_three = "hotbar.3"
	hotbar_four = "hotbar.4"
	hotbar_five = "hotbar.5"
	hotbar_six = "hotbar.6"
	hotbar_seven = "hotbar.7"
	hotbar_eight = "hotbar.9"
	hotbar_nine = "hotbar.9"
	load_toolbar_activator = "loadToolbarActivator"
	save_toolbar_activator = "saveToolbarActivator"
	player_list = "playerlist"
	chat = "chat"
	command = "command"
	advancements = "advancements"
	outline_spectators = "spectatorOutlines"
	screenshot = "screenshot"
	cinematic_camera = "smoothCamera"
	fullscreen = "fullscreen"
	toggle_perspective = "togglePerspective"

# Used for advancements
class advancement_action(enum.Enum):
	grant = "grant"
	revoke = "revoke"

# Used for advancements
# "from" is a reserved keywored
class selection(enum.Enum):
	everything = "everything"
	From = "from"
	only = "only"
	through = "through"
	until = "until"