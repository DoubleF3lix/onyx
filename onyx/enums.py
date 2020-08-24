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
    """Used for ``align`` in execute command

    * x
    * y
    * z
    """
    x = "x"
    y = "y"
    z = "z"


# Used for execute anchored
class anchor(enum.Enum):
    """Used for ``anchored`` in execute command

    * feet
    * eyes
    """
    feet = "feet"
    eyes = "eyes"


class dimension(enum.Enum):
    """Used for ``in`` in execute command

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
    """Used for text-component elements ``HoverEvent`` and ``ClickEvent``

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
    """Used for text-component element ``keybind``

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
    """Used for the ``action`` value for the ``attribute`` command

    * grant
    * revoke
    """
    grant = "grant"
    revoke = "revoke"


class selection(enum.Enum):
    """Used for the ``selection`` value for the ``attribute`` command

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
    """Used in ``datapack enable``

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
    """Used for the ``data`` command

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


class mask_mode(enum.Enum):
    """Masked mode for clone command (first mode argument)

    * filtered
    * masked
    * replace
    """
    filtered = "filtered"
    masked = "masked"
    replace = "replace"


class clone_mode(enum.Enum):
    """Clone mode for clone command (second mode argument)

    * force
    * move
    * normal
    """
    force = "force"
    move = "move"
    normal = "normal"


