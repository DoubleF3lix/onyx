import os
import time
<<<<<<< Updated upstream
import json
import shutil
from typing import Union
from .handler import Handler
from .enums import tag_type


class function:
    """Defines a standalone function without a data pack (libs and things will NOT work)

    Args:
        path (str): The path of the function (raw path, include extension)
    """
    def __init__(self, path):
        self._path = path
        Handler(None, None, None, None)

    def __enter__(self):
        return self

    def __exit__(self, excpt_type, excpt_value, traceback):
        with open(self._path, "w") as _file:
            _file.write('\n'.join(Handler._cmds) + "\n")
=======
from typing import Callable

import beet

import onyx.storage
from onyx.class_types import Stringable
from onyx.commands import Commands
from onyx.dev_util import snakify


class DataPack(Stringable):
    """
    DataPack - Class for creating data packs

    Args:
        name (str): The name of the data pack
        path (str, optional): The output path of the data pack. Defaults to None.
        description (str, optional): The description in ``pack.mcmeta``. Defaults to None.
        version (int, optional): The pack format version. Defaults to 7.
    """

    def __init__(
        self, name: str, path: str = None, description: str = None, version: int = 7
    ) -> None:
        self.pack_data = {
            "name": name,
            "path": path,
            "description": description or "Data Pack",
            "format": version,
        }

        self.pack_object = beet.DataPack(self.pack_data["name"])
        self.pack_object.pack_format = self.pack_data["format"]
        self.pack_object.description = self.pack_data["description"]
        self.init_contents = []

        onyx.storage.cpo = self

        self.gen_time_start = time.time()

    def advancement(self, path: str, contents: dict) -> "Advancement":
        """
        advancement - Creates an advancement

        Args:
            path (str): The path of the advancement. Given as ``namespace:path/to/file``, or ``path/to/file``. If no namespace is specified, then the snake case format of the data pack name will be used.
            contents (dict): The contents of the advancement

        Returns:
            Advancement: An advancement object
        """
        return Advancement(path, contents, self)

    def function(
        self, path: str, link: Callable, init: bool = False, loop: bool = False
    ) -> "Function":
        """
        function - Creates a function

        Args:
            path (str): The path of the function. Given as ``namespace:path/to/file``, or ``path/to/file``. If no namespace is specified, then the snake case format of the data pack name will be used.
            contents (dict): The contents of the function

        Returns:
            Function: A function object
        """
        return Function(path, link, init, loop, self)

    def item_modifier(self, path: str, contents: dict) -> "ItemModifier":
        """
        item_modifier - Creates an item modifier

        Args:
            path (str): The path of the item modifier. Given as ``namespace:path/to/file``, or ``path/to/file``. If no namespace is specified, then the snake case format of the data pack name will be used.
            contents (dict): The contents of the item modifier

        Returns:
            ItemModifier: An item modifier object
        """
        return ItemModifier(path, contents, self)

    def loot_table(self, path: str, contents: dict) -> "LootTable":
        """
        loot_table - Creates a loot table

        Args:
            path (str): The path of the loot table. Given as ``namespace:path/to/file``, or ``path/to/file``. If no namespace is specified, then the snake case format of the data pack name will be used.
            contents (dict): The contents of the loot table

        Returns:
            LootTable: A loot table object
        """
        return LootTable(path, contents, self)

    def predicate(self, path: str, contents: dict) -> "Predicate":
        """
        predicate - Creates a predicate

        Args:
            path (str): The path of the predicate. Given as ``namespace:path/to/file``, or ``path/to/file``. If no namespace is specified, then the snake case format of the data pack name will be used.
            contents (dict): The contents of the predicate

        Returns:
            Predicate: A predicate object
        """
        return Predicate(path, contents, self)

    def recipe(self, path: str, contents: dict) -> "Recipe":
        """
        recipe - Creates a recipe

        Args:
            path (str): The path of the recipe. Given as ``namespace:path/to/file``, or ``path/to/file``. If no namespace is specified, then the snake case format of the data pack name will be used.
            contents (dict): The contents of the recipe

        Returns:
            Recipe: A recipe object
        """
        return Recipe(path, contents, self)

    def structure(self, path: str, file_path: str) -> "Structure":
        """
        structure - Creates a structure

        Args:
            path (str): The path of the structure. Given as ``namespace:path/to/file``, or ``path/to/file``. If no namespace is specified, then the snake case format of the data pack name will be used.
            file_path (str): The full file path to the structure file (``.nbt`` file)

        Returns:
            Structure: A structure object
        """
        return Structure(path, file_path, self)

    def block_tag(self, path: str, contents: dict) -> "BlockTag":
        """
        block_tag - Creates a block tag

        Args:
            path (str): The path of the block tag. Given as ``namespace:path/to/file``, or ``path/to/file``. If no namespace is specified, then the snake case format of the data pack name will be used.
            contents (dict): The contents of the block tag

        Returns:
            BlockTag: A block tag object
        """
        return BlockTag(path, contents, self)

    def entity_tag(self, path: str, contents: dict) -> "EntityTag":
        """
        entity_tag - Creates an entity tag

        Args:
            path (str): The path of the entity tag. Given as ``namespace:path/to/file``, or ``path/to/file``. If no namespace is specified, then the snake case format of the data pack name will be used.
            contents (dict): The contents of the entity tag

        Returns:
            EntityTag: An entity tag object
        """
        return EntityTag(path, contents, self)

    def fluid_tag(self, path: str, contents: dict) -> "FluidTag":
        """
        fluid_tag - Creates a fluid tag

        Args:
            path (str): The path of the fluid tag. Given as ``namespace:path/to/file``, or ``path/to/file``. If no namespace is specified, then the snake case format of the data pack name will be used.
            contents (dict): The contents of the fluid tag

        Returns:
            FluidTag: A fluid tag object
        """
        return FluidTag(path, contents, self)

    def function_tag(self, path: str, contents: dict) -> "FunctionTag":
        """
        function_tag - Creates a function tag

        Args:
            path (str): The path of the function tag. Given as ``namespace:path/to/file``, or ``path/to/file``. If no namespace is specified, then the snake case format of the data pack name will be used.
            contents (dict): The contents of the function tag

        Returns:
            FunctionTag: A function tag object
        """
        return FunctionTag(path, contents, self)

    def game_event_tag(self, path: str, contents: dict) -> "GameEventTag":
        """
        game_event_tag - Creates a game event tag

        Args:
            path (str): The path of the game event tag. Given as ``namespace:path/to/file``, or ``path/to/file``. If no namespace is specified, then the snake case format of the data pack name will be used.
            contents (dict): The contents of the game event tag

        Returns:
            GameEventTag: A game event tag object
        """
        return GameEventTag(path, contents, self)

    def item_tag(self, path: str, contents: dict) -> "ItemTag":
        """
        item_tag - Creates an item tag

        Args:
            path (str): The path of the item tag. Given as ``namespace:path/to/file``, or ``path/to/file``. If no namespace is specified, then the snake case format of the data pack name will be used.
            contents (dict): The contents of the item tag

        Returns:
            ItemTag: An item tag object
        """
        return ItemTag(path, contents, self)

    def dimension(self, path: str, contents: dict) -> "Dimension":
        """
        dimension - Creates a dimension

        Args:
            path (str): The path of the dimension. Given as ``namespace:path/to/file``, or ``path/to/file``. If no namespace is specified, then the snake case format of the data pack name will be used.
            contents (dict): The contents of the dimension

        Returns:
            Dimension: A dimension object
        """
        return Dimension(path, contents, self)

    def dimension_type(self, path: str, contents: dict) -> "DimensionType":
        """
        dimension_type - Creates a dimension type

        Args:
            path (str): The path of the dimension type. Given as ``namespace:path/to/file``, or ``path/to/file``. If no namespace is specified, then the snake case format of the data pack name will be used.
            contents (dict): The contents of the dimension type

        Returns:
            DimensionType: A dimension type object
        """
        return DimensionType(path, contents, self)

    def worldgen_biome(self, path: str, contents: dict) -> "Worldgen_Biome":
        """
        worldgen_biome - Creates a worldgen biome

        Args:
            path (str): The path of the worldgen biome. Given as ``namespace:path/to/file``, or ``path/to/file``. If no namespace is specified, then the snake case format of the data pack name will be used.
            contents (dict): The contents of the worldgen biome

        Returns:
            Worldgen_Biome: A worldgen biome object
        """
        return Worldgen_Biome(path, contents, self)

    def worldgen_configuredcarver(
        self, path: str, contents: dict
    ) -> "Worldgen_ConfiguredCarver":
        """
        worldgen_configuredcarver - Creates a worldgen configured carver

        Args:
            path (str): The path of the worldgen configured carver. Given as ``namespace:path/to/file``, or ``path/to/file``. If no namespace is specified, then the snake case format of the data pack name will be used.
            contents (dict): The contents of the worldgen configured carver

        Returns:
            Worldgen_ConfiguredCarver: A worldgen configured carver object
        """
        return Worldgen_ConfiguredCarver(path, contents, self)

    def worldgen_configured_feature(
        self, path: str, contents: dict
    ) -> "Worldgen_ConfiguredFeature":
        """
        worldgen_configured_feature - Creates a worldgen configured feature

        Args:
            path (str): The path of the worldgen configured feature. Given as ``namespace:path/to/file``, or ``path/to/file``. If no namespace is specified, then the snake case format of the data pack name will be used.
            contents (dict): The contents of the worldgen configured feature

        Returns:
            Worldgen_ConfiguredFeature: A worldgen configured feature object
        """
        return Worldgen_ConfiguredFeature(path, contents, self)

    def worldgen_configured_structure_feature(
        self, path: str, contents: dict
    ) -> "Worldgen_ConfiguredStructureFeature":
        """
        worldgen_configured_structure_feature - Creates a worldgen configured structure feature

        Args:
            path (str): The path of the worldgen configured structure feature. Given as ``namespace:path/to/file``, or ``path/to/file``. If no namespace is specified, then the snake case format of the data pack name will be used.
            contents (dict): The contents of the worldgen configured structure feature

        Returns:
            Worldgen_ConfiguredStructureFeature: A worldgen configured structure feature object
        """
        return Worldgen_ConfiguredStructureFeature(path, contents, self)

    def worldgen_configured_surface_builder(
        self, path: str, contents: dict
    ) -> "Worldgen_ConfiguredSurfaceBuilder":
        """
        worldgen_configured_surface_builder - Creates a worldgen configured surface builder

        Args:
            path (str): The path of the worldgen configured surface builder. Given as ``namespace:path/to/file``, or ``path/to/file``. If no namespace is specified, then the snake case format of the data pack name will be used.
            contents (dict): The contents of the worldgen configured surface builder

        Returns:
            Worldgen_ConfiguredSurfaceBuilder: A worldgen configured surface builder object
        """
        return Worldgen_ConfiguredSurfaceBuilder(path, contents, self)

    def worldgen_noise_settings(
        self, path: str, contents: dict
    ) -> "Worldgen_NoiseSettings":
        """
        worldgen_noise_settings - Creates a worldgen noise settings

        Args:
            path (str): The path of the worldgen noise settings. Given as ``namespace:path/to/file``, or ``path/to/file``. If no namespace is specified, then the snake case format of the data pack name will be used.
            contents (dict): The contents of the worldgen noise settings

        Returns:
            Worldgen_NoiseSettings: A worldgen noise settings object
        """
        return Worldgen_NoiseSettings(path, contents, self)

    def worldgen_processor_list(
        self, path: str, contents: dict
    ) -> "Worldgen_ProcessorList":
        """
        worldgen_processor_list - Creates a worldgen processor list

        Args:
            path (str): The path of the worldgen processor list. Given as ``namespace:path/to/file``, or ``path/to/file``. If no namespace is specified, then the snake case format of the data pack name will be used.
            contents (dict): The contents of the worldgen processor list

        Returns:
            Worldgen_ProcessorList: A worldgen processor list object
        """
        return Worldgen_ProcessorList(path, contents, self)

    def worldgen_template_pool(
        self, path: str, contents: dict
    ) -> "Worldgen_TemplatePool":
        """
        worldgen_template_pool - Creates a worldgen template pool

        Args:
            path (str): The path of the worldgen template pool. Given as ``namespace:path/to/file``, or ``path/to/file``. If no namespace is specified, then the snake case format of the data pack name will be used.
            contents (dict): The contents of the worldgen template pool

        Returns:
            Worldgen_TemplatePool: A worldgen template pool object
        """
        return Worldgen_TemplatePool(path, contents, self)

    def generate(
        self,
        overwrite: bool = True,
        zipped: bool = False,
        print_generation_time: bool = False,
    ) -> None:
        """
        generate - Generates the data pack

        Args:
            overwrite (bool, optional): Whether to overwrite the data pack if it already exists. Defaults to True.
            zipped (bool, optional): Whether to generate a zipped data pack. If ``False``, a folder will be generated instead. Defaults to False.
            print_generation_time (bool): Whether or not the generation time should be printed to the console. Defaults to False.
        """
        # Generate the initialization function file (make sure it has any commands in it, otherwise don't bother)
        if self.init_contents:
            self.pack_object[
                f"{snakify(self.pack_data['name'])}:_init"
            ] = beet.Function(self.init_contents, tags=["minecraft:load"])

        # Determine the data pack output path
        if self.pack_data["path"] is None:
            pack_output_path = os.path.join(os.getcwd())
        else:
            pack_output_path = os.path.join(self.pack_data["path"])

        # Create the data pack
        output_path = self.pack_object.save(
            directory=pack_output_path, overwrite=overwrite, zipped=zipped
        )
        print(f"Data pack {self.pack_data['name']} generated in '{output_path}'")
        if print_generation_time:
            print(
                f"Generation Time: {round(time.time() - self.gen_time_start, 4)} seconds"
            )

    def __str__(self) -> str:
        """
        __str__ - Returns the name of the data pack

        Returns:
            str: The data pack name
        """
        return snakify(self.pack_data["name"])


