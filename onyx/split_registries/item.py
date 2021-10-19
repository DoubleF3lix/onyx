import enum


class item(enum.Enum):
	"""
	item

	* acacia_boat
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
	* acacia_wood
	* activator_rail
	* air
	* allium
	* amethyst_block
	* amethyst_cluster
	* amethyst_shard
	* ancient_debris
	* andesite
	* andesite_slab
	* andesite_stairs
	* andesite_wall
	* anvil
	* apple
	* armor_stand
	* arrow
	* axolotl_bucket
	* axolotl_spawn_egg
	* azalea
	* azalea_leaves
	* azure_bluet
	* baked_potato
	* bamboo
	* barrel
	* barrier
	* basalt
	* bat_spawn_egg
	* beacon
	* bedrock
	* bee_nest
	* bee_spawn_egg
	* beef
	* beehive
	* beetroot
	* beetroot_seeds
	* beetroot_soup
	* bell
	* big_dripleaf
	* birch_boat
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
	* birch_wood
	* black_banner
	* black_bed
	* black_candle
	* black_carpet
	* black_concrete
	* black_concrete_powder
	* black_dye
	* black_glazed_terracotta
	* black_shulker_box
	* black_stained_glass
	* black_stained_glass_pane
	* black_terracotta
	* black_wool
	* blackstone
	* blackstone_slab
	* blackstone_stairs
	* blackstone_wall
	* blast_furnace
	* blaze_powder
	* blaze_rod
	* blaze_spawn_egg
	* blue_banner
	* blue_bed
	* blue_candle
	* blue_carpet
	* blue_concrete
	* blue_concrete_powder
	* blue_dye
	* blue_glazed_terracotta
	* blue_ice
	* blue_orchid
	* blue_shulker_box
	* blue_stained_glass
	* blue_stained_glass_pane
	* blue_terracotta
	* blue_wool
	* bone
	* bone_block
	* bone_meal
	* book
	* bookshelf
	* bow
	* bowl
	* brain_coral
	* brain_coral_block
	* brain_coral_fan
	* bread
	* brewing_stand
	* brick
	* brick_slab
	* brick_stairs
	* brick_wall
	* bricks
	* brown_banner
	* brown_bed
	* brown_candle
	* brown_carpet
	* brown_concrete
	* brown_concrete_powder
	* brown_dye
	* brown_glazed_terracotta
	* brown_mushroom
	* brown_mushroom_block
	* brown_shulker_box
	* brown_stained_glass
	* brown_stained_glass_pane
	* brown_terracotta
	* brown_wool
	* bubble_coral
	* bubble_coral_block
	* bubble_coral_fan
	* bucket
	* budding_amethyst
	* bundle
	* cactus
	* cake
	* calcite
	* campfire
	* candle
	* carrot
	* carrot_on_a_stick
	* cartography_table
	* carved_pumpkin
	* cat_spawn_egg
	* cauldron
	* cave_spider_spawn_egg
	* chain
	* chain_command_block
	* chainmail_boots
	* chainmail_chestplate
	* chainmail_helmet
	* chainmail_leggings
	* charcoal
	* chest
	* chest_minecart
	* chicken
	* chicken_spawn_egg
	* chipped_anvil
	* chiseled_deepslate
	* chiseled_nether_bricks
	* chiseled_polished_blackstone
	* chiseled_quartz_block
	* chiseled_red_sandstone
	* chiseled_sandstone
	* chiseled_stone_bricks
	* chorus_flower
	* chorus_fruit
	* chorus_plant
	* clay
	* clay_ball
	* clock
	* coal
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
	* cocoa_beans
	* cod
	* cod_bucket
	* cod_spawn_egg
	* command_block
	* command_block_minecart
	* comparator
	* compass
	* composter
	* conduit
	* cooked_beef
	* cooked_chicken
	* cooked_cod
	* cooked_mutton
	* cooked_porkchop
	* cooked_rabbit
	* cooked_salmon
	* cookie
	* copper_block
	* copper_ingot
	* copper_ore
	* cornflower
	* cow_spawn_egg
	* cracked_deepslate_bricks
	* cracked_deepslate_tiles
	* cracked_nether_bricks
	* cracked_polished_blackstone_bricks
	* cracked_stone_bricks
	* crafting_table
	* creeper_banner_pattern
	* creeper_head
	* creeper_spawn_egg
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
	* crossbow
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
	* cyan_carpet
	* cyan_concrete
	* cyan_concrete_powder
	* cyan_dye
	* cyan_glazed_terracotta
	* cyan_shulker_box
	* cyan_stained_glass
	* cyan_stained_glass_pane
	* cyan_terracotta
	* cyan_wool
	* damaged_anvil
	* dandelion
	* dark_oak_boat
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
	* dark_oak_wood
	* dark_prismarine
	* dark_prismarine_slab
	* dark_prismarine_stairs
	* daylight_detector
	* dead_brain_coral
	* dead_brain_coral_block
	* dead_brain_coral_fan
	* dead_bubble_coral
	* dead_bubble_coral_block
	* dead_bubble_coral_fan
	* dead_bush
	* dead_fire_coral
	* dead_fire_coral_block
	* dead_fire_coral_fan
	* dead_horn_coral
	* dead_horn_coral_block
	* dead_horn_coral_fan
	* dead_tube_coral
	* dead_tube_coral_block
	* dead_tube_coral_fan
	* debug_stick
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
	* diamond
	* diamond_axe
	* diamond_block
	* diamond_boots
	* diamond_chestplate
	* diamond_helmet
	* diamond_hoe
	* diamond_horse_armor
	* diamond_leggings
	* diamond_ore
	* diamond_pickaxe
	* diamond_shovel
	* diamond_sword
	* diorite
	* diorite_slab
	* diorite_stairs
	* diorite_wall
	* dirt
	* dirt_path
	* dispenser
	* dolphin_spawn_egg
	* donkey_spawn_egg
	* dragon_breath
	* dragon_egg
	* dragon_head
	* dried_kelp
	* dried_kelp_block
	* dripstone_block
	* dropper
	* drowned_spawn_egg
	* egg
	* elder_guardian_spawn_egg
	* elytra
	* emerald
	* emerald_block
	* emerald_ore
	* enchanted_book
	* enchanted_golden_apple
	* enchanting_table
	* end_crystal
	* end_portal_frame
	* end_rod
	* end_stone
	* end_stone_brick_slab
	* end_stone_brick_stairs
	* end_stone_brick_wall
	* end_stone_bricks
	* ender_chest
	* ender_eye
	* ender_pearl
	* enderman_spawn_egg
	* endermite_spawn_egg
	* evoker_spawn_egg
	* experience_bottle
	* exposed_copper
	* exposed_cut_copper
	* exposed_cut_copper_slab
	* exposed_cut_copper_stairs
	* farmland
	* feather
	* fermented_spider_eye
	* fern
	* filled_map
	* fire_charge
	* fire_coral
	* fire_coral_block
	* fire_coral_fan
	* firework_rocket
	* firework_star
	* fishing_rod
	* fletching_table
	* flint
	* flint_and_steel
	* flower_banner_pattern
	* flower_pot
	* flowering_azalea
	* flowering_azalea_leaves
	* fox_spawn_egg
	* furnace
	* furnace_minecart
	* ghast_spawn_egg
	* ghast_tear
	* gilded_blackstone
	* glass
	* glass_bottle
	* glass_pane
	* glistering_melon_slice
	* globe_banner_pattern
	* glow_berries
	* glow_ink_sac
	* glow_item_frame
	* glow_lichen
	* glow_squid_spawn_egg
	* glowstone
	* glowstone_dust
	* goat_spawn_egg
	* gold_block
	* gold_ingot
	* gold_nugget
	* gold_ore
	* golden_apple
	* golden_axe
	* golden_boots
	* golden_carrot
	* golden_chestplate
	* golden_helmet
	* golden_hoe
	* golden_horse_armor
	* golden_leggings
	* golden_pickaxe
	* golden_shovel
	* golden_sword
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
	* gray_carpet
	* gray_concrete
	* gray_concrete_powder
	* gray_dye
	* gray_glazed_terracotta
	* gray_shulker_box
	* gray_stained_glass
	* gray_stained_glass_pane
	* gray_terracotta
	* gray_wool
	* green_banner
	* green_bed
	* green_candle
	* green_carpet
	* green_concrete
	* green_concrete_powder
	* green_dye
	* green_glazed_terracotta
	* green_shulker_box
	* green_stained_glass
	* green_stained_glass_pane
	* green_terracotta
	* green_wool
	* grindstone
	* guardian_spawn_egg
	* gunpowder
	* hanging_roots
	* hay_block
	* heart_of_the_sea
	* heavy_weighted_pressure_plate
	* hoglin_spawn_egg
	* honey_block
	* honey_bottle
	* honeycomb
	* honeycomb_block
	* hopper
	* hopper_minecart
	* horn_coral
	* horn_coral_block
	* horn_coral_fan
	* horse_spawn_egg
	* husk_spawn_egg
	* ice
	* infested_chiseled_stone_bricks
	* infested_cobblestone
	* infested_cracked_stone_bricks
	* infested_deepslate
	* infested_mossy_stone_bricks
	* infested_stone
	* infested_stone_bricks
	* ink_sac
	* iron_axe
	* iron_bars
	* iron_block
	* iron_boots
	* iron_chestplate
	* iron_door
	* iron_helmet
	* iron_hoe
	* iron_horse_armor
	* iron_ingot
	* iron_leggings
	* iron_nugget
	* iron_ore
	* iron_pickaxe
	* iron_shovel
	* iron_sword
	* iron_trapdoor
	* item_frame
	* jack_o_lantern
	* jigsaw
	* jukebox
	* jungle_boat
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
	* jungle_wood
	* kelp
	* knowledge_book
	* ladder
	* lantern
	* lapis_block
	* lapis_lazuli
	* lapis_ore
	* large_amethyst_bud
	* large_fern
	* lava_bucket
	* lead
	* leather
	* leather_boots
	* leather_chestplate
	* leather_helmet
	* leather_horse_armor
	* leather_leggings
	* lectern
	* lever
	* light
	* light_blue_banner
	* light_blue_bed
	* light_blue_candle
	* light_blue_carpet
	* light_blue_concrete
	* light_blue_concrete_powder
	* light_blue_dye
	* light_blue_glazed_terracotta
	* light_blue_shulker_box
	* light_blue_stained_glass
	* light_blue_stained_glass_pane
	* light_blue_terracotta
	* light_blue_wool
	* light_gray_banner
	* light_gray_bed
	* light_gray_candle
	* light_gray_carpet
	* light_gray_concrete
	* light_gray_concrete_powder
	* light_gray_dye
	* light_gray_glazed_terracotta
	* light_gray_shulker_box
	* light_gray_stained_glass
	* light_gray_stained_glass_pane
	* light_gray_terracotta
	* light_gray_wool
	* light_weighted_pressure_plate
	* lightning_rod
	* lilac
	* lily_of_the_valley
	* lily_pad
	* lime_banner
	* lime_bed
	* lime_candle
	* lime_carpet
	* lime_concrete
	* lime_concrete_powder
	* lime_dye
	* lime_glazed_terracotta
	* lime_shulker_box
	* lime_stained_glass
	* lime_stained_glass_pane
	* lime_terracotta
	* lime_wool
	* lingering_potion
	* llama_spawn_egg
	* lodestone
	* loom
	* magenta_banner
	* magenta_bed
	* magenta_candle
	* magenta_carpet
	* magenta_concrete
	* magenta_concrete_powder
	* magenta_dye
	* magenta_glazed_terracotta
	* magenta_shulker_box
	* magenta_stained_glass
	* magenta_stained_glass_pane
	* magenta_terracotta
	* magenta_wool
	* magma_block
	* magma_cream
	* magma_cube_spawn_egg
	* map
	* medium_amethyst_bud
	* melon
	* melon_seeds
	* melon_slice
	* milk_bucket
	* minecart
	* mojang_banner_pattern
	* mooshroom_spawn_egg
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
	* mule_spawn_egg
	* mushroom_stem
	* mushroom_stew
	* music_disc_11
	* music_disc_13
	* music_disc_blocks
	* music_disc_cat
	* music_disc_chirp
	* music_disc_far
	* music_disc_mall
	* music_disc_mellohi
	* music_disc_pigstep
	* music_disc_stal
	* music_disc_strad
	* music_disc_wait
	* music_disc_ward
	* mutton
	* mycelium
	* name_tag
	* nautilus_shell
	* nether_brick
	* nether_brick_fence
	* nether_brick_slab
	* nether_brick_stairs
	* nether_brick_wall
	* nether_bricks
	* nether_gold_ore
	* nether_quartz_ore
	* nether_sprouts
	* nether_star
	* nether_wart
	* nether_wart_block
	* netherite_axe
	* netherite_block
	* netherite_boots
	* netherite_chestplate
	* netherite_helmet
	* netherite_hoe
	* netherite_ingot
	* netherite_leggings
	* netherite_pickaxe
	* netherite_scrap
	* netherite_shovel
	* netherite_sword
	* netherrack
	* note_block
	* oak_boat
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
	* oak_wood
	* observer
	* obsidian
	* ocelot_spawn_egg
	* orange_banner
	* orange_bed
	* orange_candle
	* orange_carpet
	* orange_concrete
	* orange_concrete_powder
	* orange_dye
	* orange_glazed_terracotta
	* orange_shulker_box
	* orange_stained_glass
	* orange_stained_glass_pane
	* orange_terracotta
	* orange_tulip
	* orange_wool
	* oxeye_daisy
	* oxidized_copper
	* oxidized_cut_copper
	* oxidized_cut_copper_slab
	* oxidized_cut_copper_stairs
	* packed_ice
	* painting
	* panda_spawn_egg
	* paper
	* parrot_spawn_egg
	* peony
	* petrified_oak_slab
	* phantom_membrane
	* phantom_spawn_egg
	* pig_spawn_egg
	* piglin_banner_pattern
	* piglin_brute_spawn_egg
	* piglin_spawn_egg
	* pillager_spawn_egg
	* pink_banner
	* pink_bed
	* pink_candle
	* pink_carpet
	* pink_concrete
	* pink_concrete_powder
	* pink_dye
	* pink_glazed_terracotta
	* pink_shulker_box
	* pink_stained_glass
	* pink_stained_glass_pane
	* pink_terracotta
	* pink_tulip
	* pink_wool
	* piston
	* player_head
	* podzol
	* pointed_dripstone
	* poisonous_potato
	* polar_bear_spawn_egg
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
	* popped_chorus_fruit
	* poppy
	* porkchop
	* potato
	* potion
	* powder_snow_bucket
	* powered_rail
	* prismarine
	* prismarine_brick_slab
	* prismarine_brick_stairs
	* prismarine_bricks
	* prismarine_crystals
	* prismarine_shard
	* prismarine_slab
	* prismarine_stairs
	* prismarine_wall
	* pufferfish
	* pufferfish_bucket
	* pufferfish_spawn_egg
	* pumpkin
	* pumpkin_pie
	* pumpkin_seeds
	* purple_banner
	* purple_bed
	* purple_candle
	* purple_carpet
	* purple_concrete
	* purple_concrete_powder
	* purple_dye
	* purple_glazed_terracotta
	* purple_shulker_box
	* purple_stained_glass
	* purple_stained_glass_pane
	* purple_terracotta
	* purple_wool
	* purpur_block
	* purpur_pillar
	* purpur_slab
	* purpur_stairs
	* quartz
	* quartz_block
	* quartz_bricks
	* quartz_pillar
	* quartz_slab
	* quartz_stairs
	* rabbit
	* rabbit_foot
	* rabbit_hide
	* rabbit_spawn_egg
	* rabbit_stew
	* rail
	* ravager_spawn_egg
	* raw_copper
	* raw_copper_block
	* raw_gold
	* raw_gold_block
	* raw_iron
	* raw_iron_block
	* red_banner
	* red_bed
	* red_candle
	* red_carpet
	* red_concrete
	* red_concrete_powder
	* red_dye
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
	* red_wool
	* redstone
	* redstone_block
	* redstone_lamp
	* redstone_ore
	* redstone_torch
	* repeater
	* repeating_command_block
	* respawn_anchor
	* rooted_dirt
	* rose_bush
	* rotten_flesh
	* saddle
	* salmon
	* salmon_bucket
	* salmon_spawn_egg
	* sand
	* sandstone
	* sandstone_slab
	* sandstone_stairs
	* sandstone_wall
	* scaffolding
	* sculk_sensor
	* scute
	* sea_lantern
	* sea_pickle
	* seagrass
	* shears
	* sheep_spawn_egg
	* shield
	* shroomlight
	* shulker_box
	* shulker_shell
	* shulker_spawn_egg
	* silverfish_spawn_egg
	* skeleton_horse_spawn_egg
	* skeleton_skull
	* skeleton_spawn_egg
	* skull_banner_pattern
	* slime_ball
	* slime_block
	* slime_spawn_egg
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
	* snowball
	* soul_campfire
	* soul_lantern
	* soul_sand
	* soul_soil
	* soul_torch
	* spawner
	* spectral_arrow
	* spider_eye
	* spider_spawn_egg
	* splash_potion
	* sponge
	* spore_blossom
	* spruce_boat
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
	* spruce_wood
	* spyglass
	* squid_spawn_egg
	* stick
	* sticky_piston
	* stone
	* stone_axe
	* stone_brick_slab
	* stone_brick_stairs
	* stone_brick_wall
	* stone_bricks
	* stone_button
	* stone_hoe
	* stone_pickaxe
	* stone_pressure_plate
	* stone_shovel
	* stone_slab
	* stone_stairs
	* stone_sword
	* stonecutter
	* stray_spawn_egg
	* strider_spawn_egg
	* string
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
	* sugar
	* sugar_cane
	* sunflower
	* suspicious_stew
	* sweet_berries
	* tall_grass
	* target
	* terracotta
	* tinted_glass
	* tipped_arrow
	* tnt
	* tnt_minecart
	* torch
	* totem_of_undying
	* trader_llama_spawn_egg
	* trapped_chest
	* trident
	* tripwire_hook
	* tropical_fish
	* tropical_fish_bucket
	* tropical_fish_spawn_egg
	* tube_coral
	* tube_coral_block
	* tube_coral_fan
	* tuff
	* turtle_egg
	* turtle_helmet
	* turtle_spawn_egg
	* twisting_vines
	* vex_spawn_egg
	* villager_spawn_egg
	* vindicator_spawn_egg
	* vine
	* wandering_trader_spawn_egg
	* warped_button
	* warped_door
	* warped_fence
	* warped_fence_gate
	* warped_fungus
	* warped_fungus_on_a_stick
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
	* warped_wart_block
	* water_bucket
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
	* wet_sponge
	* wheat
	* wheat_seeds
	* white_banner
	* white_bed
	* white_candle
	* white_carpet
	* white_concrete
	* white_concrete_powder
	* white_dye
	* white_glazed_terracotta
	* white_shulker_box
	* white_stained_glass
	* white_stained_glass_pane
	* white_terracotta
	* white_tulip
	* white_wool
	* witch_spawn_egg
	* wither_rose
	* wither_skeleton_skull
	* wither_skeleton_spawn_egg
	* wolf_spawn_egg
	* wooden_axe
	* wooden_hoe
	* wooden_pickaxe
	* wooden_shovel
	* wooden_sword
	* writable_book
	* written_book
	* yellow_banner
	* yellow_bed
	* yellow_candle
	* yellow_carpet
	* yellow_concrete
	* yellow_concrete_powder
	* yellow_dye
	* yellow_glazed_terracotta
	* yellow_shulker_box
	* yellow_stained_glass
	* yellow_stained_glass_pane
	* yellow_terracotta
	* yellow_wool
	* zoglin_spawn_egg
	* zombie_head
	* zombie_horse_spawn_egg
	* zombie_spawn_egg
	* zombie_villager_spawn_egg
	* zombified_piglin_spawn_egg
	"""
	acacia_boat = "minecraft:acacia_boat"
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
	acacia_wood = "minecraft:acacia_wood"
	activator_rail = "minecraft:activator_rail"
	air = "minecraft:air"
	allium = "minecraft:allium"
	amethyst_block = "minecraft:amethyst_block"
	amethyst_cluster = "minecraft:amethyst_cluster"
	amethyst_shard = "minecraft:amethyst_shard"
	ancient_debris = "minecraft:ancient_debris"
	andesite = "minecraft:andesite"
	andesite_slab = "minecraft:andesite_slab"
	andesite_stairs = "minecraft:andesite_stairs"
	andesite_wall = "minecraft:andesite_wall"
	anvil = "minecraft:anvil"
	apple = "minecraft:apple"
	armor_stand = "minecraft:armor_stand"
	arrow = "minecraft:arrow"
	axolotl_bucket = "minecraft:axolotl_bucket"
	axolotl_spawn_egg = "minecraft:axolotl_spawn_egg"
	azalea = "minecraft:azalea"
	azalea_leaves = "minecraft:azalea_leaves"
	azure_bluet = "minecraft:azure_bluet"
	baked_potato = "minecraft:baked_potato"
	bamboo = "minecraft:bamboo"
	barrel = "minecraft:barrel"
	barrier = "minecraft:barrier"
	basalt = "minecraft:basalt"
	bat_spawn_egg = "minecraft:bat_spawn_egg"
	beacon = "minecraft:beacon"
	bedrock = "minecraft:bedrock"
	bee_nest = "minecraft:bee_nest"
	bee_spawn_egg = "minecraft:bee_spawn_egg"
	beef = "minecraft:beef"
	beehive = "minecraft:beehive"
	beetroot = "minecraft:beetroot"
	beetroot_seeds = "minecraft:beetroot_seeds"
	beetroot_soup = "minecraft:beetroot_soup"
	bell = "minecraft:bell"
	big_dripleaf = "minecraft:big_dripleaf"
	birch_boat = "minecraft:birch_boat"
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
	birch_wood = "minecraft:birch_wood"
	black_banner = "minecraft:black_banner"
	black_bed = "minecraft:black_bed"
	black_candle = "minecraft:black_candle"
	black_carpet = "minecraft:black_carpet"
	black_concrete = "minecraft:black_concrete"
	black_concrete_powder = "minecraft:black_concrete_powder"
	black_dye = "minecraft:black_dye"
	black_glazed_terracotta = "minecraft:black_glazed_terracotta"
	black_shulker_box = "minecraft:black_shulker_box"
	black_stained_glass = "minecraft:black_stained_glass"
	black_stained_glass_pane = "minecraft:black_stained_glass_pane"
	black_terracotta = "minecraft:black_terracotta"
	black_wool = "minecraft:black_wool"
	blackstone = "minecraft:blackstone"
	blackstone_slab = "minecraft:blackstone_slab"
	blackstone_stairs = "minecraft:blackstone_stairs"
	blackstone_wall = "minecraft:blackstone_wall"
	blast_furnace = "minecraft:blast_furnace"
	blaze_powder = "minecraft:blaze_powder"
	blaze_rod = "minecraft:blaze_rod"
	blaze_spawn_egg = "minecraft:blaze_spawn_egg"
	blue_banner = "minecraft:blue_banner"
	blue_bed = "minecraft:blue_bed"
	blue_candle = "minecraft:blue_candle"
	blue_carpet = "minecraft:blue_carpet"
	blue_concrete = "minecraft:blue_concrete"
	blue_concrete_powder = "minecraft:blue_concrete_powder"
	blue_dye = "minecraft:blue_dye"
	blue_glazed_terracotta = "minecraft:blue_glazed_terracotta"
	blue_ice = "minecraft:blue_ice"
	blue_orchid = "minecraft:blue_orchid"
	blue_shulker_box = "minecraft:blue_shulker_box"
	blue_stained_glass = "minecraft:blue_stained_glass"
	blue_stained_glass_pane = "minecraft:blue_stained_glass_pane"
	blue_terracotta = "minecraft:blue_terracotta"
	blue_wool = "minecraft:blue_wool"
	bone = "minecraft:bone"
	bone_block = "minecraft:bone_block"
	bone_meal = "minecraft:bone_meal"
	book = "minecraft:book"
	bookshelf = "minecraft:bookshelf"
	bow = "minecraft:bow"
	bowl = "minecraft:bowl"
	brain_coral = "minecraft:brain_coral"
	brain_coral_block = "minecraft:brain_coral_block"
	brain_coral_fan = "minecraft:brain_coral_fan"
	bread = "minecraft:bread"
	brewing_stand = "minecraft:brewing_stand"
	brick = "minecraft:brick"
	brick_slab = "minecraft:brick_slab"
	brick_stairs = "minecraft:brick_stairs"
	brick_wall = "minecraft:brick_wall"
	bricks = "minecraft:bricks"
	brown_banner = "minecraft:brown_banner"
	brown_bed = "minecraft:brown_bed"
	brown_candle = "minecraft:brown_candle"
	brown_carpet = "minecraft:brown_carpet"
	brown_concrete = "minecraft:brown_concrete"
	brown_concrete_powder = "minecraft:brown_concrete_powder"
	brown_dye = "minecraft:brown_dye"
	brown_glazed_terracotta = "minecraft:brown_glazed_terracotta"
	brown_mushroom = "minecraft:brown_mushroom"
	brown_mushroom_block = "minecraft:brown_mushroom_block"
	brown_shulker_box = "minecraft:brown_shulker_box"
	brown_stained_glass = "minecraft:brown_stained_glass"
	brown_stained_glass_pane = "minecraft:brown_stained_glass_pane"
	brown_terracotta = "minecraft:brown_terracotta"
	brown_wool = "minecraft:brown_wool"
	bubble_coral = "minecraft:bubble_coral"
	bubble_coral_block = "minecraft:bubble_coral_block"
	bubble_coral_fan = "minecraft:bubble_coral_fan"
	bucket = "minecraft:bucket"
	budding_amethyst = "minecraft:budding_amethyst"
	bundle = "minecraft:bundle"
	cactus = "minecraft:cactus"
	cake = "minecraft:cake"
	calcite = "minecraft:calcite"
	campfire = "minecraft:campfire"
	candle = "minecraft:candle"
	carrot = "minecraft:carrot"
	carrot_on_a_stick = "minecraft:carrot_on_a_stick"
	cartography_table = "minecraft:cartography_table"
	carved_pumpkin = "minecraft:carved_pumpkin"
	cat_spawn_egg = "minecraft:cat_spawn_egg"
	cauldron = "minecraft:cauldron"
	cave_spider_spawn_egg = "minecraft:cave_spider_spawn_egg"
	chain = "minecraft:chain"
	chain_command_block = "minecraft:chain_command_block"
	chainmail_boots = "minecraft:chainmail_boots"
	chainmail_chestplate = "minecraft:chainmail_chestplate"
	chainmail_helmet = "minecraft:chainmail_helmet"
	chainmail_leggings = "minecraft:chainmail_leggings"
	charcoal = "minecraft:charcoal"
	chest = "minecraft:chest"
	chest_minecart = "minecraft:chest_minecart"
	chicken = "minecraft:chicken"
	chicken_spawn_egg = "minecraft:chicken_spawn_egg"
	chipped_anvil = "minecraft:chipped_anvil"
	chiseled_deepslate = "minecraft:chiseled_deepslate"
	chiseled_nether_bricks = "minecraft:chiseled_nether_bricks"
	chiseled_polished_blackstone = "minecraft:chiseled_polished_blackstone"
	chiseled_quartz_block = "minecraft:chiseled_quartz_block"
	chiseled_red_sandstone = "minecraft:chiseled_red_sandstone"
	chiseled_sandstone = "minecraft:chiseled_sandstone"
	chiseled_stone_bricks = "minecraft:chiseled_stone_bricks"
	chorus_flower = "minecraft:chorus_flower"
	chorus_fruit = "minecraft:chorus_fruit"
	chorus_plant = "minecraft:chorus_plant"
	clay = "minecraft:clay"
	clay_ball = "minecraft:clay_ball"
	clock = "minecraft:clock"
	coal = "minecraft:coal"
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
	cocoa_beans = "minecraft:cocoa_beans"
	cod = "minecraft:cod"
	cod_bucket = "minecraft:cod_bucket"
	cod_spawn_egg = "minecraft:cod_spawn_egg"
	command_block = "minecraft:command_block"
	command_block_minecart = "minecraft:command_block_minecart"
	comparator = "minecraft:comparator"
	compass = "minecraft:compass"
	composter = "minecraft:composter"
	conduit = "minecraft:conduit"
	cooked_beef = "minecraft:cooked_beef"
	cooked_chicken = "minecraft:cooked_chicken"
	cooked_cod = "minecraft:cooked_cod"
	cooked_mutton = "minecraft:cooked_mutton"
	cooked_porkchop = "minecraft:cooked_porkchop"
	cooked_rabbit = "minecraft:cooked_rabbit"
	cooked_salmon = "minecraft:cooked_salmon"
	cookie = "minecraft:cookie"
	copper_block = "minecraft:copper_block"
	copper_ingot = "minecraft:copper_ingot"
	copper_ore = "minecraft:copper_ore"
	cornflower = "minecraft:cornflower"
	cow_spawn_egg = "minecraft:cow_spawn_egg"
	cracked_deepslate_bricks = "minecraft:cracked_deepslate_bricks"
	cracked_deepslate_tiles = "minecraft:cracked_deepslate_tiles"
	cracked_nether_bricks = "minecraft:cracked_nether_bricks"
	cracked_polished_blackstone_bricks = "minecraft:cracked_polished_blackstone_bricks"
	cracked_stone_bricks = "minecraft:cracked_stone_bricks"
	crafting_table = "minecraft:crafting_table"
	creeper_banner_pattern = "minecraft:creeper_banner_pattern"
	creeper_head = "minecraft:creeper_head"
	creeper_spawn_egg = "minecraft:creeper_spawn_egg"
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
	crossbow = "minecraft:crossbow"
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
	cyan_carpet = "minecraft:cyan_carpet"
	cyan_concrete = "minecraft:cyan_concrete"
	cyan_concrete_powder = "minecraft:cyan_concrete_powder"
	cyan_dye = "minecraft:cyan_dye"
	cyan_glazed_terracotta = "minecraft:cyan_glazed_terracotta"
	cyan_shulker_box = "minecraft:cyan_shulker_box"
	cyan_stained_glass = "minecraft:cyan_stained_glass"
	cyan_stained_glass_pane = "minecraft:cyan_stained_glass_pane"
	cyan_terracotta = "minecraft:cyan_terracotta"
	cyan_wool = "minecraft:cyan_wool"
	damaged_anvil = "minecraft:damaged_anvil"
	dandelion = "minecraft:dandelion"
	dark_oak_boat = "minecraft:dark_oak_boat"
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
	dark_oak_wood = "minecraft:dark_oak_wood"
	dark_prismarine = "minecraft:dark_prismarine"
	dark_prismarine_slab = "minecraft:dark_prismarine_slab"
	dark_prismarine_stairs = "minecraft:dark_prismarine_stairs"
	daylight_detector = "minecraft:daylight_detector"
	dead_brain_coral = "minecraft:dead_brain_coral"
	dead_brain_coral_block = "minecraft:dead_brain_coral_block"
	dead_brain_coral_fan = "minecraft:dead_brain_coral_fan"
	dead_bubble_coral = "minecraft:dead_bubble_coral"
	dead_bubble_coral_block = "minecraft:dead_bubble_coral_block"
	dead_bubble_coral_fan = "minecraft:dead_bubble_coral_fan"
	dead_bush = "minecraft:dead_bush"
	dead_fire_coral = "minecraft:dead_fire_coral"
	dead_fire_coral_block = "minecraft:dead_fire_coral_block"
	dead_fire_coral_fan = "minecraft:dead_fire_coral_fan"
	dead_horn_coral = "minecraft:dead_horn_coral"
	dead_horn_coral_block = "minecraft:dead_horn_coral_block"
	dead_horn_coral_fan = "minecraft:dead_horn_coral_fan"
	dead_tube_coral = "minecraft:dead_tube_coral"
	dead_tube_coral_block = "minecraft:dead_tube_coral_block"
	dead_tube_coral_fan = "minecraft:dead_tube_coral_fan"
	debug_stick = "minecraft:debug_stick"
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
	diamond = "minecraft:diamond"
	diamond_axe = "minecraft:diamond_axe"
	diamond_block = "minecraft:diamond_block"
	diamond_boots = "minecraft:diamond_boots"
	diamond_chestplate = "minecraft:diamond_chestplate"
	diamond_helmet = "minecraft:diamond_helmet"
	diamond_hoe = "minecraft:diamond_hoe"
	diamond_horse_armor = "minecraft:diamond_horse_armor"
	diamond_leggings = "minecraft:diamond_leggings"
	diamond_ore = "minecraft:diamond_ore"
	diamond_pickaxe = "minecraft:diamond_pickaxe"
	diamond_shovel = "minecraft:diamond_shovel"
	diamond_sword = "minecraft:diamond_sword"
	diorite = "minecraft:diorite"
	diorite_slab = "minecraft:diorite_slab"
	diorite_stairs = "minecraft:diorite_stairs"
	diorite_wall = "minecraft:diorite_wall"
	dirt = "minecraft:dirt"
	dirt_path = "minecraft:dirt_path"
	dispenser = "minecraft:dispenser"
	dolphin_spawn_egg = "minecraft:dolphin_spawn_egg"
	donkey_spawn_egg = "minecraft:donkey_spawn_egg"
	dragon_breath = "minecraft:dragon_breath"
	dragon_egg = "minecraft:dragon_egg"
	dragon_head = "minecraft:dragon_head"
	dried_kelp = "minecraft:dried_kelp"
	dried_kelp_block = "minecraft:dried_kelp_block"
	dripstone_block = "minecraft:dripstone_block"
	dropper = "minecraft:dropper"
	drowned_spawn_egg = "minecraft:drowned_spawn_egg"
	egg = "minecraft:egg"
	elder_guardian_spawn_egg = "minecraft:elder_guardian_spawn_egg"
	elytra = "minecraft:elytra"
	emerald = "minecraft:emerald"
	emerald_block = "minecraft:emerald_block"
	emerald_ore = "minecraft:emerald_ore"
	enchanted_book = "minecraft:enchanted_book"
	enchanted_golden_apple = "minecraft:enchanted_golden_apple"
	enchanting_table = "minecraft:enchanting_table"
	end_crystal = "minecraft:end_crystal"
	end_portal_frame = "minecraft:end_portal_frame"
	end_rod = "minecraft:end_rod"
	end_stone = "minecraft:end_stone"
	end_stone_brick_slab = "minecraft:end_stone_brick_slab"
	end_stone_brick_stairs = "minecraft:end_stone_brick_stairs"
	end_stone_brick_wall = "minecraft:end_stone_brick_wall"
	end_stone_bricks = "minecraft:end_stone_bricks"
	ender_chest = "minecraft:ender_chest"
	ender_eye = "minecraft:ender_eye"
	ender_pearl = "minecraft:ender_pearl"
	enderman_spawn_egg = "minecraft:enderman_spawn_egg"
	endermite_spawn_egg = "minecraft:endermite_spawn_egg"
	evoker_spawn_egg = "minecraft:evoker_spawn_egg"
	experience_bottle = "minecraft:experience_bottle"
	exposed_copper = "minecraft:exposed_copper"
	exposed_cut_copper = "minecraft:exposed_cut_copper"
	exposed_cut_copper_slab = "minecraft:exposed_cut_copper_slab"
	exposed_cut_copper_stairs = "minecraft:exposed_cut_copper_stairs"
	farmland = "minecraft:farmland"
	feather = "minecraft:feather"
	fermented_spider_eye = "minecraft:fermented_spider_eye"
	fern = "minecraft:fern"
	filled_map = "minecraft:filled_map"
	fire_charge = "minecraft:fire_charge"
	fire_coral = "minecraft:fire_coral"
	fire_coral_block = "minecraft:fire_coral_block"
	fire_coral_fan = "minecraft:fire_coral_fan"
	firework_rocket = "minecraft:firework_rocket"
	firework_star = "minecraft:firework_star"
	fishing_rod = "minecraft:fishing_rod"
	fletching_table = "minecraft:fletching_table"
	flint = "minecraft:flint"
	flint_and_steel = "minecraft:flint_and_steel"
	flower_banner_pattern = "minecraft:flower_banner_pattern"
	flower_pot = "minecraft:flower_pot"
	flowering_azalea = "minecraft:flowering_azalea"
	flowering_azalea_leaves = "minecraft:flowering_azalea_leaves"
	fox_spawn_egg = "minecraft:fox_spawn_egg"
	furnace = "minecraft:furnace"
	furnace_minecart = "minecraft:furnace_minecart"
	ghast_spawn_egg = "minecraft:ghast_spawn_egg"
	ghast_tear = "minecraft:ghast_tear"
	gilded_blackstone = "minecraft:gilded_blackstone"
	glass = "minecraft:glass"
	glass_bottle = "minecraft:glass_bottle"
	glass_pane = "minecraft:glass_pane"
	glistering_melon_slice = "minecraft:glistering_melon_slice"
	globe_banner_pattern = "minecraft:globe_banner_pattern"
	glow_berries = "minecraft:glow_berries"
	glow_ink_sac = "minecraft:glow_ink_sac"
	glow_item_frame = "minecraft:glow_item_frame"
	glow_lichen = "minecraft:glow_lichen"
	glow_squid_spawn_egg = "minecraft:glow_squid_spawn_egg"
	glowstone = "minecraft:glowstone"
	glowstone_dust = "minecraft:glowstone_dust"
	goat_spawn_egg = "minecraft:goat_spawn_egg"
	gold_block = "minecraft:gold_block"
	gold_ingot = "minecraft:gold_ingot"
	gold_nugget = "minecraft:gold_nugget"
	gold_ore = "minecraft:gold_ore"
	golden_apple = "minecraft:golden_apple"
	golden_axe = "minecraft:golden_axe"
	golden_boots = "minecraft:golden_boots"
	golden_carrot = "minecraft:golden_carrot"
	golden_chestplate = "minecraft:golden_chestplate"
	golden_helmet = "minecraft:golden_helmet"
	golden_hoe = "minecraft:golden_hoe"
	golden_horse_armor = "minecraft:golden_horse_armor"
	golden_leggings = "minecraft:golden_leggings"
	golden_pickaxe = "minecraft:golden_pickaxe"
	golden_shovel = "minecraft:golden_shovel"
	golden_sword = "minecraft:golden_sword"
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
	gray_carpet = "minecraft:gray_carpet"
	gray_concrete = "minecraft:gray_concrete"
	gray_concrete_powder = "minecraft:gray_concrete_powder"
	gray_dye = "minecraft:gray_dye"
	gray_glazed_terracotta = "minecraft:gray_glazed_terracotta"
	gray_shulker_box = "minecraft:gray_shulker_box"
	gray_stained_glass = "minecraft:gray_stained_glass"
	gray_stained_glass_pane = "minecraft:gray_stained_glass_pane"
	gray_terracotta = "minecraft:gray_terracotta"
	gray_wool = "minecraft:gray_wool"
	green_banner = "minecraft:green_banner"
	green_bed = "minecraft:green_bed"
	green_candle = "minecraft:green_candle"
	green_carpet = "minecraft:green_carpet"
	green_concrete = "minecraft:green_concrete"
	green_concrete_powder = "minecraft:green_concrete_powder"
	green_dye = "minecraft:green_dye"
	green_glazed_terracotta = "minecraft:green_glazed_terracotta"
	green_shulker_box = "minecraft:green_shulker_box"
	green_stained_glass = "minecraft:green_stained_glass"
	green_stained_glass_pane = "minecraft:green_stained_glass_pane"
	green_terracotta = "minecraft:green_terracotta"
	green_wool = "minecraft:green_wool"
	grindstone = "minecraft:grindstone"
	guardian_spawn_egg = "minecraft:guardian_spawn_egg"
	gunpowder = "minecraft:gunpowder"
	hanging_roots = "minecraft:hanging_roots"
	hay_block = "minecraft:hay_block"
	heart_of_the_sea = "minecraft:heart_of_the_sea"
	heavy_weighted_pressure_plate = "minecraft:heavy_weighted_pressure_plate"
	hoglin_spawn_egg = "minecraft:hoglin_spawn_egg"
	honey_block = "minecraft:honey_block"
	honey_bottle = "minecraft:honey_bottle"
	honeycomb = "minecraft:honeycomb"
	honeycomb_block = "minecraft:honeycomb_block"
	hopper = "minecraft:hopper"
	hopper_minecart = "minecraft:hopper_minecart"
	horn_coral = "minecraft:horn_coral"
	horn_coral_block = "minecraft:horn_coral_block"
	horn_coral_fan = "minecraft:horn_coral_fan"
	horse_spawn_egg = "minecraft:horse_spawn_egg"
	husk_spawn_egg = "minecraft:husk_spawn_egg"
	ice = "minecraft:ice"
	infested_chiseled_stone_bricks = "minecraft:infested_chiseled_stone_bricks"
	infested_cobblestone = "minecraft:infested_cobblestone"
	infested_cracked_stone_bricks = "minecraft:infested_cracked_stone_bricks"
	infested_deepslate = "minecraft:infested_deepslate"
	infested_mossy_stone_bricks = "minecraft:infested_mossy_stone_bricks"
	infested_stone = "minecraft:infested_stone"
	infested_stone_bricks = "minecraft:infested_stone_bricks"
	ink_sac = "minecraft:ink_sac"
	iron_axe = "minecraft:iron_axe"
	iron_bars = "minecraft:iron_bars"
	iron_block = "minecraft:iron_block"
	iron_boots = "minecraft:iron_boots"
	iron_chestplate = "minecraft:iron_chestplate"
	iron_door = "minecraft:iron_door"
	iron_helmet = "minecraft:iron_helmet"
	iron_hoe = "minecraft:iron_hoe"
	iron_horse_armor = "minecraft:iron_horse_armor"
	iron_ingot = "minecraft:iron_ingot"
	iron_leggings = "minecraft:iron_leggings"
	iron_nugget = "minecraft:iron_nugget"
	iron_ore = "minecraft:iron_ore"
	iron_pickaxe = "minecraft:iron_pickaxe"
	iron_shovel = "minecraft:iron_shovel"
	iron_sword = "minecraft:iron_sword"
	iron_trapdoor = "minecraft:iron_trapdoor"
	item_frame = "minecraft:item_frame"
	jack_o_lantern = "minecraft:jack_o_lantern"
	jigsaw = "minecraft:jigsaw"
	jukebox = "minecraft:jukebox"
	jungle_boat = "minecraft:jungle_boat"
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
	jungle_wood = "minecraft:jungle_wood"
	kelp = "minecraft:kelp"
	knowledge_book = "minecraft:knowledge_book"
	ladder = "minecraft:ladder"
	lantern = "minecraft:lantern"
	lapis_block = "minecraft:lapis_block"
	lapis_lazuli = "minecraft:lapis_lazuli"
	lapis_ore = "minecraft:lapis_ore"
	large_amethyst_bud = "minecraft:large_amethyst_bud"
	large_fern = "minecraft:large_fern"
	lava_bucket = "minecraft:lava_bucket"
	lead = "minecraft:lead"
	leather = "minecraft:leather"
	leather_boots = "minecraft:leather_boots"
	leather_chestplate = "minecraft:leather_chestplate"
	leather_helmet = "minecraft:leather_helmet"
	leather_horse_armor = "minecraft:leather_horse_armor"
	leather_leggings = "minecraft:leather_leggings"
	lectern = "minecraft:lectern"
	lever = "minecraft:lever"
	light = "minecraft:light"
	light_blue_banner = "minecraft:light_blue_banner"
	light_blue_bed = "minecraft:light_blue_bed"
	light_blue_candle = "minecraft:light_blue_candle"
	light_blue_carpet = "minecraft:light_blue_carpet"
	light_blue_concrete = "minecraft:light_blue_concrete"
	light_blue_concrete_powder = "minecraft:light_blue_concrete_powder"
	light_blue_dye = "minecraft:light_blue_dye"
	light_blue_glazed_terracotta = "minecraft:light_blue_glazed_terracotta"
	light_blue_shulker_box = "minecraft:light_blue_shulker_box"
	light_blue_stained_glass = "minecraft:light_blue_stained_glass"
	light_blue_stained_glass_pane = "minecraft:light_blue_stained_glass_pane"
	light_blue_terracotta = "minecraft:light_blue_terracotta"
	light_blue_wool = "minecraft:light_blue_wool"
	light_gray_banner = "minecraft:light_gray_banner"
	light_gray_bed = "minecraft:light_gray_bed"
	light_gray_candle = "minecraft:light_gray_candle"
	light_gray_carpet = "minecraft:light_gray_carpet"
	light_gray_concrete = "minecraft:light_gray_concrete"
	light_gray_concrete_powder = "minecraft:light_gray_concrete_powder"
	light_gray_dye = "minecraft:light_gray_dye"
	light_gray_glazed_terracotta = "minecraft:light_gray_glazed_terracotta"
	light_gray_shulker_box = "minecraft:light_gray_shulker_box"
	light_gray_stained_glass = "minecraft:light_gray_stained_glass"
	light_gray_stained_glass_pane = "minecraft:light_gray_stained_glass_pane"
	light_gray_terracotta = "minecraft:light_gray_terracotta"
	light_gray_wool = "minecraft:light_gray_wool"
	light_weighted_pressure_plate = "minecraft:light_weighted_pressure_plate"
	lightning_rod = "minecraft:lightning_rod"
	lilac = "minecraft:lilac"
	lily_of_the_valley = "minecraft:lily_of_the_valley"
	lily_pad = "minecraft:lily_pad"
	lime_banner = "minecraft:lime_banner"
	lime_bed = "minecraft:lime_bed"
	lime_candle = "minecraft:lime_candle"
	lime_carpet = "minecraft:lime_carpet"
	lime_concrete = "minecraft:lime_concrete"
	lime_concrete_powder = "minecraft:lime_concrete_powder"
	lime_dye = "minecraft:lime_dye"
	lime_glazed_terracotta = "minecraft:lime_glazed_terracotta"
	lime_shulker_box = "minecraft:lime_shulker_box"
	lime_stained_glass = "minecraft:lime_stained_glass"
	lime_stained_glass_pane = "minecraft:lime_stained_glass_pane"
	lime_terracotta = "minecraft:lime_terracotta"
	lime_wool = "minecraft:lime_wool"
	lingering_potion = "minecraft:lingering_potion"
	llama_spawn_egg = "minecraft:llama_spawn_egg"
	lodestone = "minecraft:lodestone"
	loom = "minecraft:loom"
	magenta_banner = "minecraft:magenta_banner"
	magenta_bed = "minecraft:magenta_bed"
	magenta_candle = "minecraft:magenta_candle"
	magenta_carpet = "minecraft:magenta_carpet"
	magenta_concrete = "minecraft:magenta_concrete"
	magenta_concrete_powder = "minecraft:magenta_concrete_powder"
	magenta_dye = "minecraft:magenta_dye"
	magenta_glazed_terracotta = "minecraft:magenta_glazed_terracotta"
	magenta_shulker_box = "minecraft:magenta_shulker_box"
	magenta_stained_glass = "minecraft:magenta_stained_glass"
	magenta_stained_glass_pane = "minecraft:magenta_stained_glass_pane"
	magenta_terracotta = "minecraft:magenta_terracotta"
	magenta_wool = "minecraft:magenta_wool"
	magma_block = "minecraft:magma_block"
	magma_cream = "minecraft:magma_cream"
	magma_cube_spawn_egg = "minecraft:magma_cube_spawn_egg"
	map = "minecraft:map"
	medium_amethyst_bud = "minecraft:medium_amethyst_bud"
	melon = "minecraft:melon"
	melon_seeds = "minecraft:melon_seeds"
	melon_slice = "minecraft:melon_slice"
	milk_bucket = "minecraft:milk_bucket"
	minecart = "minecraft:minecart"
	mojang_banner_pattern = "minecraft:mojang_banner_pattern"
	mooshroom_spawn_egg = "minecraft:mooshroom_spawn_egg"
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
	mule_spawn_egg = "minecraft:mule_spawn_egg"
	mushroom_stem = "minecraft:mushroom_stem"
	mushroom_stew = "minecraft:mushroom_stew"
	music_disc_11 = "minecraft:music_disc_11"
	music_disc_13 = "minecraft:music_disc_13"
	music_disc_blocks = "minecraft:music_disc_blocks"
	music_disc_cat = "minecraft:music_disc_cat"
	music_disc_chirp = "minecraft:music_disc_chirp"
	music_disc_far = "minecraft:music_disc_far"
	music_disc_mall = "minecraft:music_disc_mall"
	music_disc_mellohi = "minecraft:music_disc_mellohi"
	music_disc_pigstep = "minecraft:music_disc_pigstep"
	music_disc_stal = "minecraft:music_disc_stal"
	music_disc_strad = "minecraft:music_disc_strad"
	music_disc_wait = "minecraft:music_disc_wait"
	music_disc_ward = "minecraft:music_disc_ward"
	mutton = "minecraft:mutton"
	mycelium = "minecraft:mycelium"
	name_tag = "minecraft:name_tag"
	nautilus_shell = "minecraft:nautilus_shell"
	nether_brick = "minecraft:nether_brick"
	nether_brick_fence = "minecraft:nether_brick_fence"
	nether_brick_slab = "minecraft:nether_brick_slab"
	nether_brick_stairs = "minecraft:nether_brick_stairs"
	nether_brick_wall = "minecraft:nether_brick_wall"
	nether_bricks = "minecraft:nether_bricks"
	nether_gold_ore = "minecraft:nether_gold_ore"
	nether_quartz_ore = "minecraft:nether_quartz_ore"
	nether_sprouts = "minecraft:nether_sprouts"
	nether_star = "minecraft:nether_star"
	nether_wart = "minecraft:nether_wart"
	nether_wart_block = "minecraft:nether_wart_block"
	netherite_axe = "minecraft:netherite_axe"
	netherite_block = "minecraft:netherite_block"
	netherite_boots = "minecraft:netherite_boots"
	netherite_chestplate = "minecraft:netherite_chestplate"
	netherite_helmet = "minecraft:netherite_helmet"
	netherite_hoe = "minecraft:netherite_hoe"
	netherite_ingot = "minecraft:netherite_ingot"
	netherite_leggings = "minecraft:netherite_leggings"
	netherite_pickaxe = "minecraft:netherite_pickaxe"
	netherite_scrap = "minecraft:netherite_scrap"
	netherite_shovel = "minecraft:netherite_shovel"
	netherite_sword = "minecraft:netherite_sword"
	netherrack = "minecraft:netherrack"
	note_block = "minecraft:note_block"
	oak_boat = "minecraft:oak_boat"
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
	oak_wood = "minecraft:oak_wood"
	observer = "minecraft:observer"
	obsidian = "minecraft:obsidian"
	ocelot_spawn_egg = "minecraft:ocelot_spawn_egg"
	orange_banner = "minecraft:orange_banner"
	orange_bed = "minecraft:orange_bed"
	orange_candle = "minecraft:orange_candle"
	orange_carpet = "minecraft:orange_carpet"
	orange_concrete = "minecraft:orange_concrete"
	orange_concrete_powder = "minecraft:orange_concrete_powder"
	orange_dye = "minecraft:orange_dye"
	orange_glazed_terracotta = "minecraft:orange_glazed_terracotta"
	orange_shulker_box = "minecraft:orange_shulker_box"
	orange_stained_glass = "minecraft:orange_stained_glass"
	orange_stained_glass_pane = "minecraft:orange_stained_glass_pane"
	orange_terracotta = "minecraft:orange_terracotta"
	orange_tulip = "minecraft:orange_tulip"
	orange_wool = "minecraft:orange_wool"
	oxeye_daisy = "minecraft:oxeye_daisy"
	oxidized_copper = "minecraft:oxidized_copper"
	oxidized_cut_copper = "minecraft:oxidized_cut_copper"
	oxidized_cut_copper_slab = "minecraft:oxidized_cut_copper_slab"
	oxidized_cut_copper_stairs = "minecraft:oxidized_cut_copper_stairs"
	packed_ice = "minecraft:packed_ice"
	painting = "minecraft:painting"
	panda_spawn_egg = "minecraft:panda_spawn_egg"
	paper = "minecraft:paper"
	parrot_spawn_egg = "minecraft:parrot_spawn_egg"
	peony = "minecraft:peony"
	petrified_oak_slab = "minecraft:petrified_oak_slab"
	phantom_membrane = "minecraft:phantom_membrane"
	phantom_spawn_egg = "minecraft:phantom_spawn_egg"
	pig_spawn_egg = "minecraft:pig_spawn_egg"
	piglin_banner_pattern = "minecraft:piglin_banner_pattern"
	piglin_brute_spawn_egg = "minecraft:piglin_brute_spawn_egg"
	piglin_spawn_egg = "minecraft:piglin_spawn_egg"
	pillager_spawn_egg = "minecraft:pillager_spawn_egg"
	pink_banner = "minecraft:pink_banner"
	pink_bed = "minecraft:pink_bed"
	pink_candle = "minecraft:pink_candle"
	pink_carpet = "minecraft:pink_carpet"
	pink_concrete = "minecraft:pink_concrete"
	pink_concrete_powder = "minecraft:pink_concrete_powder"
	pink_dye = "minecraft:pink_dye"
	pink_glazed_terracotta = "minecraft:pink_glazed_terracotta"
	pink_shulker_box = "minecraft:pink_shulker_box"
	pink_stained_glass = "minecraft:pink_stained_glass"
	pink_stained_glass_pane = "minecraft:pink_stained_glass_pane"
	pink_terracotta = "minecraft:pink_terracotta"
	pink_tulip = "minecraft:pink_tulip"
	pink_wool = "minecraft:pink_wool"
	piston = "minecraft:piston"
	player_head = "minecraft:player_head"
	podzol = "minecraft:podzol"
	pointed_dripstone = "minecraft:pointed_dripstone"
	poisonous_potato = "minecraft:poisonous_potato"
	polar_bear_spawn_egg = "minecraft:polar_bear_spawn_egg"
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
	popped_chorus_fruit = "minecraft:popped_chorus_fruit"
	poppy = "minecraft:poppy"
	porkchop = "minecraft:porkchop"
	potato = "minecraft:potato"
	potion = "minecraft:potion"
	powder_snow_bucket = "minecraft:powder_snow_bucket"
	powered_rail = "minecraft:powered_rail"
	prismarine = "minecraft:prismarine"
	prismarine_brick_slab = "minecraft:prismarine_brick_slab"
	prismarine_brick_stairs = "minecraft:prismarine_brick_stairs"
	prismarine_bricks = "minecraft:prismarine_bricks"
	prismarine_crystals = "minecraft:prismarine_crystals"
	prismarine_shard = "minecraft:prismarine_shard"
	prismarine_slab = "minecraft:prismarine_slab"
	prismarine_stairs = "minecraft:prismarine_stairs"
	prismarine_wall = "minecraft:prismarine_wall"
	pufferfish = "minecraft:pufferfish"
	pufferfish_bucket = "minecraft:pufferfish_bucket"
	pufferfish_spawn_egg = "minecraft:pufferfish_spawn_egg"
	pumpkin = "minecraft:pumpkin"
	pumpkin_pie = "minecraft:pumpkin_pie"
	pumpkin_seeds = "minecraft:pumpkin_seeds"
	purple_banner = "minecraft:purple_banner"
	purple_bed = "minecraft:purple_bed"
	purple_candle = "minecraft:purple_candle"
	purple_carpet = "minecraft:purple_carpet"
	purple_concrete = "minecraft:purple_concrete"
	purple_concrete_powder = "minecraft:purple_concrete_powder"
	purple_dye = "minecraft:purple_dye"
	purple_glazed_terracotta = "minecraft:purple_glazed_terracotta"
	purple_shulker_box = "minecraft:purple_shulker_box"
	purple_stained_glass = "minecraft:purple_stained_glass"
	purple_stained_glass_pane = "minecraft:purple_stained_glass_pane"
	purple_terracotta = "minecraft:purple_terracotta"
	purple_wool = "minecraft:purple_wool"
	purpur_block = "minecraft:purpur_block"
	purpur_pillar = "minecraft:purpur_pillar"
	purpur_slab = "minecraft:purpur_slab"
	purpur_stairs = "minecraft:purpur_stairs"
	quartz = "minecraft:quartz"
	quartz_block = "minecraft:quartz_block"
	quartz_bricks = "minecraft:quartz_bricks"
	quartz_pillar = "minecraft:quartz_pillar"
	quartz_slab = "minecraft:quartz_slab"
	quartz_stairs = "minecraft:quartz_stairs"
	rabbit = "minecraft:rabbit"
	rabbit_foot = "minecraft:rabbit_foot"
	rabbit_hide = "minecraft:rabbit_hide"
	rabbit_spawn_egg = "minecraft:rabbit_spawn_egg"
	rabbit_stew = "minecraft:rabbit_stew"
	rail = "minecraft:rail"
	ravager_spawn_egg = "minecraft:ravager_spawn_egg"
	raw_copper = "minecraft:raw_copper"
	raw_copper_block = "minecraft:raw_copper_block"
	raw_gold = "minecraft:raw_gold"
	raw_gold_block = "minecraft:raw_gold_block"
	raw_iron = "minecraft:raw_iron"
	raw_iron_block = "minecraft:raw_iron_block"
	red_banner = "minecraft:red_banner"
	red_bed = "minecraft:red_bed"
	red_candle = "minecraft:red_candle"
	red_carpet = "minecraft:red_carpet"
	red_concrete = "minecraft:red_concrete"
	red_concrete_powder = "minecraft:red_concrete_powder"
	red_dye = "minecraft:red_dye"
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
	red_wool = "minecraft:red_wool"
	redstone = "minecraft:redstone"
	redstone_block = "minecraft:redstone_block"
	redstone_lamp = "minecraft:redstone_lamp"
	redstone_ore = "minecraft:redstone_ore"
	redstone_torch = "minecraft:redstone_torch"
	repeater = "minecraft:repeater"
	repeating_command_block = "minecraft:repeating_command_block"
	respawn_anchor = "minecraft:respawn_anchor"
	rooted_dirt = "minecraft:rooted_dirt"
	rose_bush = "minecraft:rose_bush"
	rotten_flesh = "minecraft:rotten_flesh"
	saddle = "minecraft:saddle"
	salmon = "minecraft:salmon"
	salmon_bucket = "minecraft:salmon_bucket"
	salmon_spawn_egg = "minecraft:salmon_spawn_egg"
	sand = "minecraft:sand"
	sandstone = "minecraft:sandstone"
	sandstone_slab = "minecraft:sandstone_slab"
	sandstone_stairs = "minecraft:sandstone_stairs"
	sandstone_wall = "minecraft:sandstone_wall"
	scaffolding = "minecraft:scaffolding"
	sculk_sensor = "minecraft:sculk_sensor"
	scute = "minecraft:scute"
	sea_lantern = "minecraft:sea_lantern"
	sea_pickle = "minecraft:sea_pickle"
	seagrass = "minecraft:seagrass"
	shears = "minecraft:shears"
	sheep_spawn_egg = "minecraft:sheep_spawn_egg"
	shield = "minecraft:shield"
	shroomlight = "minecraft:shroomlight"
	shulker_box = "minecraft:shulker_box"
	shulker_shell = "minecraft:shulker_shell"
	shulker_spawn_egg = "minecraft:shulker_spawn_egg"
	silverfish_spawn_egg = "minecraft:silverfish_spawn_egg"
	skeleton_horse_spawn_egg = "minecraft:skeleton_horse_spawn_egg"
	skeleton_skull = "minecraft:skeleton_skull"
	skeleton_spawn_egg = "minecraft:skeleton_spawn_egg"
	skull_banner_pattern = "minecraft:skull_banner_pattern"
	slime_ball = "minecraft:slime_ball"
	slime_block = "minecraft:slime_block"
	slime_spawn_egg = "minecraft:slime_spawn_egg"
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
	snowball = "minecraft:snowball"
	soul_campfire = "minecraft:soul_campfire"
	soul_lantern = "minecraft:soul_lantern"
	soul_sand = "minecraft:soul_sand"
	soul_soil = "minecraft:soul_soil"
	soul_torch = "minecraft:soul_torch"
	spawner = "minecraft:spawner"
	spectral_arrow = "minecraft:spectral_arrow"
	spider_eye = "minecraft:spider_eye"
	spider_spawn_egg = "minecraft:spider_spawn_egg"
	splash_potion = "minecraft:splash_potion"
	sponge = "minecraft:sponge"
	spore_blossom = "minecraft:spore_blossom"
	spruce_boat = "minecraft:spruce_boat"
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
	spruce_wood = "minecraft:spruce_wood"
	spyglass = "minecraft:spyglass"
	squid_spawn_egg = "minecraft:squid_spawn_egg"
	stick = "minecraft:stick"
	sticky_piston = "minecraft:sticky_piston"
	stone = "minecraft:stone"
	stone_axe = "minecraft:stone_axe"
	stone_brick_slab = "minecraft:stone_brick_slab"
	stone_brick_stairs = "minecraft:stone_brick_stairs"
	stone_brick_wall = "minecraft:stone_brick_wall"
	stone_bricks = "minecraft:stone_bricks"
	stone_button = "minecraft:stone_button"
	stone_hoe = "minecraft:stone_hoe"
	stone_pickaxe = "minecraft:stone_pickaxe"
	stone_pressure_plate = "minecraft:stone_pressure_plate"
	stone_shovel = "minecraft:stone_shovel"
	stone_slab = "minecraft:stone_slab"
	stone_stairs = "minecraft:stone_stairs"
	stone_sword = "minecraft:stone_sword"
	stonecutter = "minecraft:stonecutter"
	stray_spawn_egg = "minecraft:stray_spawn_egg"
	strider_spawn_egg = "minecraft:strider_spawn_egg"
	string = "minecraft:string"
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
	sugar = "minecraft:sugar"
	sugar_cane = "minecraft:sugar_cane"
	sunflower = "minecraft:sunflower"
	suspicious_stew = "minecraft:suspicious_stew"
	sweet_berries = "minecraft:sweet_berries"
	tall_grass = "minecraft:tall_grass"
	target = "minecraft:target"
	terracotta = "minecraft:terracotta"
	tinted_glass = "minecraft:tinted_glass"
	tipped_arrow = "minecraft:tipped_arrow"
	tnt = "minecraft:tnt"
	tnt_minecart = "minecraft:tnt_minecart"
	torch = "minecraft:torch"
	totem_of_undying = "minecraft:totem_of_undying"
	trader_llama_spawn_egg = "minecraft:trader_llama_spawn_egg"
	trapped_chest = "minecraft:trapped_chest"
	trident = "minecraft:trident"
	tripwire_hook = "minecraft:tripwire_hook"
	tropical_fish = "minecraft:tropical_fish"
	tropical_fish_bucket = "minecraft:tropical_fish_bucket"
	tropical_fish_spawn_egg = "minecraft:tropical_fish_spawn_egg"
	tube_coral = "minecraft:tube_coral"
	tube_coral_block = "minecraft:tube_coral_block"
	tube_coral_fan = "minecraft:tube_coral_fan"
	tuff = "minecraft:tuff"
	turtle_egg = "minecraft:turtle_egg"
	turtle_helmet = "minecraft:turtle_helmet"
	turtle_spawn_egg = "minecraft:turtle_spawn_egg"
	twisting_vines = "minecraft:twisting_vines"
	vex_spawn_egg = "minecraft:vex_spawn_egg"
	villager_spawn_egg = "minecraft:villager_spawn_egg"
	vindicator_spawn_egg = "minecraft:vindicator_spawn_egg"
	vine = "minecraft:vine"
	wandering_trader_spawn_egg = "minecraft:wandering_trader_spawn_egg"
	warped_button = "minecraft:warped_button"
	warped_door = "minecraft:warped_door"
	warped_fence = "minecraft:warped_fence"
	warped_fence_gate = "minecraft:warped_fence_gate"
	warped_fungus = "minecraft:warped_fungus"
	warped_fungus_on_a_stick = "minecraft:warped_fungus_on_a_stick"
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
	warped_wart_block = "minecraft:warped_wart_block"
	water_bucket = "minecraft:water_bucket"
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
	wet_sponge = "minecraft:wet_sponge"
	wheat = "minecraft:wheat"
	wheat_seeds = "minecraft:wheat_seeds"
	white_banner = "minecraft:white_banner"
	white_bed = "minecraft:white_bed"
	white_candle = "minecraft:white_candle"
	white_carpet = "minecraft:white_carpet"
	white_concrete = "minecraft:white_concrete"
	white_concrete_powder = "minecraft:white_concrete_powder"
	white_dye = "minecraft:white_dye"
	white_glazed_terracotta = "minecraft:white_glazed_terracotta"
	white_shulker_box = "minecraft:white_shulker_box"
	white_stained_glass = "minecraft:white_stained_glass"
	white_stained_glass_pane = "minecraft:white_stained_glass_pane"
	white_terracotta = "minecraft:white_terracotta"
	white_tulip = "minecraft:white_tulip"
	white_wool = "minecraft:white_wool"
	witch_spawn_egg = "minecraft:witch_spawn_egg"
	wither_rose = "minecraft:wither_rose"
	wither_skeleton_skull = "minecraft:wither_skeleton_skull"
	wither_skeleton_spawn_egg = "minecraft:wither_skeleton_spawn_egg"
	wolf_spawn_egg = "minecraft:wolf_spawn_egg"
	wooden_axe = "minecraft:wooden_axe"
	wooden_hoe = "minecraft:wooden_hoe"
	wooden_pickaxe = "minecraft:wooden_pickaxe"
	wooden_shovel = "minecraft:wooden_shovel"
	wooden_sword = "minecraft:wooden_sword"
	writable_book = "minecraft:writable_book"
	written_book = "minecraft:written_book"
	yellow_banner = "minecraft:yellow_banner"
	yellow_bed = "minecraft:yellow_bed"
	yellow_candle = "minecraft:yellow_candle"
	yellow_carpet = "minecraft:yellow_carpet"
	yellow_concrete = "minecraft:yellow_concrete"
	yellow_concrete_powder = "minecraft:yellow_concrete_powder"
	yellow_dye = "minecraft:yellow_dye"
	yellow_glazed_terracotta = "minecraft:yellow_glazed_terracotta"
	yellow_shulker_box = "minecraft:yellow_shulker_box"
	yellow_stained_glass = "minecraft:yellow_stained_glass"
	yellow_stained_glass_pane = "minecraft:yellow_stained_glass_pane"
	yellow_terracotta = "minecraft:yellow_terracotta"
	yellow_wool = "minecraft:yellow_wool"
	zoglin_spawn_egg = "minecraft:zoglin_spawn_egg"
	zombie_head = "minecraft:zombie_head"
	zombie_horse_spawn_egg = "minecraft:zombie_horse_spawn_egg"
	zombie_spawn_egg = "minecraft:zombie_spawn_egg"
	zombie_villager_spawn_egg = "minecraft:zombie_villager_spawn_egg"
	zombified_piglin_spawn_egg = "minecraft:zombified_piglin_spawn_egg"
