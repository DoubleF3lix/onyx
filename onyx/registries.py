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


class keybind(enum.Enum):
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
    hotbar_1 = "hotbar.1"
    hotbar_2 = "hotbar.2"
    hotbar_3 = "hotbar.3"
    hotbar_4 = "hotbar.4"
    hotbar_5 = "hotbar.5"
    hotbar_6 = "hotbar.6"
    hotbar_7 = "hotbar.7"
    hotbar_8 = "hotbar.9"
    hotbar_9 = "hotbar.9"
    load_toolbar_activator = "loadToolbarActivator"
    save_toolbar_activator = "saveToolbarActivator"
    player_list = "playerlist"
    chat = "chat"
    command = "command"
    advancements = "advancements"
    spectator_outlines = "spectatorOutlines"
    outline_spectators = "spectatorOutlines"
    screenshot = "screenshot"
    smooth_camera = "smoothCamera"
    cinematic_camera = "smoothCamera"
    fullscreen = "fullscreen"
    toggle_perspective = "togglePerspective"


class click_event_action(enum.Enum):
    change_page = "change_page"
    copy_to_clipboard = "copy_to_clipboard"
    open_url = "open_url"
    run_command = "run_command"
    suggest_command = "suggest_command"


class hover_event_action(enum.Enum):
    show_text = "show_text"
    show_item = "show_item"


class axis(enum.Enum):
    x = "x"
    y = "y"
    z = "z"


class anchor(enum.Enum):
    feet = "feet"
    eyes = "eyes"


class dimension(enum.Enum):
    overworld = "overworld"
    the_end = "the_end"
    the_nether = "the_nether"


class data_type(enum.Enum):
    byte = "byte"
    double = "double"
    float = "float"
    int = "int"
    long = "long"
    short = "short"


class bossbar_location(enum.Enum):
    max = "max"
    value = "value"


class execute_blocks_mask(enum.Enum):
    all = "all"
    masked = "masked"
 

class source_type(enum.Enum):
    block = "block"
    entity = "entity"
    storage = "storage"