class PackResource(Stringable):
    """
    PackResource - Template class for all data pack objects

    Args:
        path (str): The path of the resource. Given as ``namespace:path/to/file``, or ``path/to/file``. If no namespace is specified, then the snake case format of the data pack name will be used.
        parent_pack (DataPack): The data pack which the resource belongs to
        beet_obj (beet.NamespaceFile): A beet object coresponding to the pack resource
    """

    def __init__(
        self, path: str, parent_pack: DataPack, beet_obj: beet.NamespaceFile
    ) -> None:
        self.path = path
        if ":" not in self.path:
            self.path = f"{snakify(parent_pack.pack_data['name'])}:{path}"
        self.parent_pack = parent_pack
        self.beet_obj = beet_obj

        parent_pack.pack_object[path] = self.beet_obj

    def __str__(self) -> str:
        """
        __str__ - Returns the path of the resource

        Returns:
            str: The resource path
        """
        return self.path


class Advancement(PackResource):
    """
    Advancement - A data pack advancement. Do not create manually. Instead, use the ``DataPack.advancement`` method.

    Args:
        path (str): The path of the advancement. Given as ``namespace:path/to/file``, or ``path/to/file``. If no namespace is specified, then the snake case format of the data pack name will be used.
        contents (dict): The contents of the advancement
        parent_pack (DataPack): The data pack which the advancement belongs to
    """
