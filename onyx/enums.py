import enum


class mode(enum.Enum):
    """Gamemode list

    * survival
    * creative
    * adventure
    * spectator
    """
    survival = "survival"
    creative = "creative"
    adventure = "adventure"
    spectator = "spectator"


class sort(enum.Enum):
    """Used for sort property in selectors

    * arbitrary
    * furthest
    * nearest
    * random
    """
    arbitrary = "arbitrary"
    furthest = "furthest"
    nearest = "nearest"
    random = "random"


class at(enum.Enum):
    """Used for selector type

    * all_players
    * all_entities
    * nearest_player
    * random_player
    * selected_entity
    """
    all_players = "@a"
    all_entities = "@e"
    nearest_player = "@p"
    random_player = "@r"
    selected_entity = "@s"


# Used for execute align
class axis(enum.Enum):
    """Used for `align` in execute command

    * x
    * y
    * z
    """
    x = "x"
    y = "y"
    z = "z"


# Used for execute anchored
class anchor(enum.Enum):
    """Used for `anchored` in execute command

    * feet
    * eyes
    """
    feet = "feet"
    eyes = "eyes"


class dimension(enum.Enum):
    """Used for `in` in execute command

    * overworld
    * nether
    * end
    """
    overworld = "overworld"
    nether = "the_nether"
    end = "the_end"


class bossbar_trait(enum.Enum):
    """Used for modifying a bossbar property

    * color
    * max_value
    * name
    * players
    * style
    * value
    """
    color = "color"         		# set
    max_value = "max"       		# set and get
    name = "name"           		# set
    players = "players"     		# set and get
    style = "style"         		# set
    value = "value"      		    # set and get


class style(enum.Enum):
    """Used for modifying the style of a bossbar

    * six_segments
    * ten_segments
    * twelve_segments
    * twenty_segments
    * solid
    """
    six_segments = "notched_6"
    ten_segments = "notched_10"
    twelve_segments = "notched_12"
    twenty_segments = "notched_20"
    solid = "progress"


