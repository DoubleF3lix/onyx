import enum


class block(enum.Enum):
	"""
	block

	* acacia_button
	* acacia_door
	* acacia_fence
	* acacia_fence_gate
	* acacia_leaves
	* acacia_log
	* acacia_planks
	* acacia_pressure_plate
	* acacia_sapling
	* acacia_sign
	* acacia_slab
	* acacia_stairs
	* acacia_trapdoor
	* acacia_wall_sign
	* acacia_wood
	* activator_rail
	* air
	* allium
	* amethyst_block
	* amethyst_cluster
	* ancient_debris
	* andesite
	* andesite_slab
	* andesite_stairs
	* andesite_wall
	* anvil
	* attached_melon_stem
	* attached_pumpkin_stem
	* azalea
	* azalea_leaves
	* azure_bluet
	* bamboo
	* bamboo_sapling
	* barrel
	* barrier
	* basalt
	* beacon
	* bedrock
	* bee_nest
	* beehive
	* beetroots
	* bell
	* big_dripleaf
	* big_dripleaf_stem
	* birch_button
	* birch_door
	* birch_fence
	* birch_fence_gate
	* birch_leaves
	* birch_log
	* birch_planks
	* birch_pressure_plate
	* birch_sapling
	* birch_sign
	* birch_slab
	* birch_stairs
	* birch_trapdoor
	* birch_wall_sign
	* birch_wood
	* black_banner
	* black_bed
	* black_candle
	* black_candle_cake
	* black_carpet
	* black_concrete
	* black_concrete_powder
	* black_glazed_terracotta
	* black_shulker_box
	* black_stained_glass
	* black_stained_glass_pane
	* black_terracotta
	* black_wall_banner
	* black_wool
	* blackstone
	* blackstone_slab
	* blackstone_stairs
	* blackstone_wall
	* blast_furnace
	* blue_banner
	* blue_bed
	* blue_candle
	* blue_candle_cake
	* blue_carpet
	* blue_concrete
	* blue_concrete_powder
	* blue_glazed_terracotta
	* blue_ice
	* blue_orchid
	* blue_shulker_box
	* blue_stained_glass
	* blue_stained_glass_pane
	* blue_terracotta
	* blue_wall_banner
	* blue_wool
	* bone_block
	* bookshelf
	* brain_coral
	* brain_coral_block
	* brain_coral_fan
	* brain_coral_wall_fan
	* brewing_stand
	* brick_slab
	* brick_stairs
	* brick_wall
	* bricks
	* brown_banner
	* brown_bed
	* brown_candle
	* brown_candle_cake
	* brown_carpet
	* brown_concrete
	* brown_concrete_powder
	* brown_glazed_terracotta
	* brown_mushroom
	* brown_mushroom_block
	* brown_shulker_box
	* brown_stained_glass
	* brown_stained_glass_pane
	* brown_terracotta
	* brown_wall_banner
	* brown_wool
	* bubble_column
	* bubble_coral
	* bubble_coral_block
	* bubble_coral_fan
	* bubble_coral_wall_fan
	* budding_amethyst
	* cactus
	* cake
	* calcite
	* campfire
	* candle
	* candle_cake
	* carrots
	* cartography_table
	* carved_pumpkin
	* cauldron
	* cave_air
	* cave_vines
	* cave_vines_plant
	* chain
	* chain_command_block
	* chest
	* chipped_anvil
	* chiseled_deepslate
	* chiseled_nether_bricks
	* chiseled_polished_blackstone
	* chiseled_quartz_block
	* chiseled_red_sandstone
	* chiseled_sandstone
	* chiseled_stone_bricks
	* chorus_flower
	* chorus_plant
	* clay
	* coal_block
	* coal_ore
	* coarse_dirt
	* cobbled_deepslate
	* cobbled_deepslate_slab
	* cobbled_deepslate_stairs
	* cobbled_deepslate_wall
	* cobblestone
	* cobblestone_slab
	* cobblestone_stairs
	* cobblestone_wall
	* cobweb
	* cocoa
	* command_block
	* comparator
	* composter
	* conduit
	* copper_block
	* copper_ore
	* cornflower
	* cracked_deepslate_bricks
	* cracked_deepslate_tiles
	* cracked_nether_bricks
	* cracked_polished_blackstone_bricks
	* cracked_stone_bricks
	* crafting_table
	* creeper_head
	* creeper_wall_head
	* crimson_button
	* crimson_door
	* crimson_fence
	* crimson_fence_gate
	* crimson_fungus
	* crimson_hyphae
	* crimson_nylium
	* crimson_planks
	* crimson_pressure_plate
	* crimson_roots
	* crimson_sign
	* crimson_slab
	* crimson_stairs
	* crimson_stem
	* crimson_trapdoor
	* crimson_wall_sign
	* crying_obsidian
	* cut_copper
	* cut_copper_slab
	* cut_copper_stairs
	* cut_red_sandstone
	* cut_red_sandstone_slab
	* cut_sandstone
	* cut_sandstone_slab
	* cyan_banner
	* cyan_bed
	* cyan_candle
	* cyan_candle_cake
	* cyan_carpet
	* cyan_concrete
	* cyan_concrete_powder
	* cyan_glazed_terracotta
	* cyan_shulker_box
	* cyan_stained_glass
	* cyan_stained_glass_pane
	* cyan_terracotta
	* cyan_wall_banner
	* cyan_wool
	* damaged_anvil
	* dandelion
	* dark_oak_button
	* dark_oak_door
	* dark_oak_fence
	* dark_oak_fence_gate
	* dark_oak_leaves
	* dark_oak_log
	* dark_oak_planks
	* dark_oak_pressure_plate
	* dark_oak_sapling
	* dark_oak_sign
	* dark_oak_slab
	* dark_oak_stairs
	* dark_oak_trapdoor
	* dark_oak_wall_sign
	* dark_oak_wood
	* dark_prismarine
	* dark_prismarine_slab
	* dark_prismarine_stairs
	* daylight_detector
	* dead_brain_coral
	* dead_brain_coral_block
	* dead_brain_coral_fan
	* dead_brain_coral_wall_fan
	* dead_bubble_coral
	* dead_bubble_coral_block
	* dead_bubble_coral_fan
	* dead_bubble_coral_wall_fan
	* dead_bush
	* dead_fire_coral
	* dead_fire_coral_block
	* dead_fire_coral_fan
	* dead_fire_coral_wall_fan
	* dead_horn_coral
	* dead_horn_coral_block
	* dead_horn_coral_fan
	* dead_horn_coral_wall_fan
	* dead_tube_coral
	* dead_tube_coral_block
	* dead_tube_coral_fan
	* dead_tube_coral_wall_fan
	* deepslate
	* deepslate_brick_slab
	* deepslate_brick_stairs
	* deepslate_brick_wall
	* deepslate_bricks
	* deepslate_coal_ore
	* deepslate_copper_ore
	* deepslate_diamond_ore
	* deepslate_emerald_ore
	* deepslate_gold_ore
	* deepslate_iron_ore
	* deepslate_lapis_ore
	* deepslate_redstone_ore
	* deepslate_tile_slab
	* deepslate_tile_stairs
	* deepslate_tile_wall
	* deepslate_tiles
	* detector_rail
	* diamond_block
	* diamond_ore
	* diorite
	* diorite_slab
	* diorite_stairs
	* diorite_wall
	* dirt
	* dirt_path
	* dispenser
	* dragon_egg
	* dragon_head
	* dragon_wall_head
	* dried_kelp_block
	* dripstone_block
	* dropper
	* emerald_block
	* emerald_ore
	* enchanting_table
	* end_gateway
	* end_portal
	* end_portal_frame
	* end_rod
	* end_stone
	* end_stone_brick_slab
	* end_stone_brick_stairs
	* end_stone_brick_wall
	* end_stone_bricks
	* ender_chest
	* exposed_copper
	* exposed_cut_copper
	* exposed_cut_copper_slab
	* exposed_cut_copper_stairs
	* farmland
	* fern
	* fire
	* fire_coral
	* fire_coral_block
	* fire_coral_fan
	* fire_coral_wall_fan
	* fletching_table
	* flower_pot
	* flowering_azalea
	* flowering_azalea_leaves
	* frosted_ice
	* furnace
	* gilded_blackstone
	* glass
	* glass_pane
	* glow_lichen
	* glowstone
	* gold_block
	* gold_ore
	* granite
	* granite_slab
	* granite_stairs
	* granite_wall
	* grass
	* grass_block
	* gravel
	* gray_banner
	* gray_bed
	* gray_candle
	* gray_candle_cake
	* gray_carpet
	* gray_concrete
	* gray_concrete_powder
	* gray_glazed_terracotta
	* gray_shulker_box
	* gray_stained_glass
	* gray_stained_glass_pane
	* gray_terracotta
	* gray_wall_banner
	* gray_wool
	* green_banner
	* green_bed
	* green_candle
	* green_candle_cake
	* green_carpet
	* green_concrete
	* green_concrete_powder
	* green_glazed_terracotta
	* green_shulker_box
	* green_stained_glass
	* green_stained_glass_pane
	* green_terracotta
	* green_wall_banner
	* green_wool
	* grindstone
	* hanging_roots
	* hay_block
	* heavy_weighted_pressure_plate
	* honey_block
	* honeycomb_block
	* hopper
	* horn_coral
	* horn_coral_block
	* horn_coral_fan
	* horn_coral_wall_fan
	* ice
	* infested_chiseled_stone_bricks
	* infested_cobblestone
	* infested_cracked_stone_bricks
	* infested_deepslate
	* infested_mossy_stone_bricks
	* infested_stone
	* infested_stone_bricks
	* iron_bars
	* iron_block
	* iron_door
	* iron_ore
	* iron_trapdoor
	* jack_o_lantern
	* jigsaw
	* jukebox
	* jungle_button
	* jungle_door
	* jungle_fence
	* jungle_fence_gate
	* jungle_leaves
	* jungle_log
	* jungle_planks
	* jungle_pressure_plate
	* jungle_sapling
	* jungle_sign
	* jungle_slab
	* jungle_stairs
	* jungle_trapdoor
	* jungle_wall_sign
	* jungle_wood
	* kelp
	* kelp_plant
	* ladder
	* lantern
	* lapis_block
	* lapis_ore
	* large_amethyst_bud
	* large_fern
	* lava
	* lava_cauldron
	* lectern
	* lever
	* light
	* light_blue_banner
	* light_blue_bed
	* light_blue_candle
	* light_blue_candle_cake
	* light_blue_carpet
	* light_blue_concrete
	* light_blue_concrete_powder
	* light_blue_glazed_terracotta
	* light_blue_shulker_box
	* light_blue_stained_glass
	* light_blue_stained_glass_pane
	* light_blue_terracotta
	* light_blue_wall_banner
	* light_blue_wool
	* light_gray_banner
	* light_gray_bed
	* light_gray_candle
	* light_gray_candle_cake
	* light_gray_carpet
	* light_gray_concrete
	* light_gray_concrete_powder
	* light_gray_glazed_terracotta
	* light_gray_shulker_box
	* light_gray_stained_glass
	* light_gray_stained_glass_pane
	* light_gray_terracotta
	* light_gray_wall_banner
	* light_gray_wool
	* light_weighted_pressure_plate
	* lightning_rod
	* lilac
	* lily_of_the_valley
	* lily_pad
	* lime_banner
	* lime_bed
	* lime_candle
	* lime_candle_cake
	* lime_carpet
	* lime_concrete
	* lime_concrete_powder
	* lime_glazed_terracotta
	* lime_shulker_box
	* lime_stained_glass
	* lime_stained_glass_pane
	* lime_terracotta
	* lime_wall_banner
	* lime_wool
	* lodestone
	* loom
	* magenta_banner
	* magenta_bed
	* magenta_candle
	* magenta_candle_cake
	* magenta_carpet
	* magenta_concrete
	* magenta_concrete_powder
	* magenta_glazed_terracotta
	* magenta_shulker_box
	* magenta_stained_glass
	* magenta_stained_glass_pane
	* magenta_terracotta
	* magenta_wall_banner
	* magenta_wool
	* magma_block
	* medium_amethyst_bud
	* melon
	* melon_stem
	* moss_block
	* moss_carpet
	* mossy_cobblestone
	* mossy_cobblestone_slab
	* mossy_cobblestone_stairs
	* mossy_cobblestone_wall
	* mossy_stone_brick_slab
	* mossy_stone_brick_stairs
	* mossy_stone_brick_wall
	* mossy_stone_bricks
	* moving_piston
	* mushroom_stem
	* mycelium
	* nether_brick_fence
	* nether_brick_slab
	* nether_brick_stairs
	* nether_brick_wall
	* nether_bricks
	* nether_gold_ore
	* nether_portal
	* nether_quartz_ore
	* nether_sprouts
	* nether_wart
	* nether_wart_block
	* netherite_block
	* netherrack
	* note_block
	* oak_button
	* oak_door
	* oak_fence
	* oak_fence_gate
	* oak_leaves
	* oak_log
	* oak_planks
	* oak_pressure_plate
	* oak_sapling
	* oak_sign
	* oak_slab
	* oak_stairs
	* oak_trapdoor
	* oak_wall_sign
	* oak_wood
	* observer
	* obsidian
	* orange_banner
	* orange_bed
	* orange_candle
	* orange_candle_cake
	* orange_carpet
	* orange_concrete
	* orange_concrete_powder
	* orange_glazed_terracotta
	* orange_shulker_box
	* orange_stained_glass
	* orange_stained_glass_pane
	* orange_terracotta
	* orange_tulip
	* orange_wall_banner
	* orange_wool
	* oxeye_daisy
	* oxidized_copper
	* oxidized_cut_copper
	* oxidized_cut_copper_slab
	* oxidized_cut_copper_stairs
	* packed_ice
	* peony
	* petrified_oak_slab
	* pink_banner
	* pink_bed
	* pink_candle
	* pink_candle_cake
	* pink_carpet
	* pink_concrete
	* pink_concrete_powder
	* pink_glazed_terracotta
	* pink_shulker_box
	* pink_stained_glass
	* pink_stained_glass_pane
	* pink_terracotta
	* pink_tulip
	* pink_wall_banner
	* pink_wool
	* piston
	* piston_head
	* player_head
	* player_wall_head
	* podzol
	* pointed_dripstone
	* polished_andesite
	* polished_andesite_slab
	* polished_andesite_stairs
	* polished_basalt
	* polished_blackstone
	* polished_blackstone_brick_slab
	* polished_blackstone_brick_stairs
	* polished_blackstone_brick_wall
	* polished_blackstone_bricks
	* polished_blackstone_button
	* polished_blackstone_pressure_plate
	* polished_blackstone_slab
	* polished_blackstone_stairs
	* polished_blackstone_wall
	* polished_deepslate
	* polished_deepslate_slab
	* polished_deepslate_stairs
	* polished_deepslate_wall
	* polished_diorite
	* polished_diorite_slab
	* polished_diorite_stairs
	* polished_granite
	* polished_granite_slab
	* polished_granite_stairs
	* poppy
	* potatoes
	* potted_acacia_sapling
	* potted_allium
	* potted_azalea_bush
	* potted_azure_bluet
	* potted_bamboo
	* potted_birch_sapling
	* potted_blue_orchid
	* potted_brown_mushroom
	* potted_cactus
	* potted_cornflower
	* potted_crimson_fungus
	* potted_crimson_roots
	* potted_dandelion
	* potted_dark_oak_sapling
	* potted_dead_bush
	* potted_fern
	* potted_flowering_azalea_bush
	* potted_jungle_sapling
	* potted_lily_of_the_valley
	* potted_oak_sapling
	* potted_orange_tulip
	* potted_oxeye_daisy
	* potted_pink_tulip
	* potted_poppy
	* potted_red_mushroom
	* potted_red_tulip
	* potted_spruce_sapling
	* potted_warped_fungus
	* potted_warped_roots
	* potted_white_tulip
	* potted_wither_rose
	* powder_snow
	* powder_snow_cauldron
	* powered_rail
	* prismarine
	* prismarine_brick_slab
	* prismarine_brick_stairs
	* prismarine_bricks
	* prismarine_slab
	* prismarine_stairs
	* prismarine_wall
	* pumpkin
	* pumpkin_stem
	* purple_banner
	* purple_bed
	* purple_candle
	* purple_candle_cake
	* purple_carpet
	* purple_concrete
	* purple_concrete_powder
	* purple_glazed_terracotta
	* purple_shulker_box
	* purple_stained_glass
	* purple_stained_glass_pane
	* purple_terracotta
	* purple_wall_banner
	* purple_wool
	* purpur_block
	* purpur_pillar
	* purpur_slab
	* purpur_stairs
	* quartz_block
	* quartz_bricks
	* quartz_pillar
	* quartz_slab
	* quartz_stairs
	* rail
	* raw_copper_block
	* raw_gold_block
	* raw_iron_block
	* red_banner
	* red_bed
	* red_candle
	* red_candle_cake
	* red_carpet
	* red_concrete
	* red_concrete_powder
	* red_glazed_terracotta
	* red_mushroom
	* red_mushroom_block
	* red_nether_brick_slab
	* red_nether_brick_stairs
	* red_nether_brick_wall
	* red_nether_bricks
	* red_sand
	* red_sandstone
	* red_sandstone_slab
	* red_sandstone_stairs
	* red_sandstone_wall
	* red_shulker_box
	* red_stained_glass
	* red_stained_glass_pane
	* red_terracotta
	* red_tulip
	* red_wall_banner
	* red_wool
	* redstone_block
	* redstone_lamp
	* redstone_ore
	* redstone_torch
	* redstone_wall_torch
	* redstone_wire
	* repeater
	* repeating_command_block
	* respawn_anchor
	* rooted_dirt
	* rose_bush
	* sand
	* sandstone
	* sandstone_slab
	* sandstone_stairs
	* sandstone_wall
	* scaffolding
	* sculk_sensor
	* sea_lantern
	* sea_pickle
	* seagrass
	* shroomlight
	* shulker_box
	* skeleton_skull
	* skeleton_wall_skull
	* slime_block
	* small_amethyst_bud
	* small_dripleaf
	* smithing_table
	* smoker
	* smooth_basalt
	* smooth_quartz
	* smooth_quartz_slab
	* smooth_quartz_stairs
	* smooth_red_sandstone
	* smooth_red_sandstone_slab
	* smooth_red_sandstone_stairs
	* smooth_sandstone
	* smooth_sandstone_slab
	* smooth_sandstone_stairs
	* smooth_stone
	* smooth_stone_slab
	* snow
	* snow_block
	* soul_campfire
	* soul_fire
	* soul_lantern
	* soul_sand
	* soul_soil
	* soul_torch
	* soul_wall_torch
	* spawner
	* sponge
	* spore_blossom
	* spruce_button
	* spruce_door
	* spruce_fence
	* spruce_fence_gate
	* spruce_leaves
	* spruce_log
	* spruce_planks
	* spruce_pressure_plate
	* spruce_sapling
	* spruce_sign
	* spruce_slab
	* spruce_stairs
	* spruce_trapdoor
	* spruce_wall_sign
	* spruce_wood
	* sticky_piston
	* stone
	* stone_brick_slab
	* stone_brick_stairs
	* stone_brick_wall
	* stone_bricks
	* stone_button
	* stone_pressure_plate
	* stone_slab
	* stone_stairs
	* stonecutter
	* stripped_acacia_log
	* stripped_acacia_wood
	* stripped_birch_log
	* stripped_birch_wood
	* stripped_crimson_hyphae
	* stripped_crimson_stem
	* stripped_dark_oak_log
	* stripped_dark_oak_wood
	* stripped_jungle_log
	* stripped_jungle_wood
	* stripped_oak_log
	* stripped_oak_wood
	* stripped_spruce_log
	* stripped_spruce_wood
	* stripped_warped_hyphae
	* stripped_warped_stem
	* structure_block
	* structure_void
	* sugar_cane
	* sunflower
	* sweet_berry_bush
	* tall_grass
	* tall_seagrass
	* target
	* terracotta
	* tinted_glass
	* tnt
	* torch
	* trapped_chest
	* tripwire
	* tripwire_hook
	* tube_coral
	* tube_coral_block
	* tube_coral_fan
	* tube_coral_wall_fan
	* tuff
	* turtle_egg
	* twisting_vines
	* twisting_vines_plant
	* vine
	* void_air
	* wall_torch
	* warped_button
	* warped_door
	* warped_fence
	* warped_fence_gate
	* warped_fungus
	* warped_hyphae
	* warped_nylium
	* warped_planks
	* warped_pressure_plate
	* warped_roots
	* warped_sign
	* warped_slab
	* warped_stairs
	* warped_stem
	* warped_trapdoor
	* warped_wall_sign
	* warped_wart_block
	* water
	* water_cauldron
	* waxed_copper_block
	* waxed_cut_copper
	* waxed_cut_copper_slab
	* waxed_cut_copper_stairs
	* waxed_exposed_copper
	* waxed_exposed_cut_copper
	* waxed_exposed_cut_copper_slab
	* waxed_exposed_cut_copper_stairs
	* waxed_oxidized_copper
	* waxed_oxidized_cut_copper
	* waxed_oxidized_cut_copper_slab
	* waxed_oxidized_cut_copper_stairs
	* waxed_weathered_copper
	* waxed_weathered_cut_copper
	* waxed_weathered_cut_copper_slab
	* waxed_weathered_cut_copper_stairs
	* weathered_copper
	* weathered_cut_copper
	* weathered_cut_copper_slab
	* weathered_cut_copper_stairs
	* weeping_vines
	* weeping_vines_plant
	* wet_sponge
	* wheat
	* white_banner
	* white_bed
	* white_candle
	* white_candle_cake
	* white_carpet
	* white_concrete
	* white_concrete_powder
	* white_glazed_terracotta
	* white_shulker_box
	* white_stained_glass
	* white_stained_glass_pane
	* white_terracotta
	* white_tulip
	* white_wall_banner
	* white_wool
	* wither_rose
	* wither_skeleton_skull
	* wither_skeleton_wall_skull
	* yellow_banner
	* yellow_bed
	* yellow_candle
	* yellow_candle_cake
	* yellow_carpet
	* yellow_concrete
	* yellow_concrete_powder
	* yellow_glazed_terracotta
	* yellow_shulker_box
	* yellow_stained_glass
	* yellow_stained_glass_pane
	* yellow_terracotta
	* yellow_wall_banner
	* yellow_wool
	* zombie_head
	* zombie_wall_head
	"""
	acacia_button = "minecraft:acacia_button"
	acacia_door = "minecraft:acacia_door"
	acacia_fence = "minecraft:acacia_fence"
	acacia_fence_gate = "minecraft:acacia_fence_gate"
	acacia_leaves = "minecraft:acacia_leaves"
	acacia_log = "minecraft:acacia_log"
	acacia_planks = "minecraft:acacia_planks"
	acacia_pressure_plate = "minecraft:acacia_pressure_plate"
	acacia_sapling = "minecraft:acacia_sapling"
	acacia_sign = "minecraft:acacia_sign"
	acacia_slab = "minecraft:acacia_slab"
	acacia_stairs = "minecraft:acacia_stairs"
	acacia_trapdoor = "minecraft:acacia_trapdoor"
	acacia_wall_sign = "minecraft:acacia_wall_sign"
	acacia_wood = "minecraft:acacia_wood"
	activator_rail = "minecraft:activator_rail"
	air = "minecraft:air"
	allium = "minecraft:allium"
	amethyst_block = "minecraft:amethyst_block"
	amethyst_cluster = "minecraft:amethyst_cluster"
	ancient_debris = "minecraft:ancient_debris"
	andesite = "minecraft:andesite"
	andesite_slab = "minecraft:andesite_slab"
	andesite_stairs = "minecraft:andesite_stairs"
	andesite_wall = "minecraft:andesite_wall"
	anvil = "minecraft:anvil"
	attached_melon_stem = "minecraft:attached_melon_stem"
	attached_pumpkin_stem = "minecraft:attached_pumpkin_stem"
	azalea = "minecraft:azalea"
	azalea_leaves = "minecraft:azalea_leaves"
	azure_bluet = "minecraft:azure_bluet"
	bamboo = "minecraft:bamboo"
	bamboo_sapling = "minecraft:bamboo_sapling"
	barrel = "minecraft:barrel"
	barrier = "minecraft:barrier"
	basalt = "minecraft:basalt"
	beacon = "minecraft:beacon"
	bedrock = "minecraft:bedrock"
	bee_nest = "minecraft:bee_nest"
	beehive = "minecraft:beehive"
	beetroots = "minecraft:beetroots"
	bell = "minecraft:bell"
	big_dripleaf = "minecraft:big_dripleaf"
	big_dripleaf_stem = "minecraft:big_dripleaf_stem"
	birch_button = "minecraft:birch_button"
	birch_door = "minecraft:birch_door"
	birch_fence = "minecraft:birch_fence"
	birch_fence_gate = "minecraft:birch_fence_gate"
	birch_leaves = "minecraft:birch_leaves"
	birch_log = "minecraft:birch_log"
	birch_planks = "minecraft:birch_planks"
	birch_pressure_plate = "minecraft:birch_pressure_plate"
	birch_sapling = "minecraft:birch_sapling"
	birch_sign = "minecraft:birch_sign"
	birch_slab = "minecraft:birch_slab"
	birch_stairs = "minecraft:birch_stairs"
	birch_trapdoor = "minecraft:birch_trapdoor"
	birch_wall_sign = "minecraft:birch_wall_sign"
	birch_wood = "minecraft:birch_wood"
	black_banner = "minecraft:black_banner"
	black_bed = "minecraft:black_bed"
	black_candle = "minecraft:black_candle"
	black_candle_cake = "minecraft:black_candle_cake"
	black_carpet = "minecraft:black_carpet"
	black_concrete = "minecraft:black_concrete"
	black_concrete_powder = "minecraft:black_concrete_powder"
	black_glazed_terracotta = "minecraft:black_glazed_terracotta"
	black_shulker_box = "minecraft:black_shulker_box"
	black_stained_glass = "minecraft:black_stained_glass"
	black_stained_glass_pane = "minecraft:black_stained_glass_pane"
	black_terracotta = "minecraft:black_terracotta"
	black_wall_banner = "minecraft:black_wall_banner"
	black_wool = "minecraft:black_wool"
	blackstone = "minecraft:blackstone"
	blackstone_slab = "minecraft:blackstone_slab"
	blackstone_stairs = "minecraft:blackstone_stairs"
	blackstone_wall = "minecraft:blackstone_wall"
	blast_furnace = "minecraft:blast_furnace"
	blue_banner = "minecraft:blue_banner"
	blue_bed = "minecraft:blue_bed"
	blue_candle = "minecraft:blue_candle"
	blue_candle_cake = "minecraft:blue_candle_cake"
	blue_carpet = "minecraft:blue_carpet"
	blue_concrete = "minecraft:blue_concrete"
	blue_concrete_powder = "minecraft:blue_concrete_powder"
	blue_glazed_terracotta = "minecraft:blue_glazed_terracotta"
	blue_ice = "minecraft:blue_ice"
	blue_orchid = "minecraft:blue_orchid"
	blue_shulker_box = "minecraft:blue_shulker_box"
	blue_stained_glass = "minecraft:blue_stained_glass"
	blue_stained_glass_pane = "minecraft:blue_stained_glass_pane"
	blue_terracotta = "minecraft:blue_terracotta"
	blue_wall_banner = "minecraft:blue_wall_banner"
	blue_wool = "minecraft:blue_wool"
	bone_block = "minecraft:bone_block"
	bookshelf = "minecraft:bookshelf"
	brain_coral = "minecraft:brain_coral"
	brain_coral_block = "minecraft:brain_coral_block"
	brain_coral_fan = "minecraft:brain_coral_fan"
	brain_coral_wall_fan = "minecraft:brain_coral_wall_fan"
	brewing_stand = "minecraft:brewing_stand"
	brick_slab = "minecraft:brick_slab"
	brick_stairs = "minecraft:brick_stairs"
	brick_wall = "minecraft:brick_wall"
	bricks = "minecraft:bricks"
	brown_banner = "minecraft:brown_banner"
	brown_bed = "minecraft:brown_bed"
	brown_candle = "minecraft:brown_candle"
	brown_candle_cake = "minecraft:brown_candle_cake"
	brown_carpet = "minecraft:brown_carpet"
	brown_concrete = "minecraft:brown_concrete"
	brown_concrete_powder = "minecraft:brown_concrete_powder"
	brown_glazed_terracotta = "minecraft:brown_glazed_terracotta"
	brown_mushroom = "minecraft:brown_mushroom"
	brown_mushroom_block = "minecraft:brown_mushroom_block"
	brown_shulker_box = "minecraft:brown_shulker_box"
	brown_stained_glass = "minecraft:brown_stained_glass"
	brown_stained_glass_pane = "minecraft:brown_stained_glass_pane"
	brown_terracotta = "minecraft:brown_terracotta"
	brown_wall_banner = "minecraft:brown_wall_banner"
	brown_wool = "minecraft:brown_wool"
	bubble_column = "minecraft:bubble_column"
	bubble_coral = "minecraft:bubble_coral"
	bubble_coral_block = "minecraft:bubble_coral_block"
	bubble_coral_fan = "minecraft:bubble_coral_fan"
	bubble_coral_wall_fan = "minecraft:bubble_coral_wall_fan"
	budding_amethyst = "minecraft:budding_amethyst"
	cactus = "minecraft:cactus"
	cake = "minecraft:cake"
	calcite = "minecraft:calcite"
	campfire = "minecraft:campfire"
	candle = "minecraft:candle"
	candle_cake = "minecraft:candle_cake"
	carrots = "minecraft:carrots"
	cartography_table = "minecraft:cartography_table"
	carved_pumpkin = "minecraft:carved_pumpkin"
	cauldron = "minecraft:cauldron"
	cave_air = "minecraft:cave_air"
	cave_vines = "minecraft:cave_vines"
	cave_vines_plant = "minecraft:cave_vines_plant"
	chain = "minecraft:chain"
	chain_command_block = "minecraft:chain_command_block"
	chest = "minecraft:chest"
	chipped_anvil = "minecraft:chipped_anvil"
	chiseled_deepslate = "minecraft:chiseled_deepslate"
	chiseled_nether_bricks = "minecraft:chiseled_nether_bricks"
	chiseled_polished_blackstone = "minecraft:chiseled_polished_blackstone"
	chiseled_quartz_block = "minecraft:chiseled_quartz_block"
	chiseled_red_sandstone = "minecraft:chiseled_red_sandstone"
	chiseled_sandstone = "minecraft:chiseled_sandstone"
	chiseled_stone_bricks = "minecraft:chiseled_stone_bricks"
	chorus_flower = "minecraft:chorus_flower"
	chorus_plant = "minecraft:chorus_plant"
	clay = "minecraft:clay"
	coal_block = "minecraft:coal_block"
	coal_ore = "minecraft:coal_ore"
	coarse_dirt = "minecraft:coarse_dirt"
	cobbled_deepslate = "minecraft:cobbled_deepslate"
	cobbled_deepslate_slab = "minecraft:cobbled_deepslate_slab"
	cobbled_deepslate_stairs = "minecraft:cobbled_deepslate_stairs"
	cobbled_deepslate_wall = "minecraft:cobbled_deepslate_wall"
	cobblestone = "minecraft:cobblestone"
	cobblestone_slab = "minecraft:cobblestone_slab"
	cobblestone_stairs = "minecraft:cobblestone_stairs"
	cobblestone_wall = "minecraft:cobblestone_wall"
	cobweb = "minecraft:cobweb"
	cocoa = "minecraft:cocoa"
	command_block = "minecraft:command_block"
	comparator = "minecraft:comparator"
	composter = "minecraft:composter"
	conduit = "minecraft:conduit"
	copper_block = "minecraft:copper_block"
	copper_ore = "minecraft:copper_ore"
	cornflower = "minecraft:cornflower"
	cracked_deepslate_bricks = "minecraft:cracked_deepslate_bricks"
	cracked_deepslate_tiles = "minecraft:cracked_deepslate_tiles"
	cracked_nether_bricks = "minecraft:cracked_nether_bricks"
	cracked_polished_blackstone_bricks = "minecraft:cracked_polished_blackstone_bricks"
	cracked_stone_bricks = "minecraft:cracked_stone_bricks"
	crafting_table = "minecraft:crafting_table"
	creeper_head = "minecraft:creeper_head"
	creeper_wall_head = "minecraft:creeper_wall_head"
	crimson_button = "minecraft:crimson_button"
	crimson_door = "minecraft:crimson_door"
	crimson_fence = "minecraft:crimson_fence"
	crimson_fence_gate = "minecraft:crimson_fence_gate"
	crimson_fungus = "minecraft:crimson_fungus"
	crimson_hyphae = "minecraft:crimson_hyphae"
	crimson_nylium = "minecraft:crimson_nylium"
	crimson_planks = "minecraft:crimson_planks"
	crimson_pressure_plate = "minecraft:crimson_pressure_plate"
	crimson_roots = "minecraft:crimson_roots"
	crimson_sign = "minecraft:crimson_sign"
	crimson_slab = "minecraft:crimson_slab"
	crimson_stairs = "minecraft:crimson_stairs"
	crimson_stem = "minecraft:crimson_stem"
	crimson_trapdoor = "minecraft:crimson_trapdoor"
	crimson_wall_sign = "minecraft:crimson_wall_sign"
	crying_obsidian = "minecraft:crying_obsidian"
	cut_copper = "minecraft:cut_copper"
	cut_copper_slab = "minecraft:cut_copper_slab"
	cut_copper_stairs = "minecraft:cut_copper_stairs"
	cut_red_sandstone = "minecraft:cut_red_sandstone"
	cut_red_sandstone_slab = "minecraft:cut_red_sandstone_slab"
	cut_sandstone = "minecraft:cut_sandstone"
	cut_sandstone_slab = "minecraft:cut_sandstone_slab"
	cyan_banner = "minecraft:cyan_banner"
	cyan_bed = "minecraft:cyan_bed"
	cyan_candle = "minecraft:cyan_candle"
	cyan_candle_cake = "minecraft:cyan_candle_cake"
	cyan_carpet = "minecraft:cyan_carpet"
	cyan_concrete = "minecraft:cyan_concrete"
	cyan_concrete_powder = "minecraft:cyan_concrete_powder"
	cyan_glazed_terracotta = "minecraft:cyan_glazed_terracotta"
	cyan_shulker_box = "minecraft:cyan_shulker_box"
	cyan_stained_glass = "minecraft:cyan_stained_glass"
	cyan_stained_glass_pane = "minecraft:cyan_stained_glass_pane"
	cyan_terracotta = "minecraft:cyan_terracotta"
	cyan_wall_banner = "minecraft:cyan_wall_banner"
	cyan_wool = "minecraft:cyan_wool"
	damaged_anvil = "minecraft:damaged_anvil"
	dandelion = "minecraft:dandelion"
	dark_oak_button = "minecraft:dark_oak_button"
	dark_oak_door = "minecraft:dark_oak_door"
	dark_oak_fence = "minecraft:dark_oak_fence"
	dark_oak_fence_gate = "minecraft:dark_oak_fence_gate"
	dark_oak_leaves = "minecraft:dark_oak_leaves"
	dark_oak_log = "minecraft:dark_oak_log"
	dark_oak_planks = "minecraft:dark_oak_planks"
	dark_oak_pressure_plate = "minecraft:dark_oak_pressure_plate"
	dark_oak_sapling = "minecraft:dark_oak_sapling"
	dark_oak_sign = "minecraft:dark_oak_sign"
	dark_oak_slab = "minecraft:dark_oak_slab"
	dark_oak_stairs = "minecraft:dark_oak_stairs"
	dark_oak_trapdoor = "minecraft:dark_oak_trapdoor"
	dark_oak_wall_sign = "minecraft:dark_oak_wall_sign"
	dark_oak_wood = "minecraft:dark_oak_wood"
	dark_prismarine = "minecraft:dark_prismarine"
	dark_prismarine_slab = "minecraft:dark_prismarine_slab"
	dark_prismarine_stairs = "minecraft:dark_prismarine_stairs"
	daylight_detector = "minecraft:daylight_detector"
	dead_brain_coral = "minecraft:dead_brain_coral"
	dead_brain_coral_block = "minecraft:dead_brain_coral_block"
	dead_brain_coral_fan = "minecraft:dead_brain_coral_fan"
	dead_brain_coral_wall_fan = "minecraft:dead_brain_coral_wall_fan"
	dead_bubble_coral = "minecraft:dead_bubble_coral"
	dead_bubble_coral_block = "minecraft:dead_bubble_coral_block"
	dead_bubble_coral_fan = "minecraft:dead_bubble_coral_fan"
	dead_bubble_coral_wall_fan = "minecraft:dead_bubble_coral_wall_fan"
	dead_bush = "minecraft:dead_bush"
	dead_fire_coral = "minecraft:dead_fire_coral"
	dead_fire_coral_block = "minecraft:dead_fire_coral_block"
	dead_fire_coral_fan = "minecraft:dead_fire_coral_fan"
	dead_fire_coral_wall_fan = "minecraft:dead_fire_coral_wall_fan"
	dead_horn_coral = "minecraft:dead_horn_coral"
	dead_horn_coral_block = "minecraft:dead_horn_coral_block"
	dead_horn_coral_fan = "minecraft:dead_horn_coral_fan"
	dead_horn_coral_wall_fan = "minecraft:dead_horn_coral_wall_fan"
	dead_tube_coral = "minecraft:dead_tube_coral"
	dead_tube_coral_block = "minecraft:dead_tube_coral_block"
	dead_tube_coral_fan = "minecraft:dead_tube_coral_fan"
	dead_tube_coral_wall_fan = "minecraft:dead_tube_coral_wall_fan"
	deepslate = "minecraft:deepslate"
	deepslate_brick_slab = "minecraft:deepslate_brick_slab"
	deepslate_brick_stairs = "minecraft:deepslate_brick_stairs"
	deepslate_brick_wall = "minecraft:deepslate_brick_wall"
	deepslate_bricks = "minecraft:deepslate_bricks"
	deepslate_coal_ore = "minecraft:deepslate_coal_ore"
	deepslate_copper_ore = "minecraft:deepslate_copper_ore"
	deepslate_diamond_ore = "minecraft:deepslate_diamond_ore"
	deepslate_emerald_ore = "minecraft:deepslate_emerald_ore"
	deepslate_gold_ore = "minecraft:deepslate_gold_ore"
	deepslate_iron_ore = "minecraft:deepslate_iron_ore"
	deepslate_lapis_ore = "minecraft:deepslate_lapis_ore"
	deepslate_redstone_ore = "minecraft:deepslate_redstone_ore"
	deepslate_tile_slab = "minecraft:deepslate_tile_slab"
	deepslate_tile_stairs = "minecraft:deepslate_tile_stairs"
	deepslate_tile_wall = "minecraft:deepslate_tile_wall"
	deepslate_tiles = "minecraft:deepslate_tiles"
	detector_rail = "minecraft:detector_rail"
	diamond_block = "minecraft:diamond_block"
	diamond_ore = "minecraft:diamond_ore"
	diorite = "minecraft:diorite"
	diorite_slab = "minecraft:diorite_slab"
	diorite_stairs = "minecraft:diorite_stairs"
	diorite_wall = "minecraft:diorite_wall"
	dirt = "minecraft:dirt"
	dirt_path = "minecraft:dirt_path"
	dispenser = "minecraft:dispenser"
	dragon_egg = "minecraft:dragon_egg"
	dragon_head = "minecraft:dragon_head"
	dragon_wall_head = "minecraft:dragon_wall_head"
	dried_kelp_block = "minecraft:dried_kelp_block"
	dripstone_block = "minecraft:dripstone_block"
	dropper = "minecraft:dropper"
	emerald_block = "minecraft:emerald_block"
	emerald_ore = "minecraft:emerald_ore"
	enchanting_table = "minecraft:enchanting_table"
	end_gateway = "minecraft:end_gateway"
	end_portal = "minecraft:end_portal"
	end_portal_frame = "minecraft:end_portal_frame"
	end_rod = "minecraft:end_rod"
	end_stone = "minecraft:end_stone"
	end_stone_brick_slab = "minecraft:end_stone_brick_slab"
	end_stone_brick_stairs = "minecraft:end_stone_brick_stairs"
	end_stone_brick_wall = "minecraft:end_stone_brick_wall"
	end_stone_bricks = "minecraft:end_stone_bricks"
	ender_chest = "minecraft:ender_chest"
	exposed_copper = "minecraft:exposed_copper"
	exposed_cut_copper = "minecraft:exposed_cut_copper"
	exposed_cut_copper_slab = "minecraft:exposed_cut_copper_slab"
	exposed_cut_copper_stairs = "minecraft:exposed_cut_copper_stairs"
	farmland = "minecraft:farmland"
	fern = "minecraft:fern"
	fire = "minecraft:fire"
	fire_coral = "minecraft:fire_coral"
	fire_coral_block = "minecraft:fire_coral_block"
	fire_coral_fan = "minecraft:fire_coral_fan"
	fire_coral_wall_fan = "minecraft:fire_coral_wall_fan"
	fletching_table = "minecraft:fletching_table"
	flower_pot = "minecraft:flower_pot"
	flowering_azalea = "minecraft:flowering_azalea"
	flowering_azalea_leaves = "minecraft:flowering_azalea_leaves"
	frosted_ice = "minecraft:frosted_ice"
	furnace = "minecraft:furnace"
	gilded_blackstone = "minecraft:gilded_blackstone"
	glass = "minecraft:glass"
	glass_pane = "minecraft:glass_pane"
	glow_lichen = "minecraft:glow_lichen"
	glowstone = "minecraft:glowstone"
	gold_block = "minecraft:gold_block"
	gold_ore = "minecraft:gold_ore"
	granite = "minecraft:granite"
	granite_slab = "minecraft:granite_slab"
	granite_stairs = "minecraft:granite_stairs"
	granite_wall = "minecraft:granite_wall"
	grass = "minecraft:grass"
	grass_block = "minecraft:grass_block"
	gravel = "minecraft:gravel"
	gray_banner = "minecraft:gray_banner"
	gray_bed = "minecraft:gray_bed"
	gray_candle = "minecraft:gray_candle"
	gray_candle_cake = "minecraft:gray_candle_cake"
	gray_carpet = "minecraft:gray_carpet"
	gray_concrete = "minecraft:gray_concrete"
	gray_concrete_powder = "minecraft:gray_concrete_powder"
	gray_glazed_terracotta = "minecraft:gray_glazed_terracotta"
	gray_shulker_box = "minecraft:gray_shulker_box"
	gray_stained_glass = "minecraft:gray_stained_glass"
	gray_stained_glass_pane = "minecraft:gray_stained_glass_pane"
	gray_terracotta = "minecraft:gray_terracotta"
	gray_wall_banner = "minecraft:gray_wall_banner"
	gray_wool = "minecraft:gray_wool"
	green_banner = "minecraft:green_banner"
	green_bed = "minecraft:green_bed"
	green_candle = "minecraft:green_candle"
	green_candle_cake = "minecraft:green_candle_cake"
	green_carpet = "minecraft:green_carpet"
	green_concrete = "minecraft:green_concrete"
	green_concrete_powder = "minecraft:green_concrete_powder"
	green_glazed_terracotta = "minecraft:green_glazed_terracotta"
	green_shulker_box = "minecraft:green_shulker_box"
	green_stained_glass = "minecraft:green_stained_glass"
	green_stained_glass_pane = "minecraft:green_stained_glass_pane"
	green_terracotta = "minecraft:green_terracotta"
	green_wall_banner = "minecraft:green_wall_banner"
	green_wool = "minecraft:green_wool"
	grindstone = "minecraft:grindstone"
	hanging_roots = "minecraft:hanging_roots"
	hay_block = "minecraft:hay_block"
	heavy_weighted_pressure_plate = "minecraft:heavy_weighted_pressure_plate"
	honey_block = "minecraft:honey_block"
	honeycomb_block = "minecraft:honeycomb_block"
	hopper = "minecraft:hopper"
	horn_coral = "minecraft:horn_coral"
	horn_coral_block = "minecraft:horn_coral_block"
	horn_coral_fan = "minecraft:horn_coral_fan"
	horn_coral_wall_fan = "minecraft:horn_coral_wall_fan"
	ice = "minecraft:ice"
	infested_chiseled_stone_bricks = "minecraft:infested_chiseled_stone_bricks"
	infested_cobblestone = "minecraft:infested_cobblestone"
	infested_cracked_stone_bricks = "minecraft:infested_cracked_stone_bricks"
	infested_deepslate = "minecraft:infested_deepslate"
	infested_mossy_stone_bricks = "minecraft:infested_mossy_stone_bricks"
	infested_stone = "minecraft:infested_stone"
	infested_stone_bricks = "minecraft:infested_stone_bricks"
	iron_bars = "minecraft:iron_bars"
	iron_block = "minecraft:iron_block"
	iron_door = "minecraft:iron_door"
	iron_ore = "minecraft:iron_ore"
	iron_trapdoor = "minecraft:iron_trapdoor"
	jack_o_lantern = "minecraft:jack_o_lantern"
	jigsaw = "minecraft:jigsaw"
	jukebox = "minecraft:jukebox"
	jungle_button = "minecraft:jungle_button"
	jungle_door = "minecraft:jungle_door"
	jungle_fence = "minecraft:jungle_fence"
	jungle_fence_gate = "minecraft:jungle_fence_gate"
	jungle_leaves = "minecraft:jungle_leaves"
	jungle_log = "minecraft:jungle_log"
	jungle_planks = "minecraft:jungle_planks"
	jungle_pressure_plate = "minecraft:jungle_pressure_plate"
	jungle_sapling = "minecraft:jungle_sapling"
	jungle_sign = "minecraft:jungle_sign"
	jungle_slab = "minecraft:jungle_slab"
	jungle_stairs = "minecraft:jungle_stairs"
	jungle_trapdoor = "minecraft:jungle_trapdoor"
	jungle_wall_sign = "minecraft:jungle_wall_sign"
	jungle_wood = "minecraft:jungle_wood"
	kelp = "minecraft:kelp"
	kelp_plant = "minecraft:kelp_plant"
	ladder = "minecraft:ladder"
	lantern = "minecraft:lantern"
	lapis_block = "minecraft:lapis_block"
	lapis_ore = "minecraft:lapis_ore"
	large_amethyst_bud = "minecraft:large_amethyst_bud"
	large_fern = "minecraft:large_fern"
	lava = "minecraft:lava"
	lava_cauldron = "minecraft:lava_cauldron"
	lectern = "minecraft:lectern"
	lever = "minecraft:lever"
	light = "minecraft:light"
	light_blue_banner = "minecraft:light_blue_banner"
	light_blue_bed = "minecraft:light_blue_bed"
	light_blue_candle = "minecraft:light_blue_candle"
	light_blue_candle_cake = "minecraft:light_blue_candle_cake"
	light_blue_carpet = "minecraft:light_blue_carpet"
	light_blue_concrete = "minecraft:light_blue_concrete"
	light_blue_concrete_powder = "minecraft:light_blue_concrete_powder"
	light_blue_glazed_terracotta = "minecraft:light_blue_glazed_terracotta"
	light_blue_shulker_box = "minecraft:light_blue_shulker_box"
	light_blue_stained_glass = "minecraft:light_blue_stained_glass"
	light_blue_stained_glass_pane = "minecraft:light_blue_stained_glass_pane"
	light_blue_terracotta = "minecraft:light_blue_terracotta"
	light_blue_wall_banner = "minecraft:light_blue_wall_banner"
	light_blue_wool = "minecraft:light_blue_wool"
	light_gray_banner = "minecraft:light_gray_banner"
	light_gray_bed = "minecraft:light_gray_bed"
	light_gray_candle = "minecraft:light_gray_candle"
	light_gray_candle_cake = "minecraft:light_gray_candle_cake"
	light_gray_carpet = "minecraft:light_gray_carpet"
	light_gray_concrete = "minecraft:light_gray_concrete"
	light_gray_concrete_powder = "minecraft:light_gray_concrete_powder"
	light_gray_glazed_terracotta = "minecraft:light_gray_glazed_terracotta"
	light_gray_shulker_box = "minecraft:light_gray_shulker_box"
	light_gray_stained_glass = "minecraft:light_gray_stained_glass"
	light_gray_stained_glass_pane = "minecraft:light_gray_stained_glass_pane"
	light_gray_terracotta = "minecraft:light_gray_terracotta"
	light_gray_wall_banner = "minecraft:light_gray_wall_banner"
	light_gray_wool = "minecraft:light_gray_wool"
	light_weighted_pressure_plate = "minecraft:light_weighted_pressure_plate"
	lightning_rod = "minecraft:lightning_rod"
	lilac = "minecraft:lilac"
	lily_of_the_valley = "minecraft:lily_of_the_valley"
	lily_pad = "minecraft:lily_pad"
	lime_banner = "minecraft:lime_banner"
	lime_bed = "minecraft:lime_bed"
	lime_candle = "minecraft:lime_candle"
	lime_candle_cake = "minecraft:lime_candle_cake"
	lime_carpet = "minecraft:lime_carpet"
	lime_concrete = "minecraft:lime_concrete"
	lime_concrete_powder = "minecraft:lime_concrete_powder"
	lime_glazed_terracotta = "minecraft:lime_glazed_terracotta"
	lime_shulker_box = "minecraft:lime_shulker_box"
	lime_stained_glass = "minecraft:lime_stained_glass"
	lime_stained_glass_pane = "minecraft:lime_stained_glass_pane"
	lime_terracotta = "minecraft:lime_terracotta"
	lime_wall_banner = "minecraft:lime_wall_banner"
	lime_wool = "minecraft:lime_wool"
	lodestone = "minecraft:lodestone"
	loom = "minecraft:loom"
	magenta_banner = "minecraft:magenta_banner"
	magenta_bed = "minecraft:magenta_bed"
	magenta_candle = "minecraft:magenta_candle"
	magenta_candle_cake = "minecraft:magenta_candle_cake"
	magenta_carpet = "minecraft:magenta_carpet"
	magenta_concrete = "minecraft:magenta_concrete"
	magenta_concrete_powder = "minecraft:magenta_concrete_powder"
	magenta_glazed_terracotta = "minecraft:magenta_glazed_terracotta"
	magenta_shulker_box = "minecraft:magenta_shulker_box"
	magenta_stained_glass = "minecraft:magenta_stained_glass"
	magenta_stained_glass_pane = "minecraft:magenta_stained_glass_pane"
	magenta_terracotta = "minecraft:magenta_terracotta"
	magenta_wall_banner = "minecraft:magenta_wall_banner"
	magenta_wool = "minecraft:magenta_wool"
	magma_block = "minecraft:magma_block"
	medium_amethyst_bud = "minecraft:medium_amethyst_bud"
	melon = "minecraft:melon"
	melon_stem = "minecraft:melon_stem"
	moss_block = "minecraft:moss_block"
	moss_carpet = "minecraft:moss_carpet"
	mossy_cobblestone = "minecraft:mossy_cobblestone"
	mossy_cobblestone_slab = "minecraft:mossy_cobblestone_slab"
	mossy_cobblestone_stairs = "minecraft:mossy_cobblestone_stairs"
	mossy_cobblestone_wall = "minecraft:mossy_cobblestone_wall"
	mossy_stone_brick_slab = "minecraft:mossy_stone_brick_slab"
	mossy_stone_brick_stairs = "minecraft:mossy_stone_brick_stairs"
	mossy_stone_brick_wall = "minecraft:mossy_stone_brick_wall"
	mossy_stone_bricks = "minecraft:mossy_stone_bricks"
	moving_piston = "minecraft:moving_piston"
	mushroom_stem = "minecraft:mushroom_stem"
	mycelium = "minecraft:mycelium"
	nether_brick_fence = "minecraft:nether_brick_fence"
	nether_brick_slab = "minecraft:nether_brick_slab"
	nether_brick_stairs = "minecraft:nether_brick_stairs"
	nether_brick_wall = "minecraft:nether_brick_wall"
	nether_bricks = "minecraft:nether_bricks"
	nether_gold_ore = "minecraft:nether_gold_ore"
	nether_portal = "minecraft:nether_portal"
	nether_quartz_ore = "minecraft:nether_quartz_ore"
	nether_sprouts = "minecraft:nether_sprouts"
	nether_wart = "minecraft:nether_wart"
	nether_wart_block = "minecraft:nether_wart_block"
	netherite_block = "minecraft:netherite_block"
	netherrack = "minecraft:netherrack"
	note_block = "minecraft:note_block"
	oak_button = "minecraft:oak_button"
	oak_door = "minecraft:oak_door"
	oak_fence = "minecraft:oak_fence"
	oak_fence_gate = "minecraft:oak_fence_gate"
	oak_leaves = "minecraft:oak_leaves"
	oak_log = "minecraft:oak_log"
	oak_planks = "minecraft:oak_planks"
	oak_pressure_plate = "minecraft:oak_pressure_plate"
	oak_sapling = "minecraft:oak_sapling"
	oak_sign = "minecraft:oak_sign"
	oak_slab = "minecraft:oak_slab"
	oak_stairs = "minecraft:oak_stairs"
	oak_trapdoor = "minecraft:oak_trapdoor"
	oak_wall_sign = "minecraft:oak_wall_sign"
	oak_wood = "minecraft:oak_wood"
	observer = "minecraft:observer"
	obsidian = "minecraft:obsidian"
	orange_banner = "minecraft:orange_banner"
	orange_bed = "minecraft:orange_bed"
	orange_candle = "minecraft:orange_candle"
	orange_candle_cake = "minecraft:orange_candle_cake"
	orange_carpet = "minecraft:orange_carpet"
	orange_concrete = "minecraft:orange_concrete"
	orange_concrete_powder = "minecraft:orange_concrete_powder"
	orange_glazed_terracotta = "minecraft:orange_glazed_terracotta"
	orange_shulker_box = "minecraft:orange_shulker_box"
	orange_stained_glass = "minecraft:orange_stained_glass"
	orange_stained_glass_pane = "minecraft:orange_stained_glass_pane"
	orange_terracotta = "minecraft:orange_terracotta"
	orange_tulip = "minecraft:orange_tulip"
	orange_wall_banner = "minecraft:orange_wall_banner"
	orange_wool = "minecraft:orange_wool"
	oxeye_daisy = "minecraft:oxeye_daisy"
	oxidized_copper = "minecraft:oxidized_copper"
	oxidized_cut_copper = "minecraft:oxidized_cut_copper"
	oxidized_cut_copper_slab = "minecraft:oxidized_cut_copper_slab"
	oxidized_cut_copper_stairs = "minecraft:oxidized_cut_copper_stairs"
	packed_ice = "minecraft:packed_ice"
	peony = "minecraft:peony"
	petrified_oak_slab = "minecraft:petrified_oak_slab"
	pink_banner = "minecraft:pink_banner"
	pink_bed = "minecraft:pink_bed"
	pink_candle = "minecraft:pink_candle"
	pink_candle_cake = "minecraft:pink_candle_cake"
	pink_carpet = "minecraft:pink_carpet"
	pink_concrete = "minecraft:pink_concrete"
	pink_concrete_powder = "minecraft:pink_concrete_powder"
	pink_glazed_terracotta = "minecraft:pink_glazed_terracotta"
	pink_shulker_box = "minecraft:pink_shulker_box"
	pink_stained_glass = "minecraft:pink_stained_glass"
	pink_stained_glass_pane = "minecraft:pink_stained_glass_pane"
	pink_terracotta = "minecraft:pink_terracotta"
	pink_tulip = "minecraft:pink_tulip"
	pink_wall_banner = "minecraft:pink_wall_banner"
	pink_wool = "minecraft:pink_wool"
	piston = "minecraft:piston"
	piston_head = "minecraft:piston_head"
	player_head = "minecraft:player_head"
	player_wall_head = "minecraft:player_wall_head"
	podzol = "minecraft:podzol"
	pointed_dripstone = "minecraft:pointed_dripstone"
	polished_andesite = "minecraft:polished_andesite"
	polished_andesite_slab = "minecraft:polished_andesite_slab"
	polished_andesite_stairs = "minecraft:polished_andesite_stairs"
	polished_basalt = "minecraft:polished_basalt"
	polished_blackstone = "minecraft:polished_blackstone"
	polished_blackstone_brick_slab = "minecraft:polished_blackstone_brick_slab"
	polished_blackstone_brick_stairs = "minecraft:polished_blackstone_brick_stairs"
	polished_blackstone_brick_wall = "minecraft:polished_blackstone_brick_wall"
	polished_blackstone_bricks = "minecraft:polished_blackstone_bricks"
	polished_blackstone_button = "minecraft:polished_blackstone_button"
	polished_blackstone_pressure_plate = "minecraft:polished_blackstone_pressure_plate"
	polished_blackstone_slab = "minecraft:polished_blackstone_slab"
	polished_blackstone_stairs = "minecraft:polished_blackstone_stairs"
	polished_blackstone_wall = "minecraft:polished_blackstone_wall"
	polished_deepslate = "minecraft:polished_deepslate"
	polished_deepslate_slab = "minecraft:polished_deepslate_slab"
	polished_deepslate_stairs = "minecraft:polished_deepslate_stairs"
	polished_deepslate_wall = "minecraft:polished_deepslate_wall"
	polished_diorite = "minecraft:polished_diorite"
	polished_diorite_slab = "minecraft:polished_diorite_slab"
	polished_diorite_stairs = "minecraft:polished_diorite_stairs"
	polished_granite = "minecraft:polished_granite"
	polished_granite_slab = "minecraft:polished_granite_slab"
	polished_granite_stairs = "minecraft:polished_granite_stairs"
	poppy = "minecraft:poppy"
	potatoes = "minecraft:potatoes"
	potted_acacia_sapling = "minecraft:potted_acacia_sapling"
	potted_allium = "minecraft:potted_allium"
	potted_azalea_bush = "minecraft:potted_azalea_bush"
	potted_azure_bluet = "minecraft:potted_azure_bluet"
	potted_bamboo = "minecraft:potted_bamboo"
	potted_birch_sapling = "minecraft:potted_birch_sapling"
	potted_blue_orchid = "minecraft:potted_blue_orchid"
	potted_brown_mushroom = "minecraft:potted_brown_mushroom"
	potted_cactus = "minecraft:potted_cactus"
	potted_cornflower = "minecraft:potted_cornflower"
	potted_crimson_fungus = "minecraft:potted_crimson_fungus"
	potted_crimson_roots = "minecraft:potted_crimson_roots"
	potted_dandelion = "minecraft:potted_dandelion"
	potted_dark_oak_sapling = "minecraft:potted_dark_oak_sapling"
	potted_dead_bush = "minecraft:potted_dead_bush"
	potted_fern = "minecraft:potted_fern"
	potted_flowering_azalea_bush = "minecraft:potted_flowering_azalea_bush"
	potted_jungle_sapling = "minecraft:potted_jungle_sapling"
	potted_lily_of_the_valley = "minecraft:potted_lily_of_the_valley"
	potted_oak_sapling = "minecraft:potted_oak_sapling"
	potted_orange_tulip = "minecraft:potted_orange_tulip"
	potted_oxeye_daisy = "minecraft:potted_oxeye_daisy"
	potted_pink_tulip = "minecraft:potted_pink_tulip"
	potted_poppy = "minecraft:potted_poppy"
	potted_red_mushroom = "minecraft:potted_red_mushroom"
	potted_red_tulip = "minecraft:potted_red_tulip"
	potted_spruce_sapling = "minecraft:potted_spruce_sapling"
	potted_warped_fungus = "minecraft:potted_warped_fungus"
	potted_warped_roots = "minecraft:potted_warped_roots"
	potted_white_tulip = "minecraft:potted_white_tulip"
	potted_wither_rose = "minecraft:potted_wither_rose"
	powder_snow = "minecraft:powder_snow"
	powder_snow_cauldron = "minecraft:powder_snow_cauldron"
	powered_rail = "minecraft:powered_rail"
	prismarine = "minecraft:prismarine"
	prismarine_brick_slab = "minecraft:prismarine_brick_slab"
	prismarine_brick_stairs = "minecraft:prismarine_brick_stairs"
	prismarine_bricks = "minecraft:prismarine_bricks"
	prismarine_slab = "minecraft:prismarine_slab"
	prismarine_stairs = "minecraft:prismarine_stairs"
	prismarine_wall = "minecraft:prismarine_wall"
	pumpkin = "minecraft:pumpkin"
	pumpkin_stem = "minecraft:pumpkin_stem"
	purple_banner = "minecraft:purple_banner"
	purple_bed = "minecraft:purple_bed"
	purple_candle = "minecraft:purple_candle"
	purple_candle_cake = "minecraft:purple_candle_cake"
	purple_carpet = "minecraft:purple_carpet"
	purple_concrete = "minecraft:purple_concrete"
	purple_concrete_powder = "minecraft:purple_concrete_powder"
	purple_glazed_terracotta = "minecraft:purple_glazed_terracotta"
	purple_shulker_box = "minecraft:purple_shulker_box"
	purple_stained_glass = "minecraft:purple_stained_glass"
	purple_stained_glass_pane = "minecraft:purple_stained_glass_pane"
	purple_terracotta = "minecraft:purple_terracotta"
	purple_wall_banner = "minecraft:purple_wall_banner"
	purple_wool = "minecraft:purple_wool"
	purpur_block = "minecraft:purpur_block"
	purpur_pillar = "minecraft:purpur_pillar"
	purpur_slab = "minecraft:purpur_slab"
	purpur_stairs = "minecraft:purpur_stairs"
	quartz_block = "minecraft:quartz_block"
	quartz_bricks = "minecraft:quartz_bricks"
	quartz_pillar = "minecraft:quartz_pillar"
	quartz_slab = "minecraft:quartz_slab"
	quartz_stairs = "minecraft:quartz_stairs"
	rail = "minecraft:rail"
	raw_copper_block = "minecraft:raw_copper_block"
	raw_gold_block = "minecraft:raw_gold_block"
	raw_iron_block = "minecraft:raw_iron_block"
	red_banner = "minecraft:red_banner"
	red_bed = "minecraft:red_bed"
	red_candle = "minecraft:red_candle"
	red_candle_cake = "minecraft:red_candle_cake"
	red_carpet = "minecraft:red_carpet"
	red_concrete = "minecraft:red_concrete"
	red_concrete_powder = "minecraft:red_concrete_powder"
	red_glazed_terracotta = "minecraft:red_glazed_terracotta"
	red_mushroom = "minecraft:red_mushroom"
	red_mushroom_block = "minecraft:red_mushroom_block"
	red_nether_brick_slab = "minecraft:red_nether_brick_slab"
	red_nether_brick_stairs = "minecraft:red_nether_brick_stairs"
	red_nether_brick_wall = "minecraft:red_nether_brick_wall"
	red_nether_bricks = "minecraft:red_nether_bricks"
	red_sand = "minecraft:red_sand"
	red_sandstone = "minecraft:red_sandstone"
	red_sandstone_slab = "minecraft:red_sandstone_slab"
	red_sandstone_stairs = "minecraft:red_sandstone_stairs"
	red_sandstone_wall = "minecraft:red_sandstone_wall"
	red_shulker_box = "minecraft:red_shulker_box"
	red_stained_glass = "minecraft:red_stained_glass"
	red_stained_glass_pane = "minecraft:red_stained_glass_pane"
	red_terracotta = "minecraft:red_terracotta"
	red_tulip = "minecraft:red_tulip"
	red_wall_banner = "minecraft:red_wall_banner"
	red_wool = "minecraft:red_wool"
	redstone_block = "minecraft:redstone_block"
	redstone_lamp = "minecraft:redstone_lamp"
	redstone_ore = "minecraft:redstone_ore"
	redstone_torch = "minecraft:redstone_torch"
	redstone_wall_torch = "minecraft:redstone_wall_torch"
	redstone_wire = "minecraft:redstone_wire"
	repeater = "minecraft:repeater"
	repeating_command_block = "minecraft:repeating_command_block"
	respawn_anchor = "minecraft:respawn_anchor"
	rooted_dirt = "minecraft:rooted_dirt"
	rose_bush = "minecraft:rose_bush"
	sand = "minecraft:sand"
	sandstone = "minecraft:sandstone"
	sandstone_slab = "minecraft:sandstone_slab"
	sandstone_stairs = "minecraft:sandstone_stairs"
	sandstone_wall = "minecraft:sandstone_wall"
	scaffolding = "minecraft:scaffolding"
	sculk_sensor = "minecraft:sculk_sensor"
	sea_lantern = "minecraft:sea_lantern"
	sea_pickle = "minecraft:sea_pickle"
	seagrass = "minecraft:seagrass"
	shroomlight = "minecraft:shroomlight"
	shulker_box = "minecraft:shulker_box"
	skeleton_skull = "minecraft:skeleton_skull"
	skeleton_wall_skull = "minecraft:skeleton_wall_skull"
	slime_block = "minecraft:slime_block"
	small_amethyst_bud = "minecraft:small_amethyst_bud"
	small_dripleaf = "minecraft:small_dripleaf"
	smithing_table = "minecraft:smithing_table"
	smoker = "minecraft:smoker"
	smooth_basalt = "minecraft:smooth_basalt"
	smooth_quartz = "minecraft:smooth_quartz"
	smooth_quartz_slab = "minecraft:smooth_quartz_slab"
	smooth_quartz_stairs = "minecraft:smooth_quartz_stairs"
	smooth_red_sandstone = "minecraft:smooth_red_sandstone"
	smooth_red_sandstone_slab = "minecraft:smooth_red_sandstone_slab"
	smooth_red_sandstone_stairs = "minecraft:smooth_red_sandstone_stairs"
	smooth_sandstone = "minecraft:smooth_sandstone"
	smooth_sandstone_slab = "minecraft:smooth_sandstone_slab"
	smooth_sandstone_stairs = "minecraft:smooth_sandstone_stairs"
	smooth_stone = "minecraft:smooth_stone"
	smooth_stone_slab = "minecraft:smooth_stone_slab"
	snow = "minecraft:snow"
	snow_block = "minecraft:snow_block"
	soul_campfire = "minecraft:soul_campfire"
	soul_fire = "minecraft:soul_fire"
	soul_lantern = "minecraft:soul_lantern"
	soul_sand = "minecraft:soul_sand"
	soul_soil = "minecraft:soul_soil"
	soul_torch = "minecraft:soul_torch"
	soul_wall_torch = "minecraft:soul_wall_torch"
	spawner = "minecraft:spawner"
	sponge = "minecraft:sponge"
	spore_blossom = "minecraft:spore_blossom"
	spruce_button = "minecraft:spruce_button"
	spruce_door = "minecraft:spruce_door"
	spruce_fence = "minecraft:spruce_fence"
	spruce_fence_gate = "minecraft:spruce_fence_gate"
	spruce_leaves = "minecraft:spruce_leaves"
	spruce_log = "minecraft:spruce_log"
	spruce_planks = "minecraft:spruce_planks"
	spruce_pressure_plate = "minecraft:spruce_pressure_plate"
	spruce_sapling = "minecraft:spruce_sapling"
	spruce_sign = "minecraft:spruce_sign"
	spruce_slab = "minecraft:spruce_slab"
	spruce_stairs = "minecraft:spruce_stairs"
	spruce_trapdoor = "minecraft:spruce_trapdoor"
	spruce_wall_sign = "minecraft:spruce_wall_sign"
	spruce_wood = "minecraft:spruce_wood"
	sticky_piston = "minecraft:sticky_piston"
	stone = "minecraft:stone"
	stone_brick_slab = "minecraft:stone_brick_slab"
	stone_brick_stairs = "minecraft:stone_brick_stairs"
	stone_brick_wall = "minecraft:stone_brick_wall"
	stone_bricks = "minecraft:stone_bricks"
	stone_button = "minecraft:stone_button"
	stone_pressure_plate = "minecraft:stone_pressure_plate"
	stone_slab = "minecraft:stone_slab"
	stone_stairs = "minecraft:stone_stairs"
	stonecutter = "minecraft:stonecutter"
	stripped_acacia_log = "minecraft:stripped_acacia_log"
	stripped_acacia_wood = "minecraft:stripped_acacia_wood"
	stripped_birch_log = "minecraft:stripped_birch_log"
	stripped_birch_wood = "minecraft:stripped_birch_wood"
	stripped_crimson_hyphae = "minecraft:stripped_crimson_hyphae"
	stripped_crimson_stem = "minecraft:stripped_crimson_stem"
	stripped_dark_oak_log = "minecraft:stripped_dark_oak_log"
	stripped_dark_oak_wood = "minecraft:stripped_dark_oak_wood"
	stripped_jungle_log = "minecraft:stripped_jungle_log"
	stripped_jungle_wood = "minecraft:stripped_jungle_wood"
	stripped_oak_log = "minecraft:stripped_oak_log"
	stripped_oak_wood = "minecraft:stripped_oak_wood"
	stripped_spruce_log = "minecraft:stripped_spruce_log"
	stripped_spruce_wood = "minecraft:stripped_spruce_wood"
	stripped_warped_hyphae = "minecraft:stripped_warped_hyphae"
	stripped_warped_stem = "minecraft:stripped_warped_stem"
	structure_block = "minecraft:structure_block"
	structure_void = "minecraft:structure_void"
	sugar_cane = "minecraft:sugar_cane"
	sunflower = "minecraft:sunflower"
	sweet_berry_bush = "minecraft:sweet_berry_bush"
	tall_grass = "minecraft:tall_grass"
	tall_seagrass = "minecraft:tall_seagrass"
	target = "minecraft:target"
	terracotta = "minecraft:terracotta"
	tinted_glass = "minecraft:tinted_glass"
	tnt = "minecraft:tnt"
	torch = "minecraft:torch"
	trapped_chest = "minecraft:trapped_chest"
	tripwire = "minecraft:tripwire"
	tripwire_hook = "minecraft:tripwire_hook"
	tube_coral = "minecraft:tube_coral"
	tube_coral_block = "minecraft:tube_coral_block"
	tube_coral_fan = "minecraft:tube_coral_fan"
	tube_coral_wall_fan = "minecraft:tube_coral_wall_fan"
	tuff = "minecraft:tuff"
	turtle_egg = "minecraft:turtle_egg"
	twisting_vines = "minecraft:twisting_vines"
	twisting_vines_plant = "minecraft:twisting_vines_plant"
	vine = "minecraft:vine"
	void_air = "minecraft:void_air"
	wall_torch = "minecraft:wall_torch"
	warped_button = "minecraft:warped_button"
	warped_door = "minecraft:warped_door"
	warped_fence = "minecraft:warped_fence"
	warped_fence_gate = "minecraft:warped_fence_gate"
	warped_fungus = "minecraft:warped_fungus"
	warped_hyphae = "minecraft:warped_hyphae"
	warped_nylium = "minecraft:warped_nylium"
	warped_planks = "minecraft:warped_planks"
	warped_pressure_plate = "minecraft:warped_pressure_plate"
	warped_roots = "minecraft:warped_roots"
	warped_sign = "minecraft:warped_sign"
	warped_slab = "minecraft:warped_slab"
	warped_stairs = "minecraft:warped_stairs"
	warped_stem = "minecraft:warped_stem"
	warped_trapdoor = "minecraft:warped_trapdoor"
	warped_wall_sign = "minecraft:warped_wall_sign"
	warped_wart_block = "minecraft:warped_wart_block"
	water = "minecraft:water"
	water_cauldron = "minecraft:water_cauldron"
	waxed_copper_block = "minecraft:waxed_copper_block"
	waxed_cut_copper = "minecraft:waxed_cut_copper"
	waxed_cut_copper_slab = "minecraft:waxed_cut_copper_slab"
	waxed_cut_copper_stairs = "minecraft:waxed_cut_copper_stairs"
	waxed_exposed_copper = "minecraft:waxed_exposed_copper"
	waxed_exposed_cut_copper = "minecraft:waxed_exposed_cut_copper"
	waxed_exposed_cut_copper_slab = "minecraft:waxed_exposed_cut_copper_slab"
	waxed_exposed_cut_copper_stairs = "minecraft:waxed_exposed_cut_copper_stairs"
	waxed_oxidized_copper = "minecraft:waxed_oxidized_copper"
	waxed_oxidized_cut_copper = "minecraft:waxed_oxidized_cut_copper"
	waxed_oxidized_cut_copper_slab = "minecraft:waxed_oxidized_cut_copper_slab"
	waxed_oxidized_cut_copper_stairs = "minecraft:waxed_oxidized_cut_copper_stairs"
	waxed_weathered_copper = "minecraft:waxed_weathered_copper"
	waxed_weathered_cut_copper = "minecraft:waxed_weathered_cut_copper"
	waxed_weathered_cut_copper_slab = "minecraft:waxed_weathered_cut_copper_slab"
	waxed_weathered_cut_copper_stairs = "minecraft:waxed_weathered_cut_copper_stairs"
	weathered_copper = "minecraft:weathered_copper"
	weathered_cut_copper = "minecraft:weathered_cut_copper"
	weathered_cut_copper_slab = "minecraft:weathered_cut_copper_slab"
	weathered_cut_copper_stairs = "minecraft:weathered_cut_copper_stairs"
	weeping_vines = "minecraft:weeping_vines"
	weeping_vines_plant = "minecraft:weeping_vines_plant"
	wet_sponge = "minecraft:wet_sponge"
	wheat = "minecraft:wheat"
	white_banner = "minecraft:white_banner"
	white_bed = "minecraft:white_bed"
	white_candle = "minecraft:white_candle"
	white_candle_cake = "minecraft:white_candle_cake"
	white_carpet = "minecraft:white_carpet"
	white_concrete = "minecraft:white_concrete"
	white_concrete_powder = "minecraft:white_concrete_powder"
	white_glazed_terracotta = "minecraft:white_glazed_terracotta"
	white_shulker_box = "minecraft:white_shulker_box"
	white_stained_glass = "minecraft:white_stained_glass"
	white_stained_glass_pane = "minecraft:white_stained_glass_pane"
	white_terracotta = "minecraft:white_terracotta"
	white_tulip = "minecraft:white_tulip"
	white_wall_banner = "minecraft:white_wall_banner"
	white_wool = "minecraft:white_wool"
	wither_rose = "minecraft:wither_rose"
	wither_skeleton_skull = "minecraft:wither_skeleton_skull"
	wither_skeleton_wall_skull = "minecraft:wither_skeleton_wall_skull"
	yellow_banner = "minecraft:yellow_banner"
	yellow_bed = "minecraft:yellow_bed"
	yellow_candle = "minecraft:yellow_candle"
	yellow_candle_cake = "minecraft:yellow_candle_cake"
	yellow_carpet = "minecraft:yellow_carpet"
	yellow_concrete = "minecraft:yellow_concrete"
	yellow_concrete_powder = "minecraft:yellow_concrete_powder"
	yellow_glazed_terracotta = "minecraft:yellow_glazed_terracotta"
	yellow_shulker_box = "minecraft:yellow_shulker_box"
	yellow_stained_glass = "minecraft:yellow_stained_glass"
	yellow_stained_glass_pane = "minecraft:yellow_stained_glass_pane"
	yellow_terracotta = "minecraft:yellow_terracotta"
	yellow_wall_banner = "minecraft:yellow_wall_banner"
	yellow_wool = "minecraft:yellow_wool"
	zombie_head = "minecraft:zombie_head"
	zombie_wall_head = "minecraft:zombie_wall_head"
