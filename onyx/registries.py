import enum


class gamemode(enum.Enum):
    """
    gamemode

    * survival
    * creative
    * spectator
    * adventure
    """

    survival = "survival"
    creative = "creative"
    spectator = "spectator"
    adventure = "adventure"


class selector_type(enum.Enum):
    """
    selector_type

    * all_players
    * all_entities
    * random_player
    * nearest_player
    * selected_entity
    """

    all_players = "@a"
    all_entities = "@e"
    random_player = "@r"
    nearest_player = "@p"
    selected_entity = "@s"


class entity_sort(enum.Enum):
    """
    entity_sort

    * arbitrary
    * furthest
    * nearest
    * random
    """

    arbitrary = "arbitrary"
    furthest = "furthest"
    nearest = "nearest"
    random = "random"


class scoreboard_display(enum.Enum):
    """
    scoreboard_display

    * below_name
    * list
    * sidebar
    * team_black
    * team_dark_blue
    * team_dark_green
    * team_dark_aqua
    * team_dark_red
    * team_dark_purple
    * team_gold
    * team_gray
    * team_dark_gray
    * team_blue
    * team_green
    * team_aqua
    * team_red
    * team_light_purple
    * team_yellow
    * team_white
    """

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
    """
    scoreboard_trait

    * display_name
    * render_type
    """

    display_name = "displayname"
    render_type = "rendertype"


class scoreboard_render_type(enum.Enum):
    """
    scoreboard_render_type

    * hearts
    * integer
    """

    hearts = "hearts"
    integer = "integer"


class color(enum.Enum):
    """
    color

    * black
    * dark_blue
    * dark_green
    * dark_aqua
    * dark_red
    * dark_purple
    * gold
    * gray
    * dark_gray
    * blue
    * green
    * aqua
    * red
    * light_purple
    * yellow
    * white
    """

    black = "black"
    dark_blue = "dark_blue"
    dark_green = "dark_green"
    dark_aqua = "dark_aqua"
    dark_red = "dark_red"
    dark_purple = "dark_purple"
    gold = "gold"
    gray = "gray"
    dark_gray = "dark_gray"
    blue = "blue"
    green = "green"
    aqua = "aqua"
    red = "red"
    light_purple = "light_purple"
    yellow = "yellow"
    white = "white"


class keybind(enum.Enum):
    """
    keybind

    * jump
    * sneak
    * sprint
    * left
    * right
    * back
    * forward
    * attack
    * pick_item
    * use
    * drop
    * hotbar_1
    * hotbar_2
    * hotbar_3
    * hotbar_4
    * hotbar_5
    * hotbar_6
    * hotbar_7
    * hotbar_8
    * hotbar_9
    * load_toolbar_activator
    * save_toolbar_activator
    * player_list
    * chat
    * command
    * advancements
    * spectator_outlines
    * outline_spectators
    * screenshot
    * smooth_camera
    * cinematic_camera
    * fullscreen
    * toggle_perspective
    """

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
    """
    click_event_action

    * change_page
    * copy_to_clipboard
    * open_url
    * run_command
    * suggest_command
    """

    change_page = "change_page"
    copy_to_clipboard = "copy_to_clipboard"
    open_url = "open_url"
    run_command = "run_command"
    suggest_command = "suggest_command"


class hover_event_action(enum.Enum):
    """
    hover_event_action

    * show_text
    * show_item
    """

    show_text = "show_text"
    show_item = "show_item"


class axis(enum.Enum):
    """
    axis

    * x
    * y
    * z
    """

    x = "x"
    y = "y"
    z = "z"


class anchor(enum.Enum):
    """
    anchor

    * feet
    * eyes
    """

    feet = "feet"
    eyes = "eyes"


class dimension(enum.Enum):
    """
    dimension

    * overworld
    * the_end
    * the_nether
    """

    overworld = "overworld"
    the_end = "the_end"
    the_nether = "the_nether"


