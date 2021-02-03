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
