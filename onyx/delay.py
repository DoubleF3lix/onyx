import os
from typing import Union
from onyx.handler import Handler


class delay:
    def __init__(self, delay_time: Union[str, int]):
        # Save the old function path
        self.old_func = Handler._active_func
        self.old_mcfunc = Handler._active_mcfunc_path

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

        # Add "generated" to the mcfunction path
        Handler._active_mcfunc_path = Handler._active_mcfunc_path.split("/")
        if len(Handler._active_mcfunc_path) > 1:
            Handler._active_mcfunc_path.insert(-1, "generated")
            Handler._active_mcfunc_path[-1] = Handler._active_mcfunc_path[-1] + differentiator
        else:
            Handler._active_mcfunc_path = "".join(Handler._active_mcfunc_path).split(":")
            del Handler._active_mcfunc_path[-1]
            Handler._active_mcfunc_path[0] = Handler._active_mcfunc_path[0] + ":"
            Handler._active_mcfunc_path.append("generated")
            Handler._active_mcfunc_path.append(function_name_extensionless + differentiator)

        Handler._active_mcfunc_path = "/".join(Handler._active_mcfunc_path).replace(":/", ":")

        Handler._cmds.append(f"schedule function {Handler._active_mcfunc_path} {self.delay_time}")
        self.old_cmds = Handler._cmds
        Handler._cmds = []

        os.makedirs(os.path.join(functionless_path, "generated"), exist_ok=True)
        Handler._active_func = os.path.join(functionless_path, "generated", function_name_extensionless + differentiator + ".mcfunction").replace("\\.\\", "\\")

    def __exit__(self, excpt_type, excpt_value, traceback):
        # Write the commands to the new file
        Handler._write_function()
        # Restore the old function settings
        Handler._active_func = self.old_func
        Handler._active_mcfunc_path = self.old_mcfunc
        Handler._cmds = self.old_cmds