from typing import Union

import nbtlib
from nbtlib.tag import Compound

import onyx.storage
from onyx.class_types import Particle, Vector2, Vector3
from onyx.dev_util import (
    convert_day_time,
    convert_experience_amount,
    convert_schedule_time,
    translate,
)
from onyx.registries import (
    advancement_mode,
    attribute,
    attribute_mode,
    clone_mask_mode,
    clone_mode,
    collision_rule,
    color,
    data_operator,
    datapack_enable_mode,
    death_message_visibility,
    difficulty,
    experience_type,
    fill_mode,
    gamemode,
    hand,
    nametag_visibility,
    schedule_mode,
    setblock_mode,
    sound_channel,
    team_attribute,
    time,
    time_query,
    weather_type,
)
from onyx.selector import Selector
from onyx.split_registries.biome import biome
from onyx.split_registries.block import block
from onyx.split_registries.effect import effect
from onyx.split_registries.enchantment import enchantment
from onyx.split_registries.entity import entity
from onyx.split_registries.gamerule import gamerule
from onyx.split_registries.item import item
from onyx.split_registries.recipe import recipe
from onyx.split_registries.structure import structure
from onyx.text_component import TextComponent
from onyx.util import AttributeModifier, Block, DataSource, Item


class Bossbar:
    """
    Bossbar commands
    """

    @staticmethod
    def list() -> str:
        """
        list - Gets a list of all bossbars. Only useful with ``execute store``.

        Returns:
            str: Command
        """
        return Commands.push("bossbar list")


class Data:
    """
    Data commands
    """

    @staticmethod
    def get(data_source: DataSource) -> str:
        """
        get - Gets a piece of data from a source

        Args:
            data_source (DataSource): The entity to get the data from. Only specify ``source_type``, ``location``, and ``path`` for the ``DataSource`` object.

        Returns:
            str: Command
        """
        return Commands.push(f"data get {translate(data_source)}")

    @staticmethod
    def merge(data_source: DataSource, data: Compound) -> str:
        """
        merge - Merges NBT with the data source

        Args:
            data_source (DataSource): The entity to merge the data with. Only specify ``source_type`` and ``location`` for the ``DataSource`` object.
            data (Compound): The data to be merged with the entity. Use ``nbtlib.Compound`` or stringified NBT.

        Returns:
            str: Command
        """
        return Commands.push(f"data merge {translate(data_source)} {translate(data)}")

    @staticmethod
    def modify(
        data_source: DataSource,
        operation: data_operator,
        value: Union[DataSource, nbtlib.Base],
        insert_index: int = None,
    ) -> str:
        """
        modify - Directly modify a piece of data on an entity

        Args:
            data_source (DataSource): The entity to modify the data of. Only specify ``source_type``, ``location``, and ``path`` for the ``DataSource`` object.
            operation (data_operator): How the data should be modified (append, insert, merge, prepend, or set). Use ``set_from`` if the data is being copied from another entity. Otherwise, use ``set_value``.
            value (Union[DataSource, nbtlib.Base]): Either another ``DataSource`` object to copy data from, or the value to set the data to. Use ``nbtlib.Base`` or stringified NBT if setting to a specific value.
            insert_index (int, optional): The index of ``path`` to modify the data of. Only specify if ``operation`` is ``insert``. Defaults to None.

        Returns:
            str: Command
        """
        if isinstance(value, DataSource):
            value = f"from {translate(value)}"
        return Commands.push(
            f"data modify {translate(data_source)} {translate(operation)}{(' ' + str(insert_index)) if insert_index else ''} {translate(value)}"
        )

    @staticmethod
    def remove(data_source: DataSource) -> str:
        """
        remove - Deletes a piece of data from an entity

        Args:
            data_source (DataSource): The data path to remove. Only specify ``source_type``, ``location``, and ``path`` for the ``DataSource`` object.

        Returns:
            str: Command
        """
        return Commands.push(f"data remove {translate(data_source)}")


class Datapack:
    """
    Datapack commands
    """

    @staticmethod
    def disable(pack_name: Union[str, "DataPack"]) -> str:
        """
        disable - Disables a data pack. Do not use this to have a data pack disable itself. You will not be able to re-enable it without running the command directly or without another data pack.

        Args:
            pack_name (Union[str, DataPack]): The data pack to disable. This can infer the data pack name from the ``DataPack`` object.

        Returns:
            str: Command
        """
        return Commands.push(f"datapack disable {pack_name}")

    @staticmethod
    def enable(
        pack_name: Union[str, "DataPack"],
        mode: datapack_enable_mode = None,
        other_pack: Union[str, "DataPack"] = None,
    ) -> str:
        """
        enable - Enables a data pack

        Args:
            pack_name (Union[str, DataPack]): The pack to enable
            mode (datapack_enable_mode, optional): How the data pack should be enabled (prepend, append, first, or last). Defaults to None.
            other_pack (Union[str, "DataPack"], optional): A pack that this pack should be enabled relative to. Only use if ``mode`` is ``after`` or ``before``. Defaults to None.

        Returns:
            str: Command
        """
        return Commands.push(
            f"datapack enable {translate(pack_name)}{' ' + translate(mode) if translate(mode) in {'first', 'last'} else ''}{' ' + translate(mode) if translate(mode) in {'after', 'before'} else ''}{' ' + translate(other_pack) if translate(mode) in {'after', 'before'} else ''}"
        )

    @staticmethod
    def list() -> str:
        """
        list - Gets a list of all data packs. Only useful with ``execute store``.

        Returns:
            str: Command
        """
        return Commands.push("datapack list")


class Debug:
    """
    Debug commands
    """

    @staticmethod
    def function(function: Union[str, "Function"]) -> str:
        """
        function - Debugs a function and stores relevant information in a text file

        Args:
            function (Union[str, Function]): The function to debug. This can infer the function name from the ``Function`` object.

        Returns:
            str: Command
        """
        return Commands.push(f"debug function {translate(function)}")

    @staticmethod
    def start() -> str:
        """
        start - Starts the debug mode

        Returns:
            str: Command
        """
        return Commands.push("debug start")

    @staticmethod
    def stop() -> str:
        """
        stop - Stops the debug mode

        Returns:
            str: Command
        """
        return Commands.push("debug stop")