>>>>>>> Stashed changes

    def __init__(self, path: str, contents: dict, parent_pack: DataPack) -> None:
        super().__init__(path, parent_pack, beet.Advancement(contents))

<<<<<<< Updated upstream
class Function:
    def __init__(self, datapack_path, datapack_name, function_path, function_name, loop):
        self._datapack_path = datapack_path
        self._datapack_name = datapack_name

        # Define the function path and create it if it doesn't exist
        self._function_path = os.path.join(datapack_path, "data", datapack_name, "functions", os.path.normpath(function_path))
        os.makedirs(self._function_path, exist_ok=True)

        # Store the function path that is used by the game (pack_name:function/path/here)
        q = self._function_path.split(os.sep)
        q = q[q.index('functions') + 1:]
        if q[0] == ".":
            self._mcfunction_path = f"{self._datapack_name}:{function_name}"
        else:
            self._mcfunction_path = f"{self._datapack_name}:{f'/'.join(q)}/{function_name}"

        # The file name itself is added after the directory is created to avoid a folder called "xyz.mcfunction" being created
        self._function_path = os.path.join(self._function_path, function_name + ".mcfunction")

        # Initalize the Handler
        Handler(self._function_path, self._mcfunction_path, self._datapack_path, self._datapack_name)

        if loop:
            # Make the tick.json directory if it doesn't exist
            tick_dir = os.path.join(datapack_path, "data", "minecraft", "tags", "functions")
            os.makedirs(tick_dir, exist_ok=True)

            # Get the tick.json contents and set default values if they don't exist
            try:
                with open(os.path.join(tick_dir, "tick.json"), "r") as tick_json:
                    current_data = json.load(tick_json)
            except FileNotFoundError:
                current_data = {"values": []}

            # Update (or create) the file
            with open(os.path.join(tick_dir, "tick.json"), "w") as tick_json:
                # Get the function path, split it, and then keep only everything past /data/namespace/functions/

                # Add the data to the list and dump it
                current_data["values"].append(f"{self._mcfunction_path}")
                json.dump(current_data, tick_json, indent=4)

            Handler._status(f"Added function to tick.json: {self._mcfunction_path}")

    def __enter__(self):
        Handler._active_func = self._function_path
        return self

    def __exit__(self, excpt_type, excpt_value, traceback):
        Handler._write_function()


