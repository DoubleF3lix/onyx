import enum

class mode(enum.Enum):
    survival = 0
    creative = 1
    adventure = 2
    spectator = 3

class sort(enum.Enum):
    arbitrary = 0
    furthest = 1
    nearest = 2
    random = 3

class at(enum.Enum):
    all_players = "@a"
    all_entities = "@e"
    nearest_player = "@p"
    random_player = "@r"
    selected_entity = "@s"

class axis(enum.Enum):
    x = "x"
    y = "y"
    z = "z"

class anchor(enum.Enum):
    feet = "feet"
    eyes = "eyes"

class dimension(enum.Enum):
    overworld = "overworld"
    nether = "the_nether"
    end = "the_end"