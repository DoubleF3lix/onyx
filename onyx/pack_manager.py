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
            "description": description,
            "format": version
        }

        self.pack_object = beet.DataPack(self.pack_data["name"])
        self.pack_object.pack_format = self.pack_data["format"]
        self.pack_object.description = self.pack_data["description"]

        # Initalize the commands static class
        Commands()
    
    def function(self, function_path: str, link: Callable):
        return Function(function_path, link, self)

    def generate(self, overwrite: bool = True, zipped: bool = False):
        # Determine the data pack output path
        if self.pack_data["path"] == None:
            pack_output_path = os.path.join(os.getcwd())
        else:
            pack_output_path = os.path.join(self.pack_data["path"])

        # Create the data pack
        output_path = self.pack_object.save(directory=pack_output_path, overwrite=overwrite, zipped=zipped)
        print(f"Data pack {self.pack_data['name']} generated in '{output_path}'")


class Function:
    def __init__(self, function_path: str, link: Callable, parent_pack: DataPack):
        self.function_path = function_path
        self.link = link

        self.function_object = beet.Function([])

        # link() just contains function calls which add to Commands.function_contents. 
        # The current function object gets these commands added to it.
        # Then, the function is generated and Commands.function_contents is cleared to prepare for the next function. 
        self.link()
        self.add(Commands.function_contents)
        Commands.function_contents = []

        if ":" not in function_path:
            function_path = f"{snakify(parent_pack.pack_data['name'])}:{function_path}"
        parent_pack.pack_object[function_path] = self.function_object

    def add(self, commands: list):
        self.function_object.lines.extend(commands)