class data_type(enum.Enum):
    """
    data_type

    * byte
    * double
    * float
    * int
    * long
    * short
    """

    byte = "byte"
    double = "double"
    float = "float"
    int = "int"
    long = "long"
    short = "short"


class bossbar_location(enum.Enum):
    """
    bossbar_location

    * max
    * value
    """

    max = "max"
    value = "value"


class source_type(enum.Enum):
    """
    source_type

    * block
    * entity
    * storage
    """

    block = "block"
    entity = "entity"
    storage = "storage"


class difficulty(enum.Enum):
    """
    difficulty

    * peaceful
    * easy
    * normal
    * hard
    """

    peaceful = "peaceful"
    easy = "easy"
    normal = "normal"
    hard = "hard"


class experience_type(enum.Enum):
    """
    experience_type

    * levels
    * point
    """

    levels = "levels"
    points = "points"


class weather_type(enum.Enum):
    """
    weather_type

    * clear
    * rain
    * thunder
    """

    clear = "clear"
    rain = "rain"
    thunder = "thunder"


class sound_channel(enum.Enum):
    """
    sound_channel

    * any
    * ambient
    * block
    * hostile
    * master
    * music
    * neutral
    * player
    * record
    * voice
    * weather
    """

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
    """
    setblock_mode

    * destroy
    * keep
    * replace
    """

    destroy = "destroy"
    keep = "keep"
    replace = "replace"


class fill_mode(enum.Enum):
    """
    fill_mode

    * destroy
    * hollow
    * keep
    * outline
    * replace
    """

    destroy = "destroy"
    hollow = "hollow"
    keep = "keep"
    outline = "outline"
    replace = "replace"


class clone_mask_mode(enum.Enum):
    """
    clone_mask_mode

    * filtered
    * masked
    * replace
    """

    filtered = "filtered"
    masked = "masked"
    replace = "replace"


class clone_mode(enum.Enum):
    """
    clone_mode

    * force
    * move
    * normal
    """

    force = "force"
    move = "move"
    normal = "normal"


class time_query(enum.Enum):
    """
    time_query

    * day
    * daytime
    * gametime
    """

    day = "day"
    daytime = "daytime"
    gametime = "gametime"


class time(enum.Enum):
    """
    time

    * day
    * midnight
    * night
    * noon
    """

    day = "day"
    midnight = "midnight"
    night = "night"
    noon = "noon"


class team_attribute(enum.Enum):
    """
    team_attribute

    * collision_rule
    * color
    * death_message_visibility
    * display_name
    * friendly_fire
    * nametag_visibility
    * prefix
    * see_friendly_invisibles
    * suffix
    """

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
    """
    collision_rule

    * always
    * never
    * push_other_teams
    * push_own_team
    """

    always = "always"
    never = "never"
    push_other_teams = "pushOtherTeams"
    push_own_team = "pushOwnTeam"


class _team_visibility(enum.Enum):
    """
    _team_visibility - Aliased by ``death_message_visibility`` and ``nametag_visibility``

    * always
    * hide_for_other_teams
    * hide_for_own_team
    * never
    """

    always = "always"
    hide_for_other_teams = "hideForOtherTeams"
    hide_for_own_team = "hideForOwnTeam"
    never = "never"


death_message_visibility = _team_visibility
nametag_visibility = _team_visibility


class advancement_mode(enum.Enum):
    """
    advancement_mode

    * everything
    * from_
    * only
    * through
    * until
    """

    everything = "everything"
    from_ = "from"
    only = "only"
    through = "through"
    until = "until"


