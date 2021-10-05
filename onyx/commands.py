from nbtlib.tag import Compound
from onyx.class_types import Particle, Vector2, Vector3
from typing import Union
from onyx.text_component import TextComponent
from onyx.selector import Selector
from onyx.dev_util import translate, convert_experience_amount, convert_time
from onyx.registries import color, gamemode, difficulty, experience_type, weather_type, sound_channel, setblock_mode, fill_mode, clone_mask_mode, clone_mode, time_query, time, team_attribute, death_message_visibility, collision_rule, nametag_visibility
from onyx.split_registries.biome import biome
from onyx.split_registries.block import block
from onyx.split_registries.effect import effect
from onyx.split_registries.enchantment import enchantment
from onyx.split_registries.entity import entity
from onyx.split_registries.gamerule import gamerule
from onyx.split_registries.item import item
from onyx.split_registries.recipe import recipe
from onyx.split_registries.structure import structure
from onyx.util import Item, AbsPos2D, BlockPredicate


class Effect:
    @staticmethod
    def clear(targets: Selector, effect: Union[effect, list] = None):
        return Commands.push(f"effect clear {translate(targets)} {translate(effect)}")

    @staticmethod
    def give(targets: Selector, effect: effect, seconds: int = 30, amplifier: int = 1, show_particles: bool = False):
        return Commands.push(f"effect give {translate(targets)} {translate(effect)} {translate(seconds)} {translate(amplifier)} {translate(show_particles, normalize_boolean=True)}")


class Experience:
    @staticmethod
    def _template(type, players, amount, experience_type):
        if experience_type is None:
            amount = convert_experience_amount(amount)
            return Commands.push(f"experience {type} {translate(players)} {amount[0]} {amount[1]}")
        return Commands.push(f"experience {type} {translate(players)} {translate(amount)} {translate(experience_type)}")

    @staticmethod
    def add(players: Selector, amount: Union[int, str], experience_type: experience_type = None):
        return Experience._template("add", players, amount, experience_type)

    @staticmethod
    def clear(players: Selector):
        # Setting to 0 levels doesn't clear the points
        return Experience._template("add", players, -2147483647, experience_type.levels)

    @staticmethod
    def query(player: Selector, type: experience_type = experience_type.levels):
        return Commands.push(f"experience query {translate(player)} {translate(type)}")

    @staticmethod
    def set(players: Selector, amount: Union[int, str], experience_type: experience_type = None):
        return Experience._template("set", players, amount, experience_type)


class Forceload:
    @staticmethod
    def add(pos1: Vector2, pos2: Vector2 = None):
        if pos2 is None:
            pos2 = pos1
        return Commands.push(f"forceload add {translate(pos1)} {translate(pos2)}")

    @staticmethod
    def query(position: Vector2):
        return Commands.push(f"forceload query {translate(position)}")

    @staticmethod
    def remove(pos1: Vector2, pos2: Vector2 = None):
        if pos2 is None:
            pos2 = pos1
        return Commands.push(f"forceload remove {translate(pos1)} {translate(pos2)}")

    @staticmethod
    def remove_all():
        return Commands.push("forceload remove all")


class Recipe:
    @staticmethod
    def _template(mode, players, recipe):
        return Commands.push(f"recipe {mode} {translate(players)} {translate(recipe)}")

    @staticmethod
    def give(players: Selector, recipe: recipe):
        return Recipe._template("give", players, recipe)

    @staticmethod
    def take(players: Selector, recipe: recipe):
        return Recipe._template("take", players, recipe)


class Scoreboard:
    @staticmethod
    def list_player_scores(target: Selector):
        return Commands.push(f"scoreboard players list {translate(target)}")

    @staticmethod
    def reset_player_scores(target: Selector):
        return Commands.push(f"scoreboard players reset {translate(target)}")

    @staticmethod
    def list_objectives():
        return Commands.push("scoreboard objectives list")


class Tag:
    @staticmethod
    def add(targets: Selector, tag_name: str):
        return Commands.push(f"tag {translate(targets)} add {translate(tag_name)}")

    @staticmethod
    def list(targets: Selector):
        return Commands.push(f"tag {translate(targets)} list")

    @staticmethod
    def remove(targets: Selector, tag_name: str):
        return Commands.push(f"tag {translate(targets)} remove {translate(tag_name)}")


