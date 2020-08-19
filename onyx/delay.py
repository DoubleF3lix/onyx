import os
from typing import Union
from onyx.handler import Handler


class delay:
    def __init__(self, delay_time: Union[str, int]):
        # Save the old function path
        self.old_func = Handler._active_func

        # Modify the time if there are any custom suffixes (just minutes and hours, since schedule only supports ticks, seconds, and days)
        if isinstance(delay_time, int):
            delay_time = f"{delay_time}t"
        elif delay_time[-1] == "m":
            delay_time = f"{int(delay_time[:-1]) * 60}s"
        elif delay_time[-1] == "h":
            delay_time = f"{int(delay_time[:-1]) * 3600}s"
        self.delay_time = delay_time

    def __enter__(self):
        # Call the new function and save all the old commands
        # Get the current function path without the function file itself
        functionless_path = os.path.dirname(Handler._active_func)
        if functionless_path.endswith("\\."):
            functionless_path = functionless_path[:-1]
        function_name = os.path.basename(os.path.normpath(Handler._active_func))
        function_name_extensionless = os.path.splitext(function_name)[0]
        differentiator = Handler._get_differentiator()

        Handler._cmds.append(f"schedule function {Handler._datapack_name}:generated/{function_name_extensionless}{differentiator} {self.delay_time}")
        self.old_cmds = Handler._cmds
        Handler._cmds = []

        os.makedirs(os.path.join(functionless_path, "generated"), exist_ok=True)
        Handler._active_func = os.path.join(functionless_path, "generated", function_name_extensionless + differentiator + ".mcfunction").replace("\\.\\", "\\")

    def __exit__(self, excpt_type, excpt_value, traceback):
        # Write the commands to the new file
        Handler._write_function()
        # Restore the old function settings
        Handler._active_func = self.old_func
        Handler._cmds = self.old_cmds