class Effect:
    """
    Effect commands
    """

    @staticmethod
    def clear(
        targets: Selector, effect: Union[effect, list] = None
    ) -> Union[str, list]:
        """
        clear - Clears an effect from the selected targets

        Args:
            targets (Selector): The targets to clear the effect from
            effect (Union[effect, list], optional): The effects to remove. Set to a list of effects to remove multiple at once. Defaults to None.

        Returns:
            Union[str, list]: Command(s)
        """
        if isinstance(effect, list):
            return [
                Commands.push(f"effect clear {translate(targets)} {translate(q)}")
                for q in effect
            ]
        return Commands.push(f"effect clear {translate(targets)} {translate(effect)}")

    @staticmethod
    def give(
        targets: Selector,
        effect: effect,
        seconds: int = 30,
        amplifier: int = 1,
        show_particles: bool = False,
    ) -> str:
        """
        give - Gives an effect to the selected targets

        Args:
            targets (Selector): The targets to give the effect to
            effect (effect): The effect to give
            seconds (int, optional): The duration of the effect. Defaults to 30.
            amplifier (int, optional): How strong the effect is. Defaults to 1.
            show_particles (bool, optional): Whether or not effect particles should be shown. Defaults to False.

        Returns:
            str: Command
        """
        return Commands.push(
            f"effect give {translate(targets)} {translate(effect)} {translate(seconds)} {translate(amplifier)} {translate(show_particles, normalize_boolean=True)}"
        )


class Experience:
    """
    Experience commands
    """

    @staticmethod
    def _template(type, players, amount, experience_type):
        if experience_type is None:
            amount = convert_experience_amount(amount)
            return Commands.push(
                f"experience {type} {translate(players)} {amount[0]} {amount[1]}"
            )
        return Commands.push(
            f"experience {type} {translate(players)} {translate(amount)} {translate(experience_type)}"
        )

    @staticmethod
    def add(
        players: Selector,
        amount: Union[int, str],
        experience_type: experience_type = None,
    ) -> str:
        """
        add - Gives experience to a player

        Args:
            players (Selector): The player(s) to give experience to
            amount (Union[int, str]): The amount of experience to give. Supports both points with ``300`` and levels with ``"300L"``.

        Returns:
            str: Command
        """
        return Experience._template("add", players, amount, experience_type)

    @staticmethod
    def clear(players: Selector) -> str:
        """
        clear - Clears all experience from the player(s)

        Args:
            players (Selector): The players to clear experience from

        Returns:
            str: Command
        """
        return Experience._template("add", players, -2147483647, experience_type.levels)

    @staticmethod
    def query(player: Selector, type: experience_type = experience_type.levels) -> str:
        """
        query - Get the amount of experience from the player(s). Only useful with ``execute store``.

        Args:
            player (Selector): The players to get the experience of. If this selector targets multiple players, only the last targetted players experience will be saved.
            type (experience_type, optional): Levels or points. Defaults to experience_type.levels.

        Returns:
            str: Command
        """
        return Commands.push(f"experience query {translate(player)} {translate(type)}")

    @staticmethod
    def set(
        players: Selector,
        amount: Union[int, str],
        experience_type: experience_type = None,
    ) -> str:
        """
        set - Sets the player(s) experience

        Args:
            players (Selector): The players to set the experience of
            amount (Union[int, str]): What the experience should be set to. Supports both points with ``300`` and levels with ``"300L"``.
            experience_type (experience_type, optional): Levels or points. Defaults to None.

        Returns:
            str: Command
        """
        return Experience._template("set", players, amount, experience_type)


class Forceload:
    """
    Forceload commands
    """

    @staticmethod
    def add(pos1: Vector2, pos2: Vector2 = None) -> str:
        """
        add - Forceloads all chunks in the selected area

        Args:
            pos1 (Vector2): The first corner of the selection area
            pos2 (Vector2, optional): The second corner of the selection area. If left unspecified, then the first corner is used as the second corner. Defaults to None.

        Returns:
            str: Command
        """
        if pos2 is None:
            pos2 = pos1
        return Commands.push(f"forceload add {translate(pos1)} {translate(pos2)}")

    @staticmethod
    def query(position: Vector2) -> str:
        """
        query - Check if a position is forceloaded

        Args:
            position (Vector2): The position to check

        Returns:
            str: Command
        """
        return Commands.push(f"forceload query {translate(position)}")

    @staticmethod
    def remove(pos1: Vector2, pos2: Vector2 = None) -> str:
        """
        remove - Remove all forceloaded chunks in the selected area

        Args:
            pos1 (Vector2): The first corner of the selection area
            pos2 (Vector2, optional): The second corner of the selection area. If left unspecified, then the first corner is used as the second corner. Defaults to None.

        Returns:
            str: Command
        """
        if pos2 is None:
            pos2 = pos1
        return Commands.push(f"forceload remove {translate(pos1)} {translate(pos2)}")

    @staticmethod
    def remove_all() -> str:
        """
        remove_all - Remove all forceloaded chunks

        Returns:
            str: Command
        """
        return Commands.push("forceload remove all")


class Item:
    """
    Item commands
    """

    @staticmethod
    def modify(source: DataSource, modifier: Union["ItemModifier", str]) -> str:
        """
        modify - Apply a modifier to an item

        Args:
            source (DataSource): The source of the item. Only specify ``source_type``, ``location``, and ``path`` (as a slot) for the ``DataSource`` object.
            modifier (Union[ItemModifier, str]): The modifier to apply

        Returns:
            str: Command
        """
        return Commands.push(f"item modify {translate(source)} {translate(modifier)}")

    @staticmethod
    def replace(
        source: DataSource,
        value: Union[Item, DataSource],
        infer_replace_mode_override: str = None,
    ) -> str:
        """
        replace - Replaces an entity at the source with another item

        Args:
            source (DataSource): The location of the item to replace
            value (Union[Item, DataSource]): The item to replace the source. Set to an item to replace directly, or use a ``DataSource`` object to replace it with an item from another source.
            infer_replace_mode_override (str, optional): Whether or not ``from`` or ``with`` should be used in the command is inferred from the type of ``value``. If you're not getting the right output, you can edit this manually by setting this. Defaults to None.

        Returns:
            str: Command
        """
        value_prefix = (
            ("from" if isinstance(value, DataSource) else "with")
            if not infer_replace_mode_override
            else infer_replace_mode_override
        )
        return Commands.push(
            f"item replace {translate(source)} {translate(value_prefix)} {translate(value)}"
        )