class color(enum.Enum):
    """Default colors (text-components and bossbars)

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
    * pink
    * purple
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
    blue = "blue"                   # bossbar compatible
    green = "green"                 # bossbar compatible
    pink = "pink"                   # bossbar exclusive
    purple = "purple"               # bossbar exclusive
    aqua = "aqua"
    red = "red"                     # bossbar compatible
    light_purple = "light_purple"
    yellow = "yellow"               # bossbar compatible
    white = "white"                 # bossbar compatible


# show_entity is not supported since it requires an external generator to convert the UUIDs, and it's just a broken mess all around.
class action(enum.Enum):
    """Used for text-component elements `HoverEvent` and `ClickEvent`

    * change_page
    * copy
    * open_url
    * run_cmd
    * suggest_cmd
    * show_text
    * show_item
    """
    change_page = "change_page"		 # clickEvent exclusive
    copy = "copy_to_clipboard"    	 # clickEvent exclusive
    open_url = "open_url"            # clickEvent exclusive
    run_cmd = "run_command"          # clickEvent exclusive
    suggest_cmd = "suggest_command"	 # clickEvent exclusive
    show_text = "show_text"			 # hoverEvent exclusive
    show_item = "show_item"			 # hoverEvent exclusive


class key(enum.Enum):
    """Used for text-component element `keybind`

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
    * hotbar_one
    * hotbar_two
    * hotbar_three
    * hotbar_four
    * hotbar_five
    * hotbar_six
    * hotbar_seven
    * hotbar_eight
    * hotbar_nine
    * load_toolbar_activator
    * save_toolbar_activator
    * player_list
    * chat
    * command
    * advancements
    * outline_spectators
    * screenshot
    * cinematic_camera
    * fullscreen
    * toggle_perspective
    """
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


class advancement_action(enum.Enum):
    """Used for the `action` value for the `attribute` command

    * grant
    * revoke
    """
    grant = "grant"
    revoke = "revoke"


class selection(enum.Enum):
    """Used for the `selection` value for the `attribute` command

    * everything
    * From (`from` is a reserved keyword)
    * only
    * through
    * until
    """
    everything = "everything"
    From = "from"
    only = "only"
    through = "through"
    until = "until"


class position(enum.Enum):
    """Used in `datapack enable`

    * after
    * before
    * first
    * last
    """
    after = "after"
    before = "before"
    first = "first"
    last = "last"


class difficulty(enum.Enum):
    """Difficulty list

    * peaceful
    * easy
    * normal
    * hard
    """
    peaceful = "peaceful"
    easy = "easy"
    normal = "normal"
    hard = "hard"


class effects(enum.Enum):
    """Effects list

    * all
    * absorption
    * bad_omen
    * blindness
    * conduit_power
    * dolphins_grace
    * fire_resistance
    * glowing
    * haste
    * health_boost
    * hero_of_the_village
    * hunger
    * instant_damage
    * instant_health
    * invisibility
    * jump_boost
    * levitation
    * luck
    * mining_fatigue
    * nausea
    * night_vision
    * poison
    * regeneration
    * resistance
    * saturation
    * slow_falling
    * slowness
    * speed
    * strength
    * unluck
    * water_breathing
    * weakness
    * wither
    """
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


class data_operator(enum.Enum):
    """Used for the `data` command

    * append
    * insert
    * merge
    * prepend
    * set
    """
    append = "append"
    insert = "insert"
    merge = "merge"
    prepend = "prepend"
    set = "set"


class enchants(enum.Enum):
    """Enchantment list

    * aqua_affinity
    * bane_of_arthropods
    * binding_curse
    * blast_protection
    * channeling
    * depth_strider
    * efficiency
    * feather_falling
    * fire_aspect
    * fire_protection
    * flame
    * fortune
    * frost_walker
    * impaling
    * infinity
    * knockback
    * looting
    * loyalty
    * luck_of_the_sea
    * lure
    * mending
    * multishot
    * piercing
    * power
    * projectile_protection
    * protection
    * punch
    * quick_charge
    * respiration
    * riptide
    * sharpness
    * silk_touch
    * smite
    * soul_speed
    * sweeping
    * thorns
    * unbreaking
    * vanishing_curse
    """
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


class xp(enum.Enum):
    """Used to specify experience quantity type

    * levels
    * points
    """
    levels = "levels"
    points = "points"


class rule(enum.Enum):
    """Gamerule list

    * announceAdvancements
    * commandBlockOutput
    * disableElytraMovementCheck
    * disableRaids
    * doDaylightCycle
    * doEntityDrops
    * doFireTick
    * doImmediateRespawn
    * doInsomnia
    * doLimitedCrafting
    * doMobLoot
    * doMobSpawning
    * doPatrolSpawning
    * doTileDrops
    * doTraderSpawning
    * doWeatherCycle
    * drowningDamage
    * fallDamage
    * fireDamage
    * forgiveDeadPlayers
    * keepInventory
    * logAdminCommands
    * maxCommandChainLength
    * maxEntityCramming
    * mobGriefing
    * naturalRegeneration
    * randomTickSpeed
    * reducedDebugInfo
    * sendCommandFeedback
    * showDeathMessages
    * spawnRadius
    * spectatorsGenerateChunks
    * universalAnger
    """
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
    """Onyx library list (mostly used internally)

    * rng
    * calc_xp_points
    * math
    * bitwise
    """
    rng = "rng"
    calc_xp_points = "calc_xp_points"
    math = "math"
    bitwise = "bitwise"


class scoreboard_trait(enum.Enum):
    """Modifiable trait list for scoreboards

    * displayname
    * rendertype
    """
    displayname = "displayname"
    rendertype = "rendertype"


class rendertype(enum.Enum):
    """Rendertype list for scoreboards

    * hearts
    * integer
    """
    hearts = "hearts"
    integer = "integer"