class pack:
    """Defines a new datapack

    Args:
        path (str): The path of the new datapack
        override (bool, optional): Whether or not the old datapack should be deleted. Defaults to True.
        disable_status_messages (bool, optional): Whether or not status messages should be displayed. Defaults to False.
    """
    def __init__(self, path: str, override: bool = True, disable_status_messages: bool = False):
        self._start_time = time.time()
        self._datapack_path = os.path.normpath(path)
        self._datapack_name = os.path.basename(os.path.normpath(self._datapack_path)).lower().replace(" ", "_")
        Handler._disable_status = disable_status_messages

        if override:
            shutil.rmtree(self._datapack_path, ignore_errors=True)
            # Generate file structure
            path = os.path.join(self._datapack_path, "data", self._datapack_name, "functions")
            os.makedirs(path, exist_ok=True)

            # Generate pack.mcmeta
            with open(os.path.join(self._datapack_path, "pack.mcmeta"), "w+") as mc_meta_file:
                mc_meta_data = {
                    "pack": {
                        "pack_format": 5,
                        "description": f"{self._datapack_name}"
                    }
                }
                json.dump(mc_meta_data, mc_meta_file, indent=4)

        with open(os.path.join(self._datapack_path, "SIGNATURE"), "wb") as _file:
            _file.write(bytearray(b'\x02\x06\x00\x02\x01\t\x07\x04\x02\x08\x08\x02\x05\x05\x00\x01\x00\x01\x06\x00\x03\x06\x03\x03\x01\x04\x05\x07\x06\x00\x03\x08\x04\x03\x03\x01\x01\x04\x01\x07\x05\x03\x01\x03\x08\x00\x04\x08\t\x01\x04\x06\x01\x00\x02\x05\t\x04\x07\x06\t\t\x07\x05\x05\x01\x04\x06\t\x07\x03\x07\x08\x01\x05\x03\x00\x02\x03\x04\x03\x01\x08\x07\x03\x07\x05\x05\x00\x01\x02\t\x05\x08\x04\t\x01\x02\x05\x03\x03\x07\x01\x01\x01\t\x07\x06\x07\x03\x00\x08\x05\x08\x03\t\x01\x06\x08\x07\x02\x07\x08\x05\x01\x03\x05\x08\x06\x03\x08\x04\x07\x00\x03\x04\x04\x02\t\x06\x07\x00\x05\x08\x07\x06\x00\x03\x06\t\x01\x01\x04\x01\x05\x03\x08\x07\x07\t\t\x01\x07\x08\x01\x02\x00\t\t\x02\x05\x08\t\x05\x06\x00\x06\t\x02\x07\x03\x04\x07\x06\x05\x03\x01\x05\x01\x08\x07\x07\x03\x01\x02\t\x02\x06\x06\x08\x08\t\x05\t\x01\x07\x07\x08\x00\x04\t\x00\x06\x06\x04\x02\x07\x05\t\x07\x01\x03\x06\x07\x06\x05\x02\x06\x04\t\x02\x04\x04\x00\x07\x03\t\x00\x03\x03\x07\x03\x07\x03\x07\x06\t\x00\t\x02\x08\x01\x02\t\x03\x08\x04\t\x07\x02\x05\t\t\x04\x00\x03\x03\t\x05\t\x00\x08\x00\x01\x04\x06\x08\t\x05\x05\x04\t\x06\x04\x02\x05\x03\x04\x03\x03\x03\x04\x02\x08\x01\x01\x06\x01\x04\x05\x03\x08\x07\t\t\x04\x04\x01\x04\x04\x01\t\x01\x07\x06\x05\x00\x00'))

            Handler._status(f"Removed old datapack: {self._datapack_name}")
        Handler._status(f"Created new datapack: {self._datapack_name}")

    def get_generation_time(self, decimal_places: int = 3):
        """Prints the time it took to generate the datapack

        Args:
            decimal_places (int, optional): The amount of decimal places the result should be rounded to. Defaults to 3.
        """
        Handler._status(f"Datapack '{self._datapack_name}' took {round(time.time() - self._start_time, decimal_places)} seconds to generate")

    def function(self, function_path: str, function_name: str, loop=False):
        """Defines a new function

        Args:
            function_path (str): The path of the function relative to the datapack ``functions`` folder
            function_name (str): The name of the function
            loop (bool, optional): Whether or not the function should be added to tick.json. Defaults to False.
        """
        return Function(self._datapack_path, self._datapack_name, function_path, function_name, loop)

    def _multi_data(self, data_type, path, name, data, overwrite=False):
        if overwrite:
            namespace = "minecraft"
        else:
            namespace = self._datapack_name

        fileless_path = os.path.join(self._datapack_path, "data", namespace, data_type, os.path.normpath(path))
        os.makedirs(fileless_path, exist_ok=True)

        # Get the path that the game uses for this data type
        q = fileless_path.split(os.sep)
        q = q[q.index(data_type) + 1:]
        if q[0] == ".":
            mc_path = f"{self._datapack_name}:{name}"
        else:
            mc_path = f"{self._datapack_name}:{f'/'.join(q)}/{name}"

        data_path = os.path.join(fileless_path, name + ".json")
        with open(data_path, "w") as _file:
            json.dump(data, _file, indent=4)

        Handler._status(f"Created {data_type[:-1]}: {mc_path}")

        return mc_path

    def add_advancement(self, path: str, name: str, data: dict, overwrite: bool = False):
        """Adds an advancement to the datapack from raw JSON data

        Args:
            path (str): The location of the advancement relative to ``namespace/advancements``. Specify the advancement name in the ``name`` parameter.
            name (str): The name of the advancement
            data (dict): The JSON data of the advancement
            overwrite (bool, optional): Whether or not the advancement should be put in the ``minecraft`` namespace. Defaults to False.

        Returns:
            str: The path of the advancement that minecraft uses (``namespace:pa/th/name``)
        """
        return self._multi_data("advancement", path, name, data)

    def add_loot_table(self, path: str, name: str, data: dict, overwrite: bool = False):
        """Adds a loot table to the datapack from raw JSON data

        Args:
            path (str): The location of the loot table relative to ``namespace/loot_tables``. Specify the loot table name in the ``name`` parameter.
            name (str): The name of the loot table
            data (dict): The JSON data of the loot table
            overwrite (bool, optional): Whether or not the loot table should be put in the ``minecraft`` namespace. Defaults to False.

        Returns:
            str: The path of the loot table that minecraft uses (``namespace:pa/th/name``)
        """
        return self._multi_data("loot_tables", path, name, data)

    def add_predicate(self, path: str, name: str, data: dict, overwrite: bool = False):
        """Adds a predicate to the datapack from raw JSON data

        Args:
            path (str): The location of the predicate relative to ``namespace/predicates``. Specify the predicate name in the ``name`` parameter.
            name (str): The name of the predicate
            data (dict): The JSON data of the predicate
            overwrite (bool, optional): Whether or not the predicate should be put in the ``minecraft`` namespace. Defaults to False.

        Returns:
            str: The path of the predicate that minecraft uses (``namespace:pa/th/name``)
        """
        return self._multi_data("predicates", path, name, data)

    def add_recipe(self, path: str, name: str, data: dict, overwrite: bool = False):
        """Adds a recipe to the datapack from raw JSON data

        Args:
            path (str): The location of the recipe relative to ``namespace/recipes``. Specify the recipe name in the ``name`` parameter.
            name (str): The name of the recipe
            data (dict): The JSON data of the recipe
            overwrite (bool, optional): Whether or not the recipe should be put in the ``minecraft`` namespace. Defaults to False.

        Returns:
            str: The path of the recipe that minecraft uses (``namespace:pa/th/name``)
        """
        return self._multi_data("recipes", path, name, data)

    def load_structure(self, path: str, name: str, location: str, overwrite: bool = False):
        """Copies a structure into the datapack

        Args:
            path (str): The location of the structure relative to ``namespace/structures``. Specify the structure name in the ``name`` parameter.
            name (str): The name of the structure
            location (str): The file path of the structure to load
            overwrite (bool, optional): Whether or not the structure should be loaded into the ``minecraft`` namespace. Defaults to False.
        """
        if not location.endswith(".nbt"):
            location += ".nbt"

        if overwrite:
            namespace = "minecraft"
        else:
            namespace = self._datapack_name

        fileless_path = os.path.join(self._datapack_path, "data", namespace, "structures", os.path.normpath(path))
        os.makedirs(fileless_path, exist_ok=True)

        shutil.copyfile(location, os.path.join(fileless_path, name + ".nbt"))

    def add_tag(self, type: tag_type, path, name, data: Union[dict, list], overwrite: bool = False):
        """Adds a tag to the datapack from raw JSON data or a list of elements

        Args:
            type (tag_type): The type of the tag (block, entity, fluid, function, item)
            path (str): The location of the tag relative to ``namespace/tags``. Specify the tag name in the ``name`` parameter.
            name (str): The name of the tag
            data (Union[dict, list]): The data of the tag. If ``data`` is a dictionary, the raw JSON data is loaded. If ``data`` is a list, the list will be set to the ``values`` element of the tag.
            overwrite (bool, optional): Whether or not the tag should be loaded into the ``minecraft`` namespace. Defaults to False.
        """
        if overwrite:
            namespace = "minecraft"
        else:
            namespace = self._datapack_name

        fileless_path = os.path.join(self._datapack_path, "data", namespace, "tags", os.path.normpath(path))
        os.makedirs(fileless_path, exist_ok=True)

        # Get the path that the game uses for this tag
        q = fileless_path.split(os.sep)
        q = q[q.index("tags") + 1:]
        if q[0] == ".":
            mc_path = f"#{namespace}:{name}"
        else:
            mc_path = f"#{namespace}:{f'/'.join(q)}/{name}"

        tag_path = os.path.join(fileless_path, name + ".json")
        if isinstance(data, dict):
            with open(tag_path, "w") as _file:
                json.dump(data, _file, indent=4)

        elif isinstance(data, list):
            q = [Handler._translate(y) for y in data]
            with open(tag_path, "w") as _file:
                json.dump({"values": q}, _file, indent=4)

        Handler._status(f"Created tag: {mc_path}")

        return mc_path