class Loot:
    """
    Loot commands
    """

    @staticmethod
    def _multi_loot(
        type,
        target,
        loot_table,
        block,
        killed_entity,
        broken_with,
        infer_context_override,
    ):
        # Slot should only be defined for replace mode, so append it as one string if it was defined
        if loot_table and block:
            return Commands.push(
                f"loot {translate(type)} {translate(target)} {'fish' or infer_context_override} {translate(loot_table)} {translate(block)} {translate(broken_with)}"
            )
        elif killed_entity:
            return Commands.push(
                f"loot {translate(type)} {translate(target)} {'kill' or infer_context_override} {translate(killed_entity)}"
            )
        elif block:
            return Commands.push(
                f"loot {translate(type)} {translate(target)} {'mine' or infer_context_override} {translate(block)} {translate(broken_with)}"
            )
        else:
            return Commands.push(
                f"loot {translate(type)} {translate(target)} {'loot' or infer_context_override} {translate(loot_table)}"
            )

    @staticmethod
    def give(
        targets: Selector,
        loot_table: Union["LootTable", str] = None,
        block: Vector3 = None,
        killed_entity: Selector = None,
        broken_with: Union[item, hand] = None,
        infer_context_override: str = None,
    ) -> str:
        """
        give - Give a player some loot

        Args:
            targets (Selector): The players to give loot to
            loot_table (Union[LootTable, str], optional): The loot table containing the loot you want to give. Defaults to None.
            block (Vector3, optional): Either the block that was broken or where the loot should be placed in the case of ``fish``. Defaults to None.
            killed_entity (Selector, optional): The entity that was killed. Defaults to None.
            broken_with (Union[item, hand], optional): The item the block was broken with. Defaults to None.
            infer_context_override (str, optional): The context for the command is inferred from the parameters passed in. You can override this by setting this variable (should be ``fish``, ``mine``, ``loot``, or ``kill``). Defaults to None.

        Returns:
            str: Command
        """
        return Loot._multi_loot(
            "give",
            targets,
            loot_table,
            block,
            killed_entity,
            broken_with,
            infer_context_override,
        )

    @staticmethod
    def insert(
        target: Vector3,
        loot_table: Union["LootTable", str] = None,
        block: Vector3 = None,
        killed_entity: Selector = None,
        broken_with: Union[item, hand] = None,
        infer_context_override: str = None,
    ) -> str:
        """
        insert - Insert loot into a container

        Args:
            targets (Vector3): The block to insert the items in
            loot_table (Union[LootTable, str], optional): The loot table containing the loot you want to give. Defaults to None.
            block (Vector3, optional): Either the block that was broken or where the loot should be placed in the case of ``fish``. Defaults to None.
            killed_entity (Selector, optional): The entity that was killed. Defaults to None.
            broken_with (Union[item, hand], optional): The item the block was broken with. Defaults to None.
            infer_context_override (str, optional): The context for the command is inferred from the parameters passed in. You can override this by setting this variable (should be ``fish``, ``mine``, ``loot``, or ``kill``). Defaults to None.

        Returns:
            str: Command
        """
        return Loot._multi_loot(
            "insert",
            target,
            loot_table,
            block,
            killed_entity,
            broken_with,
            infer_context_override,
        )

    @staticmethod
    def replace(
        targets: DataSource,
        loot_table: Union["LootTable", str] = None,
        block: Vector3 = None,
        killed_entity: Selector = None,
        broken_with: Union[item, hand] = None,
        infer_context_override: str = None,
    ) -> str:
        """
        replace - Replace a slot in a container with loot

        Args:
            targets (DataSource): The data location to put the items in. Only specify ``source_type``, ``location``, and ``path`` in the ``DataSource`` object (where ``path`` is a slot name).
            loot_table (Union[LootTable, str], optional): The loot table containing the loot you want to give. Defaults to None.
            block (Vector3, optional): Either the block that was broken or where the loot should be placed in the case of ``fish``. Defaults to None.
            killed_entity (Selector, optional): The entity that was killed. Defaults to None.
            broken_with (Union[item, hand], optional): The item the block was broken with. Defaults to None.
            infer_context_override (str, optional): The context for the command is inferred from the parameters passed in. You can override this by setting this variable (should be ``fish``, ``mine``, ``loot``, or ``kill``). Defaults to None.

        Returns:
            str: Command
        """
        return Loot._multi_loot(
            "replace",
            targets,
            loot_table,
            block,
            killed_entity,
            broken_with,
            infer_context_override,
        )

    @staticmethod
    def spawn(
        target: Vector3,
        loot_table: Union["LootTable", str] = None,
        block: Vector3 = None,
        killed_entity: Selector = None,
        broken_with: Union[item, hand] = None,
        infer_context_override: str = None,
    ) -> str:
        """
        spawn - Summons loot as items

        Args:
            targets (Vector3): The location to spawn the items at
            loot_table (Union[LootTable, str], optional): The loot table containing the loot you want to give. Defaults to None.
            block (Vector3, optional): Either the block that was broken or where the loot should be placed in the case of ``fish``. Defaults to None.
            killed_entity (Selector, optional): The entity that was killed. Defaults to None.
            broken_with (Union[item, hand], optional): The item the block was broken with. Defaults to None.
            infer_context_override (str, optional): The context for the command is inferred from the parameters passed in. You can override this by setting this variable (should be ``fish``, ``mine``, ``loot``, or ``kill``). Defaults to None.

        Returns:
            str: Command
        """
        return Loot._multi_loot(
            "spawn",
            target,
            loot_table,
            block,
            killed_entity,
            broken_with,
            infer_context_override,
        )


class Perf:
    """
    Perf commands
    """

    @staticmethod
    def start() -> str:
        """
        start - Start capturing metrics on a server. This will automatically stop after 10 seconds.

        Returns:
            str: Command
        """
        return Commands.push("perf start")

    @staticmethod
    def stop() -> str:
        """
        stop - Stop capturing metrics on a server prematurely

        Returns:
            str: Command
        """
        return Commands.push("perf stop")


class Recipe:
    """
    Recipe commands
    """

    @staticmethod
    def _template(mode, players, recipe) -> str:
        return Commands.push(f"recipe {mode} {translate(players)} {translate(recipe)}")

    @staticmethod
    def give(players: Selector, recipe: recipe) -> str:
        """
        give - Gives player(s) a recipe

        Args:
            players (Selector): The players to give the recipe to
            recipe (recipe): The recipe to give

        Returns:
            str: Command
        """
        return Recipe._template("give", players, recipe)

    @staticmethod
    def take(players: Selector, recipe: recipe) -> str:
        """
        take - Takes a recipe from the player(s)

        Args:
            players (Selector): The players to take the recipe from
            recipe (recipe): The recipe to take

        Returns:
            str: Command
        """
        return Recipe._template("take", players, recipe)


class Schedule:
    """
    Schedule commands
    """

    @staticmethod
    def clear(function: Union["Function", str]) -> str:
        """
        clear - Clear a function from the schedule

        Args:
            function (Union[Function, str]): The function to clear

        Returns:
            str: Command
        """
        return Commands.push(f"schedule clear {translate(function)}")

    @staticmethod
    def function(
        function: Union["Function", str],
        time: Union[int, str],
        schedule_mode: schedule_mode = schedule_mode.replace,
    ) -> str:
        """
        function - Schedules a function

        Args:
            function (Union[Function, str]): The function to schedule
            time (Union[int, str]): The time to wait before the function runs. If ``int``, unit is ticks. Ticks, seconds, minutes, hours, days, weeks are supported as a string. 3, "3t", "3s", "3m", "3h", "3d", and "3w" are all supported values. Note that the unit will be converted to the closest matching neighbor. Ticks are left as ticks, minutes are converted to seconds, hours are converted to seconds, and weeks are converted to days.
            schedule_mode (schedule_mode, optional): Whether or not the functions existing schedule time or allow multiple schedules for the same function to exist at once. Defaults to schedule_mode.replace.

        Returns:
            str: Command
        """
        return Commands.push(
            f"schedule function {translate(function)} {convert_schedule_time(translate(time))} {translate(schedule_mode)}"
        )


