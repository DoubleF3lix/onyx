execute store result score $xp_levels onyx.lib run experience query @s levels
experience set @s 0 levels
experience set @s 0 points
execute if score $xp_levels onyx.lib matches 512.. run experience remove @s 512 levels
execute if score $xp_levels onyx.lib matches 512.. run scoreboard players remove $xp_levels onyx.lib 512
execute if score $xp_levels onyx.lib matches 256.. run experience remove @s 256 levels
execute if score $xp_levels onyx.lib matches 256.. run scoreboard players remove $xp_levels onyx.lib 256
execute if score $xp_levels onyx.lib matches 128.. run experience remove @s 128 levels
execute if score $xp_levels onyx.lib matches 128.. run scoreboard players remove $xp_levels onyx.lib 128
execute if score $xp_levels onyx.lib matches 64.. run experience remove @s 64 levels
execute if score $xp_levels onyx.lib matches 64.. run scoreboard players remove $xp_levels onyx.lib 64
execute if score $xp_levels onyx.lib matches 32.. run experience remove @s 32 levels
execute if score $xp_levels onyx.lib matches 32.. run scoreboard players remove $xp_levels onyx.lib 32
execute if score $xp_levels onyx.lib matches 8.. run experience remove @s 16 levels
execute if score $xp_levels onyx.lib matches 16.. run scoreboard players remove $xp_levels onyx.lib 16
execute if score $xp_levels onyx.lib matches 8.. run experience remove @s 8 levels
execute if score $xp_levels onyx.lib matches 8.. run scoreboard players remove $xp_levels onyx.lib 8
execute if score $xp_levels onyx.lib matches 4.. run experience remove @s 4 levels
execute if score $xp_levels onyx.lib matches 4.. run scoreboard players remove $xp_levels onyx.lib 4
execute if score $xp_levels onyx.lib matches 2.. run experience remove @s 2 levels
execute if score $xp_levels onyx.lib matches 2.. run scoreboard players remove $xp_levels onyx.lib 2
execute if score $xp_levels onyx.lib matches 1.. run experience remove @s 1 levels
execute if score $xp_levels onyx.lib matches 1.. run scoreboard players remove $xp_levels onyx.lib 1
