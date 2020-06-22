import enum


# Gamemodes
class mode(enum.Enum):
    survival = "survival"
    creative = "creative"
    adventure = "adventure"
    spectator = "spectator"


# Used for "sort" property of selectors
class sort(enum.Enum):
    arbitrary = "arbitrary"
    furthest = "furthest"
    nearest = "nearest"
    random = "random"


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


# Used for text component "clickEvent" and "hoverEvent"
# show_entity is not supported since it requires an external generate to convert the UUIDs, and it's just a broken mess all around.
class action(enum.Enum):
    change_page = "change_page"		 # clickEvent exclusive
    copy = "copy_to_clipboard"    	 # clickEvent exclusive
    open_url = "open_url"            # clickEvent exclusive
    run_cmd = "run_command"          # clickEvent exclusive
    suggest_cmd = "suggest_command"	 # clickEvent exclusive
    show_text = "show_text"			 # hoverEvent exclusive
    show_item = "show_item"			 # hoverEvent exclusive


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


# Used for advancement
class advancement_action(enum.Enum):
    grant = "grant"
    revoke = "revoke"


# Used for advancement
# "from" is a reserved keywored
class selection(enum.Enum):
    everything = "everything"
    From = "from"
    only = "only"
    through = "through"
    until = "until"


# Used for datapack enable
class position(enum.Enum):
    after = "after"
    before = "before"
    first = "first"
    last = "last"


# Used for difficulty
class difficulty(enum.Enum):
    peaceful = "peaceful"
    easy = "easy"
    normal = "normal"
    hard = "hard"


# Used for effect
class effects(enum.Enum):
    all = "all"
    absorption = "absorption"
    bad_omen = "bad_omen"
    blindness = "blindness"
    conduit_power = "conduit_power"
    dolphins_grace = "dolphins_grace"
    fire_resistance = "fire_resistance"
    glowing = "glowing"
    haste = "haste"
    health_boost = "health_boost"
    hero_of_the_village = "hero_of_the_village"
    hunger = "hunger"
    instant_damage = "instant_damage"
    instant_health = "instant_health"
    invisibility = "invisibility"
    jump_boost = "jump_boost"
    levitation = "levitation"
    luck = "luck"
    mining_fatigue = "mining_fatigue"
    nausea = "nausea"
    night_vision = "night_vision"
    poison = "poison"
    regeneration = "regeneration"
    resistance = "resistance"
    saturation = "saturation"
    slow_falling = "slow_falling"
    slowness = "slowness"
    speed = "speed"
    strength = "strength"
    unluck = "unluck"
    water_breathing = "water_breathing"
    weakness = "weakness"
    wither = "wither"


# Used for data
class data_operator(enum.Enum):
    append = "append"
    insert = "insert"
    merge = "merge"
    prepend = "prepend"
    set = "set"


# Used for enchant
class enchants(enum.Enum):
    aqua_affinity = "aqua_affinity"
    bane_of_arthropods = "bane_of_arthropods"
    binding_curse = "binding_curse"
    blast_protection = "blast_protection"
    channeling = "channeling"
    depth_strider = "depth_strider"
    efficiency = "efficiency"
    feather_falling = "feather_falling"
    fire_aspect = "fire_aspect"
    fire_protection = "fire_protection"
    flame = "flame"
    fortune = "fortune"
    frost_walker = "frost_walker"
    impaling = "impaling"
    infinity = "infinity"
    knockback = "knockback"
    looting = "looting"
    loyalty = "loyalty"
    luck_of_the_sea = "luck_of_the_sea"
    lure = "lure"
    mending = "mending"
    multishot = "multishot"
    piercing = "piercing"
    power = "power"
    projectile_protection = "projectile_protection"
    protection = "protection"
    punch = "punch"
    quick_charge = "quick_charge"
    respiration = "respiration"
    riptide = "riptide"
    sharpness = "sharpness"
    silk_touch = "silk_touch"
    smite = "smite"
    soul_speed = "soul_speed"
    sweeping = "sweeping"
    thorns = "thorns"
    unbreaking = "unbreaking"
    vanishing_curse = "vanishing_curse"


# Used for experience
class xp(enum.Enum):
    levels = "levels"
    points = "points"


# Used for gamerule
class rule(enum.Enum):
    announceAdvancements = "announceAdvancements"
    commandBlockOutput = "commandBlockOutput"
    disableElytraMovementCheck = "disableElytraMovementCheck"
    disableRaids = "disableRaids"
    doDaylightCycle = "doDaylightCycle"
    doEntityDrops = "doEntityDrops"
    doFireTick = "doFireTick"
    doImmediateRespawn = "doImmediateRespawn"
    doInsomnia = "doInsomnia"
    doLimitedCrafting = "doLimitedCrafting"
    doMobLoot = "doMobLoot"
    doMobSpawning = "doMobSpawning"
    doPatrolSpawning = "doPatrolSpawning"
    doTileDrops = "doTileDrops"
    doTraderSpawning = "doTraderSpawning"
    doWeatherCycle = "doWeatherCycle"
    drowningDamage = "drowningDamage"
    fallDamage = "fallDamage"
    fireDamage = "fireDamage"
    forgiveDeadPlayers = "forgiveDeadPlayers"
    keepInventory = "keepInventory"
    logAdminCommands = "logAdminCommands"
    maxCommandChainLength = "maxCommandChainLength"
    maxEntityCramming = "maxEntityCramming"
    mobGriefing = "mobGriefing"
    naturalRegeneration = "naturalRegeneration"
    randomTickSpeed = "randomTickSpeed"
    reducedDebugInfo = "reducedDebugInfo"
    sendCommandFeedback = "sendCommandFeedback"
    showDeathMessages = "showDeathMessages"
    spawnRadius = "spawnRadius"
    spectatorsGenerateChunks = "spectatorsGenerateChunks"
    universalAnger = "universalAnger"


class lib(enum.Enum):
    rng = "rng"
    calc_xp_points = "calc_xp_points"
    math = "math"