class attribute(enum.Enum):
    """
    attribute

    * armor
    * armor_toughness
    * attack_damage
    * attack_knockback
    * attack_speed
    * flying_speed
    * follow_range
    * knockback_resistance
    * luck
    * max_health
    * movement_speed
    * jump_strength
    * spawn_reinforcements
    """

    armor = "minecraft:generic.armor"
    armor_toughness = "minecraft:generic.armor_toughness"
    attack_damage = "minecraft:generic.attack_damage"
    attack_knockback = "minecraft:generic.attack_knockback"
    attack_speed = "minecraft:generic.attack_speed"
    flying_speed = "minecraft:generic.flying_speed"
    follow_range = "minecraft:generic.follow_range"
    knockback_resistance = "minecraft:generic.knockback_resistance"
    luck = "minecraft:generic.luck"
    max_health = "minecraft:generic.max_health"
    movement_speed = "minecraft:generic.movement_speed"
    jump_strength = "minecraft:horse.jump_strength"
    spawn_reinforcements = "minecraft:zombie.spawn_reinforcements"


class attribute_mode(enum.Enum):
    """
    attribute_mode

    * get
    * get_base
    * set_base
    * add_modifier
    * get_modifier
    * remove_modifier
    """

    get = "get"
    get_base = "base get"
    set_base = "base set"
    add_modifier = "modifier add"
    get_modifier = "modifier value get"
    remove_modifier = "modifier remove"


class attribute_modifier_mode(enum.Enum):
    """
    attribute_modifier_mode

    * add
    * multiply
    * multiply_base
    """

    add = "add"
    multiply = "multiply"
    multiply_base = "multiply_base"


class bossbar_query(enum.Enum):
    """
    bossbar_query

    * max_value
    * players
    * value
    * is_visible
    """

    max_value = "max"
    players = "players"
    value = "value"
    is_visible = "visible"


class bossbar_color(enum.Enum):
    """
    bossbar_color

    * blue
    * green
    * pink
    * purple
    * red
    * white
    * yellow
    """

    blue = "blue"
    green = "green"
    pink = "pink"
    purple = "purple"
    red = "red"
    white = "white"
    yellow = "yellow"


class bossbar_style(enum.Enum):
    """
    bossbar_style

    * nothced_6
    * notched_10
    * notched_12
    * notched_20
    * progress
    """

    nothced_6 = "nothced_6"
    notched_10 = "notched_10"
    notched_12 = "notched_12"
    notched_20 = "notched_20"
    progress = "progress"


class data_operator(enum.Enum):
    """
    data_operator

    * append
    * insert
    * merge
    * prepend
    * set_from
    * set_value
    """

    append = "append"
    insert = "insert"
    merge = "merge"
    prepend = "prepend"
    set_from = "set from"
    set_value = "set value"


class datapack_enable_mode(enum.Enum):
    """
    datapack_enable_mode

    * after
    * before
    * first
    * last
    """

    after = "after"
    before = "before"
    first = "first"
    last = "last"


class loot_mode(enum.Enum):
    """
    loot_mode

    * fish
    * kill
    * loot
    * mine
    """

    fish = "fish"
    kill = "kill"
    loot = "loot"
    mine = "mine"


class hand(enum.Enum):
    """
    hand

    * offhand
    * mainhand
    """

    offhand = "offhand"
    mainhand = "mainhand"