class fill_mode(enum.Enum):
    """Modes for fill command

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


class forceload_mode(enum.Enum):
    """Modes for forceload command

    * add
    * query
    * remove
    """
    add = "add"
    query = "query"
    remove = "remove"


class block(enum.Enum):
    """Block list

    * air
    * stone
    * granite
    * polished_granite
    * diorite
    * polished_diorite
    * andesite
    * polished_andesite
    * grass_block
    * dirt
    * coarse_dirt
    * podzol
    * cobblestone
    * oak_planks
    * spruce_planks
    * birch_planks
    * jungle_planks
    * acacia_planks
    * dark_oak_planks
    * oak_sapling
    * spruce_sapling
    * birch_sapling
    * jungle_sapling
    * acacia_sapling
    * dark_oak_sapling
    * bedrock
    * water
    * lava
    * sand
    * red_sand
    * gravel
    * gold_ore
    * iron_ore
    * coal_ore
    * nether_gold_ore
    * oak_log
    * spruce_log
    * birch_log
    * jungle_log
    * acacia_log
    * dark_oak_log
    * stripped_spruce_log
    * stripped_birch_log
    * stripped_jungle_log
    * stripped_acacia_log
    * stripped_dark_oak_log
    * stripped_oak_log
    * oak_wood
    * spruce_wood
    * birch_wood
    * jungle_wood
    * acacia_wood
    * dark_oak_wood
    * stripped_oak_wood
    * stripped_spruce_wood
    * stripped_birch_wood
    * stripped_jungle_wood
    * stripped_acacia_wood
    * stripped_dark_oak_wood
    * oak_leaves
    * spruce_leaves
    * birch_leaves
    * jungle_leaves
    * acacia_leaves
    * dark_oak_leaves
    * sponge
    * wet_sponge
    * glass
    * lapis_ore
    * lapis_block
    * dispenser
    * sandstone
    * chiseled_sandstone
    * cut_sandstone
    * note_block
    * white_bed
    * orange_bed
    * magenta_bed
    * light_blue_bed
    * yellow_bed
    * lime_bed
    * pink_bed
    * gray_bed
    * light_gray_bed
    * cyan_bed
    * purple_bed
    * blue_bed
    * brown_bed
    * green_bed
    * red_bed
    * black_bed
    * powered_rail
    * detector_rail
    * sticky_piston
    * cobweb
    * grass
    * fern
    * dead_bush
    * seagrass
    * tall_seagrass
    * piston
    * piston_head
    * white_wool
    * orange_wool
    * magenta_wool
    * light_blue_wool
    * yellow_wool
    * lime_wool
    * pink_wool
    * gray_wool
    * light_gray_wool
    * cyan_wool
    * purple_wool
    * blue_wool
    * brown_wool
    * green_wool
    * red_wool
    * black_wool
    * moving_piston
    * dandelion
    * poppy
    * blue_orchid
    * allium
    * azure_bluet
    * red_tulip
    * orange_tulip
    * white_tulip
    * pink_tulip
    * oxeye_daisy
    * cornflower
    * wither_rose
    * lily_of_the_valley
    * brown_mushroom
    * red_mushroom
    * gold_block
    * iron_block
    * bricks
    * tnt
    * bookshelf
    * mossy_cobblestone
    * obsidian
    * torch
    * wall_torch
    * fire
    * soul_fire
    * spawner
    * oak_stairs
    * chest
    * redstone_wire
    * diamond_ore
    * diamond_block
    * crafting_table
    * wheat
    * farmland
    * furnace
    * oak_sign
    * spruce_sign
    * birch_sign
    * acacia_sign
    * jungle_sign
    * dark_oak_sign
    * oak_door
    * ladder
    * rail
    * cobblestone_stairs
    * oak_wall_sign
    * spruce_wall_sign
    * birch_wall_sign
    * acacia_wall_sign
    * jungle_wall_sign
    * dark_oak_wall_sign
    * lever
    * stone_pressure_plate
    * iron_door
    * oak_pressure_plate
    * spruce_pressure_plate
    * birch_pressure_plate
    * jungle_pressure_plate
    * acacia_pressure_plate
    * dark_oak_pressure_plate
    * redstone_ore
    * redstone_torch
    * redstone_wall_torch
    * stone_button
    * snow
    * ice
    * snow_block
    * cactus
    * clay
    * sugar_cane
    * jukebox
    * oak_fence
    * pumpkin
    * netherrack
    * soul_sand
    * soul_soil
    * basalt
    * polished_basalt
    * soul_torch
    * soul_wall_torch
    * glowstone
    * nether_portal
    * carved_pumpkin
    * jack_o_lantern
    * cake
    * repeater
    * white_stained_glass
    * orange_stained_glass
    * magenta_stained_glass
    * light_blue_stained_glass
    * yellow_stained_glass
    * lime_stained_glass
    * pink_stained_glass
    * gray_stained_glass
    * light_gray_stained_glass
    * cyan_stained_glass
    * purple_stained_glass
    * blue_stained_glass
    * brown_stained_glass
    * green_stained_glass
    * red_stained_glass
    * black_stained_glass
    * oak_trapdoor
    * spruce_trapdoor
    * birch_trapdoor
    * jungle_trapdoor
    * acacia_trapdoor
    * dark_oak_trapdoor
    * stone_bricks
    * mossy_stone_bricks
    * cracked_stone_bricks
    * chiseled_stone_bricks
    * infested_stone
    * infested_cobblestone
    * infested_stone_bricks
    * infested_mossy_stone_bricks
    * infested_cracked_stone_bricks
    * infested_chiseled_stone_bricks
    * brown_mushroom_block
    * red_mushroom_block
    * mushroom_stem
    * iron_bars
    * chain
    * glass_pane
    * melon
    * attached_pumpkin_stem
    * attached_melon_stem
    * pumpkin_stem
    * melon_stem
    * vine
    * oak_fence_gate
    * brick_stairs
    * stone_brick_stairs
    * mycelium
    * lily_pad
    * nether_bricks
    * nether_brick_fence
    * nether_brick_stairs
    * nether_wart
    * enchanting_table
    * brewing_stand
    * cauldron
    * end_portal
    * end_portal_frame
    * end_stone
    * dragon_egg
    * redstone_lamp
    * cocoa
    * sandstone_stairs
    * emerald_ore
    * ender_chest
    * tripwire_hook
    * tripwire
    * emerald_block
    * spruce_stairs
    * birch_stairs
    * jungle_stairs
    * command_block
    * beacon
    * cobblestone_wall
    * mossy_cobblestone_wall
    * flower_pot
    * potted_oak_sapling
    * potted_spruce_sapling
    * potted_birch_sapling
    * potted_jungle_sapling
    * potted_acacia_sapling
    * potted_dark_oak_sapling
    * potted_fern
    * potted_dandelion
    * potted_poppy
    * potted_blue_orchid
    * potted_allium
    * potted_azure_bluet
    * potted_red_tulip
    * potted_orange_tulip
    * potted_white_tulip
    * potted_pink_tulip
    * potted_oxeye_daisy
    * potted_cornflower
    * potted_lily_of_the_valley
    * potted_wither_rose
    * potted_red_mushroom
    * potted_brown_mushroom
    * potted_dead_bush
    * potted_cactus
    * carrots
    * potatoes
    * oak_button
    * spruce_button
    * birch_button
    * jungle_button
    * acacia_button
    * dark_oak_button
    * skeleton_skull
    * skeleton_wall_skull
    * wither_skeleton_skull
    * wither_skeleton_wall_skull
    * zombie_head
    * zombie_wall_head
    * player_head
    * player_wall_head
    * creeper_head
    * creeper_wall_head
    * dragon_head
    * dragon_wall_head
    * anvil
    * chipped_anvil
    * damaged_anvil
    * trapped_chest
    * light_weighted_pressure_plate
    * heavy_weighted_pressure_plate
    * comparator
    * daylight_detector
    * redstone_block
    * nether_quartz_ore
    * hopper
    * quartz_block
    * chiseled_quartz_block
    * quartz_pillar
    * quartz_stairs
    * activator_rail
    * dropper
    * white_terracotta
    * orange_terracotta
    * magenta_terracotta
    * light_blue_terracotta
    * yellow_terracotta
    * lime_terracotta
    * pink_terracotta
    * gray_terracotta
    * light_gray_terracotta
    * cyan_terracotta
    * purple_terracotta
    * blue_terracotta
    * brown_terracotta
    * green_terracotta
    * red_terracotta
    * black_terracotta
    * white_stained_glass_pane
    * orange_stained_glass_pane
    * magenta_stained_glass_pane
    * light_blue_stained_glass_pane
    * yellow_stained_glass_pane
    * lime_stained_glass_pane
    * pink_stained_glass_pane
    * gray_stained_glass_pane
    * light_gray_stained_glass_pane
    * cyan_stained_glass_pane
    * purple_stained_glass_pane
    * blue_stained_glass_pane
    * brown_stained_glass_pane
    * green_stained_glass_pane
    * red_stained_glass_pane
    * black_stained_glass_pane
    * acacia_stairs
    * dark_oak_stairs
    * slime_block
    * barrier
    * iron_trapdoor
    * prismarine
    * prismarine_bricks
    * dark_prismarine
    * prismarine_stairs
    * prismarine_brick_stairs
    * dark_prismarine_stairs
    * prismarine_slab
    * prismarine_brick_slab
    * dark_prismarine_slab
    * sea_lantern
    * hay_block
    * white_carpet
    * orange_carpet
    * magenta_carpet
    * light_blue_carpet
    * yellow_carpet
    * lime_carpet
    * pink_carpet
    * gray_carpet
    * light_gray_carpet
    * cyan_carpet
    * purple_carpet
    * blue_carpet
    * brown_carpet
    * green_carpet
    * red_carpet
    * black_carpet
    * terracotta
    * coal_block
    * packed_ice
    * sunflower
    * lilac
    * rose_bush
    * peony
    * tall_grass
    * large_fern
    * white_banner
    * orange_banner
    * magenta_banner
    * light_blue_banner
    * yellow_banner
    * lime_banner
    * pink_banner
    * gray_banner
    * light_gray_banner
    * cyan_banner
    * purple_banner
    * blue_banner
    * brown_banner
    * green_banner
    * red_banner
    * black_banner
    * white_wall_banner
    * orange_wall_banner
    * magenta_wall_banner
    * light_blue_wall_banner
    * yellow_wall_banner
    * lime_wall_banner
    * pink_wall_banner
    * gray_wall_banner
    * light_gray_wall_banner
    * cyan_wall_banner
    * purple_wall_banner
    * blue_wall_banner
    * brown_wall_banner
    * green_wall_banner
    * red_wall_banner
    * black_wall_banner
    * red_sandstone
    * chiseled_red_sandstone
    * cut_red_sandstone
    * red_sandstone_stairs
    * oak_slab
    * spruce_slab
    * birch_slab
    * jungle_slab
    * acacia_slab
    * dark_oak_slab
    * stone_slab
    * smooth_stone_slab
    * sandstone_slab
    * cut_sandstone_slab
    * petrified_oak_slab
    * cobblestone_slab
    * brick_slab
    * stone_brick_slab
    * nether_brick_slab
    * quartz_slab
    * red_sandstone_slab
    * cut_red_sandstone_slab
    * purpur_slab
    * smooth_stone
    * smooth_sandstone
    * smooth_quartz
    * smooth_red_sandstone
    * spruce_fence_gate
    * birch_fence_gate
    * jungle_fence_gate
    * acacia_fence_gate
    * dark_oak_fence_gate
    * spruce_fence
    * birch_fence
    * jungle_fence
    * acacia_fence
    * dark_oak_fence
    * spruce_door
    * birch_door
    * jungle_door
    * acacia_door
    * dark_oak_door
    * end_rod
    * chorus_plant
    * chorus_flower
    * purpur_block
    * purpur_pillar
    * purpur_stairs
    * end_stone_bricks
    * beetroots
    * grass_path
    * end_gateway
    * repeating_command_block
    * chain_command_block
    * frosted_ice
    * magma_block
    * nether_wart_block
    * red_nether_bricks
    * bone_block
    * structure_void
    * observer
    * shulker_box
    * white_shulker_box
    * orange_shulker_box
    * magenta_shulker_box
    * light_blue_shulker_box
    * yellow_shulker_box
    * lime_shulker_box
    * pink_shulker_box
    * gray_shulker_box
    * light_gray_shulker_box
    * cyan_shulker_box
    * purple_shulker_box
    * blue_shulker_box
    * brown_shulker_box
    * green_shulker_box
    * red_shulker_box
    * black_shulker_box
    * white_glazed_terracotta
    * orange_glazed_terracotta
    * magenta_glazed_terracotta
    * light_blue_glazed_terracotta
    * yellow_glazed_terracotta
    * lime_glazed_terracotta
    * pink_glazed_terracotta
    * gray_glazed_terracotta
    * light_gray_glazed_terracotta
    * cyan_glazed_terracotta
    * purple_glazed_terracotta
    * blue_glazed_terracotta
    * brown_glazed_terracotta
    * green_glazed_terracotta
    * red_glazed_terracotta
    * black_glazed_terracotta
    * white_concrete
    * orange_concrete
    * magenta_concrete
    * light_blue_concrete
    * yellow_concrete
    * lime_concrete
    * pink_concrete
    * gray_concrete
    * light_gray_concrete
    * cyan_concrete
    * purple_concrete
    * blue_concrete
    * brown_concrete
    * green_concrete
    * red_concrete
    * black_concrete
    * white_concrete_powder
    * orange_concrete_powder
    * magenta_concrete_powder
    * light_blue_concrete_powder
    * yellow_concrete_powder
    * lime_concrete_powder
    * pink_concrete_powder
    * gray_concrete_powder
    * light_gray_concrete_powder
    * cyan_concrete_powder
    * purple_concrete_powder
    * blue_concrete_powder
    * brown_concrete_powder
    * green_concrete_powder
    * red_concrete_powder
    * black_concrete_powder
    * kelp
    * kelp_plant
    * dried_kelp_block
    * turtle_egg
    * dead_tube_coral_block
    * dead_brain_coral_block
    * dead_bubble_coral_block
    * dead_fire_coral_block
    * dead_horn_coral_block
    * tube_coral_block
    * brain_coral_block
    * bubble_coral_block
    * fire_coral_block
    * horn_coral_block
    * dead_tube_coral
    * dead_brain_coral
    * dead_bubble_coral
    * dead_fire_coral
    * dead_horn_coral
    * tube_coral
    * brain_coral
    * bubble_coral
    * fire_coral
    * horn_coral
    * dead_tube_coral_fan
    * dead_brain_coral_fan
    * dead_bubble_coral_fan
    * dead_fire_coral_fan
    * dead_horn_coral_fan
    * tube_coral_fan
    * brain_coral_fan
    * bubble_coral_fan
    * fire_coral_fan
    * horn_coral_fan
    * dead_tube_coral_wall_fan
    * dead_brain_coral_wall_fan
    * dead_bubble_coral_wall_fan
    * dead_fire_coral_wall_fan
    * dead_horn_coral_wall_fan
    * tube_coral_wall_fan
    * brain_coral_wall_fan
    * bubble_coral_wall_fan
    * fire_coral_wall_fan
    * horn_coral_wall_fan
    * sea_pickle
    * blue_ice
    * conduit
    * bamboo_sapling
    * bamboo
    * potted_bamboo
    * void_air
    * cave_air
    * bubble_column
    * polished_granite_stairs
    * smooth_red_sandstone_stairs
    * mossy_stone_brick_stairs
    * polished_diorite_stairs
    * mossy_cobblestone_stairs
    * end_stone_brick_stairs
    * stone_stairs
    * smooth_sandstone_stairs
    * smooth_quartz_stairs
    * granite_stairs
    * andesite_stairs
    * red_nether_brick_stairs
    * polished_andesite_stairs
    * diorite_stairs
    * polished_granite_slab
    * smooth_red_sandstone_slab
    * mossy_stone_brick_slab
    * polished_diorite_slab
    * mossy_cobblestone_slab
    * end_stone_brick_slab
    * smooth_sandstone_slab
    * smooth_quartz_slab
    * granite_slab
    * andesite_slab
    * red_nether_brick_slab
    * polished_andesite_slab
    * diorite_slab
    * brick_wall
    * prismarine_wall
    * red_sandstone_wall
    * mossy_stone_brick_wall
    * granite_wall
    * stone_brick_wall
    * nether_brick_wall
    * andesite_wall
    * red_nether_brick_wall
    * sandstone_wall
    * end_stone_brick_wall
    * diorite_wall
    * scaffolding
    * loom
    * barrel
    * smoker
    * blast_furnace
    * cartography_table
    * fletching_table
    * grindstone
    * lectern
    * smithing_table
    * stonecutter
    * bell
    * lantern
    * soul_lantern
    * campfire
    * soul_campfire
    * sweet_berry_bush
    * warped_stem
    * stripped_warped_stem
    * warped_hyphae
    * stripped_warped_hyphae
    * warped_nylium
    * warped_fungus
    * warped_wart_block
    * warped_roots
    * nether_sprouts
    * crimson_stem
    * stripped_crimson_stem
    * crimson_hyphae
    * stripped_crimson_hyphae
    * crimson_nylium
    * crimson_fungus
    * shroomlight
    * weeping_vines
    * weeping_vines_plant
    * twisting_vines
    * twisting_vines_plant
    * crimson_roots
    * crimson_planks
    * warped_planks
    * crimson_slab
    * warped_slab
    * crimson_pressure_plate
    * warped_pressure_plate
    * crimson_fence
    * warped_fence
    * crimson_trapdoor
    * warped_trapdoor
    * crimson_fence_gate
    * warped_fence_gate
    * crimson_stairs
    * warped_stairs
    * crimson_button
    * warped_button
    * crimson_door
    * warped_door
    * crimson_sign
    * warped_sign
    * crimson_wall_sign
    * warped_wall_sign
    * structure_block
    * jigsaw
    * composter
    * target
    * bee_nest
    * beehive
    * honey_block
    * honeycomb_block
    * netherite_block
    * ancient_debris
    * crying_obsidian
    * respawn_anchor
    * potted_crimson_fungus
    * potted_warped_fungus
    * potted_crimson_roots
    * potted_warped_roots
    * lodestone
    * blackstone
    * blackstone_stairs
    * blackstone_wall
    * blackstone_slab
    * polished_blackstone
    * polished_blackstone_bricks
    * cracked_polished_blackstone_bricks
    * chiseled_polished_blackstone
    * polished_blackstone_brick_slab
    * polished_blackstone_brick_stairs
    * polished_blackstone_brick_wall
    * gilded_blackstone
    * polished_blackstone_stairs
    * polished_blackstone_slab
    * polished_blackstone_pressure_plate
    * polished_blackstone_button
    * polished_blackstone_wall
    * chiseled_nether_bricks
    * cracked_nether_bricks
    * quartz_bricks
    """
    air = "minecraft:air"
    stone = "minecraft:stone"
    granite = "minecraft:granite"
    polished_granite = "minecraft:polished_granite"
    diorite = "minecraft:diorite"
    polished_diorite = "minecraft:polished_diorite"
    andesite = "minecraft:andesite"
    polished_andesite = "minecraft:polished_andesite"
    grass_block = "minecraft:grass_block"
    dirt = "minecraft:dirt"
    coarse_dirt = "minecraft:coarse_dirt"
    podzol = "minecraft:podzol"
    cobblestone = "minecraft:cobblestone"
    oak_planks = "minecraft:oak_planks"
    spruce_planks = "minecraft:spruce_planks"
    birch_planks = "minecraft:birch_planks"
    jungle_planks = "minecraft:jungle_planks"
    acacia_planks = "minecraft:acacia_planks"
    dark_oak_planks = "minecraft:dark_oak_planks"
    oak_sapling = "minecraft:oak_sapling"
    spruce_sapling = "minecraft:spruce_sapling"
    birch_sapling = "minecraft:birch_sapling"
    jungle_sapling = "minecraft:jungle_sapling"
    acacia_sapling = "minecraft:acacia_sapling"
    dark_oak_sapling = "minecraft:dark_oak_sapling"
    bedrock = "minecraft:bedrock"
    water = "minecraft:water"
    lava = "minecraft:lava"
    sand = "minecraft:sand"
    red_sand = "minecraft:red_sand"
    gravel = "minecraft:gravel"
    gold_ore = "minecraft:gold_ore"
    iron_ore = "minecraft:iron_ore"
    coal_ore = "minecraft:coal_ore"
    nether_gold_ore = "minecraft:nether_gold_ore"
    oak_log = "minecraft:oak_log"
    spruce_log = "minecraft:spruce_log"
    birch_log = "minecraft:birch_log"
    jungle_log = "minecraft:jungle_log"
    acacia_log = "minecraft:acacia_log"
    dark_oak_log = "minecraft:dark_oak_log"
    stripped_spruce_log = "minecraft:stripped_spruce_log"
    stripped_birch_log = "minecraft:stripped_birch_log"
    stripped_jungle_log = "minecraft:stripped_jungle_log"
    stripped_acacia_log = "minecraft:stripped_acacia_log"
    stripped_dark_oak_log = "minecraft:stripped_dark_oak_log"
    stripped_oak_log = "minecraft:stripped_oak_log"
    oak_wood = "minecraft:oak_wood"
    spruce_wood = "minecraft:spruce_wood"
    birch_wood = "minecraft:birch_wood"
    jungle_wood = "minecraft:jungle_wood"
    acacia_wood = "minecraft:acacia_wood"
    dark_oak_wood = "minecraft:dark_oak_wood"
    stripped_oak_wood = "minecraft:stripped_oak_wood"
    stripped_spruce_wood = "minecraft:stripped_spruce_wood"
    stripped_birch_wood = "minecraft:stripped_birch_wood"
    stripped_jungle_wood = "minecraft:stripped_jungle_wood"
    stripped_acacia_wood = "minecraft:stripped_acacia_wood"
    stripped_dark_oak_wood = "minecraft:stripped_dark_oak_wood"
    oak_leaves = "minecraft:oak_leaves"
    spruce_leaves = "minecraft:spruce_leaves"
    birch_leaves = "minecraft:birch_leaves"
    jungle_leaves = "minecraft:jungle_leaves"
    acacia_leaves = "minecraft:acacia_leaves"
    dark_oak_leaves = "minecraft:dark_oak_leaves"
    sponge = "minecraft:sponge"
    wet_sponge = "minecraft:wet_sponge"
    glass = "minecraft:glass"
    lapis_ore = "minecraft:lapis_ore"
    lapis_block = "minecraft:lapis_block"
    dispenser = "minecraft:dispenser"
    sandstone = "minecraft:sandstone"
    chiseled_sandstone = "minecraft:chiseled_sandstone"
    cut_sandstone = "minecraft:cut_sandstone"
    note_block = "minecraft:note_block"
    white_bed = "minecraft:white_bed"
    orange_bed = "minecraft:orange_bed"
    magenta_bed = "minecraft:magenta_bed"
    light_blue_bed = "minecraft:light_blue_bed"
    yellow_bed = "minecraft:yellow_bed"
    lime_bed = "minecraft:lime_bed"
    pink_bed = "minecraft:pink_bed"
    gray_bed = "minecraft:gray_bed"
    light_gray_bed = "minecraft:light_gray_bed"
    cyan_bed = "minecraft:cyan_bed"
    purple_bed = "minecraft:purple_bed"
    blue_bed = "minecraft:blue_bed"
    brown_bed = "minecraft:brown_bed"
    green_bed = "minecraft:green_bed"
    red_bed = "minecraft:red_bed"
    black_bed = "minecraft:black_bed"
    powered_rail = "minecraft:powered_rail"
    detector_rail = "minecraft:detector_rail"
    sticky_piston = "minecraft:sticky_piston"
    cobweb = "minecraft:cobweb"
    grass = "minecraft:grass"
    fern = "minecraft:fern"
    dead_bush = "minecraft:dead_bush"
    seagrass = "minecraft:seagrass"
    tall_seagrass = "minecraft:tall_seagrass"
    piston = "minecraft:piston"
    piston_head = "minecraft:piston_head"
    white_wool = "minecraft:white_wool"
    orange_wool = "minecraft:orange_wool"
    magenta_wool = "minecraft:magenta_wool"
    light_blue_wool = "minecraft:light_blue_wool"
    yellow_wool = "minecraft:yellow_wool"
    lime_wool = "minecraft:lime_wool"
    pink_wool = "minecraft:pink_wool"
    gray_wool = "minecraft:gray_wool"
    light_gray_wool = "minecraft:light_gray_wool"
    cyan_wool = "minecraft:cyan_wool"
    purple_wool = "minecraft:purple_wool"
    blue_wool = "minecraft:blue_wool"
    brown_wool = "minecraft:brown_wool"
    green_wool = "minecraft:green_wool"
    red_wool = "minecraft:red_wool"
    black_wool = "minecraft:black_wool"
    moving_piston = "minecraft:moving_piston"
    dandelion = "minecraft:dandelion"
    poppy = "minecraft:poppy"
    blue_orchid = "minecraft:blue_orchid"
    allium = "minecraft:allium"
    azure_bluet = "minecraft:azure_bluet"
    red_tulip = "minecraft:red_tulip"
    orange_tulip = "minecraft:orange_tulip"
    white_tulip = "minecraft:white_tulip"
    pink_tulip = "minecraft:pink_tulip"
    oxeye_daisy = "minecraft:oxeye_daisy"
    cornflower = "minecraft:cornflower"
    wither_rose = "minecraft:wither_rose"
    lily_of_the_valley = "minecraft:lily_of_the_valley"
    brown_mushroom = "minecraft:brown_mushroom"
    red_mushroom = "minecraft:red_mushroom"
    gold_block = "minecraft:gold_block"
    iron_block = "minecraft:iron_block"
    bricks = "minecraft:bricks"
    tnt = "minecraft:tnt"
    bookshelf = "minecraft:bookshelf"
    mossy_cobblestone = "minecraft:mossy_cobblestone"
    obsidian = "minecraft:obsidian"
    torch = "minecraft:torch"
    wall_torch = "minecraft:wall_torch"
    fire = "minecraft:fire"
    soul_fire = "minecraft:soul_fire"
    spawner = "minecraft:spawner"
    oak_stairs = "minecraft:oak_stairs"
    chest = "minecraft:chest"
    redstone_wire = "minecraft:redstone_wire"
    diamond_ore = "minecraft:diamond_ore"
    diamond_block = "minecraft:diamond_block"
    crafting_table = "minecraft:crafting_table"
    wheat = "minecraft:wheat"
    farmland = "minecraft:farmland"
    furnace = "minecraft:furnace"
    oak_sign = "minecraft:oak_sign"
    spruce_sign = "minecraft:spruce_sign"
    birch_sign = "minecraft:birch_sign"
    acacia_sign = "minecraft:acacia_sign"
    jungle_sign = "minecraft:jungle_sign"
    dark_oak_sign = "minecraft:dark_oak_sign"
    oak_door = "minecraft:oak_door"
    ladder = "minecraft:ladder"
    rail = "minecraft:rail"
    cobblestone_stairs = "minecraft:cobblestone_stairs"
    oak_wall_sign = "minecraft:oak_wall_sign"
    spruce_wall_sign = "minecraft:spruce_wall_sign"
    birch_wall_sign = "minecraft:birch_wall_sign"
    acacia_wall_sign = "minecraft:acacia_wall_sign"
    jungle_wall_sign = "minecraft:jungle_wall_sign"
    dark_oak_wall_sign = "minecraft:dark_oak_wall_sign"
    lever = "minecraft:lever"
    stone_pressure_plate = "minecraft:stone_pressure_plate"
    iron_door = "minecraft:iron_door"
    oak_pressure_plate = "minecraft:oak_pressure_plate"
    spruce_pressure_plate = "minecraft:spruce_pressure_plate"
    birch_pressure_plate = "minecraft:birch_pressure_plate"
    jungle_pressure_plate = "minecraft:jungle_pressure_plate"
    acacia_pressure_plate = "minecraft:acacia_pressure_plate"
    dark_oak_pressure_plate = "minecraft:dark_oak_pressure_plate"
    redstone_ore = "minecraft:redstone_ore"
    redstone_torch = "minecraft:redstone_torch"
    redstone_wall_torch = "minecraft:redstone_wall_torch"
    stone_button = "minecraft:stone_button"
    snow = "minecraft:snow"
    ice = "minecraft:ice"
    snow_block = "minecraft:snow_block"
    cactus = "minecraft:cactus"
    clay = "minecraft:clay"
    sugar_cane = "minecraft:sugar_cane"
    jukebox = "minecraft:jukebox"
    oak_fence = "minecraft:oak_fence"
    pumpkin = "minecraft:pumpkin"
    netherrack = "minecraft:netherrack"
    soul_sand = "minecraft:soul_sand"
    soul_soil = "minecraft:soul_soil"
    basalt = "minecraft:basalt"
    polished_basalt = "minecraft:polished_basalt"
    soul_torch = "minecraft:soul_torch"
    soul_wall_torch = "minecraft:soul_wall_torch"
    glowstone = "minecraft:glowstone"
    nether_portal = "minecraft:nether_portal"
    carved_pumpkin = "minecraft:carved_pumpkin"
    jack_o_lantern = "minecraft:jack_o_lantern"
    cake = "minecraft:cake"
    repeater = "minecraft:repeater"
    white_stained_glass = "minecraft:white_stained_glass"
    orange_stained_glass = "minecraft:orange_stained_glass"
    magenta_stained_glass = "minecraft:magenta_stained_glass"
    light_blue_stained_glass = "minecraft:light_blue_stained_glass"
    yellow_stained_glass = "minecraft:yellow_stained_glass"
    lime_stained_glass = "minecraft:lime_stained_glass"
    pink_stained_glass = "minecraft:pink_stained_glass"
    gray_stained_glass = "minecraft:gray_stained_glass"
    light_gray_stained_glass = "minecraft:light_gray_stained_glass"
    cyan_stained_glass = "minecraft:cyan_stained_glass"
    purple_stained_glass = "minecraft:purple_stained_glass"
    blue_stained_glass = "minecraft:blue_stained_glass"
    brown_stained_glass = "minecraft:brown_stained_glass"
    green_stained_glass = "minecraft:green_stained_glass"
    red_stained_glass = "minecraft:red_stained_glass"
    black_stained_glass = "minecraft:black_stained_glass"
    oak_trapdoor = "minecraft:oak_trapdoor"
    spruce_trapdoor = "minecraft:spruce_trapdoor"
    birch_trapdoor = "minecraft:birch_trapdoor"
    jungle_trapdoor = "minecraft:jungle_trapdoor"
    acacia_trapdoor = "minecraft:acacia_trapdoor"
    dark_oak_trapdoor = "minecraft:dark_oak_trapdoor"
    stone_bricks = "minecraft:stone_bricks"
    mossy_stone_bricks = "minecraft:mossy_stone_bricks"
    cracked_stone_bricks = "minecraft:cracked_stone_bricks"
    chiseled_stone_bricks = "minecraft:chiseled_stone_bricks"
    infested_stone = "minecraft:infested_stone"
    infested_cobblestone = "minecraft:infested_cobblestone"
    infested_stone_bricks = "minecraft:infested_stone_bricks"
    infested_mossy_stone_bricks = "minecraft:infested_mossy_stone_bricks"
    infested_cracked_stone_bricks = "minecraft:infested_cracked_stone_bricks"
    infested_chiseled_stone_bricks = "minecraft:infested_chiseled_stone_bricks"
    brown_mushroom_block = "minecraft:brown_mushroom_block"
    red_mushroom_block = "minecraft:red_mushroom_block"
    mushroom_stem = "minecraft:mushroom_stem"
    iron_bars = "minecraft:iron_bars"
    chain = "minecraft:chain"
    glass_pane = "minecraft:glass_pane"
    melon = "minecraft:melon"
    attached_pumpkin_stem = "minecraft:attached_pumpkin_stem"
    attached_melon_stem = "minecraft:attached_melon_stem"
    pumpkin_stem = "minecraft:pumpkin_stem"
    melon_stem = "minecraft:melon_stem"
    vine = "minecraft:vine"
    oak_fence_gate = "minecraft:oak_fence_gate"
    brick_stairs = "minecraft:brick_stairs"
    stone_brick_stairs = "minecraft:stone_brick_stairs"
    mycelium = "minecraft:mycelium"
    lily_pad = "minecraft:lily_pad"
    nether_bricks = "minecraft:nether_bricks"
    nether_brick_fence = "minecraft:nether_brick_fence"
    nether_brick_stairs = "minecraft:nether_brick_stairs"
    nether_wart = "minecraft:nether_wart"
    enchanting_table = "minecraft:enchanting_table"
    brewing_stand = "minecraft:brewing_stand"
    cauldron = "minecraft:cauldron"
    end_portal = "minecraft:end_portal"
    end_portal_frame = "minecraft:end_portal_frame"
    end_stone = "minecraft:end_stone"
    dragon_egg = "minecraft:dragon_egg"
    redstone_lamp = "minecraft:redstone_lamp"
    cocoa = "minecraft:cocoa"
    sandstone_stairs = "minecraft:sandstone_stairs"
    emerald_ore = "minecraft:emerald_ore"
    ender_chest = "minecraft:ender_chest"
    tripwire_hook = "minecraft:tripwire_hook"
    tripwire = "minecraft:tripwire"
    emerald_block = "minecraft:emerald_block"
    spruce_stairs = "minecraft:spruce_stairs"
    birch_stairs = "minecraft:birch_stairs"
    jungle_stairs = "minecraft:jungle_stairs"
    command_block = "minecraft:command_block"
    beacon = "minecraft:beacon"
    cobblestone_wall = "minecraft:cobblestone_wall"
    mossy_cobblestone_wall = "minecraft:mossy_cobblestone_wall"
    flower_pot = "minecraft:flower_pot"
    potted_oak_sapling = "minecraft:potted_oak_sapling"
    potted_spruce_sapling = "minecraft:potted_spruce_sapling"
    potted_birch_sapling = "minecraft:potted_birch_sapling"
    potted_jungle_sapling = "minecraft:potted_jungle_sapling"
    potted_acacia_sapling = "minecraft:potted_acacia_sapling"
    potted_dark_oak_sapling = "minecraft:potted_dark_oak_sapling"
    potted_fern = "minecraft:potted_fern"
    potted_dandelion = "minecraft:potted_dandelion"
    potted_poppy = "minecraft:potted_poppy"
    potted_blue_orchid = "minecraft:potted_blue_orchid"
    potted_allium = "minecraft:potted_allium"
    potted_azure_bluet = "minecraft:potted_azure_bluet"
    potted_red_tulip = "minecraft:potted_red_tulip"
    potted_orange_tulip = "minecraft:potted_orange_tulip"
    potted_white_tulip = "minecraft:potted_white_tulip"
    potted_pink_tulip = "minecraft:potted_pink_tulip"
    potted_oxeye_daisy = "minecraft:potted_oxeye_daisy"
    potted_cornflower = "minecraft:potted_cornflower"
    potted_lily_of_the_valley = "minecraft:potted_lily_of_the_valley"
    potted_wither_rose = "minecraft:potted_wither_rose"
    potted_red_mushroom = "minecraft:potted_red_mushroom"
    potted_brown_mushroom = "minecraft:potted_brown_mushroom"
    potted_dead_bush = "minecraft:potted_dead_bush"
    potted_cactus = "minecraft:potted_cactus"
    carrots = "minecraft:carrots"
    potatoes = "minecraft:potatoes"
    oak_button = "minecraft:oak_button"
    spruce_button = "minecraft:spruce_button"
    birch_button = "minecraft:birch_button"
    jungle_button = "minecraft:jungle_button"
    acacia_button = "minecraft:acacia_button"
    dark_oak_button = "minecraft:dark_oak_button"
    skeleton_skull = "minecraft:skeleton_skull"
    skeleton_wall_skull = "minecraft:skeleton_wall_skull"
    wither_skeleton_skull = "minecraft:wither_skeleton_skull"
    wither_skeleton_wall_skull = "minecraft:wither_skeleton_wall_skull"
    zombie_head = "minecraft:zombie_head"
    zombie_wall_head = "minecraft:zombie_wall_head"
    player_head = "minecraft:player_head"
    player_wall_head = "minecraft:player_wall_head"
    creeper_head = "minecraft:creeper_head"
    creeper_wall_head = "minecraft:creeper_wall_head"
    dragon_head = "minecraft:dragon_head"
    dragon_wall_head = "minecraft:dragon_wall_head"
    anvil = "minecraft:anvil"
    chipped_anvil = "minecraft:chipped_anvil"
    damaged_anvil = "minecraft:damaged_anvil"
    trapped_chest = "minecraft:trapped_chest"
    light_weighted_pressure_plate = "minecraft:light_weighted_pressure_plate"
    heavy_weighted_pressure_plate = "minecraft:heavy_weighted_pressure_plate"
    comparator = "minecraft:comparator"
    daylight_detector = "minecraft:daylight_detector"
    redstone_block = "minecraft:redstone_block"
    nether_quartz_ore = "minecraft:nether_quartz_ore"
    hopper = "minecraft:hopper"
    quartz_block = "minecraft:quartz_block"
    chiseled_quartz_block = "minecraft:chiseled_quartz_block"
    quartz_pillar = "minecraft:quartz_pillar"
    quartz_stairs = "minecraft:quartz_stairs"
    activator_rail = "minecraft:activator_rail"
    dropper = "minecraft:dropper"
    white_terracotta = "minecraft:white_terracotta"
    orange_terracotta = "minecraft:orange_terracotta"
    magenta_terracotta = "minecraft:magenta_terracotta"
    light_blue_terracotta = "minecraft:light_blue_terracotta"
    yellow_terracotta = "minecraft:yellow_terracotta"
    lime_terracotta = "minecraft:lime_terracotta"
    pink_terracotta = "minecraft:pink_terracotta"
    gray_terracotta = "minecraft:gray_terracotta"
    light_gray_terracotta = "minecraft:light_gray_terracotta"
    cyan_terracotta = "minecraft:cyan_terracotta"
    purple_terracotta = "minecraft:purple_terracotta"
    blue_terracotta = "minecraft:blue_terracotta"
    brown_terracotta = "minecraft:brown_terracotta"
    green_terracotta = "minecraft:green_terracotta"
    red_terracotta = "minecraft:red_terracotta"
    black_terracotta = "minecraft:black_terracotta"
    white_stained_glass_pane = "minecraft:white_stained_glass_pane"
    orange_stained_glass_pane = "minecraft:orange_stained_glass_pane"
    magenta_stained_glass_pane = "minecraft:magenta_stained_glass_pane"
    light_blue_stained_glass_pane = "minecraft:light_blue_stained_glass_pane"
    yellow_stained_glass_pane = "minecraft:yellow_stained_glass_pane"
    lime_stained_glass_pane = "minecraft:lime_stained_glass_pane"
    pink_stained_glass_pane = "minecraft:pink_stained_glass_pane"
    gray_stained_glass_pane = "minecraft:gray_stained_glass_pane"
    light_gray_stained_glass_pane = "minecraft:light_gray_stained_glass_pane"
    cyan_stained_glass_pane = "minecraft:cyan_stained_glass_pane"
    purple_stained_glass_pane = "minecraft:purple_stained_glass_pane"
    blue_stained_glass_pane = "minecraft:blue_stained_glass_pane"
    brown_stained_glass_pane = "minecraft:brown_stained_glass_pane"
    green_stained_glass_pane = "minecraft:green_stained_glass_pane"
    red_stained_glass_pane = "minecraft:red_stained_glass_pane"
    black_stained_glass_pane = "minecraft:black_stained_glass_pane"
    acacia_stairs = "minecraft:acacia_stairs"
    dark_oak_stairs = "minecraft:dark_oak_stairs"
    slime_block = "minecraft:slime_block"
    barrier = "minecraft:barrier"
    iron_trapdoor = "minecraft:iron_trapdoor"
    prismarine = "minecraft:prismarine"
    prismarine_bricks = "minecraft:prismarine_bricks"
    dark_prismarine = "minecraft:dark_prismarine"
    prismarine_stairs = "minecraft:prismarine_stairs"
    prismarine_brick_stairs = "minecraft:prismarine_brick_stairs"
    dark_prismarine_stairs = "minecraft:dark_prismarine_stairs"
    prismarine_slab = "minecraft:prismarine_slab"
    prismarine_brick_slab = "minecraft:prismarine_brick_slab"
    dark_prismarine_slab = "minecraft:dark_prismarine_slab"
    sea_lantern = "minecraft:sea_lantern"
    hay_block = "minecraft:hay_block"
    white_carpet = "minecraft:white_carpet"
    orange_carpet = "minecraft:orange_carpet"
    magenta_carpet = "minecraft:magenta_carpet"
    light_blue_carpet = "minecraft:light_blue_carpet"
    yellow_carpet = "minecraft:yellow_carpet"
    lime_carpet = "minecraft:lime_carpet"
    pink_carpet = "minecraft:pink_carpet"
    gray_carpet = "minecraft:gray_carpet"
    light_gray_carpet = "minecraft:light_gray_carpet"
    cyan_carpet = "minecraft:cyan_carpet"
    purple_carpet = "minecraft:purple_carpet"
    blue_carpet = "minecraft:blue_carpet"
    brown_carpet = "minecraft:brown_carpet"
    green_carpet = "minecraft:green_carpet"
    red_carpet = "minecraft:red_carpet"
    black_carpet = "minecraft:black_carpet"
    terracotta = "minecraft:terracotta"
    coal_block = "minecraft:coal_block"
    packed_ice = "minecraft:packed_ice"
    sunflower = "minecraft:sunflower"
    lilac = "minecraft:lilac"
    rose_bush = "minecraft:rose_bush"
    peony = "minecraft:peony"
    tall_grass = "minecraft:tall_grass"
    large_fern = "minecraft:large_fern"
    white_banner = "minecraft:white_banner"
    orange_banner = "minecraft:orange_banner"
    magenta_banner = "minecraft:magenta_banner"
    light_blue_banner = "minecraft:light_blue_banner"
    yellow_banner = "minecraft:yellow_banner"
    lime_banner = "minecraft:lime_banner"
    pink_banner = "minecraft:pink_banner"
    gray_banner = "minecraft:gray_banner"
    light_gray_banner = "minecraft:light_gray_banner"
    cyan_banner = "minecraft:cyan_banner"
    purple_banner = "minecraft:purple_banner"
    blue_banner = "minecraft:blue_banner"
    brown_banner = "minecraft:brown_banner"
    green_banner = "minecraft:green_banner"
    red_banner = "minecraft:red_banner"
    black_banner = "minecraft:black_banner"
    white_wall_banner = "minecraft:white_wall_banner"
    orange_wall_banner = "minecraft:orange_wall_banner"
    magenta_wall_banner = "minecraft:magenta_wall_banner"
    light_blue_wall_banner = "minecraft:light_blue_wall_banner"
    yellow_wall_banner = "minecraft:yellow_wall_banner"
    lime_wall_banner = "minecraft:lime_wall_banner"
    pink_wall_banner = "minecraft:pink_wall_banner"
    gray_wall_banner = "minecraft:gray_wall_banner"
    light_gray_wall_banner = "minecraft:light_gray_wall_banner"
    cyan_wall_banner = "minecraft:cyan_wall_banner"
    purple_wall_banner = "minecraft:purple_wall_banner"
    blue_wall_banner = "minecraft:blue_wall_banner"
    brown_wall_banner = "minecraft:brown_wall_banner"
    green_wall_banner = "minecraft:green_wall_banner"
    red_wall_banner = "minecraft:red_wall_banner"
    black_wall_banner = "minecraft:black_wall_banner"
    red_sandstone = "minecraft:red_sandstone"
    chiseled_red_sandstone = "minecraft:chiseled_red_sandstone"
    cut_red_sandstone = "minecraft:cut_red_sandstone"
    red_sandstone_stairs = "minecraft:red_sandstone_stairs"
    oak_slab = "minecraft:oak_slab"
    spruce_slab = "minecraft:spruce_slab"
    birch_slab = "minecraft:birch_slab"
    jungle_slab = "minecraft:jungle_slab"
    acacia_slab = "minecraft:acacia_slab"
    dark_oak_slab = "minecraft:dark_oak_slab"
    stone_slab = "minecraft:stone_slab"
    smooth_stone_slab = "minecraft:smooth_stone_slab"
    sandstone_slab = "minecraft:sandstone_slab"
    cut_sandstone_slab = "minecraft:cut_sandstone_slab"
    petrified_oak_slab = "minecraft:petrified_oak_slab"
    cobblestone_slab = "minecraft:cobblestone_slab"
    brick_slab = "minecraft:brick_slab"
    stone_brick_slab = "minecraft:stone_brick_slab"
    nether_brick_slab = "minecraft:nether_brick_slab"
    quartz_slab = "minecraft:quartz_slab"
    red_sandstone_slab = "minecraft:red_sandstone_slab"
    cut_red_sandstone_slab = "minecraft:cut_red_sandstone_slab"
    purpur_slab = "minecraft:purpur_slab"
    smooth_stone = "minecraft:smooth_stone"
    smooth_sandstone = "minecraft:smooth_sandstone"
    smooth_quartz = "minecraft:smooth_quartz"
    smooth_red_sandstone = "minecraft:smooth_red_sandstone"
    spruce_fence_gate = "minecraft:spruce_fence_gate"
    birch_fence_gate = "minecraft:birch_fence_gate"
    jungle_fence_gate = "minecraft:jungle_fence_gate"
    acacia_fence_gate = "minecraft:acacia_fence_gate"
    dark_oak_fence_gate = "minecraft:dark_oak_fence_gate"
    spruce_fence = "minecraft:spruce_fence"
    birch_fence = "minecraft:birch_fence"
    jungle_fence = "minecraft:jungle_fence"
    acacia_fence = "minecraft:acacia_fence"
    dark_oak_fence = "minecraft:dark_oak_fence"
    spruce_door = "minecraft:spruce_door"
    birch_door = "minecraft:birch_door"
    jungle_door = "minecraft:jungle_door"
    acacia_door = "minecraft:acacia_door"
    dark_oak_door = "minecraft:dark_oak_door"
    end_rod = "minecraft:end_rod"
    chorus_plant = "minecraft:chorus_plant"
    chorus_flower = "minecraft:chorus_flower"
    purpur_block = "minecraft:purpur_block"
    purpur_pillar = "minecraft:purpur_pillar"
    purpur_stairs = "minecraft:purpur_stairs"
    end_stone_bricks = "minecraft:end_stone_bricks"
    beetroots = "minecraft:beetroots"
    grass_path = "minecraft:grass_path"
    end_gateway = "minecraft:end_gateway"
    repeating_command_block = "minecraft:repeating_command_block"
    chain_command_block = "minecraft:chain_command_block"
    frosted_ice = "minecraft:frosted_ice"
    magma_block = "minecraft:magma_block"
    nether_wart_block = "minecraft:nether_wart_block"
    red_nether_bricks = "minecraft:red_nether_bricks"
    bone_block = "minecraft:bone_block"
    structure_void = "minecraft:structure_void"
    observer = "minecraft:observer"
    shulker_box = "minecraft:shulker_box"
    white_shulker_box = "minecraft:white_shulker_box"
    orange_shulker_box = "minecraft:orange_shulker_box"
    magenta_shulker_box = "minecraft:magenta_shulker_box"
    light_blue_shulker_box = "minecraft:light_blue_shulker_box"
    yellow_shulker_box = "minecraft:yellow_shulker_box"
    lime_shulker_box = "minecraft:lime_shulker_box"
    pink_shulker_box = "minecraft:pink_shulker_box"
    gray_shulker_box = "minecraft:gray_shulker_box"
    light_gray_shulker_box = "minecraft:light_gray_shulker_box"
    cyan_shulker_box = "minecraft:cyan_shulker_box"
    purple_shulker_box = "minecraft:purple_shulker_box"
    blue_shulker_box = "minecraft:blue_shulker_box"
    brown_shulker_box = "minecraft:brown_shulker_box"
    green_shulker_box = "minecraft:green_shulker_box"
    red_shulker_box = "minecraft:red_shulker_box"
    black_shulker_box = "minecraft:black_shulker_box"
    white_glazed_terracotta = "minecraft:white_glazed_terracotta"
    orange_glazed_terracotta = "minecraft:orange_glazed_terracotta"
    magenta_glazed_terracotta = "minecraft:magenta_glazed_terracotta"
    light_blue_glazed_terracotta = "minecraft:light_blue_glazed_terracotta"
    yellow_glazed_terracotta = "minecraft:yellow_glazed_terracotta"
    lime_glazed_terracotta = "minecraft:lime_glazed_terracotta"
    pink_glazed_terracotta = "minecraft:pink_glazed_terracotta"
    gray_glazed_terracotta = "minecraft:gray_glazed_terracotta"
    light_gray_glazed_terracotta = "minecraft:light_gray_glazed_terracotta"
    cyan_glazed_terracotta = "minecraft:cyan_glazed_terracotta"
    purple_glazed_terracotta = "minecraft:purple_glazed_terracotta"
    blue_glazed_terracotta = "minecraft:blue_glazed_terracotta"
    brown_glazed_terracotta = "minecraft:brown_glazed_terracotta"
    green_glazed_terracotta = "minecraft:green_glazed_terracotta"
    red_glazed_terracotta = "minecraft:red_glazed_terracotta"
    black_glazed_terracotta = "minecraft:black_glazed_terracotta"
    white_concrete = "minecraft:white_concrete"
    orange_concrete = "minecraft:orange_concrete"
    magenta_concrete = "minecraft:magenta_concrete"
    light_blue_concrete = "minecraft:light_blue_concrete"
    yellow_concrete = "minecraft:yellow_concrete"
    lime_concrete = "minecraft:lime_concrete"
    pink_concrete = "minecraft:pink_concrete"
    gray_concrete = "minecraft:gray_concrete"
    light_gray_concrete = "minecraft:light_gray_concrete"
    cyan_concrete = "minecraft:cyan_concrete"
    purple_concrete = "minecraft:purple_concrete"
    blue_concrete = "minecraft:blue_concrete"
    brown_concrete = "minecraft:brown_concrete"
    green_concrete = "minecraft:green_concrete"
    red_concrete = "minecraft:red_concrete"
    black_concrete = "minecraft:black_concrete"
    white_concrete_powder = "minecraft:white_concrete_powder"
    orange_concrete_powder = "minecraft:orange_concrete_powder"
    magenta_concrete_powder = "minecraft:magenta_concrete_powder"
    light_blue_concrete_powder = "minecraft:light_blue_concrete_powder"
    yellow_concrete_powder = "minecraft:yellow_concrete_powder"
    lime_concrete_powder = "minecraft:lime_concrete_powder"
    pink_concrete_powder = "minecraft:pink_concrete_powder"
    gray_concrete_powder = "minecraft:gray_concrete_powder"
    light_gray_concrete_powder = "minecraft:light_gray_concrete_powder"
    cyan_concrete_powder = "minecraft:cyan_concrete_powder"
    purple_concrete_powder = "minecraft:purple_concrete_powder"
    blue_concrete_powder = "minecraft:blue_concrete_powder"
    brown_concrete_powder = "minecraft:brown_concrete_powder"
    green_concrete_powder = "minecraft:green_concrete_powder"
    red_concrete_powder = "minecraft:red_concrete_powder"
    black_concrete_powder = "minecraft:black_concrete_powder"
    kelp = "minecraft:kelp"
    kelp_plant = "minecraft:kelp_plant"
    dried_kelp_block = "minecraft:dried_kelp_block"
    turtle_egg = "minecraft:turtle_egg"
    dead_tube_coral_block = "minecraft:dead_tube_coral_block"
    dead_brain_coral_block = "minecraft:dead_brain_coral_block"
    dead_bubble_coral_block = "minecraft:dead_bubble_coral_block"
    dead_fire_coral_block = "minecraft:dead_fire_coral_block"
    dead_horn_coral_block = "minecraft:dead_horn_coral_block"
    tube_coral_block = "minecraft:tube_coral_block"
    brain_coral_block = "minecraft:brain_coral_block"
    bubble_coral_block = "minecraft:bubble_coral_block"
    fire_coral_block = "minecraft:fire_coral_block"
    horn_coral_block = "minecraft:horn_coral_block"
    dead_tube_coral = "minecraft:dead_tube_coral"
    dead_brain_coral = "minecraft:dead_brain_coral"
    dead_bubble_coral = "minecraft:dead_bubble_coral"
    dead_fire_coral = "minecraft:dead_fire_coral"
    dead_horn_coral = "minecraft:dead_horn_coral"
    tube_coral = "minecraft:tube_coral"
    brain_coral = "minecraft:brain_coral"
    bubble_coral = "minecraft:bubble_coral"
    fire_coral = "minecraft:fire_coral"
    horn_coral = "minecraft:horn_coral"
    dead_tube_coral_fan = "minecraft:dead_tube_coral_fan"
    dead_brain_coral_fan = "minecraft:dead_brain_coral_fan"
    dead_bubble_coral_fan = "minecraft:dead_bubble_coral_fan"
    dead_fire_coral_fan = "minecraft:dead_fire_coral_fan"
    dead_horn_coral_fan = "minecraft:dead_horn_coral_fan"
    tube_coral_fan = "minecraft:tube_coral_fan"
    brain_coral_fan = "minecraft:brain_coral_fan"
    bubble_coral_fan = "minecraft:bubble_coral_fan"
    fire_coral_fan = "minecraft:fire_coral_fan"
    horn_coral_fan = "minecraft:horn_coral_fan"
    dead_tube_coral_wall_fan = "minecraft:dead_tube_coral_wall_fan"
    dead_brain_coral_wall_fan = "minecraft:dead_brain_coral_wall_fan"
    dead_bubble_coral_wall_fan = "minecraft:dead_bubble_coral_wall_fan"
    dead_fire_coral_wall_fan = "minecraft:dead_fire_coral_wall_fan"
    dead_horn_coral_wall_fan = "minecraft:dead_horn_coral_wall_fan"
    tube_coral_wall_fan = "minecraft:tube_coral_wall_fan"
    brain_coral_wall_fan = "minecraft:brain_coral_wall_fan"
    bubble_coral_wall_fan = "minecraft:bubble_coral_wall_fan"
    fire_coral_wall_fan = "minecraft:fire_coral_wall_fan"
    horn_coral_wall_fan = "minecraft:horn_coral_wall_fan"
    sea_pickle = "minecraft:sea_pickle"
    blue_ice = "minecraft:blue_ice"
    conduit = "minecraft:conduit"
    bamboo_sapling = "minecraft:bamboo_sapling"
    bamboo = "minecraft:bamboo"
    potted_bamboo = "minecraft:potted_bamboo"
    void_air = "minecraft:void_air"
    cave_air = "minecraft:cave_air"
    bubble_column = "minecraft:bubble_column"
    polished_granite_stairs = "minecraft:polished_granite_stairs"
    smooth_red_sandstone_stairs = "minecraft:smooth_red_sandstone_stairs"
    mossy_stone_brick_stairs = "minecraft:mossy_stone_brick_stairs"
    polished_diorite_stairs = "minecraft:polished_diorite_stairs"
    mossy_cobblestone_stairs = "minecraft:mossy_cobblestone_stairs"
    end_stone_brick_stairs = "minecraft:end_stone_brick_stairs"
    stone_stairs = "minecraft:stone_stairs"
    smooth_sandstone_stairs = "minecraft:smooth_sandstone_stairs"
    smooth_quartz_stairs = "minecraft:smooth_quartz_stairs"
    granite_stairs = "minecraft:granite_stairs"
    andesite_stairs = "minecraft:andesite_stairs"
    red_nether_brick_stairs = "minecraft:red_nether_brick_stairs"
    polished_andesite_stairs = "minecraft:polished_andesite_stairs"
    diorite_stairs = "minecraft:diorite_stairs"
    polished_granite_slab = "minecraft:polished_granite_slab"
    smooth_red_sandstone_slab = "minecraft:smooth_red_sandstone_slab"
    mossy_stone_brick_slab = "minecraft:mossy_stone_brick_slab"
    polished_diorite_slab = "minecraft:polished_diorite_slab"
    mossy_cobblestone_slab = "minecraft:mossy_cobblestone_slab"
    end_stone_brick_slab = "minecraft:end_stone_brick_slab"
    smooth_sandstone_slab = "minecraft:smooth_sandstone_slab"
    smooth_quartz_slab = "minecraft:smooth_quartz_slab"
    granite_slab = "minecraft:granite_slab"
    andesite_slab = "minecraft:andesite_slab"
    red_nether_brick_slab = "minecraft:red_nether_brick_slab"
    polished_andesite_slab = "minecraft:polished_andesite_slab"
    diorite_slab = "minecraft:diorite_slab"
    brick_wall = "minecraft:brick_wall"
    prismarine_wall = "minecraft:prismarine_wall"
    red_sandstone_wall = "minecraft:red_sandstone_wall"
    mossy_stone_brick_wall = "minecraft:mossy_stone_brick_wall"
    granite_wall = "minecraft:granite_wall"
    stone_brick_wall = "minecraft:stone_brick_wall"
    nether_brick_wall = "minecraft:nether_brick_wall"
    andesite_wall = "minecraft:andesite_wall"
    red_nether_brick_wall = "minecraft:red_nether_brick_wall"
    sandstone_wall = "minecraft:sandstone_wall"
    end_stone_brick_wall = "minecraft:end_stone_brick_wall"
    diorite_wall = "minecraft:diorite_wall"
    scaffolding = "minecraft:scaffolding"
    loom = "minecraft:loom"
    barrel = "minecraft:barrel"
    smoker = "minecraft:smoker"
    blast_furnace = "minecraft:blast_furnace"
    cartography_table = "minecraft:cartography_table"
    fletching_table = "minecraft:fletching_table"
    grindstone = "minecraft:grindstone"
    lectern = "minecraft:lectern"
    smithing_table = "minecraft:smithing_table"
    stonecutter = "minecraft:stonecutter"
    bell = "minecraft:bell"
    lantern = "minecraft:lantern"
    soul_lantern = "minecraft:soul_lantern"
    campfire = "minecraft:campfire"
    soul_campfire = "minecraft:soul_campfire"
    sweet_berry_bush = "minecraft:sweet_berry_bush"
    warped_stem = "minecraft:warped_stem"
    stripped_warped_stem = "minecraft:stripped_warped_stem"
    warped_hyphae = "minecraft:warped_hyphae"
    stripped_warped_hyphae = "minecraft:stripped_warped_hyphae"
    warped_nylium = "minecraft:warped_nylium"
    warped_fungus = "minecraft:warped_fungus"
    warped_wart_block = "minecraft:warped_wart_block"
    warped_roots = "minecraft:warped_roots"
    nether_sprouts = "minecraft:nether_sprouts"
    crimson_stem = "minecraft:crimson_stem"
    stripped_crimson_stem = "minecraft:stripped_crimson_stem"
    crimson_hyphae = "minecraft:crimson_hyphae"
    stripped_crimson_hyphae = "minecraft:stripped_crimson_hyphae"
    crimson_nylium = "minecraft:crimson_nylium"
    crimson_fungus = "minecraft:crimson_fungus"
    shroomlight = "minecraft:shroomlight"
    weeping_vines = "minecraft:weeping_vines"
    weeping_vines_plant = "minecraft:weeping_vines_plant"
    twisting_vines = "minecraft:twisting_vines"
    twisting_vines_plant = "minecraft:twisting_vines_plant"
    crimson_roots = "minecraft:crimson_roots"
    crimson_planks = "minecraft:crimson_planks"
    warped_planks = "minecraft:warped_planks"
    crimson_slab = "minecraft:crimson_slab"
    warped_slab = "minecraft:warped_slab"
    crimson_pressure_plate = "minecraft:crimson_pressure_plate"
    warped_pressure_plate = "minecraft:warped_pressure_plate"
    crimson_fence = "minecraft:crimson_fence"
    warped_fence = "minecraft:warped_fence"
    crimson_trapdoor = "minecraft:crimson_trapdoor"
    warped_trapdoor = "minecraft:warped_trapdoor"
    crimson_fence_gate = "minecraft:crimson_fence_gate"
    warped_fence_gate = "minecraft:warped_fence_gate"
    crimson_stairs = "minecraft:crimson_stairs"
    warped_stairs = "minecraft:warped_stairs"
    crimson_button = "minecraft:crimson_button"
    warped_button = "minecraft:warped_button"
    crimson_door = "minecraft:crimson_door"
    warped_door = "minecraft:warped_door"
    crimson_sign = "minecraft:crimson_sign"
    warped_sign = "minecraft:warped_sign"
    crimson_wall_sign = "minecraft:crimson_wall_sign"
    warped_wall_sign = "minecraft:warped_wall_sign"
    structure_block = "minecraft:structure_block"
    jigsaw = "minecraft:jigsaw"
    composter = "minecraft:composter"
    target = "minecraft:target"
    bee_nest = "minecraft:bee_nest"
    beehive = "minecraft:beehive"
    honey_block = "minecraft:honey_block"
    honeycomb_block = "minecraft:honeycomb_block"
    netherite_block = "minecraft:netherite_block"
    ancient_debris = "minecraft:ancient_debris"
    crying_obsidian = "minecraft:crying_obsidian"
    respawn_anchor = "minecraft:respawn_anchor"
    potted_crimson_fungus = "minecraft:potted_crimson_fungus"
    potted_warped_fungus = "minecraft:potted_warped_fungus"
    potted_crimson_roots = "minecraft:potted_crimson_roots"
    potted_warped_roots = "minecraft:potted_warped_roots"
    lodestone = "minecraft:lodestone"
    blackstone = "minecraft:blackstone"
    blackstone_stairs = "minecraft:blackstone_stairs"
    blackstone_wall = "minecraft:blackstone_wall"
    blackstone_slab = "minecraft:blackstone_slab"
    polished_blackstone = "minecraft:polished_blackstone"
    polished_blackstone_bricks = "minecraft:polished_blackstone_bricks"
    cracked_polished_blackstone_bricks = "minecraft:cracked_polished_blackstone_bricks"
    chiseled_polished_blackstone = "minecraft:chiseled_polished_blackstone"
    polished_blackstone_brick_slab = "minecraft:polished_blackstone_brick_slab"
    polished_blackstone_brick_stairs = "minecraft:polished_blackstone_brick_stairs"
    polished_blackstone_brick_wall = "minecraft:polished_blackstone_brick_wall"
    gilded_blackstone = "minecraft:gilded_blackstone"
    polished_blackstone_stairs = "minecraft:polished_blackstone_stairs"
    polished_blackstone_slab = "minecraft:polished_blackstone_slab"
    polished_blackstone_pressure_plate = "minecraft:polished_blackstone_pressure_plate"
    polished_blackstone_button = "minecraft:polished_blackstone_button"
    polished_blackstone_wall = "minecraft:polished_blackstone_wall"
    chiseled_nether_bricks = "minecraft:chiseled_nether_bricks"
    cracked_nether_bricks = "minecraft:cracked_nether_bricks"
    quartz_bricks = "minecraft:quartz_bricks"


class item(enum.Enum):
    """
    * air
    * stone
    * granite
    * polished_granite
    * diorite
    * polished_diorite
    * andesite
    * polished_andesite
    * grass_block
    * dirt
    * coarse_dirt
    * podzol
    * crimson_nylium
    * warped_nylium
    * cobblestone
    * oak_planks
    * spruce_planks
    * birch_planks
    * jungle_planks
    * acacia_planks
    * dark_oak_planks
    * crimson_planks
    * warped_planks
    * oak_sapling
    * spruce_sapling
    * birch_sapling
    * jungle_sapling
    * acacia_sapling
    * dark_oak_sapling
    * bedrock
    * sand
    * red_sand
    * gravel
    * gold_ore
    * iron_ore
    * coal_ore
    * nether_gold_ore
    * oak_log
    * spruce_log
    * birch_log
    * jungle_log
    * acacia_log
    * dark_oak_log
    * crimson_stem
    * warped_stem
    * stripped_oak_log
    * stripped_spruce_log
    * stripped_birch_log
    * stripped_jungle_log
    * stripped_acacia_log
    * stripped_dark_oak_log
    * stripped_crimson_stem
    * stripped_warped_stem
    * stripped_oak_wood
    * stripped_spruce_wood
    * stripped_birch_wood
    * stripped_jungle_wood
    * stripped_acacia_wood
    * stripped_dark_oak_wood
    * stripped_crimson_hyphae
    * stripped_warped_hyphae
    * oak_wood
    * spruce_wood
    * birch_wood
    * jungle_wood
    * acacia_wood
    * dark_oak_wood
    * crimson_hyphae
    * warped_hyphae
    * oak_leaves
    * spruce_leaves
    * birch_leaves
    * jungle_leaves
    * acacia_leaves
    * dark_oak_leaves
    * sponge
    * wet_sponge
    * glass
    * lapis_ore
    * lapis_block
    * dispenser
    * sandstone
    * chiseled_sandstone
    * cut_sandstone
    * note_block
    * powered_rail
    * detector_rail
    * sticky_piston
    * cobweb
    * grass
    * fern
    * dead_bush
    * seagrass
    * sea_pickle
    * piston
    * white_wool
    * orange_wool
    * magenta_wool
    * light_blue_wool
    * yellow_wool
    * lime_wool
    * pink_wool
    * gray_wool
    * light_gray_wool
    * cyan_wool
    * purple_wool
    * blue_wool
    * brown_wool
    * green_wool
    * red_wool
    * black_wool
    * dandelion
    * poppy
    * blue_orchid
    * allium
    * azure_bluet
    * red_tulip
    * orange_tulip
    * white_tulip
    * pink_tulip
    * oxeye_daisy
    * cornflower
    * lily_of_the_valley
    * wither_rose
    * brown_mushroom
    * red_mushroom
    * crimson_fungus
    * warped_fungus
    * crimson_roots
    * warped_roots
    * nether_sprouts
    * weeping_vines
    * twisting_vines
    * sugar_cane
    * kelp
    * bamboo
    * gold_block
    * iron_block
    * oak_slab
    * spruce_slab
    * birch_slab
    * jungle_slab
    * acacia_slab
    * dark_oak_slab
    * crimson_slab
    * warped_slab
    * stone_slab
    * smooth_stone_slab
    * sandstone_slab
    * cut_sandstone_slab
    * petrified_oak_slab
    * cobblestone_slab
    * brick_slab
    * stone_brick_slab
    * nether_brick_slab
    * quartz_slab
    * red_sandstone_slab
    * cut_red_sandstone_slab
    * purpur_slab
    * prismarine_slab
    * prismarine_brick_slab
    * dark_prismarine_slab
    * smooth_quartz
    * smooth_red_sandstone
    * smooth_sandstone
    * smooth_stone
    * bricks
    * tnt
    * bookshelf
    * mossy_cobblestone
    * obsidian
    * torch
    * end_rod
    * chorus_plant
    * chorus_flower
    * purpur_block
    * purpur_pillar
    * purpur_stairs
    * spawner
    * oak_stairs
    * chest
    * diamond_ore
    * diamond_block
    * crafting_table
    * farmland
    * furnace
    * ladder
    * rail
    * cobblestone_stairs
    * lever
    * stone_pressure_plate
    * oak_pressure_plate
    * spruce_pressure_plate
    * birch_pressure_plate
    * jungle_pressure_plate
    * acacia_pressure_plate
    * dark_oak_pressure_plate
    * crimson_pressure_plate
    * warped_pressure_plate
    * polished_blackstone_pressure_plate
    * redstone_ore
    * redstone_torch
    * snow
    * ice
    * snow_block
    * cactus
    * clay
    * jukebox
    * oak_fence
    * spruce_fence
    * birch_fence
    * jungle_fence
    * acacia_fence
    * dark_oak_fence
    * crimson_fence
    * warped_fence
    * pumpkin
    * carved_pumpkin
    * netherrack
    * soul_sand
    * soul_soil
    * basalt
    * polished_basalt
    * soul_torch
    * glowstone
    * jack_o_lantern
    * oak_trapdoor
    * spruce_trapdoor
    * birch_trapdoor
    * jungle_trapdoor
    * acacia_trapdoor
    * dark_oak_trapdoor
    * crimson_trapdoor
    * warped_trapdoor
    * infested_stone
    * infested_cobblestone
    * infested_stone_bricks
    * infested_mossy_stone_bricks
    * infested_cracked_stone_bricks
    * infested_chiseled_stone_bricks
    * stone_bricks
    * mossy_stone_bricks
    * cracked_stone_bricks
    * chiseled_stone_bricks
    * brown_mushroom_block
    * red_mushroom_block
    * mushroom_stem
    * iron_bars
    * chain
    * glass_pane
    * melon
    * vine
    * oak_fence_gate
    * spruce_fence_gate
    * birch_fence_gate
    * jungle_fence_gate
    * acacia_fence_gate
    * dark_oak_fence_gate
    * crimson_fence_gate
    * warped_fence_gate
    * brick_stairs
    * stone_brick_stairs
    * mycelium
    * lily_pad
    * nether_bricks
    * cracked_nether_bricks
    * chiseled_nether_bricks
    * nether_brick_fence
    * nether_brick_stairs
    * enchanting_table
    * end_portal_frame
    * end_stone
    * end_stone_bricks
    * dragon_egg
    * redstone_lamp
    * sandstone_stairs
    * emerald_ore
    * ender_chest
    * tripwire_hook
    * emerald_block
    * spruce_stairs
    * birch_stairs
    * jungle_stairs
    * crimson_stairs
    * warped_stairs
    * command_block
    * beacon
    * cobblestone_wall
    * mossy_cobblestone_wall
    * brick_wall
    * prismarine_wall
    * red_sandstone_wall
    * mossy_stone_brick_wall
    * granite_wall
    * stone_brick_wall
    * nether_brick_wall
    * andesite_wall
    * red_nether_brick_wall
    * sandstone_wall
    * end_stone_brick_wall
    * diorite_wall
    * blackstone_wall
    * polished_blackstone_wall
    * polished_blackstone_brick_wall
    * stone_button
    * oak_button
    * spruce_button
    * birch_button
    * jungle_button
    * acacia_button
    * dark_oak_button
    * crimson_button
    * warped_button
    * polished_blackstone_button
    * anvil
    * chipped_anvil
    * damaged_anvil
    * trapped_chest
    * light_weighted_pressure_plate
    * heavy_weighted_pressure_plate
    * daylight_detector
    * redstone_block
    * nether_quartz_ore
    * hopper
    * chiseled_quartz_block
    * quartz_block
    * quartz_bricks
    * quartz_pillar
    * quartz_stairs
    * activator_rail
    * dropper
    * white_terracotta
    * orange_terracotta
    * magenta_terracotta
    * light_blue_terracotta
    * yellow_terracotta
    * lime_terracotta
    * pink_terracotta
    * gray_terracotta
    * light_gray_terracotta
    * cyan_terracotta
    * purple_terracotta
    * blue_terracotta
    * brown_terracotta
    * green_terracotta
    * red_terracotta
    * black_terracotta
    * barrier
    * iron_trapdoor
    * hay_block
    * white_carpet
    * orange_carpet
    * magenta_carpet
    * light_blue_carpet
    * yellow_carpet
    * lime_carpet
    * pink_carpet
    * gray_carpet
    * light_gray_carpet
    * cyan_carpet
    * purple_carpet
    * blue_carpet
    * brown_carpet
    * green_carpet
    * red_carpet
    * black_carpet
    * terracotta
    * coal_block
    * packed_ice
    * acacia_stairs
    * dark_oak_stairs
    * slime_block
    * grass_path
    * sunflower
    * lilac
    * rose_bush
    * peony
    * tall_grass
    * large_fern
    * white_stained_glass
    * orange_stained_glass
    * magenta_stained_glass
    * light_blue_stained_glass
    * yellow_stained_glass
    * lime_stained_glass
    * pink_stained_glass
    * gray_stained_glass
    * light_gray_stained_glass
    * cyan_stained_glass
    * purple_stained_glass
    * blue_stained_glass
    * brown_stained_glass
    * green_stained_glass
    * red_stained_glass
    * black_stained_glass
    * white_stained_glass_pane
    * orange_stained_glass_pane
    * magenta_stained_glass_pane
    * light_blue_stained_glass_pane
    * yellow_stained_glass_pane
    * lime_stained_glass_pane
    * pink_stained_glass_pane
    * gray_stained_glass_pane
    * light_gray_stained_glass_pane
    * cyan_stained_glass_pane
    * purple_stained_glass_pane
    * blue_stained_glass_pane
    * brown_stained_glass_pane
    * green_stained_glass_pane
    * red_stained_glass_pane
    * black_stained_glass_pane
    * prismarine
    * prismarine_bricks
    * dark_prismarine
    * prismarine_stairs
    * prismarine_brick_stairs
    * dark_prismarine_stairs
    * sea_lantern
    * red_sandstone
    * chiseled_red_sandstone
    * cut_red_sandstone
    * red_sandstone_stairs
    * repeating_command_block
    * chain_command_block
    * magma_block
    * nether_wart_block
    * warped_wart_block
    * red_nether_bricks
    * bone_block
    * structure_void
    * observer
    * shulker_box
    * white_shulker_box
    * orange_shulker_box
    * magenta_shulker_box
    * light_blue_shulker_box
    * yellow_shulker_box
    * lime_shulker_box
    * pink_shulker_box
    * gray_shulker_box
    * light_gray_shulker_box
    * cyan_shulker_box
    * purple_shulker_box
    * blue_shulker_box
    * brown_shulker_box
    * green_shulker_box
    * red_shulker_box
    * black_shulker_box
    * white_glazed_terracotta
    * orange_glazed_terracotta
    * magenta_glazed_terracotta
    * light_blue_glazed_terracotta
    * yellow_glazed_terracotta
    * lime_glazed_terracotta
    * pink_glazed_terracotta
    * gray_glazed_terracotta
    * light_gray_glazed_terracotta
    * cyan_glazed_terracotta
    * purple_glazed_terracotta
    * blue_glazed_terracotta
    * brown_glazed_terracotta
    * green_glazed_terracotta
    * red_glazed_terracotta
    * black_glazed_terracotta
    * white_concrete
    * orange_concrete
    * magenta_concrete
    * light_blue_concrete
    * yellow_concrete
    * lime_concrete
    * pink_concrete
    * gray_concrete
    * light_gray_concrete
    * cyan_concrete
    * purple_concrete
    * blue_concrete
    * brown_concrete
    * green_concrete
    * red_concrete
    * black_concrete
    * white_concrete_powder
    * orange_concrete_powder
    * magenta_concrete_powder
    * light_blue_concrete_powder
    * yellow_concrete_powder
    * lime_concrete_powder
    * pink_concrete_powder
    * gray_concrete_powder
    * light_gray_concrete_powder
    * cyan_concrete_powder
    * purple_concrete_powder
    * blue_concrete_powder
    * brown_concrete_powder
    * green_concrete_powder
    * red_concrete_powder
    * black_concrete_powder
    * turtle_egg
    * dead_tube_coral_block
    * dead_brain_coral_block
    * dead_bubble_coral_block
    * dead_fire_coral_block
    * dead_horn_coral_block
    * tube_coral_block
    * brain_coral_block
    * bubble_coral_block
    * fire_coral_block
    * horn_coral_block
    * tube_coral
    * brain_coral
    * bubble_coral
    * fire_coral
    * horn_coral
    * dead_brain_coral
    * dead_bubble_coral
    * dead_fire_coral
    * dead_horn_coral
    * dead_tube_coral
    * tube_coral_fan
    * brain_coral_fan
    * bubble_coral_fan
    * fire_coral_fan
    * horn_coral_fan
    * dead_tube_coral_fan
    * dead_brain_coral_fan
    * dead_bubble_coral_fan
    * dead_fire_coral_fan
    * dead_horn_coral_fan
    * blue_ice
    * conduit
    * polished_granite_stairs
    * smooth_red_sandstone_stairs
    * mossy_stone_brick_stairs
    * polished_diorite_stairs
    * mossy_cobblestone_stairs
    * end_stone_brick_stairs
    * stone_stairs
    * smooth_sandstone_stairs
    * smooth_quartz_stairs
    * granite_stairs
    * andesite_stairs
    * red_nether_brick_stairs
    * polished_andesite_stairs
    * diorite_stairs
    * polished_granite_slab
    * smooth_red_sandstone_slab
    * mossy_stone_brick_slab
    * polished_diorite_slab
    * mossy_cobblestone_slab
    * end_stone_brick_slab
    * smooth_sandstone_slab
    * smooth_quartz_slab
    * granite_slab
    * andesite_slab
    * red_nether_brick_slab
    * polished_andesite_slab
    * diorite_slab
    * scaffolding
    * iron_door
    * oak_door
    * spruce_door
    * birch_door
    * jungle_door
    * acacia_door
    * dark_oak_door
    * crimson_door
    * warped_door
    * repeater
    * comparator
    * structure_block
    * jigsaw
    * turtle_helmet
    * scute
    * flint_and_steel
    * apple
    * bow
    * arrow
    * coal
    * charcoal
    * diamond
    * iron_ingot
    * gold_ingot
    * netherite_ingot
    * netherite_scrap
    * wooden_sword
    * wooden_shovel
    * wooden_pickaxe
    * wooden_axe
    * wooden_hoe
    * stone_sword
    * stone_shovel
    * stone_pickaxe
    * stone_axe
    * stone_hoe
    * golden_sword
    * golden_shovel
    * golden_pickaxe
    * golden_axe
    * golden_hoe
    * iron_sword
    * iron_shovel
    * iron_pickaxe
    * iron_axe
    * iron_hoe
    * diamond_sword
    * diamond_shovel
    * diamond_pickaxe
    * diamond_axe
    * diamond_hoe
    * netherite_sword
    * netherite_shovel
    * netherite_pickaxe
    * netherite_axe
    * netherite_hoe
    * stick
    * bowl
    * mushroom_stew
    * string
    * feather
    * gunpowder
    * wheat_seeds
    * wheat
    * bread
    * leather_helmet
    * leather_chestplate
    * leather_leggings
    * leather_boots
    * chainmail_helmet
    * chainmail_chestplate
    * chainmail_leggings
    * chainmail_boots
    * iron_helmet
    * iron_chestplate
    * iron_leggings
    * iron_boots
    * diamond_helmet
    * diamond_chestplate
    * diamond_leggings
    * diamond_boots
    * golden_helmet
    * golden_chestplate
    * golden_leggings
    * golden_boots
    * netherite_helmet
    * netherite_chestplate
    * netherite_leggings
    * netherite_boots
    * flint
    * porkchop
    * cooked_porkchop
    * painting
    * golden_apple
    * enchanted_golden_apple
    * oak_sign
    * spruce_sign
    * birch_sign
    * jungle_sign
    * acacia_sign
    * dark_oak_sign
    * crimson_sign
    * warped_sign
    * bucket
    * water_bucket
    * lava_bucket
    * minecart
    * saddle
    * redstone
    * snowball
    * oak_boat
    * leather
    * milk_bucket
    * pufferfish_bucket
    * salmon_bucket
    * cod_bucket
    * tropical_fish_bucket
    * brick
    * clay_ball
    * dried_kelp_block
    * paper
    * book
    * slime_ball
    * chest_minecart
    * furnace_minecart
    * egg
    * compass
    * fishing_rod
    * clock
    * glowstone_dust
    * cod
    * salmon
    * tropical_fish
    * pufferfish
    * cooked_cod
    * cooked_salmon
    * ink_sac
    * cocoa_beans
    * lapis_lazuli
    * white_dye
    * orange_dye
    * magenta_dye
    * light_blue_dye
    * yellow_dye
    * lime_dye
    * pink_dye
    * gray_dye
    * light_gray_dye
    * cyan_dye
    * purple_dye
    * blue_dye
    * brown_dye
    * green_dye
    * red_dye
    * black_dye
    * bone_meal
    * bone
    * sugar
    * cake
    * white_bed
    * orange_bed
    * magenta_bed
    * light_blue_bed
    * yellow_bed
    * lime_bed
    * pink_bed
    * gray_bed
    * light_gray_bed
    * cyan_bed
    * purple_bed
    * blue_bed
    * brown_bed
    * green_bed
    * red_bed
    * black_bed
    * cookie
    * filled_map
    * shears
    * melon_slice
    * dried_kelp
    * pumpkin_seeds
    * melon_seeds
    * beef
    * cooked_beef
    * chicken
    * cooked_chicken
    * rotten_flesh
    * ender_pearl
    * blaze_rod
    * ghast_tear
    * gold_nugget
    * nether_wart
    * potion
    * glass_bottle
    * spider_eye
    * fermented_spider_eye
    * blaze_powder
    * magma_cream
    * brewing_stand
    * cauldron
    * ender_eye
    * glistering_melon_slice
    * bat_spawn_egg
    * bee_spawn_egg
    * blaze_spawn_egg
    * cat_spawn_egg
    * cave_spider_spawn_egg
    * chicken_spawn_egg
    * cod_spawn_egg
    * cow_spawn_egg
    * creeper_spawn_egg
    * dolphin_spawn_egg
    * donkey_spawn_egg
    * drowned_spawn_egg
    * elder_guardian_spawn_egg
    * enderman_spawn_egg
    * endermite_spawn_egg
    * evoker_spawn_egg
    * fox_spawn_egg
    * ghast_spawn_egg
    * guardian_spawn_egg
    * hoglin_spawn_egg
    * horse_spawn_egg
    * husk_spawn_egg
    * llama_spawn_egg
    * magma_cube_spawn_egg
    * mooshroom_spawn_egg
    * mule_spawn_egg
    * ocelot_spawn_egg
    * panda_spawn_egg
    * parrot_spawn_egg
    * phantom_spawn_egg
    * pig_spawn_egg
    * piglin_spawn_egg
    * piglin_brute_spawn_egg
    * pillager_spawn_egg
    * polar_bear_spawn_egg
    * pufferfish_spawn_egg
    * rabbit_spawn_egg
    * ravager_spawn_egg
    * salmon_spawn_egg
    * sheep_spawn_egg
    * shulker_spawn_egg
    * silverfish_spawn_egg
    * skeleton_spawn_egg
    * skeleton_horse_spawn_egg
    * slime_spawn_egg
    * spider_spawn_egg
    * squid_spawn_egg
    * stray_spawn_egg
    * strider_spawn_egg
    * trader_llama_spawn_egg
    * tropical_fish_spawn_egg
    * turtle_spawn_egg
    * vex_spawn_egg
    * villager_spawn_egg
    * vindicator_spawn_egg
    * wandering_trader_spawn_egg
    * witch_spawn_egg
    * wither_skeleton_spawn_egg
    * wolf_spawn_egg
    * zoglin_spawn_egg
    * zombie_spawn_egg
    * zombie_horse_spawn_egg
    * zombie_villager_spawn_egg
    * zombified_piglin_spawn_egg
    * experience_bottle
    * fire_charge
    * writable_book
    * written_book
    * emerald
    * item_frame
    * flower_pot
    * carrot
    * potato
    * baked_potato
    * poisonous_potato
    * map
    * golden_carrot
    * skeleton_skull
    * wither_skeleton_skull
    * player_head
    * zombie_head
    * creeper_head
    * dragon_head
    * carrot_on_a_stick
    * warped_fungus_on_a_stick
    * nether_star
    * pumpkin_pie
    * firework_rocket
    * firework_star
    * enchanted_book
    * nether_brick
    * quartz
    * tnt_minecart
    * hopper_minecart
    * prismarine_shard
    * prismarine_crystals
    * rabbit
    * cooked_rabbit
    * rabbit_stew
    * rabbit_foot
    * rabbit_hide
    * armor_stand
    * iron_horse_armor
    * golden_horse_armor
    * diamond_horse_armor
    * leather_horse_armor
    * lead
    * name_tag
    * command_block_minecart
    * mutton
    * cooked_mutton
    * white_banner
    * orange_banner
    * magenta_banner
    * light_blue_banner
    * yellow_banner
    * lime_banner
    * pink_banner
    * gray_banner
    * light_gray_banner
    * cyan_banner
    * purple_banner
    * blue_banner
    * brown_banner
    * green_banner
    * red_banner
    * black_banner
    * end_crystal
    * chorus_fruit
    * popped_chorus_fruit
    * beetroot
    * beetroot_seeds
    * beetroot_soup
    * dragon_breath
    * splash_potion
    * spectral_arrow
    * tipped_arrow
    * lingering_potion
    * shield
    * elytra
    * spruce_boat
    * birch_boat
    * jungle_boat
    * acacia_boat
    * dark_oak_boat
    * totem_of_undying
    * shulker_shell
    * iron_nugget
    * knowledge_book
    * debug_stick
    * music_disc_13
    * music_disc_cat
    * music_disc_blocks
    * music_disc_chirp
    * music_disc_far
    * music_disc_mall
    * music_disc_mellohi
    * music_disc_stal
    * music_disc_strad
    * music_disc_ward
    * music_disc_11
    * music_disc_wait
    * music_disc_pigstep
    * trident
    * phantom_membrane
    * nautilus_shell
    * heart_of_the_sea
    * crossbow
    * suspicious_stew
    * loom
    * flower_banner_pattern
    * creeper_banner_pattern
    * skull_banner_pattern
    * mojang_banner_pattern
    * globe_banner_pattern
    * piglin_banner_pattern
    * composter
    * barrel
    * smoker
    * blast_furnace
    * cartography_table
    * fletching_table
    * grindstone
    * lectern
    * smithing_table
    * stonecutter
    * bell
    * lantern
    * soul_lantern
    * sweet_berries
    * campfire
    * soul_campfire
    * shroomlight
    * honeycomb
    * bee_nest
    * beehive
    * honey_bottle
    * honey_block
    * honeycomb_block
    * lodestone
    * netherite_block
    * ancient_debris
    * target
    * crying_obsidian
    * blackstone
    * blackstone_slab
    * blackstone_stairs
    * gilded_blackstone
    * polished_blackstone
    * polished_blackstone_slab
    * polished_blackstone_stairs
    * chiseled_polished_blackstone
    * polished_blackstone_bricks
    * polished_blackstone_brick_slab
    * polished_blackstone_brick_stairs
    * cracked_polished_blackstone_bricks
    * respawn_anchor
    """
    air = "minecraft:air"
    stone = "minecraft:stone"
    granite = "minecraft:granite"
    polished_granite = "minecraft:polished_granite"
    diorite = "minecraft:diorite"
    polished_diorite = "minecraft:polished_diorite"
    andesite = "minecraft:andesite"
    polished_andesite = "minecraft:polished_andesite"
    grass_block = "minecraft:grass_block"
    dirt = "minecraft:dirt"
    coarse_dirt = "minecraft:coarse_dirt"
    podzol = "minecraft:podzol"
    crimson_nylium = "minecraft:crimson_nylium"
    warped_nylium = "minecraft:warped_nylium"
    cobblestone = "minecraft:cobblestone"
    oak_planks = "minecraft:oak_planks"
    spruce_planks = "minecraft:spruce_planks"
    birch_planks = "minecraft:birch_planks"
    jungle_planks = "minecraft:jungle_planks"
    acacia_planks = "minecraft:acacia_planks"
    dark_oak_planks = "minecraft:dark_oak_planks"
    crimson_planks = "minecraft:crimson_planks"
    warped_planks = "minecraft:warped_planks"
    oak_sapling = "minecraft:oak_sapling"
    spruce_sapling = "minecraft:spruce_sapling"
    birch_sapling = "minecraft:birch_sapling"
    jungle_sapling = "minecraft:jungle_sapling"
    acacia_sapling = "minecraft:acacia_sapling"
    dark_oak_sapling = "minecraft:dark_oak_sapling"
    bedrock = "minecraft:bedrock"
    sand = "minecraft:sand"
    red_sand = "minecraft:red_sand"
    gravel = "minecraft:gravel"
    gold_ore = "minecraft:gold_ore"
    iron_ore = "minecraft:iron_ore"
    coal_ore = "minecraft:coal_ore"
    nether_gold_ore = "minecraft:nether_gold_ore"
    oak_log = "minecraft:oak_log"
    spruce_log = "minecraft:spruce_log"
    birch_log = "minecraft:birch_log"
    jungle_log = "minecraft:jungle_log"
    acacia_log = "minecraft:acacia_log"
    dark_oak_log = "minecraft:dark_oak_log"
    crimson_stem = "minecraft:crimson_stem"
    warped_stem = "minecraft:warped_stem"
    stripped_oak_log = "minecraft:stripped_oak_log"
    stripped_spruce_log = "minecraft:stripped_spruce_log"
    stripped_birch_log = "minecraft:stripped_birch_log"
    stripped_jungle_log = "minecraft:stripped_jungle_log"
    stripped_acacia_log = "minecraft:stripped_acacia_log"
    stripped_dark_oak_log = "minecraft:stripped_dark_oak_log"
    stripped_crimson_stem = "minecraft:stripped_crimson_stem"
    stripped_warped_stem = "minecraft:stripped_warped_stem"
    stripped_oak_wood = "minecraft:stripped_oak_wood"
    stripped_spruce_wood = "minecraft:stripped_spruce_wood"
    stripped_birch_wood = "minecraft:stripped_birch_wood"
    stripped_jungle_wood = "minecraft:stripped_jungle_wood"
    stripped_acacia_wood = "minecraft:stripped_acacia_wood"
    stripped_dark_oak_wood = "minecraft:stripped_dark_oak_wood"
    stripped_crimson_hyphae = "minecraft:stripped_crimson_hyphae"
    stripped_warped_hyphae = "minecraft:stripped_warped_hyphae"
    oak_wood = "minecraft:oak_wood"
    spruce_wood = "minecraft:spruce_wood"
    birch_wood = "minecraft:birch_wood"
    jungle_wood = "minecraft:jungle_wood"
    acacia_wood = "minecraft:acacia_wood"
    dark_oak_wood = "minecraft:dark_oak_wood"
    crimson_hyphae = "minecraft:crimson_hyphae"
    warped_hyphae = "minecraft:warped_hyphae"
    oak_leaves = "minecraft:oak_leaves"
    spruce_leaves = "minecraft:spruce_leaves"
    birch_leaves = "minecraft:birch_leaves"
    jungle_leaves = "minecraft:jungle_leaves"
    acacia_leaves = "minecraft:acacia_leaves"
    dark_oak_leaves = "minecraft:dark_oak_leaves"
    sponge = "minecraft:sponge"
    wet_sponge = "minecraft:wet_sponge"
    glass = "minecraft:glass"
    lapis_ore = "minecraft:lapis_ore"
    lapis_block = "minecraft:lapis_block"
    dispenser = "minecraft:dispenser"
    sandstone = "minecraft:sandstone"
    chiseled_sandstone = "minecraft:chiseled_sandstone"
    cut_sandstone = "minecraft:cut_sandstone"
    note_block = "minecraft:note_block"
    powered_rail = "minecraft:powered_rail"
    detector_rail = "minecraft:detector_rail"
    sticky_piston = "minecraft:sticky_piston"
    cobweb = "minecraft:cobweb"
    grass = "minecraft:grass"
    fern = "minecraft:fern"
    dead_bush = "minecraft:dead_bush"
    seagrass = "minecraft:seagrass"
    sea_pickle = "minecraft:sea_pickle"
    piston = "minecraft:piston"
    white_wool = "minecraft:white_wool"
    orange_wool = "minecraft:orange_wool"
    magenta_wool = "minecraft:magenta_wool"
    light_blue_wool = "minecraft:light_blue_wool"
    yellow_wool = "minecraft:yellow_wool"
    lime_wool = "minecraft:lime_wool"
    pink_wool = "minecraft:pink_wool"
    gray_wool = "minecraft:gray_wool"
    light_gray_wool = "minecraft:light_gray_wool"
    cyan_wool = "minecraft:cyan_wool"
    purple_wool = "minecraft:purple_wool"
    blue_wool = "minecraft:blue_wool"
    brown_wool = "minecraft:brown_wool"
    green_wool = "minecraft:green_wool"
    red_wool = "minecraft:red_wool"
    black_wool = "minecraft:black_wool"
    dandelion = "minecraft:dandelion"
    poppy = "minecraft:poppy"
    blue_orchid = "minecraft:blue_orchid"
    allium = "minecraft:allium"
    azure_bluet = "minecraft:azure_bluet"
    red_tulip = "minecraft:red_tulip"
    orange_tulip = "minecraft:orange_tulip"
    white_tulip = "minecraft:white_tulip"
    pink_tulip = "minecraft:pink_tulip"
    oxeye_daisy = "minecraft:oxeye_daisy"
    cornflower = "minecraft:cornflower"
    lily_of_the_valley = "minecraft:lily_of_the_valley"
    wither_rose = "minecraft:wither_rose"
    brown_mushroom = "minecraft:brown_mushroom"
    red_mushroom = "minecraft:red_mushroom"
    crimson_fungus = "minecraft:crimson_fungus"
    warped_fungus = "minecraft:warped_fungus"
    crimson_roots = "minecraft:crimson_roots"
    warped_roots = "minecraft:warped_roots"
    nether_sprouts = "minecraft:nether_sprouts"
    weeping_vines = "minecraft:weeping_vines"
    twisting_vines = "minecraft:twisting_vines"
    sugar_cane = "minecraft:sugar_cane"
    kelp = "minecraft:kelp"
    bamboo = "minecraft:bamboo"
    gold_block = "minecraft:gold_block"
    iron_block = "minecraft:iron_block"
    oak_slab = "minecraft:oak_slab"
    spruce_slab = "minecraft:spruce_slab"
    birch_slab = "minecraft:birch_slab"
    jungle_slab = "minecraft:jungle_slab"
    acacia_slab = "minecraft:acacia_slab"
    dark_oak_slab = "minecraft:dark_oak_slab"
    crimson_slab = "minecraft:crimson_slab"
    warped_slab = "minecraft:warped_slab"
    stone_slab = "minecraft:stone_slab"
    smooth_stone_slab = "minecraft:smooth_stone_slab"
    sandstone_slab = "minecraft:sandstone_slab"
    cut_sandstone_slab = "minecraft:cut_sandstone_slab"
    petrified_oak_slab = "minecraft:petrified_oak_slab"
    cobblestone_slab = "minecraft:cobblestone_slab"
    brick_slab = "minecraft:brick_slab"
    stone_brick_slab = "minecraft:stone_brick_slab"
    nether_brick_slab = "minecraft:nether_brick_slab"
    quartz_slab = "minecraft:quartz_slab"
    red_sandstone_slab = "minecraft:red_sandstone_slab"
    cut_red_sandstone_slab = "minecraft:cut_red_sandstone_slab"
    purpur_slab = "minecraft:purpur_slab"
    prismarine_slab = "minecraft:prismarine_slab"
    prismarine_brick_slab = "minecraft:prismarine_brick_slab"
    dark_prismarine_slab = "minecraft:dark_prismarine_slab"
    smooth_quartz = "minecraft:smooth_quartz"
    smooth_red_sandstone = "minecraft:smooth_red_sandstone"
    smooth_sandstone = "minecraft:smooth_sandstone"
    smooth_stone = "minecraft:smooth_stone"
    bricks = "minecraft:bricks"
    tnt = "minecraft:tnt"
    bookshelf = "minecraft:bookshelf"
    mossy_cobblestone = "minecraft:mossy_cobblestone"
    obsidian = "minecraft:obsidian"
    torch = "minecraft:torch"
    end_rod = "minecraft:end_rod"
    chorus_plant = "minecraft:chorus_plant"
    chorus_flower = "minecraft:chorus_flower"
    purpur_block = "minecraft:purpur_block"
    purpur_pillar = "minecraft:purpur_pillar"
    purpur_stairs = "minecraft:purpur_stairs"
    spawner = "minecraft:spawner"
    oak_stairs = "minecraft:oak_stairs"
    chest = "minecraft:chest"
    diamond_ore = "minecraft:diamond_ore"
    diamond_block = "minecraft:diamond_block"
    crafting_table = "minecraft:crafting_table"
    farmland = "minecraft:farmland"
    furnace = "minecraft:furnace"
    ladder = "minecraft:ladder"
    rail = "minecraft:rail"
    cobblestone_stairs = "minecraft:cobblestone_stairs"
    lever = "minecraft:lever"
    stone_pressure_plate = "minecraft:stone_pressure_plate"
    oak_pressure_plate = "minecraft:oak_pressure_plate"
    spruce_pressure_plate = "minecraft:spruce_pressure_plate"
    birch_pressure_plate = "minecraft:birch_pressure_plate"
    jungle_pressure_plate = "minecraft:jungle_pressure_plate"
    acacia_pressure_plate = "minecraft:acacia_pressure_plate"
    dark_oak_pressure_plate = "minecraft:dark_oak_pressure_plate"
    crimson_pressure_plate = "minecraft:crimson_pressure_plate"
    warped_pressure_plate = "minecraft:warped_pressure_plate"
    polished_blackstone_pressure_plate = "minecraft:polished_blackstone_pressure_plate"
    redstone_ore = "minecraft:redstone_ore"
    redstone_torch = "minecraft:redstone_torch"
    snow = "minecraft:snow"
    ice = "minecraft:ice"
    snow_block = "minecraft:snow_block"
    cactus = "minecraft:cactus"
    clay = "minecraft:clay"
    jukebox = "minecraft:jukebox"
    oak_fence = "minecraft:oak_fence"
    spruce_fence = "minecraft:spruce_fence"
    birch_fence = "minecraft:birch_fence"
    jungle_fence = "minecraft:jungle_fence"
    acacia_fence = "minecraft:acacia_fence"
    dark_oak_fence = "minecraft:dark_oak_fence"
    crimson_fence = "minecraft:crimson_fence"
    warped_fence = "minecraft:warped_fence"
    pumpkin = "minecraft:pumpkin"
    carved_pumpkin = "minecraft:carved_pumpkin"
    netherrack = "minecraft:netherrack"
    soul_sand = "minecraft:soul_sand"
    soul_soil = "minecraft:soul_soil"
    basalt = "minecraft:basalt"
    polished_basalt = "minecraft:polished_basalt"
    soul_torch = "minecraft:soul_torch"
    glowstone = "minecraft:glowstone"
    jack_o_lantern = "minecraft:jack_o_lantern"
    oak_trapdoor = "minecraft:oak_trapdoor"
    spruce_trapdoor = "minecraft:spruce_trapdoor"
    birch_trapdoor = "minecraft:birch_trapdoor"
    jungle_trapdoor = "minecraft:jungle_trapdoor"
    acacia_trapdoor = "minecraft:acacia_trapdoor"
    dark_oak_trapdoor = "minecraft:dark_oak_trapdoor"
    crimson_trapdoor = "minecraft:crimson_trapdoor"
    warped_trapdoor = "minecraft:warped_trapdoor"
    infested_stone = "minecraft:infested_stone"
    infested_cobblestone = "minecraft:infested_cobblestone"
    infested_stone_bricks = "minecraft:infested_stone_bricks"
    infested_mossy_stone_bricks = "minecraft:infested_mossy_stone_bricks"
    infested_cracked_stone_bricks = "minecraft:infested_cracked_stone_bricks"
    infested_chiseled_stone_bricks = "minecraft:infested_chiseled_stone_bricks"
    stone_bricks = "minecraft:stone_bricks"
    mossy_stone_bricks = "minecraft:mossy_stone_bricks"
    cracked_stone_bricks = "minecraft:cracked_stone_bricks"
    chiseled_stone_bricks = "minecraft:chiseled_stone_bricks"
    brown_mushroom_block = "minecraft:brown_mushroom_block"
    red_mushroom_block = "minecraft:red_mushroom_block"
    mushroom_stem = "minecraft:mushroom_stem"
    iron_bars = "minecraft:iron_bars"
    chain = "minecraft:chain"
    glass_pane = "minecraft:glass_pane"
    melon = "minecraft:melon"
    vine = "minecraft:vine"
    oak_fence_gate = "minecraft:oak_fence_gate"
    spruce_fence_gate = "minecraft:spruce_fence_gate"
    birch_fence_gate = "minecraft:birch_fence_gate"
    jungle_fence_gate = "minecraft:jungle_fence_gate"
    acacia_fence_gate = "minecraft:acacia_fence_gate"
    dark_oak_fence_gate = "minecraft:dark_oak_fence_gate"
    crimson_fence_gate = "minecraft:crimson_fence_gate"
    warped_fence_gate = "minecraft:warped_fence_gate"
    brick_stairs = "minecraft:brick_stairs"
    stone_brick_stairs = "minecraft:stone_brick_stairs"
    mycelium = "minecraft:mycelium"
    lily_pad = "minecraft:lily_pad"
    nether_bricks = "minecraft:nether_bricks"
    cracked_nether_bricks = "minecraft:cracked_nether_bricks"
    chiseled_nether_bricks = "minecraft:chiseled_nether_bricks"
    nether_brick_fence = "minecraft:nether_brick_fence"
    nether_brick_stairs = "minecraft:nether_brick_stairs"
    enchanting_table = "minecraft:enchanting_table"
    end_portal_frame = "minecraft:end_portal_frame"
    end_stone = "minecraft:end_stone"
    end_stone_bricks = "minecraft:end_stone_bricks"
    dragon_egg = "minecraft:dragon_egg"
    redstone_lamp = "minecraft:redstone_lamp"
    sandstone_stairs = "minecraft:sandstone_stairs"
    emerald_ore = "minecraft:emerald_ore"
    ender_chest = "minecraft:ender_chest"
    tripwire_hook = "minecraft:tripwire_hook"
    emerald_block = "minecraft:emerald_block"
    spruce_stairs = "minecraft:spruce_stairs"
    birch_stairs = "minecraft:birch_stairs"
    jungle_stairs = "minecraft:jungle_stairs"
    crimson_stairs = "minecraft:crimson_stairs"
    warped_stairs = "minecraft:warped_stairs"
    command_block = "minecraft:command_block"
    beacon = "minecraft:beacon"
    cobblestone_wall = "minecraft:cobblestone_wall"
    mossy_cobblestone_wall = "minecraft:mossy_cobblestone_wall"
    brick_wall = "minecraft:brick_wall"
    prismarine_wall = "minecraft:prismarine_wall"
    red_sandstone_wall = "minecraft:red_sandstone_wall"
    mossy_stone_brick_wall = "minecraft:mossy_stone_brick_wall"
    granite_wall = "minecraft:granite_wall"
    stone_brick_wall = "minecraft:stone_brick_wall"
    nether_brick_wall = "minecraft:nether_brick_wall"
    andesite_wall = "minecraft:andesite_wall"
    red_nether_brick_wall = "minecraft:red_nether_brick_wall"
    sandstone_wall = "minecraft:sandstone_wall"
    end_stone_brick_wall = "minecraft:end_stone_brick_wall"
    diorite_wall = "minecraft:diorite_wall"
    blackstone_wall = "minecraft:blackstone_wall"
    polished_blackstone_wall = "minecraft:polished_blackstone_wall"
    polished_blackstone_brick_wall = "minecraft:polished_blackstone_brick_wall"
    stone_button = "minecraft:stone_button"
    oak_button = "minecraft:oak_button"
    spruce_button = "minecraft:spruce_button"
    birch_button = "minecraft:birch_button"
    jungle_button = "minecraft:jungle_button"
    acacia_button = "minecraft:acacia_button"
    dark_oak_button = "minecraft:dark_oak_button"
    crimson_button = "minecraft:crimson_button"
    warped_button = "minecraft:warped_button"
    polished_blackstone_button = "minecraft:polished_blackstone_button"
    anvil = "minecraft:anvil"
    chipped_anvil = "minecraft:chipped_anvil"
    damaged_anvil = "minecraft:damaged_anvil"
    trapped_chest = "minecraft:trapped_chest"
    light_weighted_pressure_plate = "minecraft:light_weighted_pressure_plate"
    heavy_weighted_pressure_plate = "minecraft:heavy_weighted_pressure_plate"
    daylight_detector = "minecraft:daylight_detector"
    redstone_block = "minecraft:redstone_block"
    nether_quartz_ore = "minecraft:nether_quartz_ore"
    hopper = "minecraft:hopper"
    chiseled_quartz_block = "minecraft:chiseled_quartz_block"
    quartz_block = "minecraft:quartz_block"
    quartz_bricks = "minecraft:quartz_bricks"
    quartz_pillar = "minecraft:quartz_pillar"
    quartz_stairs = "minecraft:quartz_stairs"
    activator_rail = "minecraft:activator_rail"
    dropper = "minecraft:dropper"
    white_terracotta = "minecraft:white_terracotta"
    orange_terracotta = "minecraft:orange_terracotta"
    magenta_terracotta = "minecraft:magenta_terracotta"
    light_blue_terracotta = "minecraft:light_blue_terracotta"
    yellow_terracotta = "minecraft:yellow_terracotta"
    lime_terracotta = "minecraft:lime_terracotta"
    pink_terracotta = "minecraft:pink_terracotta"
    gray_terracotta = "minecraft:gray_terracotta"
    light_gray_terracotta = "minecraft:light_gray_terracotta"
    cyan_terracotta = "minecraft:cyan_terracotta"
    purple_terracotta = "minecraft:purple_terracotta"
    blue_terracotta = "minecraft:blue_terracotta"
    brown_terracotta = "minecraft:brown_terracotta"
    green_terracotta = "minecraft:green_terracotta"
    red_terracotta = "minecraft:red_terracotta"
    black_terracotta = "minecraft:black_terracotta"
    barrier = "minecraft:barrier"
    iron_trapdoor = "minecraft:iron_trapdoor"
    hay_block = "minecraft:hay_block"
    white_carpet = "minecraft:white_carpet"
    orange_carpet = "minecraft:orange_carpet"
    magenta_carpet = "minecraft:magenta_carpet"
    light_blue_carpet = "minecraft:light_blue_carpet"
    yellow_carpet = "minecraft:yellow_carpet"
    lime_carpet = "minecraft:lime_carpet"
    pink_carpet = "minecraft:pink_carpet"
    gray_carpet = "minecraft:gray_carpet"
    light_gray_carpet = "minecraft:light_gray_carpet"
    cyan_carpet = "minecraft:cyan_carpet"
    purple_carpet = "minecraft:purple_carpet"
    blue_carpet = "minecraft:blue_carpet"
    brown_carpet = "minecraft:brown_carpet"
    green_carpet = "minecraft:green_carpet"
    red_carpet = "minecraft:red_carpet"
    black_carpet = "minecraft:black_carpet"
    terracotta = "minecraft:terracotta"
    coal_block = "minecraft:coal_block"
    packed_ice = "minecraft:packed_ice"
    acacia_stairs = "minecraft:acacia_stairs"
    dark_oak_stairs = "minecraft:dark_oak_stairs"
    slime_block = "minecraft:slime_block"
    grass_path = "minecraft:grass_path"
    sunflower = "minecraft:sunflower"
    lilac = "minecraft:lilac"
    rose_bush = "minecraft:rose_bush"
    peony = "minecraft:peony"
    tall_grass = "minecraft:tall_grass"
    large_fern = "minecraft:large_fern"
    white_stained_glass = "minecraft:white_stained_glass"
    orange_stained_glass = "minecraft:orange_stained_glass"
    magenta_stained_glass = "minecraft:magenta_stained_glass"
    light_blue_stained_glass = "minecraft:light_blue_stained_glass"
    yellow_stained_glass = "minecraft:yellow_stained_glass"
    lime_stained_glass = "minecraft:lime_stained_glass"
    pink_stained_glass = "minecraft:pink_stained_glass"
    gray_stained_glass = "minecraft:gray_stained_glass"
    light_gray_stained_glass = "minecraft:light_gray_stained_glass"
    cyan_stained_glass = "minecraft:cyan_stained_glass"
    purple_stained_glass = "minecraft:purple_stained_glass"
    blue_stained_glass = "minecraft:blue_stained_glass"
    brown_stained_glass = "minecraft:brown_stained_glass"
    green_stained_glass = "minecraft:green_stained_glass"
    red_stained_glass = "minecraft:red_stained_glass"
    black_stained_glass = "minecraft:black_stained_glass"
    white_stained_glass_pane = "minecraft:white_stained_glass_pane"
    orange_stained_glass_pane = "minecraft:orange_stained_glass_pane"
    magenta_stained_glass_pane = "minecraft:magenta_stained_glass_pane"
    light_blue_stained_glass_pane = "minecraft:light_blue_stained_glass_pane"
    yellow_stained_glass_pane = "minecraft:yellow_stained_glass_pane"
    lime_stained_glass_pane = "minecraft:lime_stained_glass_pane"
    pink_stained_glass_pane = "minecraft:pink_stained_glass_pane"
    gray_stained_glass_pane = "minecraft:gray_stained_glass_pane"
    light_gray_stained_glass_pane = "minecraft:light_gray_stained_glass_pane"
    cyan_stained_glass_pane = "minecraft:cyan_stained_glass_pane"
    purple_stained_glass_pane = "minecraft:purple_stained_glass_pane"
    blue_stained_glass_pane = "minecraft:blue_stained_glass_pane"
    brown_stained_glass_pane = "minecraft:brown_stained_glass_pane"
    green_stained_glass_pane = "minecraft:green_stained_glass_pane"
    red_stained_glass_pane = "minecraft:red_stained_glass_pane"
    black_stained_glass_pane = "minecraft:black_stained_glass_pane"
    prismarine = "minecraft:prismarine"
    prismarine_bricks = "minecraft:prismarine_bricks"
    dark_prismarine = "minecraft:dark_prismarine"
    prismarine_stairs = "minecraft:prismarine_stairs"
    prismarine_brick_stairs = "minecraft:prismarine_brick_stairs"
    dark_prismarine_stairs = "minecraft:dark_prismarine_stairs"
    sea_lantern = "minecraft:sea_lantern"
    red_sandstone = "minecraft:red_sandstone"
    chiseled_red_sandstone = "minecraft:chiseled_red_sandstone"
    cut_red_sandstone = "minecraft:cut_red_sandstone"
    red_sandstone_stairs = "minecraft:red_sandstone_stairs"
    repeating_command_block = "minecraft:repeating_command_block"
    chain_command_block = "minecraft:chain_command_block"
    magma_block = "minecraft:magma_block"
    nether_wart_block = "minecraft:nether_wart_block"
    warped_wart_block = "minecraft:warped_wart_block"
    red_nether_bricks = "minecraft:red_nether_bricks"
    bone_block = "minecraft:bone_block"
    structure_void = "minecraft:structure_void"
    observer = "minecraft:observer"
    shulker_box = "minecraft:shulker_box"
    white_shulker_box = "minecraft:white_shulker_box"
    orange_shulker_box = "minecraft:orange_shulker_box"
    magenta_shulker_box = "minecraft:magenta_shulker_box"
    light_blue_shulker_box = "minecraft:light_blue_shulker_box"
    yellow_shulker_box = "minecraft:yellow_shulker_box"
    lime_shulker_box = "minecraft:lime_shulker_box"
    pink_shulker_box = "minecraft:pink_shulker_box"
    gray_shulker_box = "minecraft:gray_shulker_box"
    light_gray_shulker_box = "minecraft:light_gray_shulker_box"
    cyan_shulker_box = "minecraft:cyan_shulker_box"
    purple_shulker_box = "minecraft:purple_shulker_box"
    blue_shulker_box = "minecraft:blue_shulker_box"
    brown_shulker_box = "minecraft:brown_shulker_box"
    green_shulker_box = "minecraft:green_shulker_box"
    red_shulker_box = "minecraft:red_shulker_box"
    black_shulker_box = "minecraft:black_shulker_box"
    white_glazed_terracotta = "minecraft:white_glazed_terracotta"
    orange_glazed_terracotta = "minecraft:orange_glazed_terracotta"
    magenta_glazed_terracotta = "minecraft:magenta_glazed_terracotta"
    light_blue_glazed_terracotta = "minecraft:light_blue_glazed_terracotta"
    yellow_glazed_terracotta = "minecraft:yellow_glazed_terracotta"
    lime_glazed_terracotta = "minecraft:lime_glazed_terracotta"
    pink_glazed_terracotta = "minecraft:pink_glazed_terracotta"
    gray_glazed_terracotta = "minecraft:gray_glazed_terracotta"
    light_gray_glazed_terracotta = "minecraft:light_gray_glazed_terracotta"
    cyan_glazed_terracotta = "minecraft:cyan_glazed_terracotta"
    purple_glazed_terracotta = "minecraft:purple_glazed_terracotta"
    blue_glazed_terracotta = "minecraft:blue_glazed_terracotta"
    brown_glazed_terracotta = "minecraft:brown_glazed_terracotta"
    green_glazed_terracotta = "minecraft:green_glazed_terracotta"
    red_glazed_terracotta = "minecraft:red_glazed_terracotta"
    black_glazed_terracotta = "minecraft:black_glazed_terracotta"
    white_concrete = "minecraft:white_concrete"
    orange_concrete = "minecraft:orange_concrete"
    magenta_concrete = "minecraft:magenta_concrete"
    light_blue_concrete = "minecraft:light_blue_concrete"
    yellow_concrete = "minecraft:yellow_concrete"
    lime_concrete = "minecraft:lime_concrete"
    pink_concrete = "minecraft:pink_concrete"
    gray_concrete = "minecraft:gray_concrete"
    light_gray_concrete = "minecraft:light_gray_concrete"
    cyan_concrete = "minecraft:cyan_concrete"
    purple_concrete = "minecraft:purple_concrete"
    blue_concrete = "minecraft:blue_concrete"
    brown_concrete = "minecraft:brown_concrete"
    green_concrete = "minecraft:green_concrete"
    red_concrete = "minecraft:red_concrete"
    black_concrete = "minecraft:black_concrete"
    white_concrete_powder = "minecraft:white_concrete_powder"
    orange_concrete_powder = "minecraft:orange_concrete_powder"
    magenta_concrete_powder = "minecraft:magenta_concrete_powder"
    light_blue_concrete_powder = "minecraft:light_blue_concrete_powder"
    yellow_concrete_powder = "minecraft:yellow_concrete_powder"
    lime_concrete_powder = "minecraft:lime_concrete_powder"
    pink_concrete_powder = "minecraft:pink_concrete_powder"
    gray_concrete_powder = "minecraft:gray_concrete_powder"
    light_gray_concrete_powder = "minecraft:light_gray_concrete_powder"
    cyan_concrete_powder = "minecraft:cyan_concrete_powder"
    purple_concrete_powder = "minecraft:purple_concrete_powder"
    blue_concrete_powder = "minecraft:blue_concrete_powder"
    brown_concrete_powder = "minecraft:brown_concrete_powder"
    green_concrete_powder = "minecraft:green_concrete_powder"
    red_concrete_powder = "minecraft:red_concrete_powder"
    black_concrete_powder = "minecraft:black_concrete_powder"
    turtle_egg = "minecraft:turtle_egg"
    dead_tube_coral_block = "minecraft:dead_tube_coral_block"
    dead_brain_coral_block = "minecraft:dead_brain_coral_block"
    dead_bubble_coral_block = "minecraft:dead_bubble_coral_block"
    dead_fire_coral_block = "minecraft:dead_fire_coral_block"
    dead_horn_coral_block = "minecraft:dead_horn_coral_block"
    tube_coral_block = "minecraft:tube_coral_block"
    brain_coral_block = "minecraft:brain_coral_block"
    bubble_coral_block = "minecraft:bubble_coral_block"
    fire_coral_block = "minecraft:fire_coral_block"
    horn_coral_block = "minecraft:horn_coral_block"
    tube_coral = "minecraft:tube_coral"
    brain_coral = "minecraft:brain_coral"
    bubble_coral = "minecraft:bubble_coral"
    fire_coral = "minecraft:fire_coral"
    horn_coral = "minecraft:horn_coral"
    dead_brain_coral = "minecraft:dead_brain_coral"
    dead_bubble_coral = "minecraft:dead_bubble_coral"
    dead_fire_coral = "minecraft:dead_fire_coral"
    dead_horn_coral = "minecraft:dead_horn_coral"
    dead_tube_coral = "minecraft:dead_tube_coral"
    tube_coral_fan = "minecraft:tube_coral_fan"
    brain_coral_fan = "minecraft:brain_coral_fan"
    bubble_coral_fan = "minecraft:bubble_coral_fan"
    fire_coral_fan = "minecraft:fire_coral_fan"
    horn_coral_fan = "minecraft:horn_coral_fan"
    dead_tube_coral_fan = "minecraft:dead_tube_coral_fan"
    dead_brain_coral_fan = "minecraft:dead_brain_coral_fan"
    dead_bubble_coral_fan = "minecraft:dead_bubble_coral_fan"
    dead_fire_coral_fan = "minecraft:dead_fire_coral_fan"
    dead_horn_coral_fan = "minecraft:dead_horn_coral_fan"
    blue_ice = "minecraft:blue_ice"
    conduit = "minecraft:conduit"
    polished_granite_stairs = "minecraft:polished_granite_stairs"
    smooth_red_sandstone_stairs = "minecraft:smooth_red_sandstone_stairs"
    mossy_stone_brick_stairs = "minecraft:mossy_stone_brick_stairs"
    polished_diorite_stairs = "minecraft:polished_diorite_stairs"
    mossy_cobblestone_stairs = "minecraft:mossy_cobblestone_stairs"
    end_stone_brick_stairs = "minecraft:end_stone_brick_stairs"
    stone_stairs = "minecraft:stone_stairs"
    smooth_sandstone_stairs = "minecraft:smooth_sandstone_stairs"
    smooth_quartz_stairs = "minecraft:smooth_quartz_stairs"
    granite_stairs = "minecraft:granite_stairs"
    andesite_stairs = "minecraft:andesite_stairs"
    red_nether_brick_stairs = "minecraft:red_nether_brick_stairs"
    polished_andesite_stairs = "minecraft:polished_andesite_stairs"
    diorite_stairs = "minecraft:diorite_stairs"
    polished_granite_slab = "minecraft:polished_granite_slab"
    smooth_red_sandstone_slab = "minecraft:smooth_red_sandstone_slab"
    mossy_stone_brick_slab = "minecraft:mossy_stone_brick_slab"
    polished_diorite_slab = "minecraft:polished_diorite_slab"
    mossy_cobblestone_slab = "minecraft:mossy_cobblestone_slab"
    end_stone_brick_slab = "minecraft:end_stone_brick_slab"
    smooth_sandstone_slab = "minecraft:smooth_sandstone_slab"
    smooth_quartz_slab = "minecraft:smooth_quartz_slab"
    granite_slab = "minecraft:granite_slab"
    andesite_slab = "minecraft:andesite_slab"
    red_nether_brick_slab = "minecraft:red_nether_brick_slab"
    polished_andesite_slab = "minecraft:polished_andesite_slab"
    diorite_slab = "minecraft:diorite_slab"
    scaffolding = "minecraft:scaffolding"
    iron_door = "minecraft:iron_door"
    oak_door = "minecraft:oak_door"
    spruce_door = "minecraft:spruce_door"
    birch_door = "minecraft:birch_door"
    jungle_door = "minecraft:jungle_door"
    acacia_door = "minecraft:acacia_door"
    dark_oak_door = "minecraft:dark_oak_door"
    crimson_door = "minecraft:crimson_door"
    warped_door = "minecraft:warped_door"
    repeater = "minecraft:repeater"
    comparator = "minecraft:comparator"
    structure_block = "minecraft:structure_block"
    jigsaw = "minecraft:jigsaw"
    turtle_helmet = "minecraft:turtle_helmet"
    scute = "minecraft:scute"
    flint_and_steel = "minecraft:flint_and_steel"
    apple = "minecraft:apple"
    bow = "minecraft:bow"
    arrow = "minecraft:arrow"
    coal = "minecraft:coal"
    charcoal = "minecraft:charcoal"
    diamond = "minecraft:diamond"
    iron_ingot = "minecraft:iron_ingot"
    gold_ingot = "minecraft:gold_ingot"
    netherite_ingot = "minecraft:netherite_ingot"
    netherite_scrap = "minecraft:netherite_scrap"
    wooden_sword = "minecraft:wooden_sword"
    wooden_shovel = "minecraft:wooden_shovel"
    wooden_pickaxe = "minecraft:wooden_pickaxe"
    wooden_axe = "minecraft:wooden_axe"
    wooden_hoe = "minecraft:wooden_hoe"
    stone_sword = "minecraft:stone_sword"
    stone_shovel = "minecraft:stone_shovel"
    stone_pickaxe = "minecraft:stone_pickaxe"
    stone_axe = "minecraft:stone_axe"
    stone_hoe = "minecraft:stone_hoe"
    golden_sword = "minecraft:golden_sword"
    golden_shovel = "minecraft:golden_shovel"
    golden_pickaxe = "minecraft:golden_pickaxe"
    golden_axe = "minecraft:golden_axe"
    golden_hoe = "minecraft:golden_hoe"
    iron_sword = "minecraft:iron_sword"
    iron_shovel = "minecraft:iron_shovel"
    iron_pickaxe = "minecraft:iron_pickaxe"
    iron_axe = "minecraft:iron_axe"
    iron_hoe = "minecraft:iron_hoe"
    diamond_sword = "minecraft:diamond_sword"
    diamond_shovel = "minecraft:diamond_shovel"
    diamond_pickaxe = "minecraft:diamond_pickaxe"
    diamond_axe = "minecraft:diamond_axe"
    diamond_hoe = "minecraft:diamond_hoe"
    netherite_sword = "minecraft:netherite_sword"
    netherite_shovel = "minecraft:netherite_shovel"
    netherite_pickaxe = "minecraft:netherite_pickaxe"
    netherite_axe = "minecraft:netherite_axe"
    netherite_hoe = "minecraft:netherite_hoe"
    stick = "minecraft:stick"
    bowl = "minecraft:bowl"
    mushroom_stew = "minecraft:mushroom_stew"
    string = "minecraft:string"
    feather = "minecraft:feather"
    gunpowder = "minecraft:gunpowder"
    wheat_seeds = "minecraft:wheat_seeds"
    wheat = "minecraft:wheat"
    bread = "minecraft:bread"
    leather_helmet = "minecraft:leather_helmet"
    leather_chestplate = "minecraft:leather_chestplate"
    leather_leggings = "minecraft:leather_leggings"
    leather_boots = "minecraft:leather_boots"
    chainmail_helmet = "minecraft:chainmail_helmet"
    chainmail_chestplate = "minecraft:chainmail_chestplate"
    chainmail_leggings = "minecraft:chainmail_leggings"
    chainmail_boots = "minecraft:chainmail_boots"
    iron_helmet = "minecraft:iron_helmet"
    iron_chestplate = "minecraft:iron_chestplate"
    iron_leggings = "minecraft:iron_leggings"
    iron_boots = "minecraft:iron_boots"
    diamond_helmet = "minecraft:diamond_helmet"
    diamond_chestplate = "minecraft:diamond_chestplate"
    diamond_leggings = "minecraft:diamond_leggings"
    diamond_boots = "minecraft:diamond_boots"
    golden_helmet = "minecraft:golden_helmet"
    golden_chestplate = "minecraft:golden_chestplate"
    golden_leggings = "minecraft:golden_leggings"
    golden_boots = "minecraft:golden_boots"
    netherite_helmet = "minecraft:netherite_helmet"
    netherite_chestplate = "minecraft:netherite_chestplate"
    netherite_leggings = "minecraft:netherite_leggings"
    netherite_boots = "minecraft:netherite_boots"
    flint = "minecraft:flint"
    porkchop = "minecraft:porkchop"
    cooked_porkchop = "minecraft:cooked_porkchop"
    painting = "minecraft:painting"
    golden_apple = "minecraft:golden_apple"
    enchanted_golden_apple = "minecraft:enchanted_golden_apple"
    oak_sign = "minecraft:oak_sign"
    spruce_sign = "minecraft:spruce_sign"
    birch_sign = "minecraft:birch_sign"
    jungle_sign = "minecraft:jungle_sign"
    acacia_sign = "minecraft:acacia_sign"
    dark_oak_sign = "minecraft:dark_oak_sign"
    crimson_sign = "minecraft:crimson_sign"
    warped_sign = "minecraft:warped_sign"
    bucket = "minecraft:bucket"
    water_bucket = "minecraft:water_bucket"
    lava_bucket = "minecraft:lava_bucket"
    minecart = "minecraft:minecart"
    saddle = "minecraft:saddle"
    redstone = "minecraft:redstone"
    snowball = "minecraft:snowball"
    oak_boat = "minecraft:oak_boat"
    leather = "minecraft:leather"
    milk_bucket = "minecraft:milk_bucket"
    pufferfish_bucket = "minecraft:pufferfish_bucket"
    salmon_bucket = "minecraft:salmon_bucket"
    cod_bucket = "minecraft:cod_bucket"
    tropical_fish_bucket = "minecraft:tropical_fish_bucket"
    brick = "minecraft:brick"
    clay_ball = "minecraft:clay_ball"
    dried_kelp_block = "minecraft:dried_kelp_block"
    paper = "minecraft:paper"
    book = "minecraft:book"
    slime_ball = "minecraft:slime_ball"
    chest_minecart = "minecraft:chest_minecart"
    furnace_minecart = "minecraft:furnace_minecart"
    egg = "minecraft:egg"
    compass = "minecraft:compass"
    fishing_rod = "minecraft:fishing_rod"
    clock = "minecraft:clock"
    glowstone_dust = "minecraft:glowstone_dust"
    cod = "minecraft:cod"
    salmon = "minecraft:salmon"
    tropical_fish = "minecraft:tropical_fish"
    pufferfish = "minecraft:pufferfish"
    cooked_cod = "minecraft:cooked_cod"
    cooked_salmon = "minecraft:cooked_salmon"
    ink_sac = "minecraft:ink_sac"
    cocoa_beans = "minecraft:cocoa_beans"
    lapis_lazuli = "minecraft:lapis_lazuli"
    white_dye = "minecraft:white_dye"
    orange_dye = "minecraft:orange_dye"
    magenta_dye = "minecraft:magenta_dye"
    light_blue_dye = "minecraft:light_blue_dye"
    yellow_dye = "minecraft:yellow_dye"
    lime_dye = "minecraft:lime_dye"
    pink_dye = "minecraft:pink_dye"
    gray_dye = "minecraft:gray_dye"
    light_gray_dye = "minecraft:light_gray_dye"
    cyan_dye = "minecraft:cyan_dye"
    purple_dye = "minecraft:purple_dye"
    blue_dye = "minecraft:blue_dye"
    brown_dye = "minecraft:brown_dye"
    green_dye = "minecraft:green_dye"
    red_dye = "minecraft:red_dye"
    black_dye = "minecraft:black_dye"
    bone_meal = "minecraft:bone_meal"
    bone = "minecraft:bone"
    sugar = "minecraft:sugar"
    cake = "minecraft:cake"
    white_bed = "minecraft:white_bed"
    orange_bed = "minecraft:orange_bed"
    magenta_bed = "minecraft:magenta_bed"
    light_blue_bed = "minecraft:light_blue_bed"
    yellow_bed = "minecraft:yellow_bed"
    lime_bed = "minecraft:lime_bed"
    pink_bed = "minecraft:pink_bed"
    gray_bed = "minecraft:gray_bed"
    light_gray_bed = "minecraft:light_gray_bed"
    cyan_bed = "minecraft:cyan_bed"
    purple_bed = "minecraft:purple_bed"
    blue_bed = "minecraft:blue_bed"
    brown_bed = "minecraft:brown_bed"
    green_bed = "minecraft:green_bed"
    red_bed = "minecraft:red_bed"
    black_bed = "minecraft:black_bed"
    cookie = "minecraft:cookie"
    filled_map = "minecraft:filled_map"
    shears = "minecraft:shears"
    melon_slice = "minecraft:melon_slice"
    dried_kelp = "minecraft:dried_kelp"
    pumpkin_seeds = "minecraft:pumpkin_seeds"
    melon_seeds = "minecraft:melon_seeds"
    beef = "minecraft:beef"
    cooked_beef = "minecraft:cooked_beef"
    chicken = "minecraft:chicken"
    cooked_chicken = "minecraft:cooked_chicken"
    rotten_flesh = "minecraft:rotten_flesh"
    ender_pearl = "minecraft:ender_pearl"
    blaze_rod = "minecraft:blaze_rod"
    ghast_tear = "minecraft:ghast_tear"
    gold_nugget = "minecraft:gold_nugget"
    nether_wart = "minecraft:nether_wart"
    potion = "minecraft:potion"
    glass_bottle = "minecraft:glass_bottle"
    spider_eye = "minecraft:spider_eye"
    fermented_spider_eye = "minecraft:fermented_spider_eye"
    blaze_powder = "minecraft:blaze_powder"
    magma_cream = "minecraft:magma_cream"
    brewing_stand = "minecraft:brewing_stand"
    cauldron = "minecraft:cauldron"
    ender_eye = "minecraft:ender_eye"
    glistering_melon_slice = "minecraft:glistering_melon_slice"
    bat_spawn_egg = "minecraft:bat_spawn_egg"
    bee_spawn_egg = "minecraft:bee_spawn_egg"
    blaze_spawn_egg = "minecraft:blaze_spawn_egg"
    cat_spawn_egg = "minecraft:cat_spawn_egg"
    cave_spider_spawn_egg = "minecraft:cave_spider_spawn_egg"
    chicken_spawn_egg = "minecraft:chicken_spawn_egg"
    cod_spawn_egg = "minecraft:cod_spawn_egg"
    cow_spawn_egg = "minecraft:cow_spawn_egg"
    creeper_spawn_egg = "minecraft:creeper_spawn_egg"
    dolphin_spawn_egg = "minecraft:dolphin_spawn_egg"
    donkey_spawn_egg = "minecraft:donkey_spawn_egg"
    drowned_spawn_egg = "minecraft:drowned_spawn_egg"
    elder_guardian_spawn_egg = "minecraft:elder_guardian_spawn_egg"
    enderman_spawn_egg = "minecraft:enderman_spawn_egg"
    endermite_spawn_egg = "minecraft:endermite_spawn_egg"
    evoker_spawn_egg = "minecraft:evoker_spawn_egg"
    fox_spawn_egg = "minecraft:fox_spawn_egg"
    ghast_spawn_egg = "minecraft:ghast_spawn_egg"
    guardian_spawn_egg = "minecraft:guardian_spawn_egg"
    hoglin_spawn_egg = "minecraft:hoglin_spawn_egg"
    horse_spawn_egg = "minecraft:horse_spawn_egg"
    husk_spawn_egg = "minecraft:husk_spawn_egg"
    llama_spawn_egg = "minecraft:llama_spawn_egg"
    magma_cube_spawn_egg = "minecraft:magma_cube_spawn_egg"
    mooshroom_spawn_egg = "minecraft:mooshroom_spawn_egg"
    mule_spawn_egg = "minecraft:mule_spawn_egg"
    ocelot_spawn_egg = "minecraft:ocelot_spawn_egg"
    panda_spawn_egg = "minecraft:panda_spawn_egg"
    parrot_spawn_egg = "minecraft:parrot_spawn_egg"
    phantom_spawn_egg = "minecraft:phantom_spawn_egg"
    pig_spawn_egg = "minecraft:pig_spawn_egg"
    piglin_spawn_egg = "minecraft:piglin_spawn_egg"
    piglin_brute_spawn_egg = "minecraft:piglin_brute_spawn_egg"
    pillager_spawn_egg = "minecraft:pillager_spawn_egg"
    polar_bear_spawn_egg = "minecraft:polar_bear_spawn_egg"
    pufferfish_spawn_egg = "minecraft:pufferfish_spawn_egg"
    rabbit_spawn_egg = "minecraft:rabbit_spawn_egg"
    ravager_spawn_egg = "minecraft:ravager_spawn_egg"
    salmon_spawn_egg = "minecraft:salmon_spawn_egg"
    sheep_spawn_egg = "minecraft:sheep_spawn_egg"
    shulker_spawn_egg = "minecraft:shulker_spawn_egg"
    silverfish_spawn_egg = "minecraft:silverfish_spawn_egg"
    skeleton_spawn_egg = "minecraft:skeleton_spawn_egg"
    skeleton_horse_spawn_egg = "minecraft:skeleton_horse_spawn_egg"
    slime_spawn_egg = "minecraft:slime_spawn_egg"
    spider_spawn_egg = "minecraft:spider_spawn_egg"
    squid_spawn_egg = "minecraft:squid_spawn_egg"
    stray_spawn_egg = "minecraft:stray_spawn_egg"
    strider_spawn_egg = "minecraft:strider_spawn_egg"
    trader_llama_spawn_egg = "minecraft:trader_llama_spawn_egg"
    tropical_fish_spawn_egg = "minecraft:tropical_fish_spawn_egg"
    turtle_spawn_egg = "minecraft:turtle_spawn_egg"
    vex_spawn_egg = "minecraft:vex_spawn_egg"
    villager_spawn_egg = "minecraft:villager_spawn_egg"
    vindicator_spawn_egg = "minecraft:vindicator_spawn_egg"
    wandering_trader_spawn_egg = "minecraft:wandering_trader_spawn_egg"
    witch_spawn_egg = "minecraft:witch_spawn_egg"
    wither_skeleton_spawn_egg = "minecraft:wither_skeleton_spawn_egg"
    wolf_spawn_egg = "minecraft:wolf_spawn_egg"
    zoglin_spawn_egg = "minecraft:zoglin_spawn_egg"
    zombie_spawn_egg = "minecraft:zombie_spawn_egg"
    zombie_horse_spawn_egg = "minecraft:zombie_horse_spawn_egg"
    zombie_villager_spawn_egg = "minecraft:zombie_villager_spawn_egg"
    zombified_piglin_spawn_egg = "minecraft:zombified_piglin_spawn_egg"
    experience_bottle = "minecraft:experience_bottle"
    fire_charge = "minecraft:fire_charge"
    writable_book = "minecraft:writable_book"
    written_book = "minecraft:written_book"
    emerald = "minecraft:emerald"
    item_frame = "minecraft:item_frame"
    flower_pot = "minecraft:flower_pot"
    carrot = "minecraft:carrot"
    potato = "minecraft:potato"
    baked_potato = "minecraft:baked_potato"
    poisonous_potato = "minecraft:poisonous_potato"
    map = "minecraft:map"
    golden_carrot = "minecraft:golden_carrot"
    skeleton_skull = "minecraft:skeleton_skull"
    wither_skeleton_skull = "minecraft:wither_skeleton_skull"
    player_head = "minecraft:player_head"
    zombie_head = "minecraft:zombie_head"
    creeper_head = "minecraft:creeper_head"
    dragon_head = "minecraft:dragon_head"
    carrot_on_a_stick = "minecraft:carrot_on_a_stick"
    warped_fungus_on_a_stick = "minecraft:warped_fungus_on_a_stick"
    nether_star = "minecraft:nether_star"
    pumpkin_pie = "minecraft:pumpkin_pie"
    firework_rocket = "minecraft:firework_rocket"
    firework_star = "minecraft:firework_star"
    enchanted_book = "minecraft:enchanted_book"
    nether_brick = "minecraft:nether_brick"
    quartz = "minecraft:quartz"
    tnt_minecart = "minecraft:tnt_minecart"
    hopper_minecart = "minecraft:hopper_minecart"
    prismarine_shard = "minecraft:prismarine_shard"
    prismarine_crystals = "minecraft:prismarine_crystals"
    rabbit = "minecraft:rabbit"
    cooked_rabbit = "minecraft:cooked_rabbit"
    rabbit_stew = "minecraft:rabbit_stew"
    rabbit_foot = "minecraft:rabbit_foot"
    rabbit_hide = "minecraft:rabbit_hide"
    armor_stand = "minecraft:armor_stand"
    iron_horse_armor = "minecraft:iron_horse_armor"
    golden_horse_armor = "minecraft:golden_horse_armor"
    diamond_horse_armor = "minecraft:diamond_horse_armor"
    leather_horse_armor = "minecraft:leather_horse_armor"
    lead = "minecraft:lead"
    name_tag = "minecraft:name_tag"
    command_block_minecart = "minecraft:command_block_minecart"
    mutton = "minecraft:mutton"
    cooked_mutton = "minecraft:cooked_mutton"
    white_banner = "minecraft:white_banner"
    orange_banner = "minecraft:orange_banner"
    magenta_banner = "minecraft:magenta_banner"
    light_blue_banner = "minecraft:light_blue_banner"
    yellow_banner = "minecraft:yellow_banner"
    lime_banner = "minecraft:lime_banner"
    pink_banner = "minecraft:pink_banner"
    gray_banner = "minecraft:gray_banner"
    light_gray_banner = "minecraft:light_gray_banner"
    cyan_banner = "minecraft:cyan_banner"
    purple_banner = "minecraft:purple_banner"
    blue_banner = "minecraft:blue_banner"
    brown_banner = "minecraft:brown_banner"
    green_banner = "minecraft:green_banner"
    red_banner = "minecraft:red_banner"
    black_banner = "minecraft:black_banner"
    end_crystal = "minecraft:end_crystal"
    chorus_fruit = "minecraft:chorus_fruit"
    popped_chorus_fruit = "minecraft:popped_chorus_fruit"
    beetroot = "minecraft:beetroot"
    beetroot_seeds = "minecraft:beetroot_seeds"
    beetroot_soup = "minecraft:beetroot_soup"
    dragon_breath = "minecraft:dragon_breath"
    splash_potion = "minecraft:splash_potion"
    spectral_arrow = "minecraft:spectral_arrow"
    tipped_arrow = "minecraft:tipped_arrow"
    lingering_potion = "minecraft:lingering_potion"
    shield = "minecraft:shield"
    elytra = "minecraft:elytra"
    spruce_boat = "minecraft:spruce_boat"
    birch_boat = "minecraft:birch_boat"
    jungle_boat = "minecraft:jungle_boat"
    acacia_boat = "minecraft:acacia_boat"
    dark_oak_boat = "minecraft:dark_oak_boat"
    totem_of_undying = "minecraft:totem_of_undying"
    shulker_shell = "minecraft:shulker_shell"
    iron_nugget = "minecraft:iron_nugget"
    knowledge_book = "minecraft:knowledge_book"
    debug_stick = "minecraft:debug_stick"
    music_disc_13 = "minecraft:music_disc_13"
    music_disc_cat = "minecraft:music_disc_cat"
    music_disc_blocks = "minecraft:music_disc_blocks"
    music_disc_chirp = "minecraft:music_disc_chirp"
    music_disc_far = "minecraft:music_disc_far"
    music_disc_mall = "minecraft:music_disc_mall"
    music_disc_mellohi = "minecraft:music_disc_mellohi"
    music_disc_stal = "minecraft:music_disc_stal"
    music_disc_strad = "minecraft:music_disc_strad"
    music_disc_ward = "minecraft:music_disc_ward"
    music_disc_11 = "minecraft:music_disc_11"
    music_disc_wait = "minecraft:music_disc_wait"
    music_disc_pigstep = "minecraft:music_disc_pigstep"
    trident = "minecraft:trident"
    phantom_membrane = "minecraft:phantom_membrane"
    nautilus_shell = "minecraft:nautilus_shell"
    heart_of_the_sea = "minecraft:heart_of_the_sea"
    crossbow = "minecraft:crossbow"
    suspicious_stew = "minecraft:suspicious_stew"
    loom = "minecraft:loom"
    flower_banner_pattern = "minecraft:flower_banner_pattern"
    creeper_banner_pattern = "minecraft:creeper_banner_pattern"
    skull_banner_pattern = "minecraft:skull_banner_pattern"
    mojang_banner_pattern = "minecraft:mojang_banner_pattern"
    globe_banner_pattern = "minecraft:globe_banner_pattern"
    piglin_banner_pattern = "minecraft:piglin_banner_pattern"
    composter = "minecraft:composter"
    barrel = "minecraft:barrel"
    smoker = "minecraft:smoker"
    blast_furnace = "minecraft:blast_furnace"
    cartography_table = "minecraft:cartography_table"
    fletching_table = "minecraft:fletching_table"
    grindstone = "minecraft:grindstone"
    lectern = "minecraft:lectern"
    smithing_table = "minecraft:smithing_table"
    stonecutter = "minecraft:stonecutter"
    bell = "minecraft:bell"
    lantern = "minecraft:lantern"
    soul_lantern = "minecraft:soul_lantern"
    sweet_berries = "minecraft:sweet_berries"
    campfire = "minecraft:campfire"
    soul_campfire = "minecraft:soul_campfire"
    shroomlight = "minecraft:shroomlight"
    honeycomb = "minecraft:honeycomb"
    bee_nest = "minecraft:bee_nest"
    beehive = "minecraft:beehive"
    honey_bottle = "minecraft:honey_bottle"
    honey_block = "minecraft:honey_block"
    honeycomb_block = "minecraft:honeycomb_block"
    lodestone = "minecraft:lodestone"
    netherite_block = "minecraft:netherite_block"
    ancient_debris = "minecraft:ancient_debris"
    target = "minecraft:target"
    crying_obsidian = "minecraft:crying_obsidian"
    blackstone = "minecraft:blackstone"
    blackstone_slab = "minecraft:blackstone_slab"
    blackstone_stairs = "minecraft:blackstone_stairs"
    gilded_blackstone = "minecraft:gilded_blackstone"
    polished_blackstone = "minecraft:polished_blackstone"
    polished_blackstone_slab = "minecraft:polished_blackstone_slab"
    polished_blackstone_stairs = "minecraft:polished_blackstone_stairs"
    chiseled_polished_blackstone = "minecraft:chiseled_polished_blackstone"
    polished_blackstone_bricks = "minecraft:polished_blackstone_bricks"
    polished_blackstone_brick_slab = "minecraft:polished_blackstone_brick_slab"
    polished_blackstone_brick_stairs = "minecraft:polished_blackstone_brick_stairs"
    cracked_polished_blackstone_bricks = "minecraft:cracked_polished_blackstone_bricks"
    respawn_anchor = "minecraft:respawn_anchor"


class entity(enum.Enum):
    """
    * area_effect_cloud
    * armor_stand
    * arrow
    * bat
    * bee
    * blaze
    * boat
    * cat
    * cave_spider
    * chicken
    * cod
    * cow
    * creeper
    * dolphin
    * donkey
    * dragon_fireball
    * drowned
    * elder_guardian
    * end_crystal
    * ender_dragon
    * enderman
    * endermite
    * evoker
    * evoker_fangs
    * experience_orb
    * eye_of_ender
    * falling_block
    * firework_rocket
    * fox
    * ghast
    * giant
    * guardian
    * hoglin
    * horse
    * husk
    * illusioner
    * iron_golem
    * item
    * item_frame
    * fireball
    * leash_knot
    * lightning_bolt
    * llama
    * llama_spit
    * magma_cube
    * minecart
    * chest_minecart
    * command_block_minecart
    * furnace_minecart
    * hopper_minecart
    * spawner_minecart
    * tnt_minecart
    * mule
    * mooshroom
    * ocelot
    * painting
    * panda
    * parrot
    * phantom
    * pig
    * piglin
    * piglin_brute
    * pillager
    * polar_bear
    * tnt
    * pufferfish
    * rabbit
    * ravager
    * salmon
    * sheep
    * shulker
    * shulker_bullet
    * silverfish
    * skeleton
    * skeleton_horse
    * slime
    * small_fireball
    * snow_golem
    * snowball
    * spectral_arrow
    * spider
    * squid
    * stray
    * strider
    * egg
    * ender_pearl
    * experience_bottle
    * potion
    * trident
    * trader_llama
    * tropical_fish
    * turtle
    * vex
    * villager
    * vindicator
    * wandering_trader
    * witch
    * wither
    * wither_skeleton
    * wither_skull
    * wolf
    * zoglin
    * zombie
    * zombie_horse
    * zombie_villager
    * zombified_piglin
    * player
    * fishing_bobber
    """
    area_effect_cloud = "minecraft:area_effect_cloud"
    armor_stand = "minecraft:armor_stand"
    arrow = "minecraft:arrow"
    bat = "minecraft:bat"
    bee = "minecraft:bee"
    blaze = "minecraft:blaze"
    boat = "minecraft:boat"
    cat = "minecraft:cat"
    cave_spider = "minecraft:cave_spider"
    chicken = "minecraft:chicken"
    cod = "minecraft:cod"
    cow = "minecraft:cow"
    creeper = "minecraft:creeper"
    dolphin = "minecraft:dolphin"
    donkey = "minecraft:donkey"
    dragon_fireball = "minecraft:dragon_fireball"
    drowned = "minecraft:drowned"
    elder_guardian = "minecraft:elder_guardian"
    end_crystal = "minecraft:end_crystal"
    ender_dragon = "minecraft:ender_dragon"
    enderman = "minecraft:enderman"
    endermite = "minecraft:endermite"
    evoker = "minecraft:evoker"
    evoker_fangs = "minecraft:evoker_fangs"
    experience_orb = "minecraft:experience_orb"
    eye_of_ender = "minecraft:eye_of_ender"
    falling_block = "minecraft:falling_block"
    firework_rocket = "minecraft:firework_rocket"
    fox = "minecraft:fox"
    ghast = "minecraft:ghast"
    giant = "minecraft:giant"
    guardian = "minecraft:guardian"
    hoglin = "minecraft:hoglin"
    horse = "minecraft:horse"
    husk = "minecraft:husk"
    illusioner = "minecraft:illusioner"
    iron_golem = "minecraft:iron_golem"
    item = "minecraft:item"
    item_frame = "minecraft:item_frame"
    fireball = "minecraft:fireball"
    leash_knot = "minecraft:leash_knot"
    lightning_bolt = "minecraft:lightning_bolt"
    llama = "minecraft:llama"
    llama_spit = "minecraft:llama_spit"
    magma_cube = "minecraft:magma_cube"
    minecart = "minecraft:minecart"
    chest_minecart = "minecraft:chest_minecart"
    command_block_minecart = "minecraft:command_block_minecart"
    furnace_minecart = "minecraft:furnace_minecart"
    hopper_minecart = "minecraft:hopper_minecart"
    spawner_minecart = "minecraft:spawner_minecart"
    tnt_minecart = "minecraft:tnt_minecart"
    mule = "minecraft:mule"
    mooshroom = "minecraft:mooshroom"
    ocelot = "minecraft:ocelot"
    painting = "minecraft:painting"
    panda = "minecraft:panda"
    parrot = "minecraft:parrot"
    phantom = "minecraft:phantom"
    pig = "minecraft:pig"
    piglin = "minecraft:piglin"
    piglin_brute = "minecraft:piglin_brute"
    pillager = "minecraft:pillager"
    polar_bear = "minecraft:polar_bear"
    tnt = "minecraft:tnt"
    pufferfish = "minecraft:pufferfish"
    rabbit = "minecraft:rabbit"
    ravager = "minecraft:ravager"
    salmon = "minecraft:salmon"
    sheep = "minecraft:sheep"
    shulker = "minecraft:shulker"
    shulker_bullet = "minecraft:shulker_bullet"
    silverfish = "minecraft:silverfish"
    skeleton = "minecraft:skeleton"
    skeleton_horse = "minecraft:skeleton_horse"
    slime = "minecraft:slime"
    small_fireball = "minecraft:small_fireball"
    snow_golem = "minecraft:snow_golem"
    snowball = "minecraft:snowball"
    spectral_arrow = "minecraft:spectral_arrow"
    spider = "minecraft:spider"
    squid = "minecraft:squid"
    stray = "minecraft:stray"
    strider = "minecraft:strider"
    egg = "minecraft:egg"
    ender_pearl = "minecraft:ender_pearl"
    experience_bottle = "minecraft:experience_bottle"
    potion = "minecraft:potion"
    trident = "minecraft:trident"
    trader_llama = "minecraft:trader_llama"
    tropical_fish = "minecraft:tropical_fish"
    turtle = "minecraft:turtle"
    vex = "minecraft:vex"
    villager = "minecraft:villager"
    vindicator = "minecraft:vindicator"
    wandering_trader = "minecraft:wandering_trader"
    witch = "minecraft:witch"
    wither = "minecraft:wither"
    wither_skeleton = "minecraft:wither_skeleton"
    wither_skull = "minecraft:wither_skull"
    wolf = "minecraft:wolf"
    zoglin = "minecraft:zoglin"
    zombie = "minecraft:zombie"
    zombie_horse = "minecraft:zombie_horse"
    zombie_villager = "minecraft:zombie_villager"
    zombified_piglin = "minecraft:zombified_piglin"
    player = "minecraft:player"
    fishing_bobber = "minecraft:fishing_bobber"


class biome(enum.Enum):
    """Biome list

    * badlands
    * badlands_plateau
    * bamboo_jungle
    * bamboo_jungle_hills
    * basalt_deltas
    * beach
    * birch_forest
    * birch_forest_hills
    * cold_ocean
    * crimson_forest
    * dark_forest
    * dark_forest_hills
    * deep_cold_ocean
    * deep_frozen_ocean
    * deep_lukewarm_ocean
    * deep_ocean
    * deep_warm_ocean
    * desert
    * desert_hills
    * desert_lakes
    * end_barrens
    * end_highlands
    * end_midlands
    * eroded_badlands
    * flower_forest
    * forest
    * frozen_ocean
    * frozen_river
    * giant_spruce_taiga
    * giant_spruce_taiga_hills
    * giant_tree_taiga
    * giant_tree_taiga_hills
    * gravelly_mountains
    * ice_spikes
    * jungle
    * jungle_edge
    * jungle_hills
    * lukewarm_ocean
    * modified_badlands_plateau
    * modified_gravelly_mountains
    * modified_jungle
    * modified_jungle_edge
    * modified_wooded_badlands_plateau
    * mountains
    * mountain_edge
    * mushroom_fields
    * mushroom_field_shore
    * nether_wastes
    * ocean
    * plains
    * river
    * savanna
    * savanna_plateau
    * shattered_savanna
    * shattered_savanna_plateau
    * small_end_islands
    * snowy_beach
    * snowy_mountains
    * snowy_taiga
    * snowy_taiga_hills
    * snowy_taiga_mountains
    * snowy_tundra
    * soul_sand_valley
    * stone_shore
    * sunflower_plains
    * swamp
    * swamp_hills
    * taiga
    * taiga_hills
    * taiga_mountains
    * tall_birch_forest
    * tall_birch_hills
    * the_end
    * the_void
    * warm_ocean
    * warped_forest
    * wooded_badlands_plateau
    * wooded_hills
    * wooded_mountains
    """
    badlands = "badlands"
    badlands_plateau = "badlands_plateau"
    bamboo_jungle = "bamboo_jungle"
    bamboo_jungle_hills = "bamboo_jungle_hills"
    basalt_deltas = "basalt_deltas"
    beach = "beach"
    birch_forest = "birch_forest"
    birch_forest_hills = "birch_forest_hills"
    cold_ocean = "cold_ocean"
    crimson_forest = "crimson_forest"
    dark_forest = "dark_forest"
    dark_forest_hills = "dark_forest_hills"
    deep_cold_ocean = "deep_cold_ocean"
    deep_frozen_ocean = "deep_frozen_ocean"
    deep_lukewarm_ocean = "deep_lukewarm_ocean"
    deep_ocean = "deep_ocean"
    deep_warm_ocean = "deep_warm_ocean"
    desert = "desert"
    desert_hills = "desert_hills"
    desert_lakes = "desert_lakes"
    end_barrens = "end_barrens"
    end_highlands = "end_highlands"
    end_midlands = "end_midlands"
    eroded_badlands = "eroded_badlands"
    flower_forest = "flower_forest"
    forest = "forest"
    frozen_ocean = "frozen_ocean"
    frozen_river = "frozen_river"
    giant_spruce_taiga = "giant_spruce_taiga"
    giant_spruce_taiga_hills = "giant_spruce_taiga_hills"
    giant_tree_taiga = "giant_tree_taiga"
    giant_tree_taiga_hills = "giant_tree_taiga_hills"
    gravelly_mountains = "gravelly_mountains"
    ice_spikes = "ice_spikes"
    jungle = "jungle"
    jungle_edge = "jungle_edge"
    jungle_hills = "jungle_hills"
    lukewarm_ocean = "lukewarm_ocean"
    modified_badlands_plateau = "modified_badlands_plateau"
    modified_gravelly_mountains = "modified_gravelly_mountains"
    modified_jungle = "modified_jungle"
    modified_jungle_edge = "modified_jungle_edge"
    modified_wooded_badlands_plateau = "modified_wooded_badlands_plateau"
    mountains = "mountains"
    mountain_edge = "mountain_edge"
    mushroom_fields = "mushroom_fields"
    mushroom_field_shore = "mushroom_field_shore"
    nether_wastes = "nether_wastes"
    ocean = "ocean"
    plains = "plains"
    river = "river"
    savanna = "savanna"
    savanna_plateau = "savanna_plateau"
    shattered_savanna = "shattered_savanna"
    shattered_savanna_plateau = "shattered_savanna_plateau"
    small_end_islands = "small_end_islands"
    snowy_beach = "snowy_beach"
    snowy_mountains = "snowy_mountains"
    snowy_taiga = "snowy_taiga"
    snowy_taiga_hills = "snowy_taiga_hills"
    snowy_taiga_mountains = "snowy_taiga_mountains"
    snowy_tundra = "snowy_tundra"
    soul_sand_valley = "soul_sand_valley"
    stone_shore = "stone_shore"
    sunflower_plains = "sunflower_plains"
    swamp = "swamp"
    swamp_hills = "swamp_hills"
    taiga = "taiga"
    taiga_hills = "taiga_hills"
    taiga_mountains = "taiga_mountains"
    tall_birch_forest = "tall_birch_forest"
    tall_birch_hills = "tall_birch_hills"
    the_end = "the_end"
    the_void = "the_void"
    warm_ocean = "warm_ocean"
    warped_forest = "warped_forest"
    wooded_badlands_plateau = "wooded_badlands_plateau"
    wooded_hills = "wooded_hills"
    wooded_mountains = "wooded_mountains"


class structure(enum.Enum):
    """Structure list

    * bastion_remnant
    * buried_treasure
    * desert_pyramid
    * endcity
    * fortress
    * igloo
    * jungle_pyramid
    * mansion
    * mineshaft
    * monument
    * nether_fossil
    * ocean_ruin
    * pillager_outpost
    * ruined_portal
    * shipwreck
    * stronghold
    * swamp_hut
    * village
    """
    bastion_remnant = "bastion_remnant"
    buried_treasure = "buried_treasure"
    desert_pyramid = "desert_pyramid"
    endcity = "endcity"
    fortress = "fortress"
    igloo = "igloo"
    jungle_pyramid = "jungle_pyramid"
    mansion = "mansion"
    mineshaft = "mineshaft"
    monument = "monument"
    nether_fossil = "nether_fossil"
    ocean_ruin = "ocean_ruin"
    pillager_outpost = "pillager_outpost"
    ruined_portal = "ruined_portal"
    shipwreck = "shipwreck"
    stronghold = "stronghold"
    swamp_hut = "swamp_hut"
    village = "village"


class sound_channel(enum.Enum):
    """Channel list for playsound command

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