class Scoreboard:
    """
    Scoreboard commands
    """

    @staticmethod
    def list_player_scores(target: Selector) -> str:
        """
        list_player_scores - Get a list of all scores for a player

        Args:
            target (Selector): The players to get the scores of

        Returns:
            str: Command
        """
        return Commands.push(f"scoreboard players list {translate(target)}")

    @staticmethod
    def reset_player_scores(target: Selector) -> str:
        """
        reset_player_scores - Reset all scores of the player(s)

        Args:
            target (Selector): The players to reset the scores of

        Returns:
            str: Command
        """
        return Commands.push(f"scoreboard players reset {translate(target)}")

    @staticmethod
    def list_objectives() -> str:
        """
        list_objectives - Get a list of all objectives. Only useful with ``execute store``.

        Returns:
            str: Command
        """
        return Commands.push("scoreboard objectives list")


class Tag:
    """
    Tag commands
    """

    @staticmethod
    def add(targets: Selector, tag_name: str) -> str:
        """
        add - Add a tag to the target(s)

        Args:
            targets (Selector): The targets to add the tag to
            tag_name (str): The tag to add

        Returns:
            str: Command
        """
        return Commands.push(f"tag {translate(targets)} add {translate(tag_name)}")

    @staticmethod
    def list(targets: Selector) -> str:
        """
        list - Get a list of all tags on the target(s)

        Args:
            targets (Selector): The targets to get the tags of

        Returns:
            str: Command
        """
        return Commands.push(f"tag {translate(targets)} list")

    @staticmethod
    def remove(targets: Selector, tag_name: str) -> str:
        """
        remove - Remove a tag from the target(s)

        Args:
            targets (Selector): The targets to remove the tag from
            tag_name (str): The tag to remove

        Returns:
            str: Command
        """
        return Commands.push(f"tag {translate(targets)} remove {translate(tag_name)}")


class Team:
    """
    Team commands
    """

    @staticmethod
    def add(name: str, display_name: TextComponent = None) -> str:
        """
        add - Creates a team

        Args:
            name (str): The name of the team
            display_name (TextComponent, optional): The display name of the team. Defaults to None.

        Returns:
            str: Command
        """
        return Commands.push(
            f"team add {translate(name)} {translate(display_name) if display_name else ''}"
        )

    @staticmethod
    def empty(name: str) -> str:
        """
        empty - Empties a team

        Args:
            name (str): The team to empty

        Returns:
            str: Command
        """
        return Commands.push(f"team empty {translate(name)}")

    @staticmethod
    def join(name: str, targets: Selector) -> str:
        """
        join - Adds the target(s) to the team

        Args:
            name (str): The team to add the target(s) to
            targets (Selector): The target(s) to add to the team

        Returns:
            str: Command
        """
        return Commands.push(f"team join {translate(name)} {translate(targets)}")

    @staticmethod
    def leave(targets: Selector) -> str:
        """
        leave - Removes the target(s) from their teams

        Args:
            targets (Selector): The target(s) to remove from their teams

        Returns:
            str: Command
        """
        return Commands.push(f"team leave {translate(targets)}")

    @staticmethod
    def list(name: str = None) -> str:
        """
        list - Get a list of all players in a team

        Args:
            name (str, optional): The team to get the list of players from. Defaults to None.

        Returns:
            str: Command
        """
        return Commands.push(f"team list {translate(name) if name else ''}")

    @staticmethod
    def modify(
        name: str,
        attribute: team_attribute,
        value: Union[
            bool,
            TextComponent,
            color,
            collision_rule,
            death_message_visibility,
            nametag_visibility,
        ],
    ) -> str:
        """
        modify - Modifies a team's attribute

        Args:
            name (str): The team to modify
            attribute (team_attribute): The attribute to modify
            value (Union[bool, TextComponent, color, collision_rule, death_message_visibility, nametag_visibility]): The value to set the attribute to

        Returns:
            str: Command
        """
        return Commands.push(
            f"team modify {translate(name)} {translate(attribute)} {translate(value, normalize_boolean=True)}"
        )

    @staticmethod
    def remove(name: str) -> str:
        """
        remove - Deletes a team

        Args:
            name (str): The team to delete

        Returns:
            str: Command
        """
        return Commands.push(f"team remove {translate(name)}")


class Time:
    """
    Time commands
    """

    @staticmethod
    def add(time: str) -> str:
        """
        add - Adds time to the world

        Args:
            time (str): The amount of time to add. Seconds, minutes, hours, days, weeks are supported as a string. 3, "3s", "3m", "3h", "3d", and "3w" are all supported values. Note that all units will be converted to time units. See `this wiki page <https://minecraft.fandom.com/wiki/Daylight_cycle#Conversions>`_ for more info.

        Returns:
            str: Command
        """
        return Commands.push(f"time add {convert_day_time(translate(time))}")

    @staticmethod
    def query(type: time_query) -> str:
        """
        query - Get the current time

        Args:
            type (time_query): What type of time should be queried (day count, day time, or game time)

        Returns:
            str: Command
        """
        return Commands.push(f"time query {translate(type)}")

    @staticmethod
    def set(time: Union[str, time]) -> str:
        """
        set - Sets the time of the world

        Args:
            time (str): The amount to be set. Seconds, minutes, hours, days, weeks are supported as a string. 3, "3s", "3m", "3h", "3d", and "3w" are all supported values. Note that all units will be converted to time units. See `this wiki page <https://minecraft.fandom.com/wiki/Daylight_cycle#Conversions>`_ for more info.

        Returns:
            str: Command
        """
        return Commands.push(f"time set {convert_day_time(translate(time))}")


