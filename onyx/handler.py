import os
import traceback
import pkg_resources
import random
import shutil
import json
import enum
from .enums import lib


class _buildable:
    pass


class _position:
    pass


class Handler:
    _added_scoreboards = []
    _init_cmds = []
    _loaded_libs = []

    def __init__(self, function, mcfunction_path, datapack_path, datapack_name):
        Handler._active_func = function
        Handler._active_mcfunc_path = mcfunction_path
        Handler._cmds = []
        Handler._datapack_path = datapack_path
        Handler._datapack_name = datapack_name

    @staticmethod
    def _write_function():
        with open(Handler._active_func, "a") as _function:
            _function.write('\n'.join(Handler._cmds))

    # Print a warning in the terminal
    @staticmethod
    def _warn(text):
        # Gets the following info:
        # File "my:/file/path", line 87, in function_name
        #   function_call()
        traceback_loc = ''.join(traceback.format_list(traceback.extract_stack(limit=3)[:-2]))

        print(f"Warning: {text}")
        # Remove the last newline, then print the location and the warning text
        print(traceback_loc[:len(traceback_loc) - 1])

    # Method is to make it more clear that it is for status messages
    @staticmethod
    def _status(text, end="\n"):
        print(f"{text}", end=end)

    # Used internally for presets
    @staticmethod
    def load_lib(lib_name):
        lib_files = []

        # Get the lib directory
        lib_dir = os.path.normpath(pkg_resources.resource_filename("onyx", "lib/"))
        # Remove the unnessecary "onyx" that appears due to the above function call
        lib_dir = lib_dir.split(os.sep)
        lib_dir.reverse()
        lib_dir.remove("onyx")
        lib_dir.reverse()
        lib_dir = os.sep.join(lib_dir)

        # Copy the lib from the onyx library to the datapack
        try:
            shutil.copytree(
                # src
                os.path.normpath(os.path.join(lib_dir, Handler._translate(lib_name))),
                # dst
                os.path.join(Handler._datapack_path, "data", Handler._datapack_name, "functions", "lib", Handler._translate(lib_name))
            )

            # Get a list of files in the library folder
            for root, dirnames, files in os.walk(os.path.join(Handler._datapack_path, "data", Handler._datapack_name, "functions", "lib", Handler._translate(lib_name))):
                for _file in files:
                    lib_files.append(root + os.sep + _file)
            os.chdir(os.path.join(Handler._datapack_path, "data", Handler._datapack_name, "functions", "lib", Handler._translate(lib_name)))

            for lib_file in lib_files:
                # Change the .onyxlib extension to .mcfunction
                lib_base_name = os.path.splitext(lib_file)[0]
                lib_mcfunction = lib_base_name + ".mcfunction"
                os.rename(lib_file, lib_mcfunction)

                # Replace the nessecary tags
                with open(lib_mcfunction, "r") as _file:
                    old_contents = _file.readlines()

                contents = []
                for line in old_contents:
                    line = line.replace(":datapack_name:", Handler._datapack_name)
                    line = line.replace(":random_num1:", str(random.randint(-2147483648, 2147483647)))
                    line = line.replace(":random_num2:", str(random.randint(-2147483648, 2147483647)))
                    line = line.replace(":random_num3:", str(random.randint(-2147483648, 2147483647)))
                    line = line.replace(":random_num4:", str(random.randint(-2147483648, 2147483647)))
                    contents.append(line)

                with open(lib_mcfunction, "w") as _file:
                    _file.write(''.join(contents))

        # The library file already exists
        except FileExistsError:
            return False

        if Handler._translate(lib_name) == "rng":
            Handler._add_scoreboard("onyx.rng")
            Handler._add_scoreboard("onyx.const")
            Handler._add_to_init([
                "scoreboard players set $2 onyx.const 2",
                "scoreboard players set #multiplier onyx.rng 1103515245",
                "scoreboard players set #discard onyx.rng 16",
                f"execute unless score #seed onyx.rng matches -2147483648.. run scoreboard players set #seed onyx.rng {str(random.randint(-2147483648, 2147483647))}"
            ])

        elif Handler._translate(lib_name) == "math":
            Handler._add_scoreboard("onyx.math")
            Handler._add_to_init([
                "scoreboard players set $2 onyx.const 2",
                "scoreboard players set #scale_factor onyx.math 100"
            ])

        elif Handler._translate(lib_name) == "calc_xp_points":
            Handler._add_scoreboard("onyx.xp_points")
            Handler._add_to_init([
                "scoreboard players set $6 onyx.const 6",
                "scoreboard players set $10 onyx.const 10",
                "scoreboard players set $25 onyx.const 25",
                "scoreboard players set $45 onyx.const 45"
                "scoreboard players set $360 onyx.const 360",
                "scoreboard players set $405 onyx.const 405",
                "scoreboard players set $1625 onyx.const 1625",
                "scoreboard players set $2200 onyx.const 2200"
            ])

        elif Handler._translate(lib_name) == "bitwise":
            Handler.load_lib(lib.math)
            Handler._add_scoreboard("onyx.const")
            Handler._add_scoreboard("onyx.bitwise")
            Handler._add_to_init([
                "scoreboard players set $2 onyx.const 2",
                "scoreboard players set $-1 onyx.const -1"
            ])

        Handler._loaded_libs.append(Handler._translate(lib_name))
        return True

    @staticmethod
    def _add_to_init(cmd):
        # Make the load.json directory if it doesn't exist
        load_dir = os.path.join(Handler._datapack_path, "data", "minecraft", "tags", "functions")
        os.makedirs(load_dir, exist_ok=True)

        # Create the file which runs init.mcfunction
        with open(os.path.join(load_dir, "load.json"), "w") as load_json:
            json.dump({"values": [f"{Handler._datapack_name}:init"]}, load_json, indent=4)

        # Adds to init.mcfunction
        if cmd not in Handler._init_cmds:
            with open(os.path.join(Handler._datapack_path, "data", Handler._datapack_name, "functions", "init.mcfunction"), "a") as init:
                if isinstance(cmd, list):
                    init.write('\n'.join(cmd) + "\n")
                elif isinstance(cmd, str):
                    init.write(cmd + "\n")
            Handler._init_cmds.extend(cmd)

    @staticmethod
    def _add_scoreboard(name, critera="dummy"):
        if name not in Handler._added_scoreboards:
            Handler._add_to_init(f"scoreboard objectives add {name} {critera} {json.dumps({'text': name})}")
            Handler._added_scoreboards.append(name)

    @staticmethod
    def _translate(element, convert=False, selector=False):
        from .json_string import json_string
        from .execute import execute
        from .selector import selector
        from .util import _buildable

        if isinstance(element, enum.Enum):
            return element.value
        elif isinstance(element, _buildable):
            return element.build()
        elif convert:
            if isinstance(element, json_string):
                return json.dumps(element.output)
            else:
                return json.dumps(["", {"text": element}])
        elif isinstance(element, (execute, json_string)):
            return element.output
        elif isinstance(element, bool):
            return str(element).lower()
        elif isinstance(element, (list, tuple)):
            if selector:
                r = []
                for q in element:
                    r.append(Handler._translate(q))
                return r
            else:
                return " ".join(element)
        else:
            return element

    @staticmethod
    def _get_differentiator():
        # Find the number to put at the end of the mcfunction name by looping through all numbers and checking if it exists
        for differentiator in range(1, 32768):
            functionless_path = os.path.dirname(Handler._active_func)
            function_name = os.path.basename(os.path.normpath(Handler._active_func))
            function_name_extensionless = os.path.splitext(function_name)[0]

            if os.path.isfile(os.path.join(functionless_path, "generated", f"{function_name_extensionless}{differentiator}.mcfunction").replace("\\.\\", "\\")):
                continue
            # The loop will only exit if it finds a differentiator that isn't in use
            else:
                return str(differentiator)