=======

class Function(PackResource):
    """
    Function - A data pack function. Do not create manually. Instead, use the ``DataPack.function`` method.

    Args:
        path (str): The path of the function. Given as ``namespace:path/to/file``, or ``path/to/file``. If no namespace is specified, then the snake case format of the data pack name will be used.
        link (Callable): The python function to link to. All of the commands for this pack function should be in this python function.
        is_init (bool): Whether or not the function should be called when the data pack loads
        is_loop (bool): Whether or not the function should be called every tick
        parent_pack (DataPack): The parent pack object
    """

    def __init__(
        self,
        path: str,
        link: Callable,
        is_init: bool,
        is_loop: bool,
        parent_pack: DataPack,
    ):
        self.path = path
        self.link = link
        self.is_init = is_init
        self.is_loop = is_loop
        self.parent_pack = parent_pack

        tags = []
        if self.is_init:
            tags.append("minecraft:load")
        if self.is_loop:
            tags.append("minecraft:tick")

        self.beet_object = beet.Function([], tags=tags)

        # Mark the active function for things like execute
        Commands.active_function = self.path
        # link() just contains function calls which add to Commands.function_contents.
        self.link()
        # The current function object gets these commands added to it
        self.add(Commands.function_contents)
        # Then, variables are reset to prepare for the next function
        Commands.function_contents = []
        Commands.active_function = None

        if ":" not in self.path:
            self.path = f"{snakify(parent_pack.pack_data['name'])}:{self.path}"
        parent_pack.pack_object[self.path] = self.beet_object

    def add(self, commands: list) -> None:
        """
        add - Adds commands to the function

        Args:
            commands (list): The commands to add
        """
        self.beet_object.lines.extend(commands)

    def __call__(self) -> str:
        """
        __call__ - Outputs the command to execute this function

        Returns:
            str: Command
        """
        return Commands.push(f"function {self.path}")

    def __str__(self) -> str:
        """
        __str__ - Returns the path of the function

        Returns:
            str: The function path
        """
        return self.path


