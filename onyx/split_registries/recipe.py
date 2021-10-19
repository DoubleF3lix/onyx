import enum


class recipe(enum.Enum):
	"""
	recipe

	* all
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
	* amethyst_block
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
	* black_banner
	* black_bed
	* black_bed_from_white_bed
	* black_candle
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
	* blackstone_slab
	* blackstone_slab_from_blackstone_stonecutting
	* blackstone_stairs
	* blackstone_stairs_from_blackstone_stonecutting
	* blackstone_wall
	* blackstone_wall_from_blackstone_stonecutting
	* blast_furnace
	* blaze_powder
	* blue_banner
	* blue_bed
	* blue_bed_from_white_bed
	* blue_candle
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
	* book_cloning
	* bookshelf
	* bow
	* bowl
	* bread
	* brewing_stand
	* brick
	* brick_slab
	* brick_slab_from_bricks_stonecutting
	* brick_stairs
	* brick_stairs_from_bricks_stonecutting
	* brick_wall
	* brick_wall_from_bricks_stonecutting
	* bricks
	* brown_banner
	* brown_bed
	* brown_bed_from_white_bed
	* brown_candle
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
	* candle
	* carrot_on_a_stick
	* cartography_table
	* cauldron
	* chain
	* charcoal
	* chest
	* chest_minecart
	* chiseled_deepslate
	* chiseled_deepslate_from_cobbled_deepslate_stonecutting
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
	* coal_from_blasting_coal_ore
	* coal_from_blasting_deepslate_coal_ore
	* coal_from_smelting_coal_ore
	* coal_from_smelting_deepslate_coal_ore
	* coarse_dirt
	* cobbled_deepslate_slab
	* cobbled_deepslate_slab_from_cobbled_deepslate_stonecutting
	* cobbled_deepslate_stairs
	* cobbled_deepslate_stairs_from_cobbled_deepslate_stonecutting
	* cobbled_deepslate_wall
	* cobbled_deepslate_wall_from_cobbled_deepslate_stonecutting
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
	* copper_block
	* copper_ingot
	* copper_ingot_from_blasting_copper_ore
	* copper_ingot_from_blasting_deepslate_copper_ore
	* copper_ingot_from_blasting_raw_copper
	* copper_ingot_from_smelting_copper_ore
	* copper_ingot_from_smelting_deepslate_copper_ore
	* copper_ingot_from_smelting_raw_copper
	* copper_ingot_from_waxed_copper_block
	* cracked_deepslate_bricks
	* cracked_deepslate_tiles
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
	* cut_copper
	* cut_copper_from_copper_block_stonecutting
	* cut_copper_slab
	* cut_copper_slab_from_copper_block_stonecutting
	* cut_copper_slab_from_cut_copper_stonecutting
	* cut_copper_stairs
	* cut_copper_stairs_from_copper_block_stonecutting
	* cut_copper_stairs_from_cut_copper_stonecutting
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
	* cyan_candle
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
	* deepslate
	* deepslate_brick_slab
	* deepslate_brick_slab_from_cobbled_deepslate_stonecutting
	* deepslate_brick_slab_from_deepslate_bricks_stonecutting
	* deepslate_brick_slab_from_polished_deepslate_stonecutting
	* deepslate_brick_stairs
	* deepslate_brick_stairs_from_cobbled_deepslate_stonecutting
	* deepslate_brick_stairs_from_deepslate_bricks_stonecutting
	* deepslate_brick_stairs_from_polished_deepslate_stonecutting
	* deepslate_brick_wall
	* deepslate_brick_wall_from_cobbled_deepslate_stonecutting
	* deepslate_brick_wall_from_deepslate_bricks_stonecutting
	* deepslate_brick_wall_from_polished_deepslate_stonecutting
	* deepslate_bricks
	* deepslate_bricks_from_cobbled_deepslate_stonecutting
	* deepslate_bricks_from_polished_deepslate_stonecutting
	* deepslate_tile_slab
	* deepslate_tile_slab_from_cobbled_deepslate_stonecutting
	* deepslate_tile_slab_from_deepslate_bricks_stonecutting
	* deepslate_tile_slab_from_deepslate_tiles_stonecutting
	* deepslate_tile_slab_from_polished_deepslate_stonecutting
	* deepslate_tile_stairs
	* deepslate_tile_stairs_from_cobbled_deepslate_stonecutting
	* deepslate_tile_stairs_from_deepslate_bricks_stonecutting
	* deepslate_tile_stairs_from_deepslate_tiles_stonecutting
	* deepslate_tile_stairs_from_polished_deepslate_stonecutting
	* deepslate_tile_wall
	* deepslate_tile_wall_from_cobbled_deepslate_stonecutting
	* deepslate_tile_wall_from_deepslate_bricks_stonecutting
	* deepslate_tile_wall_from_deepslate_tiles_stonecutting
	* deepslate_tile_wall_from_polished_deepslate_stonecutting
	* deepslate_tiles
	* deepslate_tiles_from_cobbled_deepslate_stonecutting
	* deepslate_tiles_from_deepslate_bricks_stonecutting
	* deepslate_tiles_from_polished_deepslate_stonecutting
	* detector_rail
	* diamond
	* diamond_axe
	* diamond_block
	* diamond_boots
	* diamond_chestplate
	* diamond_from_blasting_deepslate_diamond_ore
	* diamond_from_blasting_diamond_ore
	* diamond_from_smelting_deepslate_diamond_ore
	* diamond_from_smelting_diamond_ore
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
	* dripstone_block
	* dropper
	* emerald
	* emerald_block
	* emerald_from_blasting_deepslate_emerald_ore
	* emerald_from_blasting_emerald_ore
	* emerald_from_smelting_deepslate_emerald_ore
	* emerald_from_smelting_emerald_ore
	* enchanting_table
	* end_crystal
	* end_rod
	* end_stone_brick_slab
	* end_stone_brick_slab_from_end_stone_brick_stonecutting
	* end_stone_brick_slab_from_end_stone_stonecutting
	* end_stone_brick_stairs
	* end_stone_brick_stairs_from_end_stone_brick_stonecutting
	* end_stone_brick_stairs_from_end_stone_stonecutting
	* end_stone_brick_wall
	* end_stone_brick_wall_from_end_stone_brick_stonecutting
	* end_stone_brick_wall_from_end_stone_stonecutting
	* end_stone_bricks
	* end_stone_bricks_from_end_stone_stonecutting
	* ender_chest
	* ender_eye
	* exposed_cut_copper
	* exposed_cut_copper_from_exposed_copper_stonecutting
	* exposed_cut_copper_slab
	* exposed_cut_copper_slab_from_exposed_copper_stonecutting
	* exposed_cut_copper_slab_from_exposed_cut_copper_stonecutting
	* exposed_cut_copper_stairs
	* exposed_cut_copper_stairs_from_exposed_copper_stonecutting
	* exposed_cut_copper_stairs_from_exposed_cut_copper_stonecutting
	* fermented_spider_eye
	* fire_charge
	* firework_rocket
	* firework_rocket_simple
	* firework_star
	* firework_star_fade
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
	* glow_item_frame
	* glowstone
	* gold_block
	* gold_ingot_from_blasting_deepslate_gold_ore
	* gold_ingot_from_blasting_gold_ore
	* gold_ingot_from_blasting_nether_gold_ore
	* gold_ingot_from_blasting_raw_gold
	* gold_ingot_from_gold_block
	* gold_ingot_from_nuggets
	* gold_ingot_from_smelting_deepslate_gold_ore
	* gold_ingot_from_smelting_gold_ore
	* gold_ingot_from_smelting_nether_gold_ore
	* gold_ingot_from_smelting_raw_gold
	* gold_nugget
	* gold_nugget_from_blasting
	* gold_nugget_from_smelting
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
	* gray_candle
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
	* green_candle
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
	* honey_block
	* honey_bottle
	* honeycomb_block
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
	* iron_ingot_from_blasting_deepslate_iron_ore
	* iron_ingot_from_blasting_iron_ore
	* iron_ingot_from_blasting_raw_iron
	* iron_ingot_from_iron_block
	* iron_ingot_from_nuggets
	* iron_ingot_from_smelting_deepslate_iron_ore
	* iron_ingot_from_smelting_iron_ore
	* iron_ingot_from_smelting_raw_iron
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
	* lapis_lazuli
	* lapis_lazuli_from_blasting_deepslate_lapis_ore
	* lapis_lazuli_from_blasting_lapis_ore
	* lapis_lazuli_from_smelting_deepslate_lapis_ore
	* lapis_lazuli_from_smelting_lapis_ore
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
	* light_blue_candle
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
	* light_gray_candle
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
	* lightning_rod
	* lime_banner
	* lime_bed
	* lime_bed_from_white_bed
	* lime_candle
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
	* magenta_candle
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
	* moss_carpet
	* mossy_cobblestone_from_moss_block
	* mossy_cobblestone_from_vine
	* mossy_cobblestone_slab
	* mossy_cobblestone_slab_from_mossy_cobblestone_stonecutting
	* mossy_cobblestone_stairs
	* mossy_cobblestone_stairs_from_mossy_cobblestone_stonecutting
	* mossy_cobblestone_wall
	* mossy_cobblestone_wall_from_mossy_cobblestone_stonecutting
	* mossy_stone_brick_slab
	* mossy_stone_brick_slab_from_mossy_stone_brick_stonecutting
	* mossy_stone_brick_stairs
	* mossy_stone_brick_stairs_from_mossy_stone_brick_stonecutting
	* mossy_stone_brick_wall
	* mossy_stone_brick_wall_from_mossy_stone_brick_stonecutting
	* mossy_stone_bricks_from_moss_block
	* mossy_stone_bricks_from_vine
	* mushroom_stew
	* nether_brick
	* nether_brick_fence
	* nether_brick_slab
	* nether_brick_slab_from_nether_bricks_stonecutting
	* nether_brick_stairs
	* nether_brick_stairs_from_nether_bricks_stonecutting
	* nether_brick_wall
	* nether_brick_wall_from_nether_bricks_stonecutting
	* nether_bricks
	* nether_wart_block
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
	* orange_candle
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
	* oxidized_cut_copper
	* oxidized_cut_copper_from_oxidized_copper_stonecutting
	* oxidized_cut_copper_slab
	* oxidized_cut_copper_slab_from_oxidized_copper_stonecutting
	* oxidized_cut_copper_slab_from_oxidized_cut_copper_stonecutting
	* oxidized_cut_copper_stairs
	* oxidized_cut_copper_stairs_from_oxidized_copper_stonecutting
	* oxidized_cut_copper_stairs_from_oxidized_cut_copper_stonecutting
	* packed_ice
	* painting
	* paper
	* pink_banner
	* pink_bed
	* pink_bed_from_white_bed
	* pink_candle
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
	* polished_blackstone_bricks
	* polished_blackstone_bricks_from_blackstone_stonecutting
	* polished_blackstone_bricks_from_polished_blackstone_stonecutting
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
	* polished_deepslate
	* polished_deepslate_from_cobbled_deepslate_stonecutting
	* polished_deepslate_slab
	* polished_deepslate_slab_from_cobbled_deepslate_stonecutting
	* polished_deepslate_slab_from_polished_deepslate_stonecutting
	* polished_deepslate_stairs
	* polished_deepslate_stairs_from_cobbled_deepslate_stonecutting
	* polished_deepslate_stairs_from_polished_deepslate_stonecutting
	* polished_deepslate_wall
	* polished_deepslate_wall_from_cobbled_deepslate_stonecutting
	* polished_deepslate_wall_from_polished_deepslate_stonecutting
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
	* prismarine_brick_slab
	* prismarine_brick_slab_from_prismarine_stonecutting
	* prismarine_brick_stairs
	* prismarine_brick_stairs_from_prismarine_stonecutting
	* prismarine_bricks
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
	* purple_candle
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
	* raw_copper
	* raw_copper_block
	* raw_gold
	* raw_gold_block
	* raw_iron
	* raw_iron_block
	* red_banner
	* red_bed
	* red_bed_from_white_bed
	* red_candle
	* red_carpet
	* red_carpet_from_white_carpet
	* red_concrete_powder
	* red_dye_from_beetroot
	* red_dye_from_poppy
	* red_dye_from_rose_bush
	* red_dye_from_tulip
	* red_glazed_terracotta
	* red_nether_brick_slab
	* red_nether_brick_slab_from_red_nether_bricks_stonecutting
	* red_nether_brick_stairs
	* red_nether_brick_stairs_from_red_nether_bricks_stonecutting
	* red_nether_brick_wall
	* red_nether_brick_wall_from_red_nether_bricks_stonecutting
	* red_nether_bricks
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
	* redstone
	* redstone_block
	* redstone_from_blasting_deepslate_redstone_ore
	* redstone_from_blasting_redstone_ore
	* redstone_from_smelting_deepslate_redstone_ore
	* redstone_from_smelting_redstone_ore
	* redstone_lamp
	* redstone_torch
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
	* smooth_basalt
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
	* spyglass
	* stick
	* stick_from_bamboo_item
	* sticky_piston
	* stone
	* stone_axe
	* stone_brick_slab
	* stone_brick_slab_from_stone_bricks_stonecutting
	* stone_brick_slab_from_stone_stonecutting
	* stone_brick_stairs
	* stone_brick_stairs_from_stone_bricks_stonecutting
	* stone_brick_stairs_from_stone_stonecutting
	* stone_brick_wall
	* stone_brick_wall_from_stone_bricks_stonecutting
	* stone_brick_walls_from_stone_stonecutting
	* stone_bricks
	* stone_bricks_from_stone_stonecutting
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
	* stonecutter
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
	* tinted_glass
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
	* waxed_copper_block_from_honeycomb
	* waxed_cut_copper
	* waxed_cut_copper_from_honeycomb
	* waxed_cut_copper_from_waxed_copper_block_stonecutting
	* waxed_cut_copper_slab
	* waxed_cut_copper_slab_from_honeycomb
	* waxed_cut_copper_slab_from_waxed_copper_block_stonecutting
	* waxed_cut_copper_slab_from_waxed_cut_copper_stonecutting
	* waxed_cut_copper_stairs
	* waxed_cut_copper_stairs_from_honeycomb
	* waxed_cut_copper_stairs_from_waxed_copper_block_stonecutting
	* waxed_cut_copper_stairs_from_waxed_cut_copper_stonecutting
	* waxed_exposed_copper_from_honeycomb
	* waxed_exposed_cut_copper
	* waxed_exposed_cut_copper_from_honeycomb
	* waxed_exposed_cut_copper_from_waxed_exposed_copper_stonecutting
	* waxed_exposed_cut_copper_slab
	* waxed_exposed_cut_copper_slab_from_honeycomb
	* waxed_exposed_cut_copper_slab_from_waxed_exposed_copper_stonecutting
	* waxed_exposed_cut_copper_slab_from_waxed_exposed_cut_copper_stonecutting
	* waxed_exposed_cut_copper_stairs
	* waxed_exposed_cut_copper_stairs_from_honeycomb
	* waxed_exposed_cut_copper_stairs_from_waxed_exposed_copper_stonecutting
	* waxed_exposed_cut_copper_stairs_from_waxed_exposed_cut_copper_stonecutting
	* waxed_oxidized_copper_from_honeycomb
	* waxed_oxidized_cut_copper
	* waxed_oxidized_cut_copper_from_honeycomb
	* waxed_oxidized_cut_copper_from_waxed_oxidized_copper_stonecutting
	* waxed_oxidized_cut_copper_slab
	* waxed_oxidized_cut_copper_slab_from_honeycomb
	* waxed_oxidized_cut_copper_slab_from_waxed_oxidized_copper_stonecutting
	* waxed_oxidized_cut_copper_slab_from_waxed_oxidized_cut_copper_stonecutting
	* waxed_oxidized_cut_copper_stairs
	* waxed_oxidized_cut_copper_stairs_from_honeycomb
	* waxed_oxidized_cut_copper_stairs_from_waxed_oxidized_copper_stonecutting
	* waxed_oxidized_cut_copper_stairs_from_waxed_oxidized_cut_copper_stonecutting
	* waxed_weathered_copper_from_honeycomb
	* waxed_weathered_cut_copper
	* waxed_weathered_cut_copper_from_honeycomb
	* waxed_weathered_cut_copper_from_waxed_weathered_copper_stonecutting
	* waxed_weathered_cut_copper_slab
	* waxed_weathered_cut_copper_slab_from_honeycomb
	* waxed_weathered_cut_copper_slab_from_waxed_weathered_copper_stonecutting
	* waxed_weathered_cut_copper_slab_from_waxed_weathered_cut_copper_stonecutting
	* waxed_weathered_cut_copper_stairs
	* waxed_weathered_cut_copper_stairs_from_honeycomb
	* waxed_weathered_cut_copper_stairs_from_waxed_weathered_copper_stonecutting
	* waxed_weathered_cut_copper_stairs_from_waxed_weathered_cut_copper_stonecutting
	* weathered_cut_copper
	* weathered_cut_copper_from_weathered_copper_stonecutting
	* weathered_cut_copper_slab
	* weathered_cut_copper_slab_from_weathered_copper_stonecutting
	* weathered_cut_copper_slab_from_weathered_cut_copper_stonecutting
	* weathered_cut_copper_stairs
	* weathered_cut_copper_stairs_from_weathered_copper_stonecutting
	* weathered_cut_copper_stairs_from_weathered_cut_copper_stonecutting
	* wheat
	* white_banner
	* white_bed
	* white_candle
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
	* yellow_candle
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
	all = "*"
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
	amethyst_block = "minecraft:amethyst_block"
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
	black_banner = "minecraft:black_banner"
	black_bed = "minecraft:black_bed"
	black_bed_from_white_bed = "minecraft:black_bed_from_white_bed"
	black_candle = "minecraft:black_candle"
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
	blackstone_slab = "minecraft:blackstone_slab"
	blackstone_slab_from_blackstone_stonecutting = "minecraft:blackstone_slab_from_blackstone_stonecutting"
	blackstone_stairs = "minecraft:blackstone_stairs"
	blackstone_stairs_from_blackstone_stonecutting = "minecraft:blackstone_stairs_from_blackstone_stonecutting"
	blackstone_wall = "minecraft:blackstone_wall"
	blackstone_wall_from_blackstone_stonecutting = "minecraft:blackstone_wall_from_blackstone_stonecutting"
	blast_furnace = "minecraft:blast_furnace"
	blaze_powder = "minecraft:blaze_powder"
	blue_banner = "minecraft:blue_banner"
	blue_bed = "minecraft:blue_bed"
	blue_bed_from_white_bed = "minecraft:blue_bed_from_white_bed"
	blue_candle = "minecraft:blue_candle"
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
	book_cloning = "minecraft:book_cloning"
	bookshelf = "minecraft:bookshelf"
	bow = "minecraft:bow"
	bowl = "minecraft:bowl"
	bread = "minecraft:bread"
	brewing_stand = "minecraft:brewing_stand"
	brick = "minecraft:brick"
	brick_slab = "minecraft:brick_slab"
	brick_slab_from_bricks_stonecutting = "minecraft:brick_slab_from_bricks_stonecutting"
	brick_stairs = "minecraft:brick_stairs"
	brick_stairs_from_bricks_stonecutting = "minecraft:brick_stairs_from_bricks_stonecutting"
	brick_wall = "minecraft:brick_wall"
	brick_wall_from_bricks_stonecutting = "minecraft:brick_wall_from_bricks_stonecutting"
	bricks = "minecraft:bricks"
	brown_banner = "minecraft:brown_banner"
	brown_bed = "minecraft:brown_bed"
	brown_bed_from_white_bed = "minecraft:brown_bed_from_white_bed"
	brown_candle = "minecraft:brown_candle"
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
	candle = "minecraft:candle"
	carrot_on_a_stick = "minecraft:carrot_on_a_stick"
	cartography_table = "minecraft:cartography_table"
	cauldron = "minecraft:cauldron"
	chain = "minecraft:chain"
	charcoal = "minecraft:charcoal"
	chest = "minecraft:chest"
	chest_minecart = "minecraft:chest_minecart"
	chiseled_deepslate = "minecraft:chiseled_deepslate"
	chiseled_deepslate_from_cobbled_deepslate_stonecutting = "minecraft:chiseled_deepslate_from_cobbled_deepslate_stonecutting"
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
	coal_from_blasting_coal_ore = "minecraft:coal_from_blasting_coal_ore"
	coal_from_blasting_deepslate_coal_ore = "minecraft:coal_from_blasting_deepslate_coal_ore"
	coal_from_smelting_coal_ore = "minecraft:coal_from_smelting_coal_ore"
	coal_from_smelting_deepslate_coal_ore = "minecraft:coal_from_smelting_deepslate_coal_ore"
	coarse_dirt = "minecraft:coarse_dirt"
	cobbled_deepslate_slab = "minecraft:cobbled_deepslate_slab"
	cobbled_deepslate_slab_from_cobbled_deepslate_stonecutting = "minecraft:cobbled_deepslate_slab_from_cobbled_deepslate_stonecutting"
	cobbled_deepslate_stairs = "minecraft:cobbled_deepslate_stairs"
	cobbled_deepslate_stairs_from_cobbled_deepslate_stonecutting = "minecraft:cobbled_deepslate_stairs_from_cobbled_deepslate_stonecutting"
	cobbled_deepslate_wall = "minecraft:cobbled_deepslate_wall"
	cobbled_deepslate_wall_from_cobbled_deepslate_stonecutting = "minecraft:cobbled_deepslate_wall_from_cobbled_deepslate_stonecutting"
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
	copper_block = "minecraft:copper_block"
	copper_ingot = "minecraft:copper_ingot"
	copper_ingot_from_blasting_copper_ore = "minecraft:copper_ingot_from_blasting_copper_ore"
	copper_ingot_from_blasting_deepslate_copper_ore = "minecraft:copper_ingot_from_blasting_deepslate_copper_ore"
	copper_ingot_from_blasting_raw_copper = "minecraft:copper_ingot_from_blasting_raw_copper"
	copper_ingot_from_smelting_copper_ore = "minecraft:copper_ingot_from_smelting_copper_ore"
	copper_ingot_from_smelting_deepslate_copper_ore = "minecraft:copper_ingot_from_smelting_deepslate_copper_ore"
	copper_ingot_from_smelting_raw_copper = "minecraft:copper_ingot_from_smelting_raw_copper"
	copper_ingot_from_waxed_copper_block = "minecraft:copper_ingot_from_waxed_copper_block"
	cracked_deepslate_bricks = "minecraft:cracked_deepslate_bricks"
	cracked_deepslate_tiles = "minecraft:cracked_deepslate_tiles"
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
	cut_copper = "minecraft:cut_copper"
	cut_copper_from_copper_block_stonecutting = "minecraft:cut_copper_from_copper_block_stonecutting"
	cut_copper_slab = "minecraft:cut_copper_slab"
	cut_copper_slab_from_copper_block_stonecutting = "minecraft:cut_copper_slab_from_copper_block_stonecutting"
	cut_copper_slab_from_cut_copper_stonecutting = "minecraft:cut_copper_slab_from_cut_copper_stonecutting"
	cut_copper_stairs = "minecraft:cut_copper_stairs"
	cut_copper_stairs_from_copper_block_stonecutting = "minecraft:cut_copper_stairs_from_copper_block_stonecutting"
	cut_copper_stairs_from_cut_copper_stonecutting = "minecraft:cut_copper_stairs_from_cut_copper_stonecutting"
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
	cyan_candle = "minecraft:cyan_candle"
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
	deepslate = "minecraft:deepslate"
	deepslate_brick_slab = "minecraft:deepslate_brick_slab"
	deepslate_brick_slab_from_cobbled_deepslate_stonecutting = "minecraft:deepslate_brick_slab_from_cobbled_deepslate_stonecutting"
	deepslate_brick_slab_from_deepslate_bricks_stonecutting = "minecraft:deepslate_brick_slab_from_deepslate_bricks_stonecutting"
	deepslate_brick_slab_from_polished_deepslate_stonecutting = "minecraft:deepslate_brick_slab_from_polished_deepslate_stonecutting"
	deepslate_brick_stairs = "minecraft:deepslate_brick_stairs"
	deepslate_brick_stairs_from_cobbled_deepslate_stonecutting = "minecraft:deepslate_brick_stairs_from_cobbled_deepslate_stonecutting"
	deepslate_brick_stairs_from_deepslate_bricks_stonecutting = "minecraft:deepslate_brick_stairs_from_deepslate_bricks_stonecutting"
	deepslate_brick_stairs_from_polished_deepslate_stonecutting = "minecraft:deepslate_brick_stairs_from_polished_deepslate_stonecutting"
	deepslate_brick_wall = "minecraft:deepslate_brick_wall"
	deepslate_brick_wall_from_cobbled_deepslate_stonecutting = "minecraft:deepslate_brick_wall_from_cobbled_deepslate_stonecutting"
	deepslate_brick_wall_from_deepslate_bricks_stonecutting = "minecraft:deepslate_brick_wall_from_deepslate_bricks_stonecutting"
	deepslate_brick_wall_from_polished_deepslate_stonecutting = "minecraft:deepslate_brick_wall_from_polished_deepslate_stonecutting"
	deepslate_bricks = "minecraft:deepslate_bricks"
	deepslate_bricks_from_cobbled_deepslate_stonecutting = "minecraft:deepslate_bricks_from_cobbled_deepslate_stonecutting"
	deepslate_bricks_from_polished_deepslate_stonecutting = "minecraft:deepslate_bricks_from_polished_deepslate_stonecutting"
	deepslate_tile_slab = "minecraft:deepslate_tile_slab"
	deepslate_tile_slab_from_cobbled_deepslate_stonecutting = "minecraft:deepslate_tile_slab_from_cobbled_deepslate_stonecutting"
	deepslate_tile_slab_from_deepslate_bricks_stonecutting = "minecraft:deepslate_tile_slab_from_deepslate_bricks_stonecutting"
	deepslate_tile_slab_from_deepslate_tiles_stonecutting = "minecraft:deepslate_tile_slab_from_deepslate_tiles_stonecutting"
	deepslate_tile_slab_from_polished_deepslate_stonecutting = "minecraft:deepslate_tile_slab_from_polished_deepslate_stonecutting"
	deepslate_tile_stairs = "minecraft:deepslate_tile_stairs"
	deepslate_tile_stairs_from_cobbled_deepslate_stonecutting = "minecraft:deepslate_tile_stairs_from_cobbled_deepslate_stonecutting"
	deepslate_tile_stairs_from_deepslate_bricks_stonecutting = "minecraft:deepslate_tile_stairs_from_deepslate_bricks_stonecutting"
	deepslate_tile_stairs_from_deepslate_tiles_stonecutting = "minecraft:deepslate_tile_stairs_from_deepslate_tiles_stonecutting"
	deepslate_tile_stairs_from_polished_deepslate_stonecutting = "minecraft:deepslate_tile_stairs_from_polished_deepslate_stonecutting"
	deepslate_tile_wall = "minecraft:deepslate_tile_wall"
	deepslate_tile_wall_from_cobbled_deepslate_stonecutting = "minecraft:deepslate_tile_wall_from_cobbled_deepslate_stonecutting"
	deepslate_tile_wall_from_deepslate_bricks_stonecutting = "minecraft:deepslate_tile_wall_from_deepslate_bricks_stonecutting"
	deepslate_tile_wall_from_deepslate_tiles_stonecutting = "minecraft:deepslate_tile_wall_from_deepslate_tiles_stonecutting"
	deepslate_tile_wall_from_polished_deepslate_stonecutting = "minecraft:deepslate_tile_wall_from_polished_deepslate_stonecutting"
	deepslate_tiles = "minecraft:deepslate_tiles"
	deepslate_tiles_from_cobbled_deepslate_stonecutting = "minecraft:deepslate_tiles_from_cobbled_deepslate_stonecutting"
	deepslate_tiles_from_deepslate_bricks_stonecutting = "minecraft:deepslate_tiles_from_deepslate_bricks_stonecutting"
	deepslate_tiles_from_polished_deepslate_stonecutting = "minecraft:deepslate_tiles_from_polished_deepslate_stonecutting"
	detector_rail = "minecraft:detector_rail"
	diamond = "minecraft:diamond"
	diamond_axe = "minecraft:diamond_axe"
	diamond_block = "minecraft:diamond_block"
	diamond_boots = "minecraft:diamond_boots"
	diamond_chestplate = "minecraft:diamond_chestplate"
	diamond_from_blasting_deepslate_diamond_ore = "minecraft:diamond_from_blasting_deepslate_diamond_ore"
	diamond_from_blasting_diamond_ore = "minecraft:diamond_from_blasting_diamond_ore"
	diamond_from_smelting_deepslate_diamond_ore = "minecraft:diamond_from_smelting_deepslate_diamond_ore"
	diamond_from_smelting_diamond_ore = "minecraft:diamond_from_smelting_diamond_ore"
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
	dripstone_block = "minecraft:dripstone_block"
	dropper = "minecraft:dropper"
	emerald = "minecraft:emerald"
	emerald_block = "minecraft:emerald_block"
	emerald_from_blasting_deepslate_emerald_ore = "minecraft:emerald_from_blasting_deepslate_emerald_ore"
	emerald_from_blasting_emerald_ore = "minecraft:emerald_from_blasting_emerald_ore"
	emerald_from_smelting_deepslate_emerald_ore = "minecraft:emerald_from_smelting_deepslate_emerald_ore"
	emerald_from_smelting_emerald_ore = "minecraft:emerald_from_smelting_emerald_ore"
	enchanting_table = "minecraft:enchanting_table"
	end_crystal = "minecraft:end_crystal"
	end_rod = "minecraft:end_rod"
	end_stone_brick_slab = "minecraft:end_stone_brick_slab"
	end_stone_brick_slab_from_end_stone_brick_stonecutting = "minecraft:end_stone_brick_slab_from_end_stone_brick_stonecutting"
	end_stone_brick_slab_from_end_stone_stonecutting = "minecraft:end_stone_brick_slab_from_end_stone_stonecutting"
	end_stone_brick_stairs = "minecraft:end_stone_brick_stairs"
	end_stone_brick_stairs_from_end_stone_brick_stonecutting = "minecraft:end_stone_brick_stairs_from_end_stone_brick_stonecutting"
	end_stone_brick_stairs_from_end_stone_stonecutting = "minecraft:end_stone_brick_stairs_from_end_stone_stonecutting"
	end_stone_brick_wall = "minecraft:end_stone_brick_wall"
	end_stone_brick_wall_from_end_stone_brick_stonecutting = "minecraft:end_stone_brick_wall_from_end_stone_brick_stonecutting"
	end_stone_brick_wall_from_end_stone_stonecutting = "minecraft:end_stone_brick_wall_from_end_stone_stonecutting"
	end_stone_bricks = "minecraft:end_stone_bricks"
	end_stone_bricks_from_end_stone_stonecutting = "minecraft:end_stone_bricks_from_end_stone_stonecutting"
	ender_chest = "minecraft:ender_chest"
	ender_eye = "minecraft:ender_eye"
	exposed_cut_copper = "minecraft:exposed_cut_copper"
	exposed_cut_copper_from_exposed_copper_stonecutting = "minecraft:exposed_cut_copper_from_exposed_copper_stonecutting"
	exposed_cut_copper_slab = "minecraft:exposed_cut_copper_slab"
	exposed_cut_copper_slab_from_exposed_copper_stonecutting = "minecraft:exposed_cut_copper_slab_from_exposed_copper_stonecutting"
	exposed_cut_copper_slab_from_exposed_cut_copper_stonecutting = "minecraft:exposed_cut_copper_slab_from_exposed_cut_copper_stonecutting"
	exposed_cut_copper_stairs = "minecraft:exposed_cut_copper_stairs"
	exposed_cut_copper_stairs_from_exposed_copper_stonecutting = "minecraft:exposed_cut_copper_stairs_from_exposed_copper_stonecutting"
	exposed_cut_copper_stairs_from_exposed_cut_copper_stonecutting = "minecraft:exposed_cut_copper_stairs_from_exposed_cut_copper_stonecutting"
	fermented_spider_eye = "minecraft:fermented_spider_eye"
	fire_charge = "minecraft:fire_charge"
	firework_rocket = "minecraft:firework_rocket"
	firework_rocket_simple = "minecraft:firework_rocket_simple"
	firework_star = "minecraft:firework_star"
	firework_star_fade = "minecraft:firework_star_fade"
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
	glow_item_frame = "minecraft:glow_item_frame"
	glowstone = "minecraft:glowstone"
	gold_block = "minecraft:gold_block"
	gold_ingot_from_blasting_deepslate_gold_ore = "minecraft:gold_ingot_from_blasting_deepslate_gold_ore"
	gold_ingot_from_blasting_gold_ore = "minecraft:gold_ingot_from_blasting_gold_ore"
	gold_ingot_from_blasting_nether_gold_ore = "minecraft:gold_ingot_from_blasting_nether_gold_ore"
	gold_ingot_from_blasting_raw_gold = "minecraft:gold_ingot_from_blasting_raw_gold"
	gold_ingot_from_gold_block = "minecraft:gold_ingot_from_gold_block"
	gold_ingot_from_nuggets = "minecraft:gold_ingot_from_nuggets"
	gold_ingot_from_smelting_deepslate_gold_ore = "minecraft:gold_ingot_from_smelting_deepslate_gold_ore"
	gold_ingot_from_smelting_gold_ore = "minecraft:gold_ingot_from_smelting_gold_ore"
	gold_ingot_from_smelting_nether_gold_ore = "minecraft:gold_ingot_from_smelting_nether_gold_ore"
	gold_ingot_from_smelting_raw_gold = "minecraft:gold_ingot_from_smelting_raw_gold"
	gold_nugget = "minecraft:gold_nugget"
	gold_nugget_from_blasting = "minecraft:gold_nugget_from_blasting"
	gold_nugget_from_smelting = "minecraft:gold_nugget_from_smelting"
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
	gray_candle = "minecraft:gray_candle"
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
	green_candle = "minecraft:green_candle"
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
	honey_block = "minecraft:honey_block"
	honey_bottle = "minecraft:honey_bottle"
	honeycomb_block = "minecraft:honeycomb_block"
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
	iron_ingot_from_blasting_deepslate_iron_ore = "minecraft:iron_ingot_from_blasting_deepslate_iron_ore"
	iron_ingot_from_blasting_iron_ore = "minecraft:iron_ingot_from_blasting_iron_ore"
	iron_ingot_from_blasting_raw_iron = "minecraft:iron_ingot_from_blasting_raw_iron"
	iron_ingot_from_iron_block = "minecraft:iron_ingot_from_iron_block"
	iron_ingot_from_nuggets = "minecraft:iron_ingot_from_nuggets"
	iron_ingot_from_smelting_deepslate_iron_ore = "minecraft:iron_ingot_from_smelting_deepslate_iron_ore"
	iron_ingot_from_smelting_iron_ore = "minecraft:iron_ingot_from_smelting_iron_ore"
	iron_ingot_from_smelting_raw_iron = "minecraft:iron_ingot_from_smelting_raw_iron"
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
	lapis_lazuli = "minecraft:lapis_lazuli"
	lapis_lazuli_from_blasting_deepslate_lapis_ore = "minecraft:lapis_lazuli_from_blasting_deepslate_lapis_ore"
	lapis_lazuli_from_blasting_lapis_ore = "minecraft:lapis_lazuli_from_blasting_lapis_ore"
	lapis_lazuli_from_smelting_deepslate_lapis_ore = "minecraft:lapis_lazuli_from_smelting_deepslate_lapis_ore"
	lapis_lazuli_from_smelting_lapis_ore = "minecraft:lapis_lazuli_from_smelting_lapis_ore"
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
	light_blue_candle = "minecraft:light_blue_candle"
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
	light_gray_candle = "minecraft:light_gray_candle"
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
	lightning_rod = "minecraft:lightning_rod"
	lime_banner = "minecraft:lime_banner"
	lime_bed = "minecraft:lime_bed"
	lime_bed_from_white_bed = "minecraft:lime_bed_from_white_bed"
	lime_candle = "minecraft:lime_candle"
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
	magenta_candle = "minecraft:magenta_candle"
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
	moss_carpet = "minecraft:moss_carpet"
	mossy_cobblestone_from_moss_block = "minecraft:mossy_cobblestone_from_moss_block"
	mossy_cobblestone_from_vine = "minecraft:mossy_cobblestone_from_vine"
	mossy_cobblestone_slab = "minecraft:mossy_cobblestone_slab"
	mossy_cobblestone_slab_from_mossy_cobblestone_stonecutting = "minecraft:mossy_cobblestone_slab_from_mossy_cobblestone_stonecutting"
	mossy_cobblestone_stairs = "minecraft:mossy_cobblestone_stairs"
	mossy_cobblestone_stairs_from_mossy_cobblestone_stonecutting = "minecraft:mossy_cobblestone_stairs_from_mossy_cobblestone_stonecutting"
	mossy_cobblestone_wall = "minecraft:mossy_cobblestone_wall"
	mossy_cobblestone_wall_from_mossy_cobblestone_stonecutting = "minecraft:mossy_cobblestone_wall_from_mossy_cobblestone_stonecutting"
	mossy_stone_brick_slab = "minecraft:mossy_stone_brick_slab"
	mossy_stone_brick_slab_from_mossy_stone_brick_stonecutting = "minecraft:mossy_stone_brick_slab_from_mossy_stone_brick_stonecutting"
	mossy_stone_brick_stairs = "minecraft:mossy_stone_brick_stairs"
	mossy_stone_brick_stairs_from_mossy_stone_brick_stonecutting = "minecraft:mossy_stone_brick_stairs_from_mossy_stone_brick_stonecutting"
	mossy_stone_brick_wall = "minecraft:mossy_stone_brick_wall"
	mossy_stone_brick_wall_from_mossy_stone_brick_stonecutting = "minecraft:mossy_stone_brick_wall_from_mossy_stone_brick_stonecutting"
	mossy_stone_bricks_from_moss_block = "minecraft:mossy_stone_bricks_from_moss_block"
	mossy_stone_bricks_from_vine = "minecraft:mossy_stone_bricks_from_vine"
	mushroom_stew = "minecraft:mushroom_stew"
	nether_brick = "minecraft:nether_brick"
	nether_brick_fence = "minecraft:nether_brick_fence"
	nether_brick_slab = "minecraft:nether_brick_slab"
	nether_brick_slab_from_nether_bricks_stonecutting = "minecraft:nether_brick_slab_from_nether_bricks_stonecutting"
	nether_brick_stairs = "minecraft:nether_brick_stairs"
	nether_brick_stairs_from_nether_bricks_stonecutting = "minecraft:nether_brick_stairs_from_nether_bricks_stonecutting"
	nether_brick_wall = "minecraft:nether_brick_wall"
	nether_brick_wall_from_nether_bricks_stonecutting = "minecraft:nether_brick_wall_from_nether_bricks_stonecutting"
	nether_bricks = "minecraft:nether_bricks"
	nether_wart_block = "minecraft:nether_wart_block"
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
	orange_candle = "minecraft:orange_candle"
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
	oxidized_cut_copper = "minecraft:oxidized_cut_copper"
	oxidized_cut_copper_from_oxidized_copper_stonecutting = "minecraft:oxidized_cut_copper_from_oxidized_copper_stonecutting"
	oxidized_cut_copper_slab = "minecraft:oxidized_cut_copper_slab"
	oxidized_cut_copper_slab_from_oxidized_copper_stonecutting = "minecraft:oxidized_cut_copper_slab_from_oxidized_copper_stonecutting"
	oxidized_cut_copper_slab_from_oxidized_cut_copper_stonecutting = "minecraft:oxidized_cut_copper_slab_from_oxidized_cut_copper_stonecutting"
	oxidized_cut_copper_stairs = "minecraft:oxidized_cut_copper_stairs"
	oxidized_cut_copper_stairs_from_oxidized_copper_stonecutting = "minecraft:oxidized_cut_copper_stairs_from_oxidized_copper_stonecutting"
	oxidized_cut_copper_stairs_from_oxidized_cut_copper_stonecutting = "minecraft:oxidized_cut_copper_stairs_from_oxidized_cut_copper_stonecutting"
	packed_ice = "minecraft:packed_ice"
	painting = "minecraft:painting"
	paper = "minecraft:paper"
	pink_banner = "minecraft:pink_banner"
	pink_bed = "minecraft:pink_bed"
	pink_bed_from_white_bed = "minecraft:pink_bed_from_white_bed"
	pink_candle = "minecraft:pink_candle"
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
	polished_blackstone_bricks = "minecraft:polished_blackstone_bricks"
	polished_blackstone_bricks_from_blackstone_stonecutting = "minecraft:polished_blackstone_bricks_from_blackstone_stonecutting"
	polished_blackstone_bricks_from_polished_blackstone_stonecutting = "minecraft:polished_blackstone_bricks_from_polished_blackstone_stonecutting"
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
	polished_deepslate = "minecraft:polished_deepslate"
	polished_deepslate_from_cobbled_deepslate_stonecutting = "minecraft:polished_deepslate_from_cobbled_deepslate_stonecutting"
	polished_deepslate_slab = "minecraft:polished_deepslate_slab"
	polished_deepslate_slab_from_cobbled_deepslate_stonecutting = "minecraft:polished_deepslate_slab_from_cobbled_deepslate_stonecutting"
	polished_deepslate_slab_from_polished_deepslate_stonecutting = "minecraft:polished_deepslate_slab_from_polished_deepslate_stonecutting"
	polished_deepslate_stairs = "minecraft:polished_deepslate_stairs"
	polished_deepslate_stairs_from_cobbled_deepslate_stonecutting = "minecraft:polished_deepslate_stairs_from_cobbled_deepslate_stonecutting"
	polished_deepslate_stairs_from_polished_deepslate_stonecutting = "minecraft:polished_deepslate_stairs_from_polished_deepslate_stonecutting"
	polished_deepslate_wall = "minecraft:polished_deepslate_wall"
	polished_deepslate_wall_from_cobbled_deepslate_stonecutting = "minecraft:polished_deepslate_wall_from_cobbled_deepslate_stonecutting"
	polished_deepslate_wall_from_polished_deepslate_stonecutting = "minecraft:polished_deepslate_wall_from_polished_deepslate_stonecutting"
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
	prismarine_brick_slab = "minecraft:prismarine_brick_slab"
	prismarine_brick_slab_from_prismarine_stonecutting = "minecraft:prismarine_brick_slab_from_prismarine_stonecutting"
	prismarine_brick_stairs = "minecraft:prismarine_brick_stairs"
	prismarine_brick_stairs_from_prismarine_stonecutting = "minecraft:prismarine_brick_stairs_from_prismarine_stonecutting"
	prismarine_bricks = "minecraft:prismarine_bricks"
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
	purple_candle = "minecraft:purple_candle"
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
	raw_copper = "minecraft:raw_copper"
	raw_copper_block = "minecraft:raw_copper_block"
	raw_gold = "minecraft:raw_gold"
	raw_gold_block = "minecraft:raw_gold_block"
	raw_iron = "minecraft:raw_iron"
	raw_iron_block = "minecraft:raw_iron_block"
	red_banner = "minecraft:red_banner"
	red_bed = "minecraft:red_bed"
	red_bed_from_white_bed = "minecraft:red_bed_from_white_bed"
	red_candle = "minecraft:red_candle"
	red_carpet = "minecraft:red_carpet"
	red_carpet_from_white_carpet = "minecraft:red_carpet_from_white_carpet"
	red_concrete_powder = "minecraft:red_concrete_powder"
	red_dye_from_beetroot = "minecraft:red_dye_from_beetroot"
	red_dye_from_poppy = "minecraft:red_dye_from_poppy"
	red_dye_from_rose_bush = "minecraft:red_dye_from_rose_bush"
	red_dye_from_tulip = "minecraft:red_dye_from_tulip"
	red_glazed_terracotta = "minecraft:red_glazed_terracotta"
	red_nether_brick_slab = "minecraft:red_nether_brick_slab"
	red_nether_brick_slab_from_red_nether_bricks_stonecutting = "minecraft:red_nether_brick_slab_from_red_nether_bricks_stonecutting"
	red_nether_brick_stairs = "minecraft:red_nether_brick_stairs"
	red_nether_brick_stairs_from_red_nether_bricks_stonecutting = "minecraft:red_nether_brick_stairs_from_red_nether_bricks_stonecutting"
	red_nether_brick_wall = "minecraft:red_nether_brick_wall"
	red_nether_brick_wall_from_red_nether_bricks_stonecutting = "minecraft:red_nether_brick_wall_from_red_nether_bricks_stonecutting"
	red_nether_bricks = "minecraft:red_nether_bricks"
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
	redstone = "minecraft:redstone"
	redstone_block = "minecraft:redstone_block"
	redstone_from_blasting_deepslate_redstone_ore = "minecraft:redstone_from_blasting_deepslate_redstone_ore"
	redstone_from_blasting_redstone_ore = "minecraft:redstone_from_blasting_redstone_ore"
	redstone_from_smelting_deepslate_redstone_ore = "minecraft:redstone_from_smelting_deepslate_redstone_ore"
	redstone_from_smelting_redstone_ore = "minecraft:redstone_from_smelting_redstone_ore"
	redstone_lamp = "minecraft:redstone_lamp"
	redstone_torch = "minecraft:redstone_torch"
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
	smooth_basalt = "minecraft:smooth_basalt"
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
	spyglass = "minecraft:spyglass"
	stick = "minecraft:stick"
	stick_from_bamboo_item = "minecraft:stick_from_bamboo_item"
	sticky_piston = "minecraft:sticky_piston"
	stone = "minecraft:stone"
	stone_axe = "minecraft:stone_axe"
	stone_brick_slab = "minecraft:stone_brick_slab"
	stone_brick_slab_from_stone_bricks_stonecutting = "minecraft:stone_brick_slab_from_stone_bricks_stonecutting"
	stone_brick_slab_from_stone_stonecutting = "minecraft:stone_brick_slab_from_stone_stonecutting"
	stone_brick_stairs = "minecraft:stone_brick_stairs"
	stone_brick_stairs_from_stone_bricks_stonecutting = "minecraft:stone_brick_stairs_from_stone_bricks_stonecutting"
	stone_brick_stairs_from_stone_stonecutting = "minecraft:stone_brick_stairs_from_stone_stonecutting"
	stone_brick_wall = "minecraft:stone_brick_wall"
	stone_brick_wall_from_stone_bricks_stonecutting = "minecraft:stone_brick_wall_from_stone_bricks_stonecutting"
	stone_brick_walls_from_stone_stonecutting = "minecraft:stone_brick_walls_from_stone_stonecutting"
	stone_bricks = "minecraft:stone_bricks"
	stone_bricks_from_stone_stonecutting = "minecraft:stone_bricks_from_stone_stonecutting"
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
	stonecutter = "minecraft:stonecutter"
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
	tinted_glass = "minecraft:tinted_glass"
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
	waxed_copper_block_from_honeycomb = "minecraft:waxed_copper_block_from_honeycomb"
	waxed_cut_copper = "minecraft:waxed_cut_copper"
	waxed_cut_copper_from_honeycomb = "minecraft:waxed_cut_copper_from_honeycomb"
	waxed_cut_copper_from_waxed_copper_block_stonecutting = "minecraft:waxed_cut_copper_from_waxed_copper_block_stonecutting"
	waxed_cut_copper_slab = "minecraft:waxed_cut_copper_slab"
	waxed_cut_copper_slab_from_honeycomb = "minecraft:waxed_cut_copper_slab_from_honeycomb"
	waxed_cut_copper_slab_from_waxed_copper_block_stonecutting = "minecraft:waxed_cut_copper_slab_from_waxed_copper_block_stonecutting"
	waxed_cut_copper_slab_from_waxed_cut_copper_stonecutting = "minecraft:waxed_cut_copper_slab_from_waxed_cut_copper_stonecutting"
	waxed_cut_copper_stairs = "minecraft:waxed_cut_copper_stairs"
	waxed_cut_copper_stairs_from_honeycomb = "minecraft:waxed_cut_copper_stairs_from_honeycomb"
	waxed_cut_copper_stairs_from_waxed_copper_block_stonecutting = "minecraft:waxed_cut_copper_stairs_from_waxed_copper_block_stonecutting"
	waxed_cut_copper_stairs_from_waxed_cut_copper_stonecutting = "minecraft:waxed_cut_copper_stairs_from_waxed_cut_copper_stonecutting"
	waxed_exposed_copper_from_honeycomb = "minecraft:waxed_exposed_copper_from_honeycomb"
	waxed_exposed_cut_copper = "minecraft:waxed_exposed_cut_copper"
	waxed_exposed_cut_copper_from_honeycomb = "minecraft:waxed_exposed_cut_copper_from_honeycomb"
	waxed_exposed_cut_copper_from_waxed_exposed_copper_stonecutting = "minecraft:waxed_exposed_cut_copper_from_waxed_exposed_copper_stonecutting"
	waxed_exposed_cut_copper_slab = "minecraft:waxed_exposed_cut_copper_slab"
	waxed_exposed_cut_copper_slab_from_honeycomb = "minecraft:waxed_exposed_cut_copper_slab_from_honeycomb"
	waxed_exposed_cut_copper_slab_from_waxed_exposed_copper_stonecutting = "minecraft:waxed_exposed_cut_copper_slab_from_waxed_exposed_copper_stonecutting"
	waxed_exposed_cut_copper_slab_from_waxed_exposed_cut_copper_stonecutting = "minecraft:waxed_exposed_cut_copper_slab_from_waxed_exposed_cut_copper_stonecutting"
	waxed_exposed_cut_copper_stairs = "minecraft:waxed_exposed_cut_copper_stairs"
	waxed_exposed_cut_copper_stairs_from_honeycomb = "minecraft:waxed_exposed_cut_copper_stairs_from_honeycomb"
	waxed_exposed_cut_copper_stairs_from_waxed_exposed_copper_stonecutting = "minecraft:waxed_exposed_cut_copper_stairs_from_waxed_exposed_copper_stonecutting"
	waxed_exposed_cut_copper_stairs_from_waxed_exposed_cut_copper_stonecutting = "minecraft:waxed_exposed_cut_copper_stairs_from_waxed_exposed_cut_copper_stonecutting"
	waxed_oxidized_copper_from_honeycomb = "minecraft:waxed_oxidized_copper_from_honeycomb"
	waxed_oxidized_cut_copper = "minecraft:waxed_oxidized_cut_copper"
	waxed_oxidized_cut_copper_from_honeycomb = "minecraft:waxed_oxidized_cut_copper_from_honeycomb"
	waxed_oxidized_cut_copper_from_waxed_oxidized_copper_stonecutting = "minecraft:waxed_oxidized_cut_copper_from_waxed_oxidized_copper_stonecutting"
	waxed_oxidized_cut_copper_slab = "minecraft:waxed_oxidized_cut_copper_slab"
	waxed_oxidized_cut_copper_slab_from_honeycomb = "minecraft:waxed_oxidized_cut_copper_slab_from_honeycomb"
	waxed_oxidized_cut_copper_slab_from_waxed_oxidized_copper_stonecutting = "minecraft:waxed_oxidized_cut_copper_slab_from_waxed_oxidized_copper_stonecutting"
	waxed_oxidized_cut_copper_slab_from_waxed_oxidized_cut_copper_stonecutting = "minecraft:waxed_oxidized_cut_copper_slab_from_waxed_oxidized_cut_copper_stonecutting"
	waxed_oxidized_cut_copper_stairs = "minecraft:waxed_oxidized_cut_copper_stairs"
	waxed_oxidized_cut_copper_stairs_from_honeycomb = "minecraft:waxed_oxidized_cut_copper_stairs_from_honeycomb"
	waxed_oxidized_cut_copper_stairs_from_waxed_oxidized_copper_stonecutting = "minecraft:waxed_oxidized_cut_copper_stairs_from_waxed_oxidized_copper_stonecutting"
	waxed_oxidized_cut_copper_stairs_from_waxed_oxidized_cut_copper_stonecutting = "minecraft:waxed_oxidized_cut_copper_stairs_from_waxed_oxidized_cut_copper_stonecutting"
	waxed_weathered_copper_from_honeycomb = "minecraft:waxed_weathered_copper_from_honeycomb"
	waxed_weathered_cut_copper = "minecraft:waxed_weathered_cut_copper"
	waxed_weathered_cut_copper_from_honeycomb = "minecraft:waxed_weathered_cut_copper_from_honeycomb"
	waxed_weathered_cut_copper_from_waxed_weathered_copper_stonecutting = "minecraft:waxed_weathered_cut_copper_from_waxed_weathered_copper_stonecutting"
	waxed_weathered_cut_copper_slab = "minecraft:waxed_weathered_cut_copper_slab"
	waxed_weathered_cut_copper_slab_from_honeycomb = "minecraft:waxed_weathered_cut_copper_slab_from_honeycomb"
	waxed_weathered_cut_copper_slab_from_waxed_weathered_copper_stonecutting = "minecraft:waxed_weathered_cut_copper_slab_from_waxed_weathered_copper_stonecutting"
	waxed_weathered_cut_copper_slab_from_waxed_weathered_cut_copper_stonecutting = "minecraft:waxed_weathered_cut_copper_slab_from_waxed_weathered_cut_copper_stonecutting"
	waxed_weathered_cut_copper_stairs = "minecraft:waxed_weathered_cut_copper_stairs"
	waxed_weathered_cut_copper_stairs_from_honeycomb = "minecraft:waxed_weathered_cut_copper_stairs_from_honeycomb"
	waxed_weathered_cut_copper_stairs_from_waxed_weathered_copper_stonecutting = "minecraft:waxed_weathered_cut_copper_stairs_from_waxed_weathered_copper_stonecutting"
	waxed_weathered_cut_copper_stairs_from_waxed_weathered_cut_copper_stonecutting = "minecraft:waxed_weathered_cut_copper_stairs_from_waxed_weathered_cut_copper_stonecutting"
	weathered_cut_copper = "minecraft:weathered_cut_copper"
	weathered_cut_copper_from_weathered_copper_stonecutting = "minecraft:weathered_cut_copper_from_weathered_copper_stonecutting"
	weathered_cut_copper_slab = "minecraft:weathered_cut_copper_slab"
	weathered_cut_copper_slab_from_weathered_copper_stonecutting = "minecraft:weathered_cut_copper_slab_from_weathered_copper_stonecutting"
	weathered_cut_copper_slab_from_weathered_cut_copper_stonecutting = "minecraft:weathered_cut_copper_slab_from_weathered_cut_copper_stonecutting"
	weathered_cut_copper_stairs = "minecraft:weathered_cut_copper_stairs"
	weathered_cut_copper_stairs_from_weathered_copper_stonecutting = "minecraft:weathered_cut_copper_stairs_from_weathered_copper_stonecutting"
	weathered_cut_copper_stairs_from_weathered_cut_copper_stonecutting = "minecraft:weathered_cut_copper_stairs_from_weathered_cut_copper_stonecutting"
	wheat = "minecraft:wheat"
	white_banner = "minecraft:white_banner"
	white_bed = "minecraft:white_bed"
	white_candle = "minecraft:white_candle"
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
	yellow_candle = "minecraft:yellow_candle"
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