class Title:
    """
    Title commands
    """

    @staticmethod
    def actionbar(players: Selector, text: TextComponent) -> str:
        """
        actionbar - Sets text in the action bar

        Args:
            players (Selector): The players to show the text to
            text (TextComponent): The text to show

        Returns:
            str: Command
        """
        return Commands.push(f"title {translate(players)} actionbar {translate(text)}")

    # Clears all titles
    @staticmethod
    def clear(players: Selector) -> str:
        """
        clear - Clear all titles

        Args:
            players (Selector): The players to clear the titles of

        Returns:
            str: Command
        """
        return Commands.push(f"title {translate(players)} clear")

    # Resets subtitle and times
    @staticmethod
    def reset(players: Selector) -> str:
        """
        reset - Reset subtitle and title timings to their default value

        Args:
            players (Selector): The players to reset the subtitles and title timings of

        Returns:
            str: Command
        """
        return Commands.push(f"title {translate(players)} reset")

    @staticmethod
    def subtitle(
        players: Selector, text: TextComponent, only_subtitle: bool = False
    ) -> str:
        """
        subtitle - Sets text as a subtitle

        Args:
            players (Selector): The players to show the text to
            text (TextComponent): The text to show
            only_subtitle (bool, optional): Whether or not the subtitle will be shown by itself. If ``True``, a blank title will be created. Defaults to False.

        Returns:
            str: Command
        """
        if only_subtitle:
            Commands.push(f'title {translate(players)} title " "')
        return Commands.push(f"title {translate(players)} subtitle {translate(text)}")

    @staticmethod
    def times(players: Selector, fadeIn: int, stay: int, fadeOut: int) -> str:
        """
        times - Sets the fade in, stay, and fade out times for titles

        Args:
            players (Selector): The players to modify the title timings of
            fadeIn (int): How long it takes for the text to fade in in ticks
            stay (int): How long the text will stay in ticks
            fadeOut (int): How long it takes for the text to fade out in ticks

        Returns:
            str: Command
        """
        return Commands.push(
            f"title {translate(players)} times {fadeIn} {stay} {fadeOut}"
        )

    @staticmethod
    def title(players: Selector, text: TextComponent) -> str:
        """
        title - Sets text as a title

        Args:
            players (Selector): The players to show the text to
            text (TextComponent): The text to show

        Returns:
            str: Command
        """
        return Commands.push(f"title {translate(players)} title {translate(text)}")


class Trigger:
    """
    Trigger commands
    """

    @staticmethod
    def add(objective: Union[str, "ScoreboardObj"], value: Union[int, float]) -> str:
        """
        add - Adds to the score of a trigger objective

        Args:
            objective (Union[str,): The objective to add to the score of. Player is not specified as the scoreboard player is ``@s``.
            value (Union[int, float]): The value to add

        Returns:
            str: Command
        """
        return Commands.push(f"trigger {translate(objective)} add {translate(value)}")

    @staticmethod
    def set(objective: Union[str, "ScoreboardObj"], value: Union[int, float]) -> str:
        """
        sets - Sets a score of a trigger objective

        Args:
            objective (Union[str,): The objective to set the score of. Player is not specified as the scoreboard player is ``@s``.
            value (Union[int, float]): The value to set

        Returns:
            str: Command
        """
        return Commands.push(f"trigger {translate(objective)} set {translate(value)}")


class Worldborder:
    """
    Worldborder commands
    """

    @staticmethod
    def add(distance: int, time: int = 0) -> str:
        """
        add - Increases the area of the world border

        Args:
            distance (int): The distance in blocks that will be added to the world border (even numbers will go to half blocks)
            time (int): How long it should take for the world border to transition to the new size. Defaults to 0.

        Returns:
            str: Command
        """
        return Commands.push(f"worldborder add {translate(distance)} {translate(time)}")

    @staticmethod
    def center(position: Vector2) -> str:
        """
        center - Defines the center of the world border

        Args:
            position (AbsPos2D): The position to set the center of the world border to

        Returns:
            str: Command
        """
        return Commands.push(f"worldborder center {translate(position)}")

    @staticmethod
    def damage(per_block: int = None, buffer_distance: int = None) -> str:
        """
        damage - Sets the amount of damage done by the world border

        Args:
            per_block (int, optional): How much damage should be done to the player per second per block that they move past the world border buffer. Defaults to None.
            buffer_distance (int, optional): How distance from the world border the player must be before taking damage. Defaults to None.

        Raises:
            ValueError: Neither ``per_block`` nor ``buffer_distance`` are specified

        Returns:
            str: Command
        """
        if per_block is None and buffer_distance is None:
            raise ValueError("Must define either 'per_block' or 'buffer_distance'")
        output = []
        if per_block:
            output.append(
                Commands.push(f"worldborder damage amount {translate(per_block)}")
            )
        if buffer_distance:
            output.append(
                Commands.push(f"worldborder damage buffer {translate(buffer_distance)}")
            )
        return output

    @staticmethod
    def get() -> str:
        """
        get - Gets the world border size. Only useful with ``execute store``.

        Returns:
            str: Command
        """
        return Commands.push("worldborder get")

    @staticmethod
    def set(distance: int, time: int = 0) -> str:
        """
        set - Sets the world border size

        Args:
            distance (int): The new size of the world border
            time (int): How long it should take for the world border to transition to the new size. Defaults to 0.

        Returns:
            str: Command
        """
        return Commands.push(f"worldborder set {translate(distance)} {translate(time)}")

    @staticmethod
    def warning(distance: int = None, time: int = None) -> list:
        """
        warning - Sets a world border warning

        Args:
            distance (int, optional): The distance the player has to be from the world border to start showing a red border.. Defaults to None.
            time (int, optional): The time in seconds the world border has to be away from the player before showing a red border. Defaults to None.

        Raises:
            ValueError: Neither ``distance`` nor ``time`` are specified

        Returns:
            list: Commands
        """
        if distance is None and time is None:
            raise ValueError("Must define either 'distance' or 'time'")
        output = []
        if distance:
            output.append(
                Commands.push(f"worldborder warning distance {translate(distance)}")
            )
        if time:
            output.append(Commands.push(f"worldborder warning time {translate(time)}"))
        return output


