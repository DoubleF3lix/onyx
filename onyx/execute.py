import os
from .enums import axis, anchor, dimension
from .selector import selector
from .handler import Handler


# Each method returns self to allow for method chaining
# Method chaining allows execute statements to be reused multiple times
class execute:
    def __init__(self):
        self.output = "execute "

        # Save the old function path
        self.old_func = Handler._active_func

    def __enter__(self):
        # Call the new function and save all the old commands
        # Get the current function path without the function file itself
        functionless_path = os.path.dirname(Handler._active_func)
        if functionless_path.endswith("\\."):
            functionless_path = functionless_path[:-1]
        function_name = os.path.basename(os.path.normpath(Handler._active_func))
        function_name_extensionless = os.path.splitext(function_name)[0]
        differentiator = Handler._get_differentiator()

        Handler._cmds.append(f"function {Handler._datapack_name}:generated/{function_name_extensionless}{differentiator}")
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

    def align(self, *args: axis):
        axes = []
        for arg in args:
            if Handler._translate(arg) not in args:
                axes.append(Handler._translate(arg))
        self.output += f"align {''.join(axes)}"
        return self

    def anchored(self, anchor_point: anchor):
        self.output += f"anchored {Handler._translate(anchor_point)} "
        return self

    def As(self, entity: selector):
        self.output += f"as {Handler._translate(entity)} "
        return self

    def at(self, entity: selector):
        self.output += f"at {Handler._translate(entity)} "
        return self

    def as_at(self, entity: selector):
        self.output += f"as {Handler._translate(entity)} at @s "
        return self

    def facing(self, entity: selector = None, pos: tuple = None):
        if entity is not None:
            if pos is not None:
                raise ValueError("You can't provide both an entity and position")
            self.output += f"facing entity {Handler._translate(entity)} "
        elif pos is not None:
            self.output += f"facing {Handler._translate(pos)} "
        else:
            raise ValueError("You must specify either an entity or position value")
        return self

    def In(self, dimension_name: dimension):
        self.output += f"in {Handler._translate(dimension_name)} "
        return self

    def positioned(self, pos: tuple):
        self.output += f"positioned {Handler._translate(pos)} "
        return self

    def rotated(self, entity: selector = None, rot: tuple = None):
        if entity is not None:
            if rot is not None:
                raise ValueError("You can't provide both an entity and rotation values")
            self.output += f"rotated as {Handler._translate(entity)} "
        elif rot is not None:
            self.output += f"rotated {Handler._translate(rot)} "
        else:
            raise ValueError("You must specify either an entity or rotation value(s)")
        return self
