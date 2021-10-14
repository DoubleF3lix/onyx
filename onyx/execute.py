import os
from typing import Union
from .enums import axis, anchor, dimension, block, container_type, score_operator, data_type, store_type, bossbar_trait
from .selector import selector
from .handler import Handler
from .util import AbsPos, LocPos, RelPos, CurrentPos, AbsRot, RelRot
from .scoreboard import Player


# Each method returns self to allow for method chaining
# Method chaining allows execute statements to be reused multiple times
class execute:
    def __init__(self):
        self.output = "execute "

        # Save the old function path
        self.old_func = Handler._active_func
        self.old_mcfunc = Handler._active_mcfunc_path

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

        Handler._cmds.append(f"{self.output}run function {Handler._active_mcfunc_path}")
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
        """A combination of ``As()`` and ``at()``
        Args:
            entity (selector): The entity to execute as and at
        """
        self.output += f"as {Handler._translate(entity)} at @s "
        return self

    def facing(self, entity: selector = None, pos: Union[AbsPos, LocPos, RelPos, CurrentPos] = None):
        """
        Args:
            entity (selector, optional): The entity to face. Defaults to None.
            pos (Union[AbsPos, LocPos, RelPos, CurrentPos], optional): The block to face. Defaults to None.
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

    def positioned(self, pos: Union[AbsPos, LocPos, RelPos, CurrentPos]):
        """
        Args:
            pos (Union[AbsPos, LocPos, RelPos, CurrentPos]): The position to execute in
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

    def if_block(self, position: Union[AbsPos, RelPos, LocPos, CurrentPos], block: Union[block, str]):
        self._multi_block("if", position, block)
        return self

    def unless_block(self, position: Union[AbsPos, RelPos, LocPos, CurrentPos], block: Union[block, str]):
        self._multi_block("unless", position, block)
        return self

    def if_blocks_match(self, corner1: Union[AbsPos, RelPos, LocPos, CurrentPos], corner2: Union[AbsPos, RelPos, LocPos, CurrentPos], location: Union[AbsPos, RelPos, LocPos, CurrentPos], include_air: bool = False):
        self._multi_blocks("if", corner1, corner2, location, include_air)
        return self

    def unless_blocks_match(self, corner1: Union[AbsPos, RelPos, LocPos, CurrentPos], corner2: Union[AbsPos, RelPos, LocPos, CurrentPos], location: Union[AbsPos, RelPos, LocPos, CurrentPos], include_air: bool = False):
        self._multi_blocks("unless", corner1, corner2, location, include_air)
        return self

    def if_data(self, container_type: container_type, location: Union[selector, AbsPos, RelPos, LocPos, CurrentPos, str], path: str):
        self._multi_data("if", container_type, location, path)
        return self

    def unless_data(self, container_type: container_type, location: Union[selector, AbsPos, RelPos, LocPos, CurrentPos, str], path: str):
        self._multi_data("unless", container_type, location, path)
        return self

    def if_entity(self, entity: selector):
        self._multi_entity("if", entity)
        return self

    def unless_entity(self, entity: selector):
        self._multi_entity("unless", entity)
        return self

    def if_predicate(self, predicate: str):
        self._multi_predicate("if", predicate)
        return self

    def unless_predicate(self, predicate: str):
        self._multi_predicate("unless", predicate)
        return self

    def if_score(self, score: Player, operator: score_operator, value: Union[int, Player]):
        self._multi_score("if", score, operator, value)
        return self

    def unless_score(self, score: Player, operator: score_operator, value: Union[int, Player]):
        self._multi_score("unless", score, operator, value)
        return self

    def store_block(self, store_type: store_type, position: Union[AbsPos, RelPos, LocPos, CurrentPos], path: str, data_type: data_type, scale: int = 1):
        self.output += f"store {Handler._translate(store_type)} block {Handler._translate(position)} {Handler._translate(path)} {Handler._translate(data_type)} {Handler._translate(scale)} "

    def store_bossbar(self, store_type: store_type, bossbar_id: str, attribute: bossbar_trait):
        if Handler._translate(attribute) not in {"max", "value"}:
            Handler._warn("Invalid value for 'attribute' specified. Assuming 'value'.")
            attribute = "value"
        self.output += f"store {Handler._translate(store_type)} bossbar {Handler._translate(bossbar_id)} {Handler._translate(attribute)} "

    def store_entity(self, store_type: store_type, target: selector, path: str, data_type: data_type, scale: int = 1):
        self.output += f"store {Handler._translate(store_type)} entity {Handler._translate(target)} {Handler._translate(path)} {Handler._translate(data_type)} {Handler._translate(scale)} "

    def store_score(self, store_type: store_type, score: Player, objective: str = None):
        if objective is None:
            objective = score.scoreboard
            score = score.name
        self.output += f"store {Handler._translate(store_type)} score {Handler._translate(score)} {Handler._translate(objective)} "

    def store_storage(self, store_type: store_type, location: str, path: str, data_type: data_type, scale: int = 1):
        self.output += f"store {Handler._translate(store_type)} storage {Handler._translate(location)} {Handler._translate(path)} {Handler._translate(data_type)} {Handler._translate(scale)} "

    def _multi_block(self, type, position, block):
        self.output += f"{type} block {Handler._translate(position)} {Handler._translate(block)} "

    def _multi_blocks(self, type, corner1, corner2, location, include_air):
        if include_air is True:
            mask_mode = "all"
        else:
            mask_mode = "masked"
        self.output += f"{type} blocks {Handler._translate(corner1)} {Handler._translate(corner2)} {Handler._translate(location)} {Handler._translate(mask_mode)} "

    def _multi_data(self, type, container_type, location, path):
        self.output += f"{type} data {Handler._translate(container_type)} {Handler._translate(location)} {Handler._translate(path)} "

    def _multi_entity(self, type, entity):
        self.output += f"{type} entity {Handler._translate(entity)} "

    def _multi_predicate(self, type, predicate):
        self.output += f"{type} predicate {Handler._translate(predicate)} "

    def _multi_score(self, type, score, operator, value):
        if Handler._translate(operator) != "matches":
            if isinstance(value, int):
                Handler._add_scoreboard("onyx.const")
                Handler._add_to_init(f"scoreboard players set {value} onyx.const {value}")
                self.output += f"{type} score {Handler._translate(score.name)} {Handler._translate(score.scoreboard)} {Handler._translate(operator)} {Handler._translate(value)} onyx.const "
            else:
                self.output += f"{type} score {Handler._translate(score.name)} {Handler._translate(score.scoreboard)} {Handler._translate(operator)} {Handler._translate(value.name)} {Handler._translate(value.scoreboard)} "
        else:
            self.output += f"{type} score {Handler._translate(score.name)} {Handler._translate(score.scoreboard)} {Handler._translate(operator)} {Handler._translate(value)} "
