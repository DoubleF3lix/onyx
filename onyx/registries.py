import enum


class gamemode(enum.Enum):
    survival = "survival"
    creative = "creative"
    spectator = "spectator"
    adventure = "adventure"


class selector_type(enum.Enum):
    all_players = "@a"
    all_entities = "@e"
    random_player = "@r"
    nearest_player = "@p"
    selected_entity = "@s"


class entity_sort(enum.Enum):
    arbitrary = "arbitrary"
    furthest = "furthest"
    nearest = "nearest"
    random = "random"


class scoreboard_display(enum.Enum):
    below_name = "belowName"
    list = "list"
    sidebar = "sidebar"
    team_black = "black"
    team_dark_blue = "dark_blue"
    team_dark_green = "dark_green"
    team_dark_aqua = "dark_aqua"
    team_dark_red = "dark_red"
    team_dark_purple = "dark_purple"
    team_gold = "gold"
    team_gray = "gray"
    team_dark_gray = "dark_gray"
    team_blue = "blue"
    team_green = "green"
    team_aqua = "aqua"
    team_red = "red" 
    team_light_purple = "light_purple"
    team_yellow = "yellow"
    team_white = "white"

class scoreboard_trait(enum.Enum):
    display_name = "displayname"
    render_type = "rendertype"

class scoreboard_render_type(enum.Enum):
    hearts = "hearts"
    integer = "integer"