class Commands:
    """
    Commands - A class containing all the commands in the game. Commands with many sub-commands are split into their own classes.
    """

    def __init__(self):
        Commands.function_contents = []
        Commands.added_scoreboards = []
        Commands.init_commands = []
        Commands.active_function = None

        Commands.bossbar = Bossbar()
        Commands.data = Data()
        Commands.datapack = Datapack()
        Commands.data_pack = Datapack()
        Commands.debug = Debug()
        Commands.effect = Effect()
        Commands.experience = Experience()
        Commands.forceload = Forceload()
        Commands.item = Item()
        Commands.loot = Loot()
        Commands.perf = Perf()
        Commands.recipe = Recipe()
        Commands.schedule = Schedule()
        Commands.scoreboard = Scoreboard()
        Commands.tag = Tag()
        Commands.team = Team()
        Commands.time = Time()
        Commands.title = Title()
        Commands.trigger = Trigger()
        Commands.worldborder = Worldborder()
        Commands.xp = Experience()

    @staticmethod
    def push(command: str, init: bool = False) -> str:
        """
        push - Adds a command to the function contents. All function calls for commands go through this function at some point.

        Args:
            command (str): The command to add
            init (bool, optional): Whether or not the command is added to the pack's ``_init.mcfunction``. Defaults to False.

        Returns:
            str: The command that was added
        """
        if isinstance(command, list):
            command = "\n".join(q.strip() for q in command)
        else:
            command = command.strip()
        if not init:
            Commands.function_contents.append(command)
            return command
        else:
            if command not in Commands.init_commands:
                onyx.storage.cpo.init_contents.append(command)
                Commands.init_commands.append(command)

    @staticmethod
    def comment(text: str, preline: int = 1, postline: int = 0) -> None:
        """
        comment - Adds a comment to the function

        Args:
            text (str): The comment contents
            preline (int, optional): How many blank lines should be inserted before the comment. Defaults to 1.
            postline (int, optional): How many blank lines should be inserted after the comment. Defaults to 0.
        """
        for _ in range(preline):
            Commands.push("")
        Commands.push(f"# {text}")
        for _ in range(postline):
            Commands.push("")

    @staticmethod
    def advancement(
        should_revoke: bool,
        players: Selector,
        advancement_mode: advancement_mode,
        advancement_source: Union["Advancement", str] = None,
    ) -> str:
        """
        advancement - Modify advancements on players

        Args:
            should_revoke (bool): Whether or not the advancement specified should be revoked or not.
            players (Selector): The players to modify the advancements of
            advancement_mode (advancement_mode): How the advancement should be modified (everything, from, only, through, until)
            advancement_source (Union[Advancement, optional): The source of the advancement that should be added or removed to players. Only specify if ``advancement_mode`` is NOT ``everything``. Defaults to None.

        Returns:
            str: Command
        """
        return Commands.push(
            f"advancement {'grant' if not should_revoke else 'revoke'} {translate(players)} {translate(advancement_mode)}{' ' + translate(advancement_source) if advancement_source else ''}"
        )

    @staticmethod
    def attribute(
        targets: Selector,
        attribute: attribute,
        attribute_mode: attribute_mode,
        modifier: AttributeModifier = None,
        scale: Union[int, float] = 1,
        base_value: int = None,
    ) -> str:
        """
        attribute - Modify attributes on entities

        Args:
            targets (Selector): The entities to modify the attributes of
            attribute (attribute): The attribute to modify
            attribute_mode (attribute_mode): How the attribute should be modified (get, get_base, set_base, add_modifier, etc.)
            modifier (AttributeModifier, optional): The modifier to apply to the selected attribute. Only use with modifier advancement modes. Defaults to None.
            scale (Union[int, float], optional): The scale at which an attribute should be retrieved. Only useful with ``execute store``. Defaults to 1.
            base_value (int, optional): The value for ``base set``. Should only be specified if ``attribute_mode`` is ``base set``. Defaults to None.

        Returns:
            str: Command
        """
        if translate(attribute) in {"modifier value get", "modifier remove"}:
            modifier = translate(modifier, just_uuid=True)
        # Scale is only used in get_modifier, get, and get_base
        translated_attribute_mode = translate(attribute_mode)
        if modifier and translated_attribute_mode == "modifier add":
            return Commands.push(
                f"attribute {translate(targets)} {translate(attribute)} {translated_attribute_mode} {translate(modifier)}"
            )
        elif modifier and translated_attribute_mode in {"modifier value get"}:
            return Commands.push(
                f"attribute {translate(targets)} {translate(attribute)} {translated_attribute_mode} {translate(modifier, just_uuid=True)} {translate(scale)}"
            )
        elif modifier and translated_attribute_mode in {"modifier remove"}:
            return Commands.push(
                f"attribute {translate(targets)} {translate(attribute)} {translated_attribute_mode} {translate(modifier, just_uuid=True)}"
            )
        elif translated_attribute_mode in {"get", "base get"}:
            return Commands.push(
                f"attribute {translate(targets)} {translate(attribute)} {translated_attribute_mode} {translate(scale)}"
            )
        elif translated_attribute_mode in {"base set"}:
            return Commands.push(
                f"attribute {translate(targets)} {translate(attribute)} {translated_attribute_mode} {translate(base_value)}"
            )

    @staticmethod
    def clear(
        players: Selector, item: Union[item, str] = None, max_count: int = None
    ) -> str:
        """
        clear - Clears an item from players

        Args:
            players (Selector): The players to clear the item from
            item (Union[item, str], optional): The item to clear. Defaults to None.
            max_count (int, optional): The limit on how many items can be cleared. Defaults to None.

        Returns:
            str: Command
        """
        return Commands.push(
            f"clear {translate(players)} {translate(item)} {translate(max_count)}"
        )

    @staticmethod
    def clone(
        corner1: Vector3,
        corner2: Vector3,
        location: Vector3,
        mask_mode: clone_mask_mode = clone_mask_mode.replace,
        filter: Block = None,
        clone_mode: clone_mode = clone_mode.normal,
    ) -> str:
        """
        clone - Clone blocks in a selected area

        Args:
            corner1 (Vector3): Corner 1 of the selection area
            corner2 (Vector3): Corner 2 of the selection area
            location (Vector3): The location the selection area should be cloned to
            mask_mode (clone_mask_mode, optional): What blocks should be selected in the clone area. ``filtered`` removes blocks that don't match the block/block tag specified in the ``filter`` argument. ``masked`` prevents air from overriding blocks at the location. ``replace`` replaces everything at the location. Defaults to clone_mask_mode.replace.
            filter (Block, optional): Argument for ``mask_mode``. Only specify if ``mask_mode`` is ``filtered``. Defaults to None.
            clone_mode (clone_mode, optional): How the cloning should be done (force, move, or normal). Defaults to clone_mode.normal.

        Returns:
            str: Command
        """
        if filter:
            mask_mode = clone_mask_mode.filtered
        return Commands.push(
            f"clone {translate(corner1)} {translate(corner2)} {translate(location)} {translate(mask_mode)}{f' {translate(filter)}' if translate(mask_mode) == 'filtered' else ''} {translate(clone_mode)}"
        )

    @staticmethod
    def defaultgamemode(mode: gamemode) -> str:
        """
        defaultgamemode - Sets the default game mode

        Args:
            mode (gamemode): The gamemode to set as the default

        Returns:
            str: Command
        """
        return Commands.push(f"defaultgamemode {translate(mode)}")

    @staticmethod
    def difficulty(difficulty: difficulty) -> str:
        """
        difficulty - Sets the difficulty

        Args:
            difficulty (difficulty): The difficulty to set

        Returns:
            str: Command
        """
        return Commands.push(f"difficulty {translate(difficulty)}")

    @staticmethod
    def enchant(
        players: Selector, enchantment: Union[enchantment, dict], level: int = 1
    ) -> Union[str, list]:
        """
        enchant - Adds enchantments to the selected item on a player

        Args:
            players (Selector): The players whose selected item should be enchanted
            enchantment (Union[enchantment, dict]): The enchantment to apply. Can either be specified as an enchantment or a dictionary. If dictionary, the keys are the enchantments and the values are the levels.
            level (int, optional): The level of the enchantment. Only specify if ``enchantment`` is not a dictionary. Defaults to 1.

        Returns:
            Union[str, list]: Command(s)
        """
        if isinstance(enchantment, dict):
            return [
                Commands.push(
                    f"enchant {translate(players)} {translate(enchant)} {translate(level)}"
                )
                for enchant, level in enchantment.items()
            ]
        else:
            return Commands.push(
                f"enchant {translate(players)} {translate(enchantment)} {translate(level)}"
            )

    @staticmethod
    def fill(
        corner1: Vector3,
        corner2: Vector3,
        block: block,
        mode: fill_mode = fill_mode.replace,
        replace_block: block = None,
    ) -> str:
        """
        fill - Fills all blocks in an area with a specified block

        Args:
            corner1 (Vector3): Corner 1 of the selection area
            corner2 (Vector3): Corner 2 of the selection area
            block (block): The block to fill in the selection area
            mode (fill_mode, optional): How the fill should be done (destroy, hollow, keep, outline, replace). Defaults to fill_mode.replace.
            replace_block (block, optional): What blocks should be replaced. Only specify if ``mode`` is ``replace``. Defaults to None.

        Returns:
            str: Command
        """
        if replace_block:
            mode = fill_mode.replace
        return Commands.push(
            f"fill {translate(corner1)} {translate(corner2)} {translate(block)} {translate(mode) if mode else ''} {translate(replace_block) if replace_block else ''}"
        )

    @staticmethod
    def function(function: Union["Function", str]) -> str:
        """
        function - Executes a function

        Args:
            function (Union[Function, str]): The function to execute. An alternative to ``function <FunctionObj>`` is just ``<FunctionObj()>``.

        Returns:
            str: Command
        """
        return Commands.push(f"function {translate(function)}")

    @staticmethod
    def gamemode(mode: gamemode, players: Selector) -> str:
        """
        gamemode - Sets the gamemode of players

        Args:
            mode (gamemode): The gamemode to set
            players (Selector): The players to set the gamemode of

        Returns:
            str: Command
        """
        return Commands.push(f"gamemode {translate(mode)} {translate(players)}")

    @staticmethod
    def gamerule(rule: gamerule, value: Union[bool, int, str]) -> str:
        """
        gamerule - Modifies a gamerule

        Args:
            rule (gamerule): The rule to modify
            value (Union[bool, int, str]): The new value of the gamerule

        Returns:
            str: Command
        """
        return Commands.push(
            f"gamerule {translate(rule)} {translate(value, normalize_boolean=True)}"
        )

    @staticmethod
    def give(players: Selector, item: Union[item, Item], count: int = None) -> str:
        """
        give - Gives an item to players

        Args:
            players (Selector): The players to give the item to
            item (Union[item, Item]): The item to be given. If you need to specify item NBT, use an ``Item`` object.
            count (int, optional): How many of the item should be given. Defaults to None.

        Returns:
            str: Command
        """
        return Commands.push(
            f"give {translate(players)} {translate(item)} {translate(count)}"
        )

    @staticmethod
    def help(command: str = None) -> str:
        """
        help - Displays help for a command

        Args:
            command (str, optional): The command to get help for. Defaults to None.

        Returns:
            str: Command
        """
        return Commands.push(f"help{' ' + translate(command) if command else ''}")

    @staticmethod
    def kill(targets: Selector, clean_kill: bool = False) -> str:
        """
        kill - Kills entities

        Args:
            targets (Selector): The entities to kill
            clean_kill (bool, optional): If ``True``, then a ``data merge`` command is used instead to leave no trace of the entity (no particles, items, etc.). This will not work on players (it won't fail, but it won't do anything to them either). Defaults to False.

        Returns:
            str: Command
        """
        if not clean_kill:
            return Commands.push(f"kill {translate(targets)}")
        return Commands.push(
            f'execute as {translate(targets)} run data merge entity @s {{Health:0.0f,DeathTime:19s,DeathLootTable:"minecraft:empty"}}'
        )

    @staticmethod
    def list(include_uuids: bool = False) -> str:
        """
        list - Lists all online players

        Args:
            include_uuids (bool, optional): Whether or not the UUID should be listed next to the player name. Defaults to False.

        Returns:
            str: Command
        """
        return Commands.push(f"list{' uuids' if translate(include_uuids) else ''}")

    @staticmethod
    def locate(structure: structure) -> str:
        """
        locate - Get the distance to the nearest specified structure

        Args:
            structure (structure): The structure to target

        Returns:
            str: Command
        """
        return Commands.push(f"locate {translate(structure)}")

    @staticmethod
    def locatebiome(biome: biome) -> str:
        """
        locatebiome - Get the distance to the nearest specified biome

        Args:
            biome (biome): The biome to target

        Returns:
            str: Command
        """
        return Commands.push(f"locatebiome {translate(biome)}")

    @staticmethod
    def me(text: str) -> str:
        """
        me - Display a message about the executor

        Args:
            text (str): The message to display

        Returns:
            str: Command
        """
        return Commands.push(f"me {translate(text)}")

    @staticmethod
    def msg(players: Selector, text: str) -> str:
        """
        msg - Messages a player

        Args:
            players (Selector): The players to message
            text (str): The message to send

        Returns:
            str: Command
        """
        return Commands.push(f"msg {translate(players)} {translate(text)}")

    @staticmethod
    def particle(
        particle_settings: Particle, force: bool = False, players: Selector = None
    ) -> str:
        """
        particle - Displays a particle

        Args:
            particle_settings (Particle): Information about the particle itself
            force (bool, optional): Whether the particle should be forced to render. Defaults to False.
            players (Selector, optional): The players who can see the particle. Defaults to None.

        Returns:
            str: Command
        """
        force = ["normal", "force"][int(translate(force))]
        return Commands.push(
            f"particle {translate(particle_settings)} {force} {translate(players)}"
        )

    @staticmethod
    def playsound(
        sound: str,
        channel: sound_channel,
        players: Selector,
        position: Vector3 = None,
        volume: Union[int, float] = None,
        pitch: float = None,
    ) -> str:
        """
        playsound - Plays a sound

        Args:
            sound (str): The sound to play
            channel (sound_channel): The channel to play the sound on
            players (Selector): The players to play the sound to
            position (Vector3, optional): The position that the sound should be played from. Defaults to None.
            volume (Union[int, float], optional): How far away the sound can be heard in blocks. Defaults to None.
            pitch (float, optional): The pitch of the sound. Defaults to None.

        Raises:
            ValueError: Invalid sound channel (``stopsound`` exclusive)
            ValueError: Invalid pitch value (must be between 0 and 2)

        Returns:
            str: Command
        """
        if translate(channel) == "any":
            raise ValueError("Sound channel 'any/*' is not supported in 'playsound'")
        if translate(pitch) < 0 and translate(pitch) > 2:
            raise ValueError("'pitch' must be between 0 and 2")

        return Commands.push(
            f"playsound {translate(sound)} {translate(channel)} {translate(players)} {translate(position)} {translate(volume)} {translate(pitch)}"
        )

    @staticmethod
    def say(text: str) -> str:
        """
        say - Prints text to chat

        Args:
            text (str): The text to print

        Returns:
            str: Command
        """
        return Commands.push(f"say {translate(text)}")

    @staticmethod
    def seed() -> str:
        """
        seed - Gets the world seed

        Returns:
            str: Command
        """
        return Commands.push("seed")

    @staticmethod
    def setblock(
        position: Vector3, block: Block, mode: setblock_mode = setblock_mode.replace
    ) -> str:
        """
        setblock - Sets a block

        Args:
            position (Vector3): The position to set the block at
            block (Block): The block to set
            mode (setblock_mode, optional): How the block should be set (destroy, keep, replace). Defaults to setblock_mode.replace.

        Returns:
            str: Command
        """
        return Commands.push(
            f"setblock {translate(position)} {translate(block)} {translate(mode)}"
        )

    @staticmethod
    def setworldspawn(position: Vector3, angle: Union[int, float] = 0) -> str:
        """
        setworldspawn - Sets the world spawn

        Args:
            position (Vector3): The position to set the world spawn at
            angle (Union[int, float], optional): The Y (horizontal) angle that the players will spawn at. Defaults to 0.

        Returns:
            str: Command
        """
        return Commands.push(f"setworldspawn {translate(position)} {translate(angle)}")

    @staticmethod
    def spawnpoint(
        players: Selector, position: Vector3, angle: Union[int, float] = 0
    ) -> str:
        """
        spawnpoint - Sets the spawn point of specific players

        Args:
            players (Selector): The players to set the spawn point of
            position (Vector3): The position to set the spawn point at
            angle (Union[int, float], optional): The Y (horizontal) angle that the players will spawn at. Defaults to 0.

        Returns:
            str: Command
        """
        return Commands.push(
            f"spawnpoint {translate(players)} {translate(position)} {translate(angle)}"
        )

    @staticmethod
    def spectate(
        target: Selector, source: Selector = "@s", put_in_gamemode: bool = False
    ) -> str:
        """
        spectate - Forces an entity to spectate another

        Args:
            target (Selector): The entity which should be spectated
            source (Selector, optional): The entity that will be spectating the target. Defaults to "@s".
            put_in_gamemode (bool, optional): Whether the target should be put in spectator mode. Defaults to False.

        Returns:
            str: Command
        """
        if put_in_gamemode:
            Commands.push(f"gamemode spectator {translate(source)}")
        return Commands.push(f"spectate {translate(target)} {translate(source)}")

    @staticmethod
    def spreadplayers(
        center: Vector2,
        spread_distance: Union[int, float],
        max_range: Union[int, float],
        respect_teams: bool,
        players: Selector,
        under: Union[int, float] = None,
    ) -> str:
        """
        spreadplayers - Spreads players around a point

        Args:
            center (Vector2): The point at which players should be spread around
            spread_distance (Union[int, float]): The minimum distance between players
            max_range (Union[int, float]): The maximum distance from the center that players should be spread to. This area is a square, not a circle.
            respect_teams (bool): Whether or not teams should be kept together
            players (Selector): The players that should be spread
            under (Union[int, float], optional): The maximum height players can be spread to. If undefined, players will be put as high as possible. Defaults to None.

        Returns:
            str: Command
        """
        return Commands.push(
            f"spreadplayers {translate(center)} {translate(spread_distance)} {translate(max_range)}{' under ' + translate(str(under)) if under else ''} {translate(respect_teams, normalize_boolean=True)} {translate(players)}"
        )

    @staticmethod
    def stopsound(
        targets: Selector, channel: sound_channel = None, sound: str = None
    ) -> str:
        """
        stopsound - Stops sound(s) for players

        Args:
            targets (Selector): The players to stop the sound(s) for
            channel (sound_channel, optional): The channel to stop the sound(s) on. Defaults to None.
            sound (str, optional): The sound to stop. Defaults to None.

        Returns:
            str: Command
        """
        return Commands.push(
            f"stopsound {translate(targets)} {translate(channel)} {translate(sound)}"
        )

    @staticmethod
    def summon(type: entity, position: Vector3, nbt: Compound = None) -> str:
        """
        summon - Summons an entity

        Args:
            type (entity): The identifier of the entity to summon
            position (Vector3): The location that the entity should be summoned at
            nbt (Compound, optional): Any NBT that should be placed on the entity. Defaults to None.

        Returns:
            str: Command
        """
        return Commands.push(
            f"summon {translate(type)} {translate(position)} {translate(nbt)}"
        )

    @staticmethod
    def teammsg(text: str) -> str:
        """
        teammsg - Sends a message to the players team

        Args:
            text (str): The message to send

        Returns:
            str: Command
        """
        return Commands.push(f"teammsg {translate(text)}")

    @staticmethod
    def teleport(
        targets: Selector,
        destination: Union[Selector, Vector3],
        facing: Union[Selector, Vector3] = None,
    ) -> str:
        """
        teleport - Teleports entities to another entity or a location

        Args:
            targets (Selector): The entities to teleport
            destination (Union[Selector, Vector3]): The location or entity the targets should be teleported to
            facing (Union[Selector, Vector3], optional): The location or entity the targets should be facing. Defaults to None.

        Returns:
            str: Command
        """
        output = Commands.push(
            f"teleport {translate(targets)} {translate(destination)}"
        )
        if facing:
            output += " facing "
            if isinstance(facing, Selector):
                output += "entity "
            output += f"{translate(facing)}"
        return output

    @staticmethod
    def tellraw(players: Selector, text: TextComponent) -> str:
        """
        tellraw - Prints a text component

        Args:
            players (Selector): The players the text should be sent to
            text (TextComponent): The text to print

        Returns:
            str: Command
        """
        return Commands.push(f"tellraw {translate(players)} {translate(text)}")

    @staticmethod
    def weather(weather_type: weather_type, duration: int = None) -> str:
        """
        weather - Modifies the weather

        Args:
            weather_type (weather_type): The weather that should be set
            duration (int, optional): How long the weather should last. Defaults to None.

        Returns:
            str: Command
        """
        return Commands.push(
            f"weather {translate(weather_type)}{' ' + translate(str(duration)) if duration else ''}"
        )