class ItemModifier(PackResource):
    """
    ItemModifier - A data pack advancement. Do not create manually. Instead, use the ``DataPack.item_modifier`` method.

    Args:
        path (str): The path of the item modifier. Given as ``namespace:path/to/file``, or ``path/to/file``. If no namespace is specified, then the snake case format of the data pack name will be used.
        contents (dict): The contents of the item modifier
        parent_pack (DataPack): The data pack which the item modifier belongs to
    """

    def __init__(self, path, contents, parent_pack):
        super().__init__(path, parent_pack, beet.ItemModifier(contents))


class LootTable(PackResource):
    """
    LootTable - A data pack loot table. Do not create manually. Instead, use the ``DataPack.loot_table`` method.

    Args:
        path (str): The path of the loot table. Given as ``namespace:path/to/file``, or ``path/to/file``. If no namespace is specified, then the snake case format of the data pack name will be used.
        contents (dict): The contents of the loot table
        parent_pack (DataPack): The data pack which the loot table belongs to
    """

    def __init__(self, path, contents, parent_pack):
        super().__init__(path, parent_pack, beet.LootTable(contents))


class Predicate(PackResource):
    """
    Predicate - A data pack predicate. Do not create manually. Instead, use the ``DataPack.predicate`` method.

    Args:
        path (str): The path of the predicate. Given as ``namespace:path/to/file``, or ``path/to/file``. If no namespace is specified, then the snake case format of the data pack name will be used.
        contents (dict): The contents of the predicate
        parent_pack (DataPack): The data pack which the predicate belongs to
    """

    def __init__(self, path, contents, parent_pack):
        super().__init__(path, parent_pack, beet.Predicate(contents))


class Recipe(PackResource):
    """
    Recipe - A data pack recipe. Do not create manually. Instead, use the ``DataPack.recipe`` method.

    Args:
        path (str): The path of the recipe. Given as ``namespace:path/to/file``, or ``path/to/file``. If no namespace is specified, then the snake case format of the data pack name will be used.
        contents (dict): The contents of the recipe
        parent_pack (DataPack): The data pack which the recipe belongs to
    """

    def __init__(self, path, contents, parent_pack):
        super().__init__(path, parent_pack, beet.Recipe(contents))