class Team:
    @staticmethod
    def add(name: str, display_name: TextComponent = None):
        return Commands.push(f"team add {translate(name)} {translate(display_name) if display_name else ''}")

    @staticmethod
    def empty(name: str):
        return Commands.push(f"team empty {translate(name)}")

    @staticmethod
    def join(name: str, targets: Selector):
        return Commands.push(f"team join {translate(name)} {translate(targets)}")

    @staticmethod
    def leave(targets: Selector):
        return Commands.push(f"team leave {translate(targets)}")

    @staticmethod
    def list(name: str = None):
        return Commands.push(f"team list {translate(name) if name else ''}")

    @staticmethod
    def modify(name: str, attribute: team_attribute, value: Union[bool, TextComponent, color, collision_rule, death_message_visibility, nametag_visibility]):
        return Commands.push(f"team modify {translate(name)} {translate(attribute)} {translate(value, normalize_boolean=True)}")

    @staticmethod
    def remove(name: str):
        return Commands.push(f"team remove {translate(name)}")


class Time:
    @staticmethod
    def add(time: str):
        return Commands.push(f"time add {convert_time(translate(time))}")

    @staticmethod
    def query(type: time_query):
        return Commands.push(f"time query {translate(type)}")

    @staticmethod
    def set(time: Union[str, time]):
        return Commands.push(f"time set {convert_time(translate(time))}")


class Worldborder:
    @staticmethod
    def add(distance: int, time: int):
        return Commands.push(f"worldborder add {translate(distance)} {translate(time)}")

    @staticmethod
    def center(position: AbsPos2D):
        return Commands.push(f"worldborder center {translate(position)}")

    @staticmethod
    def damage(per_block: int = None, buffer_distance: int = None):
        if per_block is None and buffer_distance is None:
            raise ValueError("Must define either 'per_block' or 'buffer_distance'")
        output = []
        if per_block:
            output.append(Commands.push(f"worldborder damage amount {translate(per_block)}"))
        if buffer_distance:
            output.append(Commands.push(f"worldborder damage buffer {translate(buffer_distance)}"))
        return output

    @staticmethod
    def get():
        return Commands.push("worldborder get")

    @staticmethod
    def set(distance: int, time: int):
        return Commands.push(f"worldborder set {translate(distance)} {translate(time)}")

    @staticmethod
    def warning(distance: int = None, time: int = None):
        if distance is None and time is None:
            raise ValueError("Must define either 'distance' or 'time'")
        output = []
        if distance:
            output.append(Commands.push(f"worldborder warning distance {translate(distance)}"))
        if time:
            output.append(Commands.push(f"worldborder warning time {translate(time)}"))
        return output
        

