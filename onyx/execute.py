import os
from typing import Union
from .enums import axis, anchor, dimension
from .selector import selector
from .handler import Handler
from .util import AbsPos, LocPos, RelPos, AbsRot, RelRot


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

        Handler._cmds.append(f"{self.output}function {Handler._datapack_name}:generated/{function_name_extensionless}{differentiator}")
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
        """
        Args:
            *args (axis): The axes to align with
        """
        axes = []
        for arg in args:
            if Handler._translate(arg) not in args:
                axes.append(Handler._translate(arg))
        self.output += f"align {''.join(axes)}"
        return self

    def anchored(self, anchor_point: anchor):
        """
        Args:
            anchor_point (anchor): The anchor point (feet, eyes)
        """
        self.output += f"anchored {Handler._translate(anchor_point)} "
        return self

    def As(self, entity: selector):
        """"as" is a reserved keyword

        Args:
            entity (selector): The entity to execute as
        """
        self.output += f"as {Handler._translate(entity)} "
        return self

    def at(self, entity: selector):
        """
        Args:
            entity (selector): The entity to execute at
        """
        self.output += f"at {Handler._translate(entity)} "
        return self

    def as_at(self, entity: selector):
        """A combination of `As()` and `at()`
        Args:
            entity (selector): The entity to execute as and at
        """
        self.output += f"as {Handler._translate(entity)} at @s "
        return self

    def facing(self, entity: selector = None, pos: Union[AbsPos, LocPos, RelPos] = None):
        """
        Args:
            entity (selector, optional): The entity to face. Defaults to None.
            pos (Union[AbsPos, LocPos, RelPos], optional): The block to face. Defaults to None.
        """
        if entity is not None:
            if pos is not None:
                Handler._warn("Both 'entity' and 'pos' were specified. Ignoring 'pos'.")
            self.output += f"facing entity {Handler._translate(entity)} "
        elif pos is not None:
            self.output += f"facing {Handler._translate(pos)} "
        else:
            Handler._warn("Neither 'entity' nor 'pos' were specified. Ignoring.")
        return self

    def In(self, dimension_name: Union[dimension, str]):
        """"in" is a reserved keyword

        Args:
            dimension_name (dimension): The dimension to execute in
        """
        self.output += f"in {Handler._translate(dimension_name)} "
        return self

    def positioned(self, pos: Union[AbsPos, LocPos, RelPos]):
        """
        Args:
            pos (Union[AbsPos, LocPos, RelPos]): The position to execute in
        """
        self.output += f"positioned {Handler._translate(pos)} "
        return self

    def rotated(self, entity: selector = None, rot: Union[AbsRot, RelRot] = None):
        """
        Args:
            entity (selector, optional): [description]. Defaults to None.
            rot (Union[AbsRot, RelRot], optional): [description]. Defaults to None.
        """
        if entity is not None:
            if rot is not None:
                Handler._warn("Both 'entity' and 'rot' specified. Ignoring 'rot'.")
            self.output += f"rotated as {Handler._translate(entity)} "
        elif rot is not None:
            self.output += f"rotated {Handler._translate(rot)} "
        else:
            Handler._warn("Neither 'entity' nor 'rot' were specified. Ignoring.")
        return self
