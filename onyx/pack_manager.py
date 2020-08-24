import os
import json
import shutil
import platform
from .handler import Handler


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
                current_data["values"].append(f"{datapack_name}:{self._mcfunction_path}")
                json.dump(current_data, tick_json, indent=4)

            Handler._status(f"Added function to tick.json: {datapack_name}:{self._mcfunction_path}")

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
    """
    def __init__(self, path: str, override=True):
        self._datapack_path = os.path.normpath(path)
        self._datapack_name = os.path.basename(os.path.normpath(self._datapack_path)).lower().replace(" ", "_")

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

            print(f"Removed old datapack: {self._datapack_name}")
        print(f"Created new datapack: {self._datapack_name}")

    def function(self, function_path: str, function_name: str, loop=False):
        """Defines a new function

        Args:
            function_path (str): The path of the function relative to the datapack ``functions`` folder
            function_name (str): The name of the function
            loop (bool, optional): Whether or not the function should be added to tick.json. Defaults to False.
        """
        return Function(self._datapack_path, self._datapack_name, function_path, function_name, loop)