class Structure(PackResource):
    """
    Structure - A data pack structure. Do not create manually. Instead, use the ``DataPack.structure`` method.

    Args:
        path (str): The path of the structure. Given as ``namespace:path/to/file``, or ``path/to/file``. If no namespace is specified, then the snake case format of the data pack name will be used.
        file_path (str): The full file path to the structure file (``.nbt`` file)
        parent_pack (DataPack): The data pack which the structure belongs to
    """

    def __init__(self, path, file_path, parent_pack):
        super().__init__(path, parent_pack, beet.Structure(source_type=file_path))


class BlockTag(PackResource):
    """
    BlockTag - A data pack block tag. Do not create manually. Instead, use the ``DataPack.block_tag`` method.

    Args:
        path (str): The path of the block tag. Given as ``namespace:path/to/file``, or ``path/to/file``. If no namespace is specified, then the snake case format of the data pack name will be used.
        contents (dict): The contents of the block tag
        parent_pack (DataPack): The data pack which the block tag belongs to
    """

    def __init__(self, path, contents, parent_pack):
        super().__init__(path, parent_pack, beet.BlockTag(contents))


class EntityTag(PackResource):
    """
    EntityTag - A data pack entity tag. Do not create manually. Instead, use the ``DataPack.entity_tag`` method.

    Args:
        path (str): The path of the entity tag. Given as ``namespace:path/to/file``, or ``path/to/file``. If no namespace is specified, then the snake case format of the data pack name will be used.
        contents (dict): The contents of the entity tag
        parent_pack (DataPack): The data pack which the entity tag belongs to
    """

    def __init__(self, path, contents, parent_pack):
        super().__init__(path, parent_pack, beet.EntityTypeTag(contents))


class FluidTag(PackResource):
    """
    FluidTag - A data pack fluid tag. Do not create manually. Instead, use the ``DataPack.fluid_tag`` method.

    Args:
        path (str): The path of the fluid tag. Given as ``namespace:path/to/file``, or ``path/to/file``. If no namespace is specified, then the snake case format of the data pack name will be used.
        contents (dict): The contents of the fluid tag
        parent_pack (DataPack): The data pack which the fluid tag belongs to
    """

    def __init__(self, path, contents, parent_pack):
        super().__init__(path, parent_pack, beet.FluidTag(contents))


class FunctionTag(PackResource):
    """
    FunctionTag - A data pack function tag. Do not create manually. Instead, use the ``DataPack.function_tag`` method.

    Args:
        path (str): The path of the function tag. Given as ``namespace:path/to/file``, or ``path/to/file``. If no namespace is specified, then the snake case format of the data pack name will be used.
        contents (dict): The contents of the function tag
        parent_pack (DataPack): The data pack which the function tag belongs to
    """

    def __init__(self, path, contents, parent_pack):
        super().__init__(path, parent_pack, beet.FunctionTag(contents))


class GameEventTag(PackResource):
    """
    GameEventTag - A data pack game event tag. Do not create manually. Instead, use the ``DataPack.game_event_tag`` method.

    Args:
        path (str): The path of the game event tag. Given as ``namespace:path/to/file``, or ``path/to/file``. If no namespace is specified, then the snake case format of the data pack name will be used.
        contents (dict): The contents of the game event tag
        parent_pack (DataPack): The data pack which the game event tag belongs to
    """

    def __init__(self, path, contents, parent_pack):
        super().__init__(path, parent_pack, beet.GameEventTag(contents))


class ItemTag(PackResource):
    """
    ItemTag - A data pack item tag. Do not create manually. Instead, use the ``DataPack.item_tag`` method.

    Args:
        path (str): The path of the item tag. Given as ``namespace:path/to/file``, or ``path/to/file``. If no namespace is specified, then the snake case format of the data pack name will be used.
        contents (dict): The contents of the item tag
        parent_pack (DataPack): The data pack which the item tag belongs to
    """

    def __init__(self, path, contents, parent_pack):
        super().__init__(path, parent_pack, beet.ItemTag(contents))


class Dimension(PackResource):
    """
    Dimension - A data pack dimension. Do not create manually. Instead, use the ``DataPack.dimension`` method.

    Args:
        path (str): The path of the dimension. Given as ``namespace:path/to/file``, or ``path/to/file``. If no namespace is specified, then the snake case format of the data pack name will be used.
        contents (dict): The contents of the dimension
        parent_pack (DataPack): The data pack which the dimension belongs to
    """

    def __init__(self, path, contents, parent_pack):
        super().__init__(path, parent_pack, beet.Dimension(contents))


class DimensionType(PackResource):
    """
    DimensionType - A data pack dimension type. Do not create manually. Instead, use the ``DataPack.dimension_type`` method.

    Args:
        path (str): The path of the dimension type. Given as ``namespace:path/to/file``, or ``path/to/file``. If no namespace is specified, then the snake case format of the data pack name will be used.
        contents (dict): The contents of the dimension type
        parent_pack (DataPack): The data pack which the dimension type belongs to
    """

    def __init__(self, path, contents, parent_pack):
        super().__init__(path, parent_pack, beet.DimensionType(contents))


