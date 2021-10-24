import os
import time
import zipfile
from typing import Callable, Union

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

    def generate(
        self,
        overwrite: bool = True,
        zipped: bool = False,
        only_generate_zip_object: bool = False,
        print_output_path: bool = True,
        print_generation_time: bool = True,
    ) -> dict:
        """
        generate - Generates the data pack

        Args:
            overwrite (bool, optional): Whether to overwrite the data pack if it already exists. Defaults to True.
            zipped (bool, optional): Whether to generate a zipped data pack. If ``False``, a folder will be generated instead. Defaults to False.
            only_generate_zip_object (bool, optional): If set, only returns a ``ZipFile`` object instead of generating a file/folder. Defaults to False.
            print_output_path (bool, optional): Whether to print the output path of the data pack. Defaults to True.
            print_generation_time (bool): Whether the generation time should be printed to the console. Defaults to False.

        Returns:
            dict: A dictionary containing the output path of the data pack, the generation time, and the ``ZipFile`` object if ``only_generate_zip_object`` is ``True``.
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

        return_values = {
            "output_path": pack_output_path,
            "generation_time": time.time() - self.gen_time_start,
        }

        if not only_generate_zip_object:
            output_path = self.pack_object.save(
                directory=pack_output_path, overwrite=overwrite, zipped=zipped
            )
        else:
            with zipfile.ZipFile(snakify(self.pack_data["name"]) + ".zip", "w") as zip:
                self.pack_object.dump(zip)
                return_values["zip_object"] = zip

        if print_output_path:
            if not only_generate_zip_object:
                print(
                    f"Data pack {self.pack_data['name']} generated at '{output_path}{'.zip' if zipped else ''}'"
                )
            else:
                print("Data pack generated as ZipFile object")

        if print_generation_time:
            print(
                f"Data pack generated in {round(return_values['generation_time'], 6)} seconds"
            )

        return return_values

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
        self,
        path: str,
        link: Union[Callable, str],
        init: bool = False,
        loop: bool = False,
    ) -> "Function":
        """
        function - Creates a function. If ``link`` returns ``str``, then that string is used as the function contents instead.

        Args:
            path (str): The path of the function. Given as ``namespace:path/to/file``, or ``path/to/file``. If no namespace is specified, then the snake case format of the data pack name will be used.
            link: (Union[Callable, str]): The python function to link to. All of the commands for this pack function should be in this python function. Alternatively, this function can return a string, or ``link`` can be a string itself, and that will be used as the function contents instead.
            init (bool, optional): Whether this function should be run when the pack is loaded. Defaults to False.
            loop (bool, optional): Whether this function should be run every tick. Defaults to False.

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

    def __str__(self) -> str:
        """
        __str__ - Returns the name of the data pack

        Returns:
            str: The data pack name
        """
        return snakify(self.pack_data["name"])


class PackResource(Stringable):
    """
    PackResource - Template class for all data pack objects. To get the contents, use ``PackResource.beet_obj.content``.

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

    def __init__(self, path: str, contents: dict, parent_pack: DataPack) -> None:
        super().__init__(path, parent_pack, beet.Advancement(contents))


class Function(PackResource):
    """
    Function - A data pack function. Do not create manually. Instead, use the ``DataPack.function`` method.

    Args:
        path (str): The path of the function. Given as ``namespace:path/to/file``, or ``path/to/file``. If no namespace is specified, then the snake case format of the data pack name will be used.
        link (Union[Callable, str]): The python function to link to. All of the commands for this pack function should be in this python function. Alternatively, this function can return a string, or ``link`` can be a string itself, and that will be used as the function contents instead.
        is_init (bool): Whether or not the function should be called when the data pack loads
        is_loop (bool): Whether or not the function should be called every tick
        parent_pack (DataPack): The parent pack object
    """

    def __init__(
        self,
        path: str,
        link: Union[Callable, str],
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

        # Check if the function returned a string, and if so, use that for the function contents, otherwise assume function calls to onyx.commands were used
        if type(self.link) == str:
            function_contents = self.link
        elif callable(self.link):
            function_contents = self.link()

        if type(function_contents) is not str:
            function_contents = Commands.function_contents
        else:
            # This way it works for the add() method which uses a list
            function_contents = function_contents.split("\n")

        # Strip every command in the commands list
        function_contents = [
            element.strip().replace("\n", "") for element in function_contents
        ]

        # Check len higher than 0
        if function_contents:
            if function_contents[0] == "":
                del function_contents[0]

            if function_contents[-1] == "":
                del function_contents[-1]

        # Add the commands
        self.add(function_contents)

        # Prepare for the next function
        Commands.function_contents = []
        Commands.active_function = None

        # Send the function object to the parent pack
        if ":" not in self.path:
            self.path = f"{snakify(parent_pack.pack_data['name'])}:{self.path}"

        self.send_object_to_parent_pack()

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

    def send_object_to_parent_pack(self) -> None:
        """
        send_object_to_parent_pack - Sends the function to the parent pack. You can call this manually to force update the function if you change the contents after generation.
        """
        self.parent_pack.pack_object[self.path] = self.beet_object


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
