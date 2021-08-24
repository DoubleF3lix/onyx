import os
import beet
from typing import Callable
from onyx.dev_util import snakify
from onyx.commands import Commands


class DataPack:
    def __init__(self, name: str, path: str = None, description: str = None, version: int = 7):
        self.pack_data = {
            "name": name,
            "path": path,
            "description": description or 'Data Pack',
            "format": version
        }

        self.pack_object = beet.DataPack(self.pack_data["name"])
        self.pack_object.pack_format = self.pack_data["format"]
        self.pack_object.description = self.pack_data["description"]
        self.init_contents = []

        # Initalize the commands static class
        Commands(self)
    
    def function(self, function_path: str, link: Callable, init: bool = False, loop: bool = False):
        return Function(function_path, link, init, loop, self)

    def generate(self, overwrite: bool = True, zipped: bool = False):
        # Generate the initialization function file (make sure it has any commands in it, otherwise don't bother)
        if self.init_contents:
            self.pack_object[f"{snakify(self.pack_data['name'])}:_init"] = beet.Function(self.init_contents, tags=["minecraft:load"])

        # Determine the data pack output path
        if self.pack_data["path"] is None:
            pack_output_path = os.path.join(os.getcwd())
        else:
            pack_output_path = os.path.join(self.pack_data["path"])

        # Create the data pack
        output_path = self.pack_object.save(directory=pack_output_path, overwrite=overwrite, zipped=zipped)
        print(f"Data pack {self.pack_data['name']} generated in '{output_path}'")


class Function:
    def __init__(self, function_path: str, link: Callable, is_init: bool, is_loop: bool, parent_pack: DataPack):
        self.function_path = function_path
        self.link = link
        self.is_init = is_init
        self.is_loop = is_loop

        tags = []
        if self.is_init:
            tags.append("minecraft:load")
        if self.is_loop:
            tags.append("minecraft:tick")

        self.function_object = beet.Function([], tags=tags)

        # Mark the active function for things like execute
        Commands.active_function = self.function_path
        # link() just contains function calls which add to Commands.function_contents.
        self.link()
        # The current function object gets these commands added to it
        self.add(Commands.function_contents)
        # Then, variables are reset to prepare for the next function
        Commands.function_contents = []
        Commands.active_function = None

        if ":" not in function_path:
            function_path = f"{snakify(parent_pack.pack_data['name'])}:{function_path}"
        parent_pack.pack_object[function_path] = self.function_object

    def add(self, commands: list):
        self.function_object.lines.extend(commands)