class recipes(enum.Enum):
    """Recipe list

    * acacia_boat
    * acacia_button
    * acacia_door
    * acacia_fence
    * acacia_fence_gate
    * acacia_planks
    * acacia_pressure_plate
    * acacia_sign
    * acacia_slab
    * acacia_stairs
    * acacia_trapdoor
    * acacia_wood
    * activator_rail
    * andesite
    * andesite_slab
    * andesite_slab_from_andesite_stonecutting
    * andesite_stairs
    * andesite_stairs_from_andesite_stonecutting
    * andesite_wall
    * andesite_wall_from_andesite_stonecutting
    * anvil
    * armor_dye
    * armor_stand
    * arrow
    * baked_potato
    * baked_potato_from_campfire_cooking
    * baked_potato_from_smoking
    * banner_duplicate
    * barrel
    * beacon
    * beehive
    * beetroot_soup
    * birch_boat
    * birch_button
    * birch_door
    * birch_fence
    * birch_fence_gate
    * birch_planks
    * birch_pressure_plate
    * birch_sign
    * birch_slab
    * birch_stairs
    * birch_trapdoor
    * birch_wood
    * blackstone_slab
    * blackstone_slab_from_blackstone_stonecutting
    * blackstone_stairs
    * blackstone_stairs_from_blackstone_stonecutting
    * blackstone_wall
    * blackstone_wall_from_blackstone_stonecutting
    * black_banner
    * black_bed
    * black_bed_from_white_bed
    * black_carpet
    * black_carpet_from_white_carpet
    * black_concrete_powder
    * black_dye
    * black_dye_from_wither_rose
    * black_glazed_terracotta
    * black_stained_glass
    * black_stained_glass_pane
    * black_stained_glass_pane_from_glass_pane
    * black_terracotta
    * black_wool
    * blast_furnace
    * blaze_powder
    * blue_banner
    * blue_bed
    * blue_bed_from_white_bed
    * blue_carpet
    * blue_carpet_from_white_carpet
    * blue_concrete_powder
    * blue_dye
    * blue_dye_from_cornflower
    * blue_glazed_terracotta
    * blue_ice
    * blue_stained_glass
    * blue_stained_glass_pane
    * blue_stained_glass_pane_from_glass_pane
    * blue_terracotta
    * blue_wool
    * bone_block
    * bone_meal
    * bone_meal_from_bone_block
    * book
    * bookshelf
    * book_cloning
    * bow
    * bowl
    * bread
    * brewing_stand
    * brick
    * bricks
    * brick_slab
    * brick_slab_from_bricks_stonecutting
    * brick_stairs
    * brick_stairs_from_bricks_stonecutting
    * brick_wall
    * brick_wall_from_bricks_stonecutting
    * brown_banner
    * brown_bed
    * brown_bed_from_white_bed
    * brown_carpet
    * brown_carpet_from_white_carpet
    * brown_concrete_powder
    * brown_dye
    * brown_glazed_terracotta
    * brown_stained_glass
    * brown_stained_glass_pane
    * brown_stained_glass_pane_from_glass_pane
    * brown_terracotta
    * brown_wool
    * bucket
    * cake
    * campfire
    * carrot_on_a_stick
    * cartography_table
    * cauldron
    * chain
    * charcoal
    * chest
    * chest_minecart
    * chiseled_nether_bricks
    * chiseled_nether_bricks_from_nether_bricks_stonecutting
    * chiseled_polished_blackstone
    * chiseled_polished_blackstone_from_blackstone_stonecutting
    * chiseled_polished_blackstone_from_polished_blackstone_stonecutting
    * chiseled_quartz_block
    * chiseled_quartz_block_from_quartz_block_stonecutting
    * chiseled_red_sandstone
    * chiseled_red_sandstone_from_red_sandstone_stonecutting
    * chiseled_sandstone
    * chiseled_sandstone_from_sandstone_stonecutting
    * chiseled_stone_bricks
    * chiseled_stone_bricks_from_stone_bricks_stonecutting
    * chiseled_stone_bricks_stone_from_stonecutting
    * clay
    * clock
    * coal
    * coal_block
    * coal_from_blasting
    * coal_from_smelting
    * coarse_dirt
    * cobblestone_slab
    * cobblestone_slab_from_cobblestone_stonecutting
    * cobblestone_stairs
    * cobblestone_stairs_from_cobblestone_stonecutting
    * cobblestone_wall
    * cobblestone_wall_from_cobblestone_stonecutting
    * comparator
    * compass
    * composter
    * conduit
    * cooked_beef
    * cooked_beef_from_campfire_cooking
    * cooked_beef_from_smoking
    * cooked_chicken
    * cooked_chicken_from_campfire_cooking
    * cooked_chicken_from_smoking
    * cooked_cod
    * cooked_cod_from_campfire_cooking
    * cooked_cod_from_smoking
    * cooked_mutton
    * cooked_mutton_from_campfire_cooking
    * cooked_mutton_from_smoking
    * cooked_porkchop
    * cooked_porkchop_from_campfire_cooking
    * cooked_porkchop_from_smoking
    * cooked_rabbit
    * cooked_rabbit_from_campfire_cooking
    * cooked_rabbit_from_smoking
    * cooked_salmon
    * cooked_salmon_from_campfire_cooking
    * cooked_salmon_from_smoking
    * cookie
    * cracked_nether_bricks
    * cracked_polished_blackstone_bricks
    * cracked_stone_bricks
    * crafting_table
    * creeper_banner_pattern
    * crimson_button
    * crimson_door
    * crimson_fence
    * crimson_fence_gate
    * crimson_hyphae
    * crimson_planks
    * crimson_pressure_plate
    * crimson_sign
    * crimson_slab
    * crimson_stairs
    * crimson_trapdoor
    * crossbow
    * cut_red_sandstone
    * cut_red_sandstone_from_red_sandstone_stonecutting
    * cut_red_sandstone_slab
    * cut_red_sandstone_slab_from_cut_red_sandstone_stonecutting
    * cut_red_sandstone_slab_from_red_sandstone_stonecutting
    * cut_sandstone
    * cut_sandstone_from_sandstone_stonecutting
    * cut_sandstone_slab
    * cut_sandstone_slab_from_cut_sandstone_stonecutting
    * cut_sandstone_slab_from_sandstone_stonecutting
    * cyan_banner
    * cyan_bed
    * cyan_bed_from_white_bed
    * cyan_carpet
    * cyan_carpet_from_white_carpet
    * cyan_concrete_powder
    * cyan_dye
    * cyan_glazed_terracotta
    * cyan_stained_glass
    * cyan_stained_glass_pane
    * cyan_stained_glass_pane_from_glass_pane
    * cyan_terracotta
    * cyan_wool
    * dark_oak_boat
    * dark_oak_button
    * dark_oak_door
    * dark_oak_fence
    * dark_oak_fence_gate
    * dark_oak_planks
    * dark_oak_pressure_plate
    * dark_oak_sign
    * dark_oak_slab
    * dark_oak_stairs
    * dark_oak_trapdoor
    * dark_oak_wood
    * dark_prismarine
    * dark_prismarine_slab
    * dark_prismarine_slab_from_dark_prismarine_stonecutting
    * dark_prismarine_stairs
    * dark_prismarine_stairs_from_dark_prismarine_stonecutting
    * daylight_detector
    * detector_rail
    * diamond
    * diamond_axe
    * diamond_block
    * diamond_boots
    * diamond_chestplate
    * diamond_from_blasting
    * diamond_from_smelting
    * diamond_helmet
    * diamond_hoe
    * diamond_leggings
    * diamond_pickaxe
    * diamond_shovel
    * diamond_sword
    * diorite
    * diorite_slab
    * diorite_slab_from_diorite_stonecutting
    * diorite_stairs
    * diorite_stairs_from_diorite_stonecutting
    * diorite_wall
    * diorite_wall_from_diorite_stonecutting
    * dispenser
    * dried_kelp
    * dried_kelp_block
    * dried_kelp_from_campfire_cooking
    * dried_kelp_from_smelting
    * dried_kelp_from_smoking
    * dropper
    * emerald
    * emerald_block
    * emerald_from_blasting
    * emerald_from_smelting
    * enchanting_table
    * ender_chest
    * ender_eye
    * end_crystal
    * end_rod
    * end_stone_bricks
    * end_stone_bricks_from_end_stone_stonecutting
    * end_stone_brick_slab
    * end_stone_brick_slab_from_end_stone_brick_stonecutting
    * end_stone_brick_slab_from_end_stone_stonecutting
    * end_stone_brick_stairs
    * end_stone_brick_stairs_from_end_stone_brick_stonecutting
    * end_stone_brick_stairs_from_end_stone_stonecutting
    * end_stone_brick_wall
    * end_stone_brick_wall_from_end_stone_brick_stonecutting
    * end_stone_brick_wall_from_end_stone_stonecutting
    * fermented_spider_eye
    * firework_rocket
    * firework_star
    * firework_star_fade
    * fire_charge
    * fishing_rod
    * fletching_table
    * flint_and_steel
    * flower_banner_pattern
    * flower_pot
    * furnace
    * furnace_minecart
    * glass
    * glass_bottle
    * glass_pane
    * glistering_melon_slice
    * glowstone
    * golden_apple
    * golden_axe
    * golden_boots
    * golden_carrot
    * golden_chestplate
    * golden_helmet
    * golden_hoe
    * golden_leggings
    * golden_pickaxe
    * golden_shovel
    * golden_sword
    * gold_block
    * gold_ingot
    * gold_ingot_from_blasting
    * gold_ingot_from_gold_block
    * gold_ingot_from_nuggets
    * gold_nugget
    * gold_nugget_from_blasting
    * gold_nugget_from_smelting
    * granite
    * granite_slab
    * granite_slab_from_granite_stonecutting
    * granite_stairs
    * granite_stairs_from_granite_stonecutting
    * granite_wall
    * granite_wall_from_granite_stonecutting
    * gray_banner
    * gray_bed
    * gray_bed_from_white_bed
    * gray_carpet
    * gray_carpet_from_white_carpet
    * gray_concrete_powder
    * gray_dye
    * gray_glazed_terracotta
    * gray_stained_glass
    * gray_stained_glass_pane
    * gray_stained_glass_pane_from_glass_pane
    * gray_terracotta
    * gray_wool
    * green_banner
    * green_bed
    * green_bed_from_white_bed
    * green_carpet
    * green_carpet_from_white_carpet
    * green_concrete_powder
    * green_dye
    * green_glazed_terracotta
    * green_stained_glass
    * green_stained_glass_pane
    * green_stained_glass_pane_from_glass_pane
    * green_terracotta
    * green_wool
    * grindstone
    * hay_block
    * heavy_weighted_pressure_plate
    * honeycomb_block
    * honey_block
    * honey_bottle
    * hopper
    * hopper_minecart
    * iron_axe
    * iron_bars
    * iron_block
    * iron_boots
    * iron_chestplate
    * iron_door
    * iron_helmet
    * iron_hoe
    * iron_ingot
    * iron_ingot_from_blasting
    * iron_ingot_from_iron_block
    * iron_ingot_from_nuggets
    * iron_leggings
    * iron_nugget
    * iron_nugget_from_blasting
    * iron_nugget_from_smelting
    * iron_pickaxe
    * iron_shovel
    * iron_sword
    * iron_trapdoor
    * item_frame
    * jack_o_lantern
    * jukebox
    * jungle_boat
    * jungle_button
    * jungle_door
    * jungle_fence
    * jungle_fence_gate
    * jungle_planks
    * jungle_pressure_plate
    * jungle_sign
    * jungle_slab
    * jungle_stairs
    * jungle_trapdoor
    * jungle_wood
    * ladder
    * lantern
    * lapis_block
    * lapis_from_blasting
    * lapis_from_smelting
    * lapis_lazuli
    * lead
    * leather
    * leather_boots
    * leather_chestplate
    * leather_helmet
    * leather_horse_armor
    * leather_leggings
    * lectern
    * lever
    * light_blue_banner
    * light_blue_bed
    * light_blue_bed_from_white_bed
    * light_blue_carpet
    * light_blue_carpet_from_white_carpet
    * light_blue_concrete_powder
    * light_blue_dye_from_blue_orchid
    * light_blue_dye_from_blue_white_dye
    * light_blue_glazed_terracotta
    * light_blue_stained_glass
    * light_blue_stained_glass_pane
    * light_blue_stained_glass_pane_from_glass_pane
    * light_blue_terracotta
    * light_blue_wool
    * light_gray_banner
    * light_gray_bed
    * light_gray_bed_from_white_bed
    * light_gray_carpet
    * light_gray_carpet_from_white_carpet
    * light_gray_concrete_powder
    * light_gray_dye_from_azure_bluet
    * light_gray_dye_from_black_white_dye
    * light_gray_dye_from_gray_white_dye
    * light_gray_dye_from_oxeye_daisy
    * light_gray_dye_from_white_tulip
    * light_gray_glazed_terracotta
    * light_gray_stained_glass
    * light_gray_stained_glass_pane
    * light_gray_stained_glass_pane_from_glass_pane
    * light_gray_terracotta
    * light_gray_wool
    * light_weighted_pressure_plate
    * lime_banner
    * lime_bed
    * lime_bed_from_white_bed
    * lime_carpet
    * lime_carpet_from_white_carpet
    * lime_concrete_powder
    * lime_dye
    * lime_dye_from_smelting
    * lime_glazed_terracotta
    * lime_stained_glass
    * lime_stained_glass_pane
    * lime_stained_glass_pane_from_glass_pane
    * lime_terracotta
    * lime_wool
    * lodestone
    * loom
    * magenta_banner
    * magenta_bed
    * magenta_bed_from_white_bed
    * magenta_carpet
    * magenta_carpet_from_white_carpet
    * magenta_concrete_powder
    * magenta_dye_from_allium
    * magenta_dye_from_blue_red_pink
    * magenta_dye_from_blue_red_white_dye
    * magenta_dye_from_lilac
    * magenta_dye_from_purple_and_pink
    * magenta_glazed_terracotta
    * magenta_stained_glass
    * magenta_stained_glass_pane
    * magenta_stained_glass_pane_from_glass_pane
    * magenta_terracotta
    * magenta_wool
    * magma_block
    * magma_cream
    * map
    * map_cloning
    * map_extending
    * melon
    * melon_seeds
    * minecart
    * mojang_banner_pattern
    * mossy_cobblestone
    * mossy_cobblestone_slab
    * mossy_cobblestone_slab_from_mossy_cobblestone_stonecutting
    * mossy_cobblestone_stairs
    * mossy_cobblestone_stairs_from_mossy_cobblestone_stonecutting
    * mossy_cobblestone_wall
    * mossy_cobblestone_wall_from_mossy_cobblestone_stonecutting
    * mossy_stone_bricks
    * mossy_stone_brick_slab
    * mossy_stone_brick_slab_from_mossy_stone_brick_stonecutting
    * mossy_stone_brick_stairs
    * mossy_stone_brick_stairs_from_mossy_stone_brick_stonecutting
    * mossy_stone_brick_wall
    * mossy_stone_brick_wall_from_mossy_stone_brick_stonecutting
    * mushroom_stew
    * netherite_axe_smithing
    * netherite_block
    * netherite_boots_smithing
    * netherite_chestplate_smithing
    * netherite_helmet_smithing
    * netherite_hoe_smithing
    * netherite_ingot
    * netherite_ingot_from_netherite_block
    * netherite_leggings_smithing
    * netherite_pickaxe_smithing
    * netherite_scrap
    * netherite_scrap_from_blasting
    * netherite_shovel_smithing
    * netherite_sword_smithing
    * nether_brick
    * nether_bricks
    * nether_brick_fence
    * nether_brick_slab
    * nether_brick_slab_from_nether_bricks_stonecutting
    * nether_brick_stairs
    * nether_brick_stairs_from_nether_bricks_stonecutting
    * nether_brick_wall
    * nether_brick_wall_from_nether_bricks_stonecutting
    * nether_wart_block
    * note_block
    * oak_boat
    * oak_button
    * oak_door
    * oak_fence
    * oak_fence_gate
    * oak_planks
    * oak_pressure_plate
    * oak_sign
    * oak_slab
    * oak_stairs
    * oak_trapdoor
    * oak_wood
    * observer
    * orange_banner
    * orange_bed
    * orange_bed_from_white_bed
    * orange_carpet
    * orange_carpet_from_white_carpet
    * orange_concrete_powder
    * orange_dye_from_orange_tulip
    * orange_dye_from_red_yellow
    * orange_glazed_terracotta
    * orange_stained_glass
    * orange_stained_glass_pane
    * orange_stained_glass_pane_from_glass_pane
    * orange_terracotta
    * orange_wool
    * packed_ice
    * painting
    * paper
    * pink_banner
    * pink_bed
    * pink_bed_from_white_bed
    * pink_carpet
    * pink_carpet_from_white_carpet
    * pink_concrete_powder
    * pink_dye_from_peony
    * pink_dye_from_pink_tulip
    * pink_dye_from_red_white_dye
    * pink_glazed_terracotta
    * pink_stained_glass
    * pink_stained_glass_pane
    * pink_stained_glass_pane_from_glass_pane
    * pink_terracotta
    * pink_wool
    * piston
    * polished_andesite
    * polished_andesite_from_andesite_stonecutting
    * polished_andesite_slab
    * polished_andesite_slab_from_andesite_stonecutting
    * polished_andesite_slab_from_polished_andesite_stonecutting
    * polished_andesite_stairs
    * polished_andesite_stairs_from_andesite_stonecutting
    * polished_andesite_stairs_from_polished_andesite_stonecutting
    * polished_basalt
    * polished_basalt_from_basalt_stonecutting
    * polished_blackstone
    * polished_blackstone_bricks
    * polished_blackstone_bricks_from_blackstone_stonecutting
    * polished_blackstone_bricks_from_polished_blackstone_stonecutting
    * polished_blackstone_brick_slab
    * polished_blackstone_brick_slab_from_blackstone_stonecutting
    * polished_blackstone_brick_slab_from_polished_blackstone_bricks_stonecutting
    * polished_blackstone_brick_slab_from_polished_blackstone_stonecutting
    * polished_blackstone_brick_stairs
    * polished_blackstone_brick_stairs_from_blackstone_stonecutting
    * polished_blackstone_brick_stairs_from_polished_blackstone_bricks_stonecutting
    * polished_blackstone_brick_stairs_from_polished_blackstone_stonecutting
    * polished_blackstone_brick_wall
    * polished_blackstone_brick_wall_from_blackstone_stonecutting
    * polished_blackstone_brick_wall_from_polished_blackstone_bricks_stonecutting
    * polished_blackstone_brick_wall_from_polished_blackstone_stonecutting
    * polished_blackstone_button
    * polished_blackstone_from_blackstone_stonecutting
    * polished_blackstone_pressure_plate
    * polished_blackstone_slab
    * polished_blackstone_slab_from_blackstone_stonecutting
    * polished_blackstone_slab_from_polished_blackstone_stonecutting
    * polished_blackstone_stairs
    * polished_blackstone_stairs_from_blackstone_stonecutting
    * polished_blackstone_stairs_from_polished_blackstone_stonecutting
    * polished_blackstone_wall
    * polished_blackstone_wall_from_blackstone_stonecutting
    * polished_blackstone_wall_from_polished_blackstone_stonecutting
    * polished_diorite
    * polished_diorite_from_diorite_stonecutting
    * polished_diorite_slab
    * polished_diorite_slab_from_diorite_stonecutting
    * polished_diorite_slab_from_polished_diorite_stonecutting
    * polished_diorite_stairs
    * polished_diorite_stairs_from_diorite_stonecutting
    * polished_diorite_stairs_from_polished_diorite_stonecutting
    * polished_granite
    * polished_granite_from_granite_stonecutting
    * polished_granite_slab
    * polished_granite_slab_from_granite_stonecutting
    * polished_granite_slab_from_polished_granite_stonecutting
    * polished_granite_stairs
    * polished_granite_stairs_from_granite_stonecutting
    * polished_granite_stairs_from_polished_granite_stonecutting
    * popped_chorus_fruit
    * powered_rail
    * prismarine
    * prismarine_bricks
    * prismarine_brick_slab
    * prismarine_brick_slab_from_prismarine_stonecutting
    * prismarine_brick_stairs
    * prismarine_brick_stairs_from_prismarine_stonecutting
    * prismarine_slab
    * prismarine_slab_from_prismarine_stonecutting
    * prismarine_stairs
    * prismarine_stairs_from_prismarine_stonecutting
    * prismarine_wall
    * prismarine_wall_from_prismarine_stonecutting
    * pumpkin_pie
    * pumpkin_seeds
    * purple_banner
    * purple_bed
    * purple_bed_from_white_bed
    * purple_carpet
    * purple_carpet_from_white_carpet
    * purple_concrete_powder
    * purple_dye
    * purple_glazed_terracotta
    * purple_stained_glass
    * purple_stained_glass_pane
    * purple_stained_glass_pane_from_glass_pane
    * purple_terracotta
    * purple_wool
    * purpur_block
    * purpur_pillar
    * purpur_pillar_from_purpur_block_stonecutting
    * purpur_slab
    * purpur_slab_from_purpur_block_stonecutting
    * purpur_stairs
    * purpur_stairs_from_purpur_block_stonecutting
    * quartz
    * quartz_block
    * quartz_bricks
    * quartz_bricks_from_quartz_block_stonecutting
    * quartz_from_blasting
    * quartz_pillar
    * quartz_pillar_from_quartz_block_stonecutting
    * quartz_slab
    * quartz_slab_from_stonecutting
    * quartz_stairs
    * quartz_stairs_from_quartz_block_stonecutting
    * rabbit_stew_from_brown_mushroom
    * rabbit_stew_from_red_mushroom
    * rail
    * redstone
    * redstone_block
    * redstone_from_blasting
    * redstone_from_smelting
    * redstone_lamp
    * redstone_torch
    * red_banner
    * red_bed
    * red_bed_from_white_bed
    * red_carpet
    * red_carpet_from_white_carpet
    * red_concrete_powder
    * red_dye_from_beetroot
    * red_dye_from_poppy
    * red_dye_from_rose_bush
    * red_dye_from_tulip
    * red_glazed_terracotta
    * red_nether_bricks
    * red_nether_brick_slab
    * red_nether_brick_slab_from_red_nether_bricks_stonecutting
    * red_nether_brick_stairs
    * red_nether_brick_stairs_from_red_nether_bricks_stonecutting
    * red_nether_brick_wall
    * red_nether_brick_wall_from_red_nether_bricks_stonecutting
    * red_sandstone
    * red_sandstone_slab
    * red_sandstone_slab_from_red_sandstone_stonecutting
    * red_sandstone_stairs
    * red_sandstone_stairs_from_red_sandstone_stonecutting
    * red_sandstone_wall
    * red_sandstone_wall_from_red_sandstone_stonecutting
    * red_stained_glass
    * red_stained_glass_pane
    * red_stained_glass_pane_from_glass_pane
    * red_terracotta
    * red_wool
    * repair_item
    * repeater
    * respawn_anchor
    * sandstone
    * sandstone_slab
    * sandstone_slab_from_sandstone_stonecutting
    * sandstone_stairs
    * sandstone_stairs_from_sandstone_stonecutting
    * sandstone_wall
    * sandstone_wall_from_sandstone_stonecutting
    * scaffolding
    * sea_lantern
    * shears
    * shield
    * shield_decoration
    * shulker_box
    * shulker_box_coloring
    * skull_banner_pattern
    * slime_ball
    * slime_block
    * smithing_table
    * smoker
    * smooth_quartz
    * smooth_quartz_slab
    * smooth_quartz_slab_from_smooth_quartz_stonecutting
    * smooth_quartz_stairs
    * smooth_quartz_stairs_from_smooth_quartz_stonecutting
    * smooth_red_sandstone
    * smooth_red_sandstone_slab
    * smooth_red_sandstone_slab_from_smooth_red_sandstone_stonecutting
    * smooth_red_sandstone_stairs
    * smooth_red_sandstone_stairs_from_smooth_red_sandstone_stonecutting
    * smooth_sandstone
    * smooth_sandstone_slab
    * smooth_sandstone_slab_from_smooth_sandstone_stonecutting
    * smooth_sandstone_stairs
    * smooth_sandstone_stairs_from_smooth_sandstone_stonecutting
    * smooth_stone
    * smooth_stone_slab
    * smooth_stone_slab_from_smooth_stone_stonecutting
    * snow
    * snow_block
    * soul_campfire
    * soul_lantern
    * soul_torch
    * spectral_arrow
    * sponge
    * spruce_boat
    * spruce_button
    * spruce_door
    * spruce_fence
    * spruce_fence_gate
    * spruce_planks
    * spruce_pressure_plate
    * spruce_sign
    * spruce_slab
    * spruce_stairs
    * spruce_trapdoor
    * spruce_wood
    * stick
    * sticky_piston
    * stick_from_bamboo_item
    * stone
    * stonecutter
    * stone_axe
    * stone_bricks
    * stone_bricks_from_stone_stonecutting
    * stone_brick_slab
    * stone_brick_slab_from_stone_bricks_stonecutting
    * stone_brick_slab_from_stone_stonecutting
    * stone_brick_stairs
    * stone_brick_stairs_from_stone_bricks_stonecutting
    * stone_brick_stairs_from_stone_stonecutting
    * stone_brick_wall
    * stone_brick_walls_from_stone_stonecutting
    * stone_brick_wall_from_stone_bricks_stonecutting
    * stone_button
    * stone_hoe
    * stone_pickaxe
    * stone_pressure_plate
    * stone_shovel
    * stone_slab
    * stone_slab_from_stone_stonecutting
    * stone_stairs
    * stone_stairs_from_stone_stonecutting
    * stone_sword
    * stripped_acacia_wood
    * stripped_birch_wood
    * stripped_crimson_hyphae
    * stripped_dark_oak_wood
    * stripped_jungle_wood
    * stripped_oak_wood
    * stripped_spruce_wood
    * stripped_warped_hyphae
    * sugar_from_honey_bottle
    * sugar_from_sugar_cane
    * suspicious_stew
    * target
    * terracotta
    * tipped_arrow
    * tnt
    * tnt_minecart
    * torch
    * trapped_chest
    * tripwire_hook
    * turtle_helmet
    * warped_button
    * warped_door
    * warped_fence
    * warped_fence_gate
    * warped_fungus_on_a_stick
    * warped_hyphae
    * warped_planks
    * warped_pressure_plate
    * warped_sign
    * warped_slab
    * warped_stairs
    * warped_trapdoor
    * wheat
    * white_banner
    * white_bed
    * white_carpet
    * white_concrete_powder
    * white_dye
    * white_dye_from_lily_of_the_valley
    * white_glazed_terracotta
    * white_stained_glass
    * white_stained_glass_pane
    * white_stained_glass_pane_from_glass_pane
    * white_terracotta
    * white_wool_from_string
    * wooden_axe
    * wooden_hoe
    * wooden_pickaxe
    * wooden_shovel
    * wooden_sword
    * writable_book
    * yellow_banner
    * yellow_bed
    * yellow_bed_from_white_bed
    * yellow_carpet
    * yellow_carpet_from_white_carpet
    * yellow_concrete_powder
    * yellow_dye_from_dandelion
    * yellow_dye_from_sunflower
    * yellow_glazed_terracotta
    * yellow_stained_glass
    * yellow_stained_glass_pane
    * yellow_stained_glass_pane_from_glass_pane
    * yellow_terracotta
    * yellow_wool
    """
    acacia_boat = "minecraft:acacia_boat"
    acacia_button = "minecraft:acacia_button"
    acacia_door = "minecraft:acacia_door"
    acacia_fence = "minecraft:acacia_fence"
    acacia_fence_gate = "minecraft:acacia_fence_gate"
    acacia_planks = "minecraft:acacia_planks"
    acacia_pressure_plate = "minecraft:acacia_pressure_plate"
    acacia_sign = "minecraft:acacia_sign"
    acacia_slab = "minecraft:acacia_slab"
    acacia_stairs = "minecraft:acacia_stairs"
    acacia_trapdoor = "minecraft:acacia_trapdoor"
    acacia_wood = "minecraft:acacia_wood"
    activator_rail = "minecraft:activator_rail"
    andesite = "minecraft:andesite"
    andesite_slab = "minecraft:andesite_slab"
    andesite_slab_from_andesite_stonecutting = "minecraft:andesite_slab_from_andesite_stonecutting"
    andesite_stairs = "minecraft:andesite_stairs"
    andesite_stairs_from_andesite_stonecutting = "minecraft:andesite_stairs_from_andesite_stonecutting"
    andesite_wall = "minecraft:andesite_wall"
    andesite_wall_from_andesite_stonecutting = "minecraft:andesite_wall_from_andesite_stonecutting"
    anvil = "minecraft:anvil"
    armor_dye = "minecraft:armor_dye"
    armor_stand = "minecraft:armor_stand"
    arrow = "minecraft:arrow"
    baked_potato = "minecraft:baked_potato"
    baked_potato_from_campfire_cooking = "minecraft:baked_potato_from_campfire_cooking"
    baked_potato_from_smoking = "minecraft:baked_potato_from_smoking"
    banner_duplicate = "minecraft:banner_duplicate"
    barrel = "minecraft:barrel"
    beacon = "minecraft:beacon"
    beehive = "minecraft:beehive"
    beetroot_soup = "minecraft:beetroot_soup"
    birch_boat = "minecraft:birch_boat"
    birch_button = "minecraft:birch_button"
    birch_door = "minecraft:birch_door"
    birch_fence = "minecraft:birch_fence"
    birch_fence_gate = "minecraft:birch_fence_gate"
    birch_planks = "minecraft:birch_planks"
    birch_pressure_plate = "minecraft:birch_pressure_plate"
    birch_sign = "minecraft:birch_sign"
    birch_slab = "minecraft:birch_slab"
    birch_stairs = "minecraft:birch_stairs"
    birch_trapdoor = "minecraft:birch_trapdoor"
    birch_wood = "minecraft:birch_wood"
    blackstone_slab = "minecraft:blackstone_slab"
    blackstone_slab_from_blackstone_stonecutting = "minecraft:blackstone_slab_from_blackstone_stonecutting"
    blackstone_stairs = "minecraft:blackstone_stairs"
    blackstone_stairs_from_blackstone_stonecutting = "minecraft:blackstone_stairs_from_blackstone_stonecutting"
    blackstone_wall = "minecraft:blackstone_wall"
    blackstone_wall_from_blackstone_stonecutting = "minecraft:blackstone_wall_from_blackstone_stonecutting"
    black_banner = "minecraft:black_banner"
    black_bed = "minecraft:black_bed"
    black_bed_from_white_bed = "minecraft:black_bed_from_white_bed"
    black_carpet = "minecraft:black_carpet"
    black_carpet_from_white_carpet = "minecraft:black_carpet_from_white_carpet"
    black_concrete_powder = "minecraft:black_concrete_powder"
    black_dye = "minecraft:black_dye"
    black_dye_from_wither_rose = "minecraft:black_dye_from_wither_rose"
    black_glazed_terracotta = "minecraft:black_glazed_terracotta"
    black_stained_glass = "minecraft:black_stained_glass"
    black_stained_glass_pane = "minecraft:black_stained_glass_pane"
    black_stained_glass_pane_from_glass_pane = "minecraft:black_stained_glass_pane_from_glass_pane"
    black_terracotta = "minecraft:black_terracotta"
    black_wool = "minecraft:black_wool"
    blast_furnace = "minecraft:blast_furnace"
    blaze_powder = "minecraft:blaze_powder"
    blue_banner = "minecraft:blue_banner"
    blue_bed = "minecraft:blue_bed"
    blue_bed_from_white_bed = "minecraft:blue_bed_from_white_bed"
    blue_carpet = "minecraft:blue_carpet"
    blue_carpet_from_white_carpet = "minecraft:blue_carpet_from_white_carpet"
    blue_concrete_powder = "minecraft:blue_concrete_powder"
    blue_dye = "minecraft:blue_dye"
    blue_dye_from_cornflower = "minecraft:blue_dye_from_cornflower"
    blue_glazed_terracotta = "minecraft:blue_glazed_terracotta"
    blue_ice = "minecraft:blue_ice"
    blue_stained_glass = "minecraft:blue_stained_glass"
    blue_stained_glass_pane = "minecraft:blue_stained_glass_pane"
    blue_stained_glass_pane_from_glass_pane = "minecraft:blue_stained_glass_pane_from_glass_pane"
    blue_terracotta = "minecraft:blue_terracotta"
    blue_wool = "minecraft:blue_wool"
    bone_block = "minecraft:bone_block"
    bone_meal = "minecraft:bone_meal"
    bone_meal_from_bone_block = "minecraft:bone_meal_from_bone_block"
    book = "minecraft:book"
    bookshelf = "minecraft:bookshelf"
    book_cloning = "minecraft:book_cloning"
    bow = "minecraft:bow"
    bowl = "minecraft:bowl"
    bread = "minecraft:bread"
    brewing_stand = "minecraft:brewing_stand"
    brick = "minecraft:brick"
    bricks = "minecraft:bricks"
    brick_slab = "minecraft:brick_slab"
    brick_slab_from_bricks_stonecutting = "minecraft:brick_slab_from_bricks_stonecutting"
    brick_stairs = "minecraft:brick_stairs"
    brick_stairs_from_bricks_stonecutting = "minecraft:brick_stairs_from_bricks_stonecutting"
    brick_wall = "minecraft:brick_wall"
    brick_wall_from_bricks_stonecutting = "minecraft:brick_wall_from_bricks_stonecutting"
    brown_banner = "minecraft:brown_banner"
    brown_bed = "minecraft:brown_bed"
    brown_bed_from_white_bed = "minecraft:brown_bed_from_white_bed"
    brown_carpet = "minecraft:brown_carpet"
    brown_carpet_from_white_carpet = "minecraft:brown_carpet_from_white_carpet"
    brown_concrete_powder = "minecraft:brown_concrete_powder"
    brown_dye = "minecraft:brown_dye"
    brown_glazed_terracotta = "minecraft:brown_glazed_terracotta"
    brown_stained_glass = "minecraft:brown_stained_glass"
    brown_stained_glass_pane = "minecraft:brown_stained_glass_pane"
    brown_stained_glass_pane_from_glass_pane = "minecraft:brown_stained_glass_pane_from_glass_pane"
    brown_terracotta = "minecraft:brown_terracotta"
    brown_wool = "minecraft:brown_wool"
    bucket = "minecraft:bucket"
    cake = "minecraft:cake"
    campfire = "minecraft:campfire"
    carrot_on_a_stick = "minecraft:carrot_on_a_stick"
    cartography_table = "minecraft:cartography_table"
    cauldron = "minecraft:cauldron"
    chain = "minecraft:chain"
    charcoal = "minecraft:charcoal"
    chest = "minecraft:chest"
    chest_minecart = "minecraft:chest_minecart"
    chiseled_nether_bricks = "minecraft:chiseled_nether_bricks"
    chiseled_nether_bricks_from_nether_bricks_stonecutting = "minecraft:chiseled_nether_bricks_from_nether_bricks_stonecutting"
    chiseled_polished_blackstone = "minecraft:chiseled_polished_blackstone"
    chiseled_polished_blackstone_from_blackstone_stonecutting = "minecraft:chiseled_polished_blackstone_from_blackstone_stonecutting"
    chiseled_polished_blackstone_from_polished_blackstone_stonecutting = "minecraft:chiseled_polished_blackstone_from_polished_blackstone_stonecutting"
    chiseled_quartz_block = "minecraft:chiseled_quartz_block"
    chiseled_quartz_block_from_quartz_block_stonecutting = "minecraft:chiseled_quartz_block_from_quartz_block_stonecutting"
    chiseled_red_sandstone = "minecraft:chiseled_red_sandstone"
    chiseled_red_sandstone_from_red_sandstone_stonecutting = "minecraft:chiseled_red_sandstone_from_red_sandstone_stonecutting"
    chiseled_sandstone = "minecraft:chiseled_sandstone"
    chiseled_sandstone_from_sandstone_stonecutting = "minecraft:chiseled_sandstone_from_sandstone_stonecutting"
    chiseled_stone_bricks = "minecraft:chiseled_stone_bricks"
    chiseled_stone_bricks_from_stone_bricks_stonecutting = "minecraft:chiseled_stone_bricks_from_stone_bricks_stonecutting"
    chiseled_stone_bricks_stone_from_stonecutting = "minecraft:chiseled_stone_bricks_stone_from_stonecutting"
    clay = "minecraft:clay"
    clock = "minecraft:clock"
    coal = "minecraft:coal"
    coal_block = "minecraft:coal_block"
    coal_from_blasting = "minecraft:coal_from_blasting"
    coal_from_smelting = "minecraft:coal_from_smelting"
    coarse_dirt = "minecraft:coarse_dirt"
    cobblestone_slab = "minecraft:cobblestone_slab"
    cobblestone_slab_from_cobblestone_stonecutting = "minecraft:cobblestone_slab_from_cobblestone_stonecutting"
    cobblestone_stairs = "minecraft:cobblestone_stairs"
    cobblestone_stairs_from_cobblestone_stonecutting = "minecraft:cobblestone_stairs_from_cobblestone_stonecutting"
    cobblestone_wall = "minecraft:cobblestone_wall"
    cobblestone_wall_from_cobblestone_stonecutting = "minecraft:cobblestone_wall_from_cobblestone_stonecutting"
    comparator = "minecraft:comparator"
    compass = "minecraft:compass"
    composter = "minecraft:composter"
    conduit = "minecraft:conduit"
    cooked_beef = "minecraft:cooked_beef"
    cooked_beef_from_campfire_cooking = "minecraft:cooked_beef_from_campfire_cooking"
    cooked_beef_from_smoking = "minecraft:cooked_beef_from_smoking"
    cooked_chicken = "minecraft:cooked_chicken"
    cooked_chicken_from_campfire_cooking = "minecraft:cooked_chicken_from_campfire_cooking"
    cooked_chicken_from_smoking = "minecraft:cooked_chicken_from_smoking"
    cooked_cod = "minecraft:cooked_cod"
    cooked_cod_from_campfire_cooking = "minecraft:cooked_cod_from_campfire_cooking"
    cooked_cod_from_smoking = "minecraft:cooked_cod_from_smoking"
    cooked_mutton = "minecraft:cooked_mutton"
    cooked_mutton_from_campfire_cooking = "minecraft:cooked_mutton_from_campfire_cooking"
    cooked_mutton_from_smoking = "minecraft:cooked_mutton_from_smoking"
    cooked_porkchop = "minecraft:cooked_porkchop"
    cooked_porkchop_from_campfire_cooking = "minecraft:cooked_porkchop_from_campfire_cooking"
    cooked_porkchop_from_smoking = "minecraft:cooked_porkchop_from_smoking"
    cooked_rabbit = "minecraft:cooked_rabbit"
    cooked_rabbit_from_campfire_cooking = "minecraft:cooked_rabbit_from_campfire_cooking"
    cooked_rabbit_from_smoking = "minecraft:cooked_rabbit_from_smoking"
    cooked_salmon = "minecraft:cooked_salmon"
    cooked_salmon_from_campfire_cooking = "minecraft:cooked_salmon_from_campfire_cooking"
    cooked_salmon_from_smoking = "minecraft:cooked_salmon_from_smoking"
    cookie = "minecraft:cookie"
    cracked_nether_bricks = "minecraft:cracked_nether_bricks"
    cracked_polished_blackstone_bricks = "minecraft:cracked_polished_blackstone_bricks"
    cracked_stone_bricks = "minecraft:cracked_stone_bricks"
    crafting_table = "minecraft:crafting_table"
    creeper_banner_pattern = "minecraft:creeper_banner_pattern"
    crimson_button = "minecraft:crimson_button"
    crimson_door = "minecraft:crimson_door"
    crimson_fence = "minecraft:crimson_fence"
    crimson_fence_gate = "minecraft:crimson_fence_gate"
    crimson_hyphae = "minecraft:crimson_hyphae"
    crimson_planks = "minecraft:crimson_planks"
    crimson_pressure_plate = "minecraft:crimson_pressure_plate"
    crimson_sign = "minecraft:crimson_sign"
    crimson_slab = "minecraft:crimson_slab"
    crimson_stairs = "minecraft:crimson_stairs"
    crimson_trapdoor = "minecraft:crimson_trapdoor"
    crossbow = "minecraft:crossbow"
    cut_red_sandstone = "minecraft:cut_red_sandstone"
    cut_red_sandstone_from_red_sandstone_stonecutting = "minecraft:cut_red_sandstone_from_red_sandstone_stonecutting"
    cut_red_sandstone_slab = "minecraft:cut_red_sandstone_slab"
    cut_red_sandstone_slab_from_cut_red_sandstone_stonecutting = "minecraft:cut_red_sandstone_slab_from_cut_red_sandstone_stonecutting"
    cut_red_sandstone_slab_from_red_sandstone_stonecutting = "minecraft:cut_red_sandstone_slab_from_red_sandstone_stonecutting"
    cut_sandstone = "minecraft:cut_sandstone"
    cut_sandstone_from_sandstone_stonecutting = "minecraft:cut_sandstone_from_sandstone_stonecutting"
    cut_sandstone_slab = "minecraft:cut_sandstone_slab"
    cut_sandstone_slab_from_cut_sandstone_stonecutting = "minecraft:cut_sandstone_slab_from_cut_sandstone_stonecutting"
    cut_sandstone_slab_from_sandstone_stonecutting = "minecraft:cut_sandstone_slab_from_sandstone_stonecutting"
    cyan_banner = "minecraft:cyan_banner"
    cyan_bed = "minecraft:cyan_bed"
    cyan_bed_from_white_bed = "minecraft:cyan_bed_from_white_bed"
    cyan_carpet = "minecraft:cyan_carpet"
    cyan_carpet_from_white_carpet = "minecraft:cyan_carpet_from_white_carpet"
    cyan_concrete_powder = "minecraft:cyan_concrete_powder"
    cyan_dye = "minecraft:cyan_dye"
    cyan_glazed_terracotta = "minecraft:cyan_glazed_terracotta"
    cyan_stained_glass = "minecraft:cyan_stained_glass"
    cyan_stained_glass_pane = "minecraft:cyan_stained_glass_pane"
    cyan_stained_glass_pane_from_glass_pane = "minecraft:cyan_stained_glass_pane_from_glass_pane"
    cyan_terracotta = "minecraft:cyan_terracotta"
    cyan_wool = "minecraft:cyan_wool"
    dark_oak_boat = "minecraft:dark_oak_boat"
    dark_oak_button = "minecraft:dark_oak_button"
    dark_oak_door = "minecraft:dark_oak_door"
    dark_oak_fence = "minecraft:dark_oak_fence"
    dark_oak_fence_gate = "minecraft:dark_oak_fence_gate"
    dark_oak_planks = "minecraft:dark_oak_planks"
    dark_oak_pressure_plate = "minecraft:dark_oak_pressure_plate"
    dark_oak_sign = "minecraft:dark_oak_sign"
    dark_oak_slab = "minecraft:dark_oak_slab"
    dark_oak_stairs = "minecraft:dark_oak_stairs"
    dark_oak_trapdoor = "minecraft:dark_oak_trapdoor"
    dark_oak_wood = "minecraft:dark_oak_wood"
    dark_prismarine = "minecraft:dark_prismarine"
    dark_prismarine_slab = "minecraft:dark_prismarine_slab"
    dark_prismarine_slab_from_dark_prismarine_stonecutting = "minecraft:dark_prismarine_slab_from_dark_prismarine_stonecutting"
    dark_prismarine_stairs = "minecraft:dark_prismarine_stairs"
    dark_prismarine_stairs_from_dark_prismarine_stonecutting = "minecraft:dark_prismarine_stairs_from_dark_prismarine_stonecutting"
    daylight_detector = "minecraft:daylight_detector"
    detector_rail = "minecraft:detector_rail"
    diamond = "minecraft:diamond"
    diamond_axe = "minecraft:diamond_axe"
    diamond_block = "minecraft:diamond_block"
    diamond_boots = "minecraft:diamond_boots"
    diamond_chestplate = "minecraft:diamond_chestplate"
    diamond_from_blasting = "minecraft:diamond_from_blasting"
    diamond_from_smelting = "minecraft:diamond_from_smelting"
    diamond_helmet = "minecraft:diamond_helmet"
    diamond_hoe = "minecraft:diamond_hoe"
    diamond_leggings = "minecraft:diamond_leggings"
    diamond_pickaxe = "minecraft:diamond_pickaxe"
    diamond_shovel = "minecraft:diamond_shovel"
    diamond_sword = "minecraft:diamond_sword"
    diorite = "minecraft:diorite"
    diorite_slab = "minecraft:diorite_slab"
    diorite_slab_from_diorite_stonecutting = "minecraft:diorite_slab_from_diorite_stonecutting"
    diorite_stairs = "minecraft:diorite_stairs"
    diorite_stairs_from_diorite_stonecutting = "minecraft:diorite_stairs_from_diorite_stonecutting"
    diorite_wall = "minecraft:diorite_wall"
    diorite_wall_from_diorite_stonecutting = "minecraft:diorite_wall_from_diorite_stonecutting"
    dispenser = "minecraft:dispenser"
    dried_kelp = "minecraft:dried_kelp"
    dried_kelp_block = "minecraft:dried_kelp_block"
    dried_kelp_from_campfire_cooking = "minecraft:dried_kelp_from_campfire_cooking"
    dried_kelp_from_smelting = "minecraft:dried_kelp_from_smelting"
    dried_kelp_from_smoking = "minecraft:dried_kelp_from_smoking"
    dropper = "minecraft:dropper"
    emerald = "minecraft:emerald"
    emerald_block = "minecraft:emerald_block"
    emerald_from_blasting = "minecraft:emerald_from_blasting"
    emerald_from_smelting = "minecraft:emerald_from_smelting"
    enchanting_table = "minecraft:enchanting_table"
    ender_chest = "minecraft:ender_chest"
    ender_eye = "minecraft:ender_eye"
    end_crystal = "minecraft:end_crystal"
    end_rod = "minecraft:end_rod"
    end_stone_bricks = "minecraft:end_stone_bricks"
    end_stone_bricks_from_end_stone_stonecutting = "minecraft:end_stone_bricks_from_end_stone_stonecutting"
    end_stone_brick_slab = "minecraft:end_stone_brick_slab"
    end_stone_brick_slab_from_end_stone_brick_stonecutting = "minecraft:end_stone_brick_slab_from_end_stone_brick_stonecutting"
    end_stone_brick_slab_from_end_stone_stonecutting = "minecraft:end_stone_brick_slab_from_end_stone_stonecutting"
    end_stone_brick_stairs = "minecraft:end_stone_brick_stairs"
    end_stone_brick_stairs_from_end_stone_brick_stonecutting = "minecraft:end_stone_brick_stairs_from_end_stone_brick_stonecutting"
    end_stone_brick_stairs_from_end_stone_stonecutting = "minecraft:end_stone_brick_stairs_from_end_stone_stonecutting"
    end_stone_brick_wall = "minecraft:end_stone_brick_wall"
    end_stone_brick_wall_from_end_stone_brick_stonecutting = "minecraft:end_stone_brick_wall_from_end_stone_brick_stonecutting"
    end_stone_brick_wall_from_end_stone_stonecutting = "minecraft:end_stone_brick_wall_from_end_stone_stonecutting"
    fermented_spider_eye = "minecraft:fermented_spider_eye"
    firework_rocket = "minecraft:firework_rocket"
    firework_star = "minecraft:firework_star"
    firework_star_fade = "minecraft:firework_star_fade"
    fire_charge = "minecraft:fire_charge"
    fishing_rod = "minecraft:fishing_rod"
    fletching_table = "minecraft:fletching_table"
    flint_and_steel = "minecraft:flint_and_steel"
    flower_banner_pattern = "minecraft:flower_banner_pattern"
    flower_pot = "minecraft:flower_pot"
    furnace = "minecraft:furnace"
    furnace_minecart = "minecraft:furnace_minecart"
    glass = "minecraft:glass"
    glass_bottle = "minecraft:glass_bottle"
    glass_pane = "minecraft:glass_pane"
    glistering_melon_slice = "minecraft:glistering_melon_slice"
    glowstone = "minecraft:glowstone"
    golden_apple = "minecraft:golden_apple"
    golden_axe = "minecraft:golden_axe"
    golden_boots = "minecraft:golden_boots"
    golden_carrot = "minecraft:golden_carrot"
    golden_chestplate = "minecraft:golden_chestplate"
    golden_helmet = "minecraft:golden_helmet"
    golden_hoe = "minecraft:golden_hoe"
    golden_leggings = "minecraft:golden_leggings"
    golden_pickaxe = "minecraft:golden_pickaxe"
    golden_shovel = "minecraft:golden_shovel"
    golden_sword = "minecraft:golden_sword"
    gold_block = "minecraft:gold_block"
    gold_ingot = "minecraft:gold_ingot"
    gold_ingot_from_blasting = "minecraft:gold_ingot_from_blasting"
    gold_ingot_from_gold_block = "minecraft:gold_ingot_from_gold_block"
    gold_ingot_from_nuggets = "minecraft:gold_ingot_from_nuggets"
    gold_nugget = "minecraft:gold_nugget"
    gold_nugget_from_blasting = "minecraft:gold_nugget_from_blasting"
    gold_nugget_from_smelting = "minecraft:gold_nugget_from_smelting"
    granite = "minecraft:granite"
    granite_slab = "minecraft:granite_slab"
    granite_slab_from_granite_stonecutting = "minecraft:granite_slab_from_granite_stonecutting"
    granite_stairs = "minecraft:granite_stairs"
    granite_stairs_from_granite_stonecutting = "minecraft:granite_stairs_from_granite_stonecutting"
    granite_wall = "minecraft:granite_wall"
    granite_wall_from_granite_stonecutting = "minecraft:granite_wall_from_granite_stonecutting"
    gray_banner = "minecraft:gray_banner"
    gray_bed = "minecraft:gray_bed"
    gray_bed_from_white_bed = "minecraft:gray_bed_from_white_bed"
    gray_carpet = "minecraft:gray_carpet"
    gray_carpet_from_white_carpet = "minecraft:gray_carpet_from_white_carpet"
    gray_concrete_powder = "minecraft:gray_concrete_powder"
    gray_dye = "minecraft:gray_dye"
    gray_glazed_terracotta = "minecraft:gray_glazed_terracotta"
    gray_stained_glass = "minecraft:gray_stained_glass"
    gray_stained_glass_pane = "minecraft:gray_stained_glass_pane"
    gray_stained_glass_pane_from_glass_pane = "minecraft:gray_stained_glass_pane_from_glass_pane"
    gray_terracotta = "minecraft:gray_terracotta"
    gray_wool = "minecraft:gray_wool"
    green_banner = "minecraft:green_banner"
    green_bed = "minecraft:green_bed"
    green_bed_from_white_bed = "minecraft:green_bed_from_white_bed"
    green_carpet = "minecraft:green_carpet"
    green_carpet_from_white_carpet = "minecraft:green_carpet_from_white_carpet"
    green_concrete_powder = "minecraft:green_concrete_powder"
    green_dye = "minecraft:green_dye"
    green_glazed_terracotta = "minecraft:green_glazed_terracotta"
    green_stained_glass = "minecraft:green_stained_glass"
    green_stained_glass_pane = "minecraft:green_stained_glass_pane"
    green_stained_glass_pane_from_glass_pane = "minecraft:green_stained_glass_pane_from_glass_pane"
    green_terracotta = "minecraft:green_terracotta"
    green_wool = "minecraft:green_wool"
    grindstone = "minecraft:grindstone"
    hay_block = "minecraft:hay_block"
    heavy_weighted_pressure_plate = "minecraft:heavy_weighted_pressure_plate"
    honeycomb_block = "minecraft:honeycomb_block"
    honey_block = "minecraft:honey_block"
    honey_bottle = "minecraft:honey_bottle"
    hopper = "minecraft:hopper"
    hopper_minecart = "minecraft:hopper_minecart"
    iron_axe = "minecraft:iron_axe"
    iron_bars = "minecraft:iron_bars"
    iron_block = "minecraft:iron_block"
    iron_boots = "minecraft:iron_boots"
    iron_chestplate = "minecraft:iron_chestplate"
    iron_door = "minecraft:iron_door"
    iron_helmet = "minecraft:iron_helmet"
    iron_hoe = "minecraft:iron_hoe"
    iron_ingot = "minecraft:iron_ingot"
    iron_ingot_from_blasting = "minecraft:iron_ingot_from_blasting"
    iron_ingot_from_iron_block = "minecraft:iron_ingot_from_iron_block"
    iron_ingot_from_nuggets = "minecraft:iron_ingot_from_nuggets"
    iron_leggings = "minecraft:iron_leggings"
    iron_nugget = "minecraft:iron_nugget"
    iron_nugget_from_blasting = "minecraft:iron_nugget_from_blasting"
    iron_nugget_from_smelting = "minecraft:iron_nugget_from_smelting"
    iron_pickaxe = "minecraft:iron_pickaxe"
    iron_shovel = "minecraft:iron_shovel"
    iron_sword = "minecraft:iron_sword"
    iron_trapdoor = "minecraft:iron_trapdoor"
    item_frame = "minecraft:item_frame"
    jack_o_lantern = "minecraft:jack_o_lantern"
    jukebox = "minecraft:jukebox"
    jungle_boat = "minecraft:jungle_boat"
    jungle_button = "minecraft:jungle_button"
    jungle_door = "minecraft:jungle_door"
    jungle_fence = "minecraft:jungle_fence"
    jungle_fence_gate = "minecraft:jungle_fence_gate"
    jungle_planks = "minecraft:jungle_planks"
    jungle_pressure_plate = "minecraft:jungle_pressure_plate"
    jungle_sign = "minecraft:jungle_sign"
    jungle_slab = "minecraft:jungle_slab"
    jungle_stairs = "minecraft:jungle_stairs"
    jungle_trapdoor = "minecraft:jungle_trapdoor"
    jungle_wood = "minecraft:jungle_wood"
    ladder = "minecraft:ladder"
    lantern = "minecraft:lantern"
    lapis_block = "minecraft:lapis_block"
    lapis_from_blasting = "minecraft:lapis_from_blasting"
    lapis_from_smelting = "minecraft:lapis_from_smelting"
    lapis_lazuli = "minecraft:lapis_lazuli"
    lead = "minecraft:lead"
    leather = "minecraft:leather"
    leather_boots = "minecraft:leather_boots"
    leather_chestplate = "minecraft:leather_chestplate"
    leather_helmet = "minecraft:leather_helmet"
    leather_horse_armor = "minecraft:leather_horse_armor"
    leather_leggings = "minecraft:leather_leggings"
    lectern = "minecraft:lectern"
    lever = "minecraft:lever"
    light_blue_banner = "minecraft:light_blue_banner"
    light_blue_bed = "minecraft:light_blue_bed"
    light_blue_bed_from_white_bed = "minecraft:light_blue_bed_from_white_bed"
    light_blue_carpet = "minecraft:light_blue_carpet"
    light_blue_carpet_from_white_carpet = "minecraft:light_blue_carpet_from_white_carpet"
    light_blue_concrete_powder = "minecraft:light_blue_concrete_powder"
    light_blue_dye_from_blue_orchid = "minecraft:light_blue_dye_from_blue_orchid"
    light_blue_dye_from_blue_white_dye = "minecraft:light_blue_dye_from_blue_white_dye"
    light_blue_glazed_terracotta = "minecraft:light_blue_glazed_terracotta"
    light_blue_stained_glass = "minecraft:light_blue_stained_glass"
    light_blue_stained_glass_pane = "minecraft:light_blue_stained_glass_pane"
    light_blue_stained_glass_pane_from_glass_pane = "minecraft:light_blue_stained_glass_pane_from_glass_pane"
    light_blue_terracotta = "minecraft:light_blue_terracotta"
    light_blue_wool = "minecraft:light_blue_wool"
    light_gray_banner = "minecraft:light_gray_banner"
    light_gray_bed = "minecraft:light_gray_bed"
    light_gray_bed_from_white_bed = "minecraft:light_gray_bed_from_white_bed"
    light_gray_carpet = "minecraft:light_gray_carpet"
    light_gray_carpet_from_white_carpet = "minecraft:light_gray_carpet_from_white_carpet"
    light_gray_concrete_powder = "minecraft:light_gray_concrete_powder"
    light_gray_dye_from_azure_bluet = "minecraft:light_gray_dye_from_azure_bluet"
    light_gray_dye_from_black_white_dye = "minecraft:light_gray_dye_from_black_white_dye"
    light_gray_dye_from_gray_white_dye = "minecraft:light_gray_dye_from_gray_white_dye"
    light_gray_dye_from_oxeye_daisy = "minecraft:light_gray_dye_from_oxeye_daisy"
    light_gray_dye_from_white_tulip = "minecraft:light_gray_dye_from_white_tulip"
    light_gray_glazed_terracotta = "minecraft:light_gray_glazed_terracotta"
    light_gray_stained_glass = "minecraft:light_gray_stained_glass"
    light_gray_stained_glass_pane = "minecraft:light_gray_stained_glass_pane"
    light_gray_stained_glass_pane_from_glass_pane = "minecraft:light_gray_stained_glass_pane_from_glass_pane"
    light_gray_terracotta = "minecraft:light_gray_terracotta"
    light_gray_wool = "minecraft:light_gray_wool"
    light_weighted_pressure_plate = "minecraft:light_weighted_pressure_plate"
    lime_banner = "minecraft:lime_banner"
    lime_bed = "minecraft:lime_bed"
    lime_bed_from_white_bed = "minecraft:lime_bed_from_white_bed"
    lime_carpet = "minecraft:lime_carpet"
    lime_carpet_from_white_carpet = "minecraft:lime_carpet_from_white_carpet"
    lime_concrete_powder = "minecraft:lime_concrete_powder"
    lime_dye = "minecraft:lime_dye"
    lime_dye_from_smelting = "minecraft:lime_dye_from_smelting"
    lime_glazed_terracotta = "minecraft:lime_glazed_terracotta"
    lime_stained_glass = "minecraft:lime_stained_glass"
    lime_stained_glass_pane = "minecraft:lime_stained_glass_pane"
    lime_stained_glass_pane_from_glass_pane = "minecraft:lime_stained_glass_pane_from_glass_pane"
    lime_terracotta = "minecraft:lime_terracotta"
    lime_wool = "minecraft:lime_wool"
    lodestone = "minecraft:lodestone"
    loom = "minecraft:loom"
    magenta_banner = "minecraft:magenta_banner"
    magenta_bed = "minecraft:magenta_bed"
    magenta_bed_from_white_bed = "minecraft:magenta_bed_from_white_bed"
    magenta_carpet = "minecraft:magenta_carpet"
    magenta_carpet_from_white_carpet = "minecraft:magenta_carpet_from_white_carpet"
    magenta_concrete_powder = "minecraft:magenta_concrete_powder"
    magenta_dye_from_allium = "minecraft:magenta_dye_from_allium"
    magenta_dye_from_blue_red_pink = "minecraft:magenta_dye_from_blue_red_pink"
    magenta_dye_from_blue_red_white_dye = "minecraft:magenta_dye_from_blue_red_white_dye"
    magenta_dye_from_lilac = "minecraft:magenta_dye_from_lilac"
    magenta_dye_from_purple_and_pink = "minecraft:magenta_dye_from_purple_and_pink"
    magenta_glazed_terracotta = "minecraft:magenta_glazed_terracotta"
    magenta_stained_glass = "minecraft:magenta_stained_glass"
    magenta_stained_glass_pane = "minecraft:magenta_stained_glass_pane"
    magenta_stained_glass_pane_from_glass_pane = "minecraft:magenta_stained_glass_pane_from_glass_pane"
    magenta_terracotta = "minecraft:magenta_terracotta"
    magenta_wool = "minecraft:magenta_wool"
    magma_block = "minecraft:magma_block"
    magma_cream = "minecraft:magma_cream"
    map = "minecraft:map"
    map_cloning = "minecraft:map_cloning"
    map_extending = "minecraft:map_extending"
    melon = "minecraft:melon"
    melon_seeds = "minecraft:melon_seeds"
    minecart = "minecraft:minecart"
    mojang_banner_pattern = "minecraft:mojang_banner_pattern"
    mossy_cobblestone = "minecraft:mossy_cobblestone"
    mossy_cobblestone_slab = "minecraft:mossy_cobblestone_slab"
    mossy_cobblestone_slab_from_mossy_cobblestone_stonecutting = "minecraft:mossy_cobblestone_slab_from_mossy_cobblestone_stonecutting"
    mossy_cobblestone_stairs = "minecraft:mossy_cobblestone_stairs"
    mossy_cobblestone_stairs_from_mossy_cobblestone_stonecutting = "minecraft:mossy_cobblestone_stairs_from_mossy_cobblestone_stonecutting"
    mossy_cobblestone_wall = "minecraft:mossy_cobblestone_wall"
    mossy_cobblestone_wall_from_mossy_cobblestone_stonecutting = "minecraft:mossy_cobblestone_wall_from_mossy_cobblestone_stonecutting"
    mossy_stone_bricks = "minecraft:mossy_stone_bricks"
    mossy_stone_brick_slab = "minecraft:mossy_stone_brick_slab"
    mossy_stone_brick_slab_from_mossy_stone_brick_stonecutting = "minecraft:mossy_stone_brick_slab_from_mossy_stone_brick_stonecutting"
    mossy_stone_brick_stairs = "minecraft:mossy_stone_brick_stairs"
    mossy_stone_brick_stairs_from_mossy_stone_brick_stonecutting = "minecraft:mossy_stone_brick_stairs_from_mossy_stone_brick_stonecutting"
    mossy_stone_brick_wall = "minecraft:mossy_stone_brick_wall"
    mossy_stone_brick_wall_from_mossy_stone_brick_stonecutting = "minecraft:mossy_stone_brick_wall_from_mossy_stone_brick_stonecutting"
    mushroom_stew = "minecraft:mushroom_stew"
    netherite_axe_smithing = "minecraft:netherite_axe_smithing"
    netherite_block = "minecraft:netherite_block"
    netherite_boots_smithing = "minecraft:netherite_boots_smithing"
    netherite_chestplate_smithing = "minecraft:netherite_chestplate_smithing"
    netherite_helmet_smithing = "minecraft:netherite_helmet_smithing"
    netherite_hoe_smithing = "minecraft:netherite_hoe_smithing"
    netherite_ingot = "minecraft:netherite_ingot"
    netherite_ingot_from_netherite_block = "minecraft:netherite_ingot_from_netherite_block"
    netherite_leggings_smithing = "minecraft:netherite_leggings_smithing"
    netherite_pickaxe_smithing = "minecraft:netherite_pickaxe_smithing"
    netherite_scrap = "minecraft:netherite_scrap"
    netherite_scrap_from_blasting = "minecraft:netherite_scrap_from_blasting"
    netherite_shovel_smithing = "minecraft:netherite_shovel_smithing"
    netherite_sword_smithing = "minecraft:netherite_sword_smithing"
    nether_brick = "minecraft:nether_brick"
    nether_bricks = "minecraft:nether_bricks"
    nether_brick_fence = "minecraft:nether_brick_fence"
    nether_brick_slab = "minecraft:nether_brick_slab"
    nether_brick_slab_from_nether_bricks_stonecutting = "minecraft:nether_brick_slab_from_nether_bricks_stonecutting"
    nether_brick_stairs = "minecraft:nether_brick_stairs"
    nether_brick_stairs_from_nether_bricks_stonecutting = "minecraft:nether_brick_stairs_from_nether_bricks_stonecutting"
    nether_brick_wall = "minecraft:nether_brick_wall"
    nether_brick_wall_from_nether_bricks_stonecutting = "minecraft:nether_brick_wall_from_nether_bricks_stonecutting"
    nether_wart_block = "minecraft:nether_wart_block"
    note_block = "minecraft:note_block"
    oak_boat = "minecraft:oak_boat"
    oak_button = "minecraft:oak_button"
    oak_door = "minecraft:oak_door"
    oak_fence = "minecraft:oak_fence"
    oak_fence_gate = "minecraft:oak_fence_gate"
    oak_planks = "minecraft:oak_planks"
    oak_pressure_plate = "minecraft:oak_pressure_plate"
    oak_sign = "minecraft:oak_sign"
    oak_slab = "minecraft:oak_slab"
    oak_stairs = "minecraft:oak_stairs"
    oak_trapdoor = "minecraft:oak_trapdoor"
    oak_wood = "minecraft:oak_wood"
    observer = "minecraft:observer"
    orange_banner = "minecraft:orange_banner"
    orange_bed = "minecraft:orange_bed"
    orange_bed_from_white_bed = "minecraft:orange_bed_from_white_bed"
    orange_carpet = "minecraft:orange_carpet"
    orange_carpet_from_white_carpet = "minecraft:orange_carpet_from_white_carpet"
    orange_concrete_powder = "minecraft:orange_concrete_powder"
    orange_dye_from_orange_tulip = "minecraft:orange_dye_from_orange_tulip"
    orange_dye_from_red_yellow = "minecraft:orange_dye_from_red_yellow"
    orange_glazed_terracotta = "minecraft:orange_glazed_terracotta"
    orange_stained_glass = "minecraft:orange_stained_glass"
    orange_stained_glass_pane = "minecraft:orange_stained_glass_pane"
    orange_stained_glass_pane_from_glass_pane = "minecraft:orange_stained_glass_pane_from_glass_pane"
    orange_terracotta = "minecraft:orange_terracotta"
    orange_wool = "minecraft:orange_wool"
    packed_ice = "minecraft:packed_ice"
    painting = "minecraft:painting"
    paper = "minecraft:paper"
    pink_banner = "minecraft:pink_banner"
    pink_bed = "minecraft:pink_bed"
    pink_bed_from_white_bed = "minecraft:pink_bed_from_white_bed"
    pink_carpet = "minecraft:pink_carpet"
    pink_carpet_from_white_carpet = "minecraft:pink_carpet_from_white_carpet"
    pink_concrete_powder = "minecraft:pink_concrete_powder"
    pink_dye_from_peony = "minecraft:pink_dye_from_peony"
    pink_dye_from_pink_tulip = "minecraft:pink_dye_from_pink_tulip"
    pink_dye_from_red_white_dye = "minecraft:pink_dye_from_red_white_dye"
    pink_glazed_terracotta = "minecraft:pink_glazed_terracotta"
    pink_stained_glass = "minecraft:pink_stained_glass"
    pink_stained_glass_pane = "minecraft:pink_stained_glass_pane"
    pink_stained_glass_pane_from_glass_pane = "minecraft:pink_stained_glass_pane_from_glass_pane"
    pink_terracotta = "minecraft:pink_terracotta"
    pink_wool = "minecraft:pink_wool"
    piston = "minecraft:piston"
    polished_andesite = "minecraft:polished_andesite"
    polished_andesite_from_andesite_stonecutting = "minecraft:polished_andesite_from_andesite_stonecutting"
    polished_andesite_slab = "minecraft:polished_andesite_slab"
    polished_andesite_slab_from_andesite_stonecutting = "minecraft:polished_andesite_slab_from_andesite_stonecutting"
    polished_andesite_slab_from_polished_andesite_stonecutting = "minecraft:polished_andesite_slab_from_polished_andesite_stonecutting"
    polished_andesite_stairs = "minecraft:polished_andesite_stairs"
    polished_andesite_stairs_from_andesite_stonecutting = "minecraft:polished_andesite_stairs_from_andesite_stonecutting"
    polished_andesite_stairs_from_polished_andesite_stonecutting = "minecraft:polished_andesite_stairs_from_polished_andesite_stonecutting"
    polished_basalt = "minecraft:polished_basalt"
    polished_basalt_from_basalt_stonecutting = "minecraft:polished_basalt_from_basalt_stonecutting"
    polished_blackstone = "minecraft:polished_blackstone"
    polished_blackstone_bricks = "minecraft:polished_blackstone_bricks"
    polished_blackstone_bricks_from_blackstone_stonecutting = "minecraft:polished_blackstone_bricks_from_blackstone_stonecutting"
    polished_blackstone_bricks_from_polished_blackstone_stonecutting = "minecraft:polished_blackstone_bricks_from_polished_blackstone_stonecutting"
    polished_blackstone_brick_slab = "minecraft:polished_blackstone_brick_slab"
    polished_blackstone_brick_slab_from_blackstone_stonecutting = "minecraft:polished_blackstone_brick_slab_from_blackstone_stonecutting"
    polished_blackstone_brick_slab_from_polished_blackstone_bricks_stonecutting = "minecraft:polished_blackstone_brick_slab_from_polished_blackstone_bricks_stonecutting"
    polished_blackstone_brick_slab_from_polished_blackstone_stonecutting = "minecraft:polished_blackstone_brick_slab_from_polished_blackstone_stonecutting"
    polished_blackstone_brick_stairs = "minecraft:polished_blackstone_brick_stairs"
    polished_blackstone_brick_stairs_from_blackstone_stonecutting = "minecraft:polished_blackstone_brick_stairs_from_blackstone_stonecutting"
    polished_blackstone_brick_stairs_from_polished_blackstone_bricks_stonecutting = "minecraft:polished_blackstone_brick_stairs_from_polished_blackstone_bricks_stonecutting"
    polished_blackstone_brick_stairs_from_polished_blackstone_stonecutting = "minecraft:polished_blackstone_brick_stairs_from_polished_blackstone_stonecutting"
    polished_blackstone_brick_wall = "minecraft:polished_blackstone_brick_wall"
    polished_blackstone_brick_wall_from_blackstone_stonecutting = "minecraft:polished_blackstone_brick_wall_from_blackstone_stonecutting"
    polished_blackstone_brick_wall_from_polished_blackstone_bricks_stonecutting = "minecraft:polished_blackstone_brick_wall_from_polished_blackstone_bricks_stonecutting"
    polished_blackstone_brick_wall_from_polished_blackstone_stonecutting = "minecraft:polished_blackstone_brick_wall_from_polished_blackstone_stonecutting"
    polished_blackstone_button = "minecraft:polished_blackstone_button"
    polished_blackstone_from_blackstone_stonecutting = "minecraft:polished_blackstone_from_blackstone_stonecutting"
    polished_blackstone_pressure_plate = "minecraft:polished_blackstone_pressure_plate"
    polished_blackstone_slab = "minecraft:polished_blackstone_slab"
    polished_blackstone_slab_from_blackstone_stonecutting = "minecraft:polished_blackstone_slab_from_blackstone_stonecutting"
    polished_blackstone_slab_from_polished_blackstone_stonecutting = "minecraft:polished_blackstone_slab_from_polished_blackstone_stonecutting"
    polished_blackstone_stairs = "minecraft:polished_blackstone_stairs"
    polished_blackstone_stairs_from_blackstone_stonecutting = "minecraft:polished_blackstone_stairs_from_blackstone_stonecutting"
    polished_blackstone_stairs_from_polished_blackstone_stonecutting = "minecraft:polished_blackstone_stairs_from_polished_blackstone_stonecutting"
    polished_blackstone_wall = "minecraft:polished_blackstone_wall"
    polished_blackstone_wall_from_blackstone_stonecutting = "minecraft:polished_blackstone_wall_from_blackstone_stonecutting"
    polished_blackstone_wall_from_polished_blackstone_stonecutting = "minecraft:polished_blackstone_wall_from_polished_blackstone_stonecutting"
    polished_diorite = "minecraft:polished_diorite"
    polished_diorite_from_diorite_stonecutting = "minecraft:polished_diorite_from_diorite_stonecutting"
    polished_diorite_slab = "minecraft:polished_diorite_slab"
    polished_diorite_slab_from_diorite_stonecutting = "minecraft:polished_diorite_slab_from_diorite_stonecutting"
    polished_diorite_slab_from_polished_diorite_stonecutting = "minecraft:polished_diorite_slab_from_polished_diorite_stonecutting"
    polished_diorite_stairs = "minecraft:polished_diorite_stairs"
    polished_diorite_stairs_from_diorite_stonecutting = "minecraft:polished_diorite_stairs_from_diorite_stonecutting"
    polished_diorite_stairs_from_polished_diorite_stonecutting = "minecraft:polished_diorite_stairs_from_polished_diorite_stonecutting"
    polished_granite = "minecraft:polished_granite"
    polished_granite_from_granite_stonecutting = "minecraft:polished_granite_from_granite_stonecutting"
    polished_granite_slab = "minecraft:polished_granite_slab"
    polished_granite_slab_from_granite_stonecutting = "minecraft:polished_granite_slab_from_granite_stonecutting"
    polished_granite_slab_from_polished_granite_stonecutting = "minecraft:polished_granite_slab_from_polished_granite_stonecutting"
    polished_granite_stairs = "minecraft:polished_granite_stairs"
    polished_granite_stairs_from_granite_stonecutting = "minecraft:polished_granite_stairs_from_granite_stonecutting"
    polished_granite_stairs_from_polished_granite_stonecutting = "minecraft:polished_granite_stairs_from_polished_granite_stonecutting"
    popped_chorus_fruit = "minecraft:popped_chorus_fruit"
    powered_rail = "minecraft:powered_rail"
    prismarine = "minecraft:prismarine"
    prismarine_bricks = "minecraft:prismarine_bricks"
    prismarine_brick_slab = "minecraft:prismarine_brick_slab"
    prismarine_brick_slab_from_prismarine_stonecutting = "minecraft:prismarine_brick_slab_from_prismarine_stonecutting"
    prismarine_brick_stairs = "minecraft:prismarine_brick_stairs"
    prismarine_brick_stairs_from_prismarine_stonecutting = "minecraft:prismarine_brick_stairs_from_prismarine_stonecutting"
    prismarine_slab = "minecraft:prismarine_slab"
    prismarine_slab_from_prismarine_stonecutting = "minecraft:prismarine_slab_from_prismarine_stonecutting"
    prismarine_stairs = "minecraft:prismarine_stairs"
    prismarine_stairs_from_prismarine_stonecutting = "minecraft:prismarine_stairs_from_prismarine_stonecutting"
    prismarine_wall = "minecraft:prismarine_wall"
    prismarine_wall_from_prismarine_stonecutting = "minecraft:prismarine_wall_from_prismarine_stonecutting"
    pumpkin_pie = "minecraft:pumpkin_pie"
    pumpkin_seeds = "minecraft:pumpkin_seeds"
    purple_banner = "minecraft:purple_banner"
    purple_bed = "minecraft:purple_bed"
    purple_bed_from_white_bed = "minecraft:purple_bed_from_white_bed"
    purple_carpet = "minecraft:purple_carpet"
    purple_carpet_from_white_carpet = "minecraft:purple_carpet_from_white_carpet"
    purple_concrete_powder = "minecraft:purple_concrete_powder"
    purple_dye = "minecraft:purple_dye"
    purple_glazed_terracotta = "minecraft:purple_glazed_terracotta"
    purple_stained_glass = "minecraft:purple_stained_glass"
    purple_stained_glass_pane = "minecraft:purple_stained_glass_pane"
    purple_stained_glass_pane_from_glass_pane = "minecraft:purple_stained_glass_pane_from_glass_pane"
    purple_terracotta = "minecraft:purple_terracotta"
    purple_wool = "minecraft:purple_wool"
    purpur_block = "minecraft:purpur_block"
    purpur_pillar = "minecraft:purpur_pillar"
    purpur_pillar_from_purpur_block_stonecutting = "minecraft:purpur_pillar_from_purpur_block_stonecutting"
    purpur_slab = "minecraft:purpur_slab"
    purpur_slab_from_purpur_block_stonecutting = "minecraft:purpur_slab_from_purpur_block_stonecutting"
    purpur_stairs = "minecraft:purpur_stairs"
    purpur_stairs_from_purpur_block_stonecutting = "minecraft:purpur_stairs_from_purpur_block_stonecutting"
    quartz = "minecraft:quartz"
    quartz_block = "minecraft:quartz_block"
    quartz_bricks = "minecraft:quartz_bricks"
    quartz_bricks_from_quartz_block_stonecutting = "minecraft:quartz_bricks_from_quartz_block_stonecutting"
    quartz_from_blasting = "minecraft:quartz_from_blasting"
    quartz_pillar = "minecraft:quartz_pillar"
    quartz_pillar_from_quartz_block_stonecutting = "minecraft:quartz_pillar_from_quartz_block_stonecutting"
    quartz_slab = "minecraft:quartz_slab"
    quartz_slab_from_stonecutting = "minecraft:quartz_slab_from_stonecutting"
    quartz_stairs = "minecraft:quartz_stairs"
    quartz_stairs_from_quartz_block_stonecutting = "minecraft:quartz_stairs_from_quartz_block_stonecutting"
    rabbit_stew_from_brown_mushroom = "minecraft:rabbit_stew_from_brown_mushroom"
    rabbit_stew_from_red_mushroom = "minecraft:rabbit_stew_from_red_mushroom"
    rail = "minecraft:rail"
    redstone = "minecraft:redstone"
    redstone_block = "minecraft:redstone_block"
    redstone_from_blasting = "minecraft:redstone_from_blasting"
    redstone_from_smelting = "minecraft:redstone_from_smelting"
    redstone_lamp = "minecraft:redstone_lamp"
    redstone_torch = "minecraft:redstone_torch"
    red_banner = "minecraft:red_banner"
    red_bed = "minecraft:red_bed"
    red_bed_from_white_bed = "minecraft:red_bed_from_white_bed"
    red_carpet = "minecraft:red_carpet"
    red_carpet_from_white_carpet = "minecraft:red_carpet_from_white_carpet"
    red_concrete_powder = "minecraft:red_concrete_powder"
    red_dye_from_beetroot = "minecraft:red_dye_from_beetroot"
    red_dye_from_poppy = "minecraft:red_dye_from_poppy"
    red_dye_from_rose_bush = "minecraft:red_dye_from_rose_bush"
    red_dye_from_tulip = "minecraft:red_dye_from_tulip"
    red_glazed_terracotta = "minecraft:red_glazed_terracotta"
    red_nether_bricks = "minecraft:red_nether_bricks"
    red_nether_brick_slab = "minecraft:red_nether_brick_slab"
    red_nether_brick_slab_from_red_nether_bricks_stonecutting = "minecraft:red_nether_brick_slab_from_red_nether_bricks_stonecutting"
    red_nether_brick_stairs = "minecraft:red_nether_brick_stairs"
    red_nether_brick_stairs_from_red_nether_bricks_stonecutting = "minecraft:red_nether_brick_stairs_from_red_nether_bricks_stonecutting"
    red_nether_brick_wall = "minecraft:red_nether_brick_wall"
    red_nether_brick_wall_from_red_nether_bricks_stonecutting = "minecraft:red_nether_brick_wall_from_red_nether_bricks_stonecutting"
    red_sandstone = "minecraft:red_sandstone"
    red_sandstone_slab = "minecraft:red_sandstone_slab"
    red_sandstone_slab_from_red_sandstone_stonecutting = "minecraft:red_sandstone_slab_from_red_sandstone_stonecutting"
    red_sandstone_stairs = "minecraft:red_sandstone_stairs"
    red_sandstone_stairs_from_red_sandstone_stonecutting = "minecraft:red_sandstone_stairs_from_red_sandstone_stonecutting"
    red_sandstone_wall = "minecraft:red_sandstone_wall"
    red_sandstone_wall_from_red_sandstone_stonecutting = "minecraft:red_sandstone_wall_from_red_sandstone_stonecutting"
    red_stained_glass = "minecraft:red_stained_glass"
    red_stained_glass_pane = "minecraft:red_stained_glass_pane"
    red_stained_glass_pane_from_glass_pane = "minecraft:red_stained_glass_pane_from_glass_pane"
    red_terracotta = "minecraft:red_terracotta"
    red_wool = "minecraft:red_wool"
    repair_item = "minecraft:repair_item"
    repeater = "minecraft:repeater"
    respawn_anchor = "minecraft:respawn_anchor"
    sandstone = "minecraft:sandstone"
    sandstone_slab = "minecraft:sandstone_slab"
    sandstone_slab_from_sandstone_stonecutting = "minecraft:sandstone_slab_from_sandstone_stonecutting"
    sandstone_stairs = "minecraft:sandstone_stairs"
    sandstone_stairs_from_sandstone_stonecutting = "minecraft:sandstone_stairs_from_sandstone_stonecutting"
    sandstone_wall = "minecraft:sandstone_wall"
    sandstone_wall_from_sandstone_stonecutting = "minecraft:sandstone_wall_from_sandstone_stonecutting"
    scaffolding = "minecraft:scaffolding"
    sea_lantern = "minecraft:sea_lantern"
    shears = "minecraft:shears"
    shield = "minecraft:shield"
    shield_decoration = "minecraft:shield_decoration"
    shulker_box = "minecraft:shulker_box"
    shulker_box_coloring = "minecraft:shulker_box_coloring"
    skull_banner_pattern = "minecraft:skull_banner_pattern"
    slime_ball = "minecraft:slime_ball"
    slime_block = "minecraft:slime_block"
    smithing_table = "minecraft:smithing_table"
    smoker = "minecraft:smoker"
    smooth_quartz = "minecraft:smooth_quartz"
    smooth_quartz_slab = "minecraft:smooth_quartz_slab"
    smooth_quartz_slab_from_smooth_quartz_stonecutting = "minecraft:smooth_quartz_slab_from_smooth_quartz_stonecutting"
    smooth_quartz_stairs = "minecraft:smooth_quartz_stairs"
    smooth_quartz_stairs_from_smooth_quartz_stonecutting = "minecraft:smooth_quartz_stairs_from_smooth_quartz_stonecutting"
    smooth_red_sandstone = "minecraft:smooth_red_sandstone"
    smooth_red_sandstone_slab = "minecraft:smooth_red_sandstone_slab"
    smooth_red_sandstone_slab_from_smooth_red_sandstone_stonecutting = "minecraft:smooth_red_sandstone_slab_from_smooth_red_sandstone_stonecutting"
    smooth_red_sandstone_stairs = "minecraft:smooth_red_sandstone_stairs"
    smooth_red_sandstone_stairs_from_smooth_red_sandstone_stonecutting = "minecraft:smooth_red_sandstone_stairs_from_smooth_red_sandstone_stonecutting"
    smooth_sandstone = "minecraft:smooth_sandstone"
    smooth_sandstone_slab = "minecraft:smooth_sandstone_slab"
    smooth_sandstone_slab_from_smooth_sandstone_stonecutting = "minecraft:smooth_sandstone_slab_from_smooth_sandstone_stonecutting"
    smooth_sandstone_stairs = "minecraft:smooth_sandstone_stairs"
    smooth_sandstone_stairs_from_smooth_sandstone_stonecutting = "minecraft:smooth_sandstone_stairs_from_smooth_sandstone_stonecutting"
    smooth_stone = "minecraft:smooth_stone"
    smooth_stone_slab = "minecraft:smooth_stone_slab"
    smooth_stone_slab_from_smooth_stone_stonecutting = "minecraft:smooth_stone_slab_from_smooth_stone_stonecutting"
    snow = "minecraft:snow"
    snow_block = "minecraft:snow_block"
    soul_campfire = "minecraft:soul_campfire"
    soul_lantern = "minecraft:soul_lantern"
    soul_torch = "minecraft:soul_torch"
    spectral_arrow = "minecraft:spectral_arrow"
    sponge = "minecraft:sponge"
    spruce_boat = "minecraft:spruce_boat"
    spruce_button = "minecraft:spruce_button"
    spruce_door = "minecraft:spruce_door"
    spruce_fence = "minecraft:spruce_fence"
    spruce_fence_gate = "minecraft:spruce_fence_gate"
    spruce_planks = "minecraft:spruce_planks"
    spruce_pressure_plate = "minecraft:spruce_pressure_plate"
    spruce_sign = "minecraft:spruce_sign"
    spruce_slab = "minecraft:spruce_slab"
    spruce_stairs = "minecraft:spruce_stairs"
    spruce_trapdoor = "minecraft:spruce_trapdoor"
    spruce_wood = "minecraft:spruce_wood"
    stick = "minecraft:stick"
    sticky_piston = "minecraft:sticky_piston"
    stick_from_bamboo_item = "minecraft:stick_from_bamboo_item"
    stone = "minecraft:stone"
    stonecutter = "minecraft:stonecutter"
    stone_axe = "minecraft:stone_axe"
    stone_bricks = "minecraft:stone_bricks"
    stone_bricks_from_stone_stonecutting = "minecraft:stone_bricks_from_stone_stonecutting"
    stone_brick_slab = "minecraft:stone_brick_slab"
    stone_brick_slab_from_stone_bricks_stonecutting = "minecraft:stone_brick_slab_from_stone_bricks_stonecutting"
    stone_brick_slab_from_stone_stonecutting = "minecraft:stone_brick_slab_from_stone_stonecutting"
    stone_brick_stairs = "minecraft:stone_brick_stairs"
    stone_brick_stairs_from_stone_bricks_stonecutting = "minecraft:stone_brick_stairs_from_stone_bricks_stonecutting"
    stone_brick_stairs_from_stone_stonecutting = "minecraft:stone_brick_stairs_from_stone_stonecutting"
    stone_brick_wall = "minecraft:stone_brick_wall"
    stone_brick_walls_from_stone_stonecutting = "minecraft:stone_brick_walls_from_stone_stonecutting"
    stone_brick_wall_from_stone_bricks_stonecutting = "minecraft:stone_brick_wall_from_stone_bricks_stonecutting"
    stone_button = "minecraft:stone_button"
    stone_hoe = "minecraft:stone_hoe"
    stone_pickaxe = "minecraft:stone_pickaxe"
    stone_pressure_plate = "minecraft:stone_pressure_plate"
    stone_shovel = "minecraft:stone_shovel"
    stone_slab = "minecraft:stone_slab"
    stone_slab_from_stone_stonecutting = "minecraft:stone_slab_from_stone_stonecutting"
    stone_stairs = "minecraft:stone_stairs"
    stone_stairs_from_stone_stonecutting = "minecraft:stone_stairs_from_stone_stonecutting"
    stone_sword = "minecraft:stone_sword"
    stripped_acacia_wood = "minecraft:stripped_acacia_wood"
    stripped_birch_wood = "minecraft:stripped_birch_wood"
    stripped_crimson_hyphae = "minecraft:stripped_crimson_hyphae"
    stripped_dark_oak_wood = "minecraft:stripped_dark_oak_wood"
    stripped_jungle_wood = "minecraft:stripped_jungle_wood"
    stripped_oak_wood = "minecraft:stripped_oak_wood"
    stripped_spruce_wood = "minecraft:stripped_spruce_wood"
    stripped_warped_hyphae = "minecraft:stripped_warped_hyphae"
    sugar_from_honey_bottle = "minecraft:sugar_from_honey_bottle"
    sugar_from_sugar_cane = "minecraft:sugar_from_sugar_cane"
    suspicious_stew = "minecraft:suspicious_stew"
    target = "minecraft:target"
    terracotta = "minecraft:terracotta"
    tipped_arrow = "minecraft:tipped_arrow"
    tnt = "minecraft:tnt"
    tnt_minecart = "minecraft:tnt_minecart"
    torch = "minecraft:torch"
    trapped_chest = "minecraft:trapped_chest"
    tripwire_hook = "minecraft:tripwire_hook"
    turtle_helmet = "minecraft:turtle_helmet"
    warped_button = "minecraft:warped_button"
    warped_door = "minecraft:warped_door"
    warped_fence = "minecraft:warped_fence"
    warped_fence_gate = "minecraft:warped_fence_gate"
    warped_fungus_on_a_stick = "minecraft:warped_fungus_on_a_stick"
    warped_hyphae = "minecraft:warped_hyphae"
    warped_planks = "minecraft:warped_planks"
    warped_pressure_plate = "minecraft:warped_pressure_plate"
    warped_sign = "minecraft:warped_sign"
    warped_slab = "minecraft:warped_slab"
    warped_stairs = "minecraft:warped_stairs"
    warped_trapdoor = "minecraft:warped_trapdoor"
    wheat = "minecraft:wheat"
    white_banner = "minecraft:white_banner"
    white_bed = "minecraft:white_bed"
    white_carpet = "minecraft:white_carpet"
    white_concrete_powder = "minecraft:white_concrete_powder"
    white_dye = "minecraft:white_dye"
    white_dye_from_lily_of_the_valley = "minecraft:white_dye_from_lily_of_the_valley"
    white_glazed_terracotta = "minecraft:white_glazed_terracotta"
    white_stained_glass = "minecraft:white_stained_glass"
    white_stained_glass_pane = "minecraft:white_stained_glass_pane"
    white_stained_glass_pane_from_glass_pane = "minecraft:white_stained_glass_pane_from_glass_pane"
    white_terracotta = "minecraft:white_terracotta"
    white_wool_from_string = "minecraft:white_wool_from_string"
    wooden_axe = "minecraft:wooden_axe"
    wooden_hoe = "minecraft:wooden_hoe"
    wooden_pickaxe = "minecraft:wooden_pickaxe"
    wooden_shovel = "minecraft:wooden_shovel"
    wooden_sword = "minecraft:wooden_sword"
    writable_book = "minecraft:writable_book"
    yellow_banner = "minecraft:yellow_banner"
    yellow_bed = "minecraft:yellow_bed"
    yellow_bed_from_white_bed = "minecraft:yellow_bed_from_white_bed"
    yellow_carpet = "minecraft:yellow_carpet"
    yellow_carpet_from_white_carpet = "minecraft:yellow_carpet_from_white_carpet"
    yellow_concrete_powder = "minecraft:yellow_concrete_powder"
    yellow_dye_from_dandelion = "minecraft:yellow_dye_from_dandelion"
    yellow_dye_from_sunflower = "minecraft:yellow_dye_from_sunflower"
    yellow_glazed_terracotta = "minecraft:yellow_glazed_terracotta"
    yellow_stained_glass = "minecraft:yellow_stained_glass"
    yellow_stained_glass_pane = "minecraft:yellow_stained_glass_pane"
    yellow_stained_glass_pane_from_glass_pane = "minecraft:yellow_stained_glass_pane_from_glass_pane"
    yellow_terracotta = "minecraft:yellow_terracotta"
    yellow_wool = "minecraft:yellow_wool"


