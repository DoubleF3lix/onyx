import os
import time
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