class Commands:
    def __init__(self, pack_object):
        Commands.function_contents = []
        Commands.pack_object = pack_object
        Commands.added_scoreboards = []
        Commands.init_commands = []
        Commands.active_function = None

        Commands.effect = Effect()
        Commands.experience = Experience()
        Commands.forceload = Forceload()
        Commands.recipe = Recipe()
        Commands.scoreboard = Scoreboard()
        Commands.tag = Tag()
        Commands.worldborder = Worldborder()

    @staticmethod
    def push(command, init=False):
        if isinstance(command, list):
            command = "\n".join(command)
        if init == False:
            Commands.function_contents.append(command)
            return command
        else:
            if command not in Commands.init_commands:
                Commands.pack_object.init_contents.append(command)
                Commands.init_commands.append(command)

    @staticmethod
    def clear(players: Selector, item: Union[item, str] = None, max_count: int = None):
        return Commands.push(f"clear {translate(players)} {translate(item)} {translate(max_count)}")

    @staticmethod
    def clone(corner1: Vector3, corner2: Vector3, location: Vector3, mask_mode: clone_mask_mode = clone_mask_mode.replace, filter: BlockPredicate = None, clone_mode: clone_mode = clone_mode.normal):
        if filter:
            mask_mode = clone_mask_mode.filtered
        return Commands.push(f"clone {translate(corner1)} {translate(corner2)} {translate(location)} {translate(mask_mode)}{f' {translate(filter)}' if translate(mask_mode) == 'filtered' else ''} {translate(clone_mode)}")

    @staticmethod
    def defaultgamemode(mode: gamemode):
        return Commands.push(f"defaultgamemode {translate(mode)}")
        
    @staticmethod
    def difficulty(difficulty: difficulty):
        return Commands.push(f"difficulty {translate(difficulty)}")

    @staticmethod
    def enchant(players: Selector, enchantment: Union[enchantment, dict], level: int = 1):
        if isinstance(enchantment, dict):
            return [Commands.push(f"enchant {translate(players)} {translate(enchant)} {translate(level)}") for enchant, level in enchantment.items()]
        else:
            return Commands.push(f"enchant {translate(players)} {translate(enchantment)} {translate(level)}")

    @staticmethod
    def fill(corner1: Vector3, corner2: Vector3, block: block, mode: fill_mode = fill_mode.replace, replace_block: block = None):
        if replace_block:
            mode = fill_mode.replace
        Commands.push(f"fill {translate(corner1)} {translate(corner2)} {translate(block)} {translate(mode) if mode else ''} {translate(replace_block) if replace_block else ''}")

    @staticmethod
    def gamemode(mode: gamemode, players: Selector):
        return Commands.push(f"gamemode {translate(mode)} {translate(players)}")

    @staticmethod
    def gamerule(rule: gamerule, value: Union[bool, int, str]):
        return Commands.push(f"gamerule {translate(rule)} {translate(value, normalize_boolean=True)}")

    @staticmethod
    def give(players: Selector, item: Union[item, Item] = None, count: int = None):
        return Commands.push(f"clear {translate(players)} {translate(item)} {translate(count)}")

    @staticmethod
    def help(command: str = None):
        return Commands.push(f"help {command if command else ''}")

    @staticmethod
    def kill(players: Selector):
        return Commands.push(f"kill {translate(players)}")

    @staticmethod
    def list(include_uuids: bool = False):
        return Commands.push(f"list {'uuids' if translate(include_uuids) else ''}")

    @staticmethod
    def locate(structure: structure):
        return Commands.push(f"locate {translate(structure)}")

    @staticmethod
    def locatebiome(biome: biome):
        return Commands.push(f"locatebiome {translate(biome)}")

    @staticmethod
    def me(text: str):
        return Commands.push(f"me {translate(text)}")

    @staticmethod
    def msg(targets: Selector, text: str):
        return Commands.push(f"msg {translate(targets)} {translate(text)}")

    @staticmethod
    def particle(particle_settings: Particle, force: bool = False, players: Selector = None):
        force = ["normal", "force"][int(translate(force))]
        return Commands.push(f"particle {translate(particle_settings)} {force} {translate(players)}")

    @staticmethod
    def playsound(sound: str, channel: sound_channel, players: Selector, position: Vector3 = None, volume: Union[int, float] = None, pitch: float = None):
        if translate(channel) == "any":
            raise ValueError("Sound channel 'any/*' is not supported in 'playsound'")
        if translate(pitch) < 0 and translate(pitch) > 2:
            raise ValueError("'pitch' must be between 0 and 2")

        return Commands.push(f"playsound {translate(sound)} {translate(channel)} {translate(players)} {translate(position)} {translate(volume)} {translate(pitch)}")

    @staticmethod
    def say(text: str):
        return Commands.push(f"say {translate(text)}")

    @staticmethod
    def seed():
        return Commands.push("seed")

    @staticmethod
    def setblock(position: Vector3, block: BlockPredicate, mode: setblock_mode = setblock_mode.replace):
        return Commands.push(f"setblock {translate(position)} {translate(block)} {translate(mode)}")

    @staticmethod
    def setworldspawn(position: Vector3, angle: Union[int, float] = 0):
        return Commands.push(f"setworldspawn {translate(position)} {translate(angle)}")

    @staticmethod
    def spawnpoint(players: Selector, position: Vector3, angle: Union[int, float] = 0):
        return Commands.push(f"spawnpoint {translate(players)} {translate(position)} {translate(angle)}")

    @staticmethod
    def spectate(target: Selector, source: Selector = "@s"):
        return Commands.push(f"spectate {translate(target)} {translate(source)}")

    @staticmethod
    def stopsound(targets: Selector, channel: sound_channel = None, sound: str = None):
        return Commands.push(f"stopsound {translate(targets)} {translate(channel)} {translate(sound)}")

    @staticmethod
    def summon(type: entity, position: Vector3, nbt: Compound = None):
        return Commands.push(f"summon {translate(type)} {translate(position)} {translate(nbt)}")

    @staticmethod
    def teammsg(text: str):
        return Commands.push(f"teammsg {translate(text)}")

    @staticmethod
    def teleport(source: Selector, destination: Union[Selector, Vector3], facing: Union[Selector, Vector3] = None):
        output = Commands.push(f"teleport {translate(source)} {destination}")
        if facing:
            output += " facing"
            if isinstance(facing, Selector):
                output += "entity "
            output += f"{translate(facing)}"
        return output

    @staticmethod
    def tellraw(players: Selector, text: TextComponent): 
        return Commands.push(f"tellraw {translate(players)} {translate(text)}")

    @staticmethod
    def weather(weather_type: weather_type):
        return Commands.push(f"weather {translate(weather_type)}")


""" 
advancement
attribute
bossbar
data
datapack
debug
item
loot
schedule
spreadplayers
title
perf
"""