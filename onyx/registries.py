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
    jump = "key.jump"
    sneak = "key.sneak"
    sprint = "key.sprint"
    left = "key.left"
    right = "key.right"
    back = "key.back"
    forward = "key.forward"
    attack = "key.attack"
    pick_item = "key.pick_item"
    use = "key.use"
    drop = "key.drop"
    hotbar_1 = "key.hotbar.1"
    hotbar_2 = "key.hotbar.2"
    hotbar_3 = "key.hotbar.3"
    hotbar_4 = "key.hotbar.4"
    hotbar_5 = "key.hotbar.5"
    hotbar_6 = "key.hotbar.6"
    hotbar_7 = "key.hotbar.7"
    hotbar_8 = "key.hotbar.9"
    hotbar_9 = "key.hotbar.9"
    load_toolbar_activator = "key.loadToolbarActivator"
    save_toolbar_activator = "key.saveToolbarActivator"
    player_list = "key.playerlist"
    chat = "key.chat"
    command = "key.command"
    advancements = "key.advancements"
    spectator_outlines = "key.spectatorOutlines"
    outline_spectators = "key.spectatorOutlines"
    screenshot = "key.screenshot"
    smooth_camera = "key.smoothCamera"
    cinematic_camera = "key.smoothCamera"
    fullscreen = "key.fullscreen"
    toggle_perspective = "key.togglePerspective"


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


class difficulty(enum.Enum):
    peaceful = "peaceful"
    easy = "easy"
    normal = "normal"
    hard = "hard"


class experience_type(enum.Enum):
    levels = "levels"
    points = "points"


class weather_type(enum.Enum):
    clear = "clear"
    rain = "rain"
    thunder = "thunder"


class sound_channel(enum.Enum):
    any = "*"
    ambient = "ambient"
    block = "block"
    hostile = "hostile"
    master = "master"
    music = "music"
    neutral = "neutral"
    player = "player"
    record = "record"
    voice = "voice"
    weather = "weather"


class setblock_mode(enum.Enum):
    destroy = "destroy"
    keep = "keep"
    replace = "replace"


class fill_mode(enum.Enum):
    destroy = "destroy"
    hollow = "hollow"
    keep = "keep"
    outline = "outline"
    replace = "replace"


class clone_mask_mode(enum.Enum):
    filtered = "filtered"
    masked = "masked"
    replace = "replace"


class clone_mode(enum.Enum):
    force = "force"
    move = "move"
    normal = "normal"


class time_query(enum.Enum):
    day = "day"
    daytime = "daytime"
    gametime = "gametime"


class time(enum.Enum):
    day = "day"
    midnight = "midnight"
    night = "night"
    noon = "noon"


class team_attribute(enum.Enum):
    collision_rule = "collisionRule"
    color = "color"
    death_message_visibility = "deathMessageVisibility"
    display_name = "displayName"
    friendly_fire = "friendlyFire"
    nametag_visibility = "nametagVisibility"
    prefix = "prefix"
    see_friendly_invisibles = "seeFriendlyInvisibles"
    suffix = "suffix"


class collision_rule(enum.Enum):
    always = "always"
    never = "never"
    push_other_teams = "pushOtherTeams"
    push_own_team = "pushOwnTeam"


class _team_visibility(enum.Enum):
    always = "always"
    hide_for_other_teams = "hideForOtherTeams"
    hide_for_own_team = "hideForOwnTeam"
    never = "never"
death_message_visibility = _team_visibility
nametag_visibility = _team_visibility