class Worldgen_Biome(PackResource):
    """
    Worldgen_Biome - A data pack worldgen biome. Do not create manually. Instead, use the ``DataPack.worldgen_biome`` method.

    Args:
        path (str): The path of the worldgen biome. Given as ``namespace:path/to/file``, or ``path/to/file``. If no namespace is specified, then the snake case format of the data pack name will be used.
        contents (dict): The contents of the worldgen biome
        parent_pack (DataPack): The data pack which the worldgen biome belongs to
    """

    def __init__(self, path, contents, parent_pack):
        super().__init__(path, parent_pack, beet.Biome(contents))


class Worldgen_ConfiguredCarver(PackResource):
    """
    Worldgen_ConfiguredCarver - A data pack worldgen configured carver. Do not create manually. Instead, use the ``DataPack.worldgen_configured_carver`` method.

    Args:
        path (str): The path of the worldgen configured carver. Given as ``namespace:path/to/file``, or ``path/to/file``. If no namespace is specified, then the snake case format of the data pack name will be used.
        contents (dict): The contents of the worldgen configured carver
        parent_pack (DataPack): The data pack which the worldgen configured carver belongs to
    """

    def __init__(self, path, contents, parent_pack):
        super().__init__(path, parent_pack, beet.ConfiguredCarver(contents))


class Worldgen_ConfiguredFeature(PackResource):
    """
    Worldgen_ConfiguredFeature - A data pack worldgen configured feature. Do not create manually. Instead, use the ``DataPack.worldgen_configured_feature`` method.

    Args:
        path (str): The path of the worldgen configured feature. Given as ``namespace:path/to/file``, or ``path/to/file``. If no namespace is specified, then the snake case format of the data pack name will be used.
        contents (dict): The contents of the worldgen configured feature
        parent_pack (DataPack): The data pack which the worldgen configured feature belongs to
    """

    def __init__(self, path, contents, parent_pack):
        super().__init__(path, parent_pack, beet.ConfiguredFeature(contents))


class Worldgen_ConfiguredStructureFeature(PackResource):
    """
    Worldgen_ConfiguredStructureFeature - A data pack worldgen configured structure feature. Do not create manually. Instead, use the ``DataPack.worldgen_configured_structure_feature`` method.

    Args:
        path (str): The path of the worldgen configured structure feature. Given as ``namespace:path/to/file``, or ``path/to/file``. If no namespace is specified, then the snake case format of the data pack name will be used.
        contents (dict): The contents of the worldgen configured structure feature
        parent_pack (DataPack): The data pack which the worldgen configured structure feature belongs to
    """

    def __init__(self, path, contents, parent_pack):
        super().__init__(path, parent_pack, beet.ConfiguredStructureFeature(contents))


class Worldgen_ConfiguredSurfaceBuilder(PackResource):
    """
    Worldgen_ConfiguredSurfaceBuilder - A data pack worldgen configured surface builder. Do not create manually. Instead, use the ``DataPack.worldgen_configured_surface_builder`` method.

    Args:
        path (str): The path of the worldgen configured surface builder. Given as ``namespace:path/to/file``, or ``path/to/file``. If no namespace is specified, then the snake case format of the data pack name will be used.
        contents (dict): The contents of the worldgen configured surface builder
        parent_pack (DataPack): The data pack which the worldgen configured surface builder belongs to
    """

    def __init__(self, path, contents, parent_pack):
        super().__init__(path, parent_pack, beet.ConfiguredSurfaceBuilder(contents))


class Worldgen_NoiseSettings(PackResource):
    """
    Worldgen_NoiseSettings - A data pack worldgen noise settings. Do not create manually. Instead, use the ``DataPack.worldgen_noise_settings`` method.

    Args:
        path (str): The path of the worldgen noise settings. Given as ``namespace:path/to/file``, or ``path/to/file``. If no namespace is specified, then the snake case format of the data pack name will be used.
        contents (dict): The contents of the worldgen noise settings
        parent_pack (DataPack): The data pack which the worldgen noise settings belongs to
    """

    def __init__(self, path, contents, parent_pack):
        super().__init__(path, parent_pack, beet.NoiseSettings(contents))


class Worldgen_ProcessorList(PackResource):
    """
    Worldgen_ProcessorList - A data pack worldgen processor list. Do not create manually. Instead, use the ``DataPack.worldgen_processor_list`` method.

    Args:
        path (str): The path of the worldgen processor list. Given as ``namespace:path/to/file``, or ``path/to/file``. If no namespace is specified, then the snake case format of the data pack name will be used.
        contents (dict): The contents of the worldgen processor list
        parent_pack (DataPack): The data pack which the worldgen processor list belongs to
    """

    def __init__(self, path, contents, parent_pack):
        super().__init__(path, parent_pack, beet.ProcessorList(contents))


class Worldgen_TemplatePool(PackResource):
    """
    Worldgen_TemplatePool - A data pack worldgen template pool. Do not create manually. Instead, use the ``DataPack.worldgen_template_pool`` method.

    Args:
        path (str): The path of the worldgen template pool. Given as ``namespace:path/to/file``, or ``path/to/file``. If no namespace is specified, then the snake case format of the data pack name will be used.
        contents (dict): The contents of the worldgen template pool
        parent_pack (DataPack): The data pack which the worldgen template pool belongs to
    """

    def __init__(self, path, contents, parent_pack):
        super().__init__(path, parent_pack, beet.TemplatePool(contents))
>>>>>>> Stashed changes