class slot(enum.Enum):
    """
    slot

    * armor_chest
    * armor_feet
    * armor_head
    * armor_legs
    * container_0
    * container_1
    * container_2
    * container_3
    * container_4
    * container_5
    * container_6
    * container_7
    * container_8
    * container_9
    * container_10
    * container_11
    * container_12
    * container_13
    * container_14
    * container_15
    * container_16
    * container_17
    * container_18
    * container_19
    * container_20
    * container_21
    * container_22
    * container_23
    * container_24
    * container_25
    * container_26
    * container_27
    * container_28
    * container_29
    * container_30
    * container_31
    * container_32
    * container_33
    * container_34
    * container_35
    * container_36
    * container_37
    * container_38
    * container_39
    * container_40
    * container_41
    * container_42
    * container_43
    * container_44
    * container_45
    * container_46
    * container_47
    * container_48
    * container_49
    * container_50
    * container_51
    * container_52
    * container_53
    * enderchest_0
    * enderchest_1
    * enderchest_2
    * enderchest_3
    * enderchest_4
    * enderchest_5
    * enderchest_6
    * enderchest_7
    * enderchest_8
    * enderchest_9
    * enderchest_10
    * enderchest_11
    * enderchest_12
    * enderchest_13
    * enderchest_14
    * enderchest_15
    * enderchest_16
    * enderchest_17
    * enderchest_18
    * enderchest_19
    * enderchest_20
    * enderchest_21
    * enderchest_22
    * enderchest_23
    * enderchest_24
    * enderchest_25
    * enderchest_26
    * horse_0
    * horse_1
    * horse_2
    * horse_3
    * horse_4
    * horse_5
    * horse_6
    * horse_7
    * horse_8
    * horse_9
    * horse_10
    * horse_11
    * horse_12
    * horse_13
    * horse_14
    * horse_armor
    * horse_chest
    * horse_saddle
    * hotbar_0
    * hotbar_1
    * hotbar_2
    * hotbar_3
    * hotbar_4
    * hotbar_5
    * hotbar_6
    * hotbar_7
    * hotbar_8
    * inventory_0
    * inventory_1
    * inventory_2
    * inventory_3
    * inventory_4
    * inventory_5
    * inventory_6
    * inventory_7
    * inventory_8
    * inventory_9
    * inventory_10
    * inventory_11
    * inventory_12
    * inventory_13
    * inventory_14
    * inventory_15
    * inventory_16
    * inventory_17
    * inventory_18
    * inventory_19
    * inventory_20
    * inventory_21
    * inventory_22
    * inventory_23
    * inventory_24
    * inventory_25
    * inventory_26
    * villager_0
    * villager_1
    * villager_2
    * villager_3
    * villager_4
    * villager_5
    * villager_6
    * villager_7
    * weapon
    * weapon_mainhand
    * weapon_offhand
    """

    armor_chest = "armor.chest"
    armor_feet = "armor.feet"
    armor_head = "armor.head"
    armor_legs = "armor.legs"
    container_0 = "container.0"
    container_1 = "container.1"
    container_2 = "container.2"
    container_3 = "container.3"
    container_4 = "container.4"
    container_5 = "container.5"
    container_6 = "container.6"
    container_7 = "container.7"
    container_8 = "container.8"
    container_9 = "container.9"
    container_10 = "container.10"
    container_11 = "container.11"
    container_12 = "container.12"
    container_13 = "container.13"
    container_14 = "container.14"
    container_15 = "container.15"
    container_16 = "container.16"
    container_17 = "container.17"
    container_18 = "container.18"
    container_19 = "container.19"
    container_20 = "container.20"
    container_21 = "container.21"
    container_22 = "container.22"
    container_23 = "container.23"
    container_24 = "container.24"
    container_25 = "container.25"
    container_26 = "container.26"
    container_27 = "container.27"
    container_28 = "container.28"
    container_29 = "container.29"
    container_30 = "container.30"
    container_31 = "container.31"
    container_32 = "container.32"
    container_33 = "container.33"
    container_34 = "container.34"
    container_35 = "container.35"
    container_36 = "container.36"
    container_37 = "container.37"
    container_38 = "container.38"
    container_39 = "container.39"
    container_40 = "container.40"
    container_41 = "container.41"
    container_42 = "container.42"
    container_43 = "container.43"
    container_44 = "container.44"
    container_45 = "container.45"
    container_46 = "container.46"
    container_47 = "container.47"
    container_48 = "container.48"
    container_49 = "container.49"
    container_50 = "container.50"
    container_51 = "container.51"
    container_52 = "container.52"
    container_53 = "container.53"
    enderchest_0 = "enderchest.0"
    enderchest_1 = "enderchest.1"
    enderchest_2 = "enderchest.2"
    enderchest_3 = "enderchest.3"
    enderchest_4 = "enderchest.4"
    enderchest_5 = "enderchest.5"
    enderchest_6 = "enderchest.6"
    enderchest_7 = "enderchest.7"
    enderchest_8 = "enderchest.8"
    enderchest_9 = "enderchest.9"
    enderchest_10 = "enderchest.10"
    enderchest_11 = "enderchest.11"
    enderchest_12 = "enderchest.12"
    enderchest_13 = "enderchest.13"
    enderchest_14 = "enderchest.14"
    enderchest_15 = "enderchest.15"
    enderchest_16 = "enderchest.16"
    enderchest_17 = "enderchest.17"
    enderchest_18 = "enderchest.18"
    enderchest_19 = "enderchest.19"
    enderchest_20 = "enderchest.20"
    enderchest_21 = "enderchest.21"
    enderchest_22 = "enderchest.22"
    enderchest_23 = "enderchest.23"
    enderchest_24 = "enderchest.24"
    enderchest_25 = "enderchest.25"
    enderchest_26 = "enderchest.26"
    horse_0 = "horse.0"
    horse_1 = "horse.1"
    horse_2 = "horse.2"
    horse_3 = "horse.3"
    horse_4 = "horse.4"
    horse_5 = "horse.5"
    horse_6 = "horse.6"
    horse_7 = "horse.7"
    horse_8 = "horse.8"
    horse_9 = "horse.9"
    horse_10 = "horse.10"
    horse_11 = "horse.11"
    horse_12 = "horse.12"
    horse_13 = "horse.13"
    horse_14 = "horse.14"
    horse_armor = "horse.armor"
    horse_chest = "horse.chest"
    horse_saddle = "horse.saddle"
    hotbar_0 = "hotbar.0"
    hotbar_1 = "hotbar.1"
    hotbar_2 = "hotbar.2"
    hotbar_3 = "hotbar.3"
    hotbar_4 = "hotbar.4"
    hotbar_5 = "hotbar.5"
    hotbar_6 = "hotbar.6"
    hotbar_7 = "hotbar.7"
    hotbar_8 = "hotbar.8"
    inventory_0 = "inventory.0"
    inventory_1 = "inventory.1"
    inventory_2 = "inventory.2"
    inventory_3 = "inventory.3"
    inventory_4 = "inventory.4"
    inventory_5 = "inventory.5"
    inventory_6 = "inventory.6"
    inventory_7 = "inventory.7"
    inventory_8 = "inventory.8"
    inventory_9 = "inventory.9"
    inventory_10 = "inventory.10"
    inventory_11 = "inventory.11"
    inventory_12 = "inventory.12"
    inventory_13 = "inventory.13"
    inventory_14 = "inventory.14"
    inventory_15 = "inventory.15"
    inventory_16 = "inventory.16"
    inventory_17 = "inventory.17"
    inventory_18 = "inventory.18"
    inventory_19 = "inventory.19"
    inventory_20 = "inventory.20"
    inventory_21 = "inventory.21"
    inventory_22 = "inventory.22"
    inventory_23 = "inventory.23"
    inventory_24 = "inventory.24"
    inventory_25 = "inventory.25"
    inventory_26 = "inventory.26"
    villager_0 = "villager.0"
    villager_1 = "villager.1"
    villager_2 = "villager.2"
    villager_3 = "villager.3"
    villager_4 = "villager.4"
    villager_5 = "villager.5"
    villager_6 = "villager.6"
    villager_7 = "villager.7"
    weapon = "weapon"
    weapon_mainhand = "weapon.mainhand"
    weapon_offhand = "weapon.offhand"


class schedule_mode(enum.Enum):
    """
    schedule_mode

    * append
    * replace
    """

    append = "append"
    replace = "replace"