class container_type(enum.Enum):
    """List of container types

    * block
    * entity
    * storage
    """
    block = "block"
    entity = "entity"
    storage = "storage"


class container_slot(enum.Enum):
    """Container slots for replaceitem command

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


class setblock_mode(enum.Enum):
    """Modes used in setblock command

    * destroy
    * keep
    * replace
    """
    destroy = "destroy"
    keep = "keep"
    replace = "replace"


class weather(enum.Enum):
    """Weather modes

    * clear
    * rain
    * thunder
    """
    clear = "clear"
    rain = "rain"
    thunder = "thunder"


class particle(enum.Enum):
    """Particle list

    * ambient_entity_effect
    * angry_villager
    * barrier
    * block
    * bubble
    * cloud
    * crit
    * damage_indicator
    * dragon_breath
    * dripping_lava
    * falling_lava
    * landing_lava
    * dripping_water
    * falling_water
    * dust
    * effect
    * elder_guardian
    * enchanted_hit
    * enchant
    * end_rod
    * entity_effect
    * explosion_emitter
    * explosion
    * falling_dust
    * firework
    * fishing
    * flame
    * soul_fire_flame
    * soul
    * flash
    * happy_villager
    * composter
    * heart
    * instant_effect
    * item
    * item_slime
    * item_snowball
    * large_smoke
    * lava
    * mycelium
    * note
    * poof
    * portal
    * rain
    * smoke
    * sneeze
    * spit
    * squid_ink
    * sweep_attack
    * totem_of_undying
    * underwater
    * splash
    * witch
    * bubble_pop
    * current_down
    * bubble_column_up
    * nautilus
    * dolphin
    * campfire_cosy_smoke
    * campfire_signal_smoke
    * dripping_honey
    * falling_honey
    * landing_honey
    * falling_nectar
    * ash
    * crimson_spore
    * warped_spore
    * dripping_obsidian_tear
    * falling_obsidian_tear
    * landing_obsidian_tear
    * reverse_portal
    * white_ash
    """
    ambient_entity_effect = "minecraft:ambient_entity_effect"
    angry_villager = "minecraft:angry_villager"
    barrier = "minecraft:barrier"
    block = "minecraft:block"
    bubble = "minecraft:bubble"
    cloud = "minecraft:cloud"
    crit = "minecraft:crit"
    damage_indicator = "minecraft:damage_indicator"
    dragon_breath = "minecraft:dragon_breath"
    dripping_lava = "minecraft:dripping_lava"
    falling_lava = "minecraft:falling_lava"
    landing_lava = "minecraft:landing_lava"
    dripping_water = "minecraft:dripping_water"
    falling_water = "minecraft:falling_water"
    dust = "minecraft:dust"
    effect = "minecraft:effect"
    elder_guardian = "minecraft:elder_guardian"
    enchanted_hit = "minecraft:enchanted_hit"
    enchant = "minecraft:enchant"
    end_rod = "minecraft:end_rod"
    entity_effect = "minecraft:entity_effect"
    explosion_emitter = "minecraft:explosion_emitter"
    explosion = "minecraft:explosion"
    falling_dust = "minecraft:falling_dust"
    firework = "minecraft:firework"
    fishing = "minecraft:fishing"
    flame = "minecraft:flame"
    soul_fire_flame = "minecraft:soul_fire_flame"
    soul = "minecraft:soul"
    flash = "minecraft:flash"
    happy_villager = "minecraft:happy_villager"
    composter = "minecraft:composter"
    heart = "minecraft:heart"
    instant_effect = "minecraft:instant_effect"
    item = "minecraft:item"
    item_slime = "minecraft:item_slime"
    item_snowball = "minecraft:item_snowball"
    large_smoke = "minecraft:large_smoke"
    lava = "minecraft:lava"
    mycelium = "minecraft:mycelium"
    note = "minecraft:note"
    poof = "minecraft:poof"
    portal = "minecraft:portal"
    rain = "minecraft:rain"
    smoke = "minecraft:smoke"
    sneeze = "minecraft:sneeze"
    spit = "minecraft:spit"
    squid_ink = "minecraft:squid_ink"
    sweep_attack = "minecraft:sweep_attack"
    totem_of_undying = "minecraft:totem_of_undying"
    underwater = "minecraft:underwater"
    splash = "minecraft:splash"
    witch = "minecraft:witch"
    bubble_pop = "minecraft:bubble_pop"
    current_down = "minecraft:current_down"
    bubble_column_up = "minecraft:bubble_column_up"
    nautilus = "minecraft:nautilus"
    dolphin = "minecraft:dolphin"
    campfire_cosy_smoke = "minecraft:campfire_cosy_smoke"
    campfire_signal_smoke = "minecraft:campfire_signal_smoke"
    dripping_honey = "minecraft:dripping_honey"
    falling_honey = "minecraft:falling_honey"
    landing_honey = "minecraft:landing_honey"
    falling_nectar = "minecraft:falling_nectar"
    ash = "minecraft:ash"
    crimson_spore = "minecraft:crimson_spore"
    warped_spore = "minecraft:warped_spore"
    dripping_obsidian_tear = "minecraft:dripping_obsidian_tear"
    falling_obsidian_tear = "minecraft:falling_obsidian_tear"
    landing_obsidian_tear = "minecraft:landing_obsidian_tear"
    reverse_portal = "minecraft:reverse_portal"
    white_ash = "minecraft:white_ash"


class schedule_mode(enum.Enum):
    """
    * append
    * replace
    """
    append = "append"
    replace = "replace"


class team_trait(enum.Enum):
    """
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
    * always
    * never
    * push_other_teams
    * push_own_team
    """
    always = "always"
    never = "never"
    push_other_teams = "pushOtherTeams"
    push_own_team = "pushOwnTeam"


class death_message_visibility(enum.Enum):
    """
    * always
    * hide_for_other_teams
    * hide_for_own_team
    * never
    """
    always = "always"
    hide_for_other_teams = "hideForOtherTeams"
    hide_for_own_team = "hideForOwnTeam"
    never = "never"


class nametag_visibility(enum.Enum):
    """
    * always
    * hide_for_other_teams
    * hide_for_own_team
    * never
    """
    always = "always"
    hide_for_other_teams = "hideForOtherTeams"
    hide_for_own_team = "hideForOwnTeam"
    never = "never"


class border_damage(enum.Enum):
    """
    * amount
    * buffer
    """
    amount = "amount"
    buffer = "buffer"


class border_warning(enum.Enum):
    """
    * distance
    * time
    """
    distance = "distance"
    time = "time"


class loot_type(enum.Enum):
    """
    * fish
    * kill
    * loot
    * mine
    """
    fish = "fish"
    kill = "kill"
    loot = "loot"
    mine = "mine"


class score_operator(enum.Enum):
    """Score operators used in :code:`execute if score`

    * less_than
    * less_than_or_equals
    * equals
    * greater_than
    * greater_than_or_equals
    * matches
    """
    less_than = "<"
    less_than_or_equals = "<="
    equals = "="
    greater_than = ">"
    greater_than_or_equals = ">="
    matches = "matches"


class store_type(enum.Enum):
    """
    * result
    * success
    """
    result = "result"
    success = "success"


class data_type(enum.Enum):
    """
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
