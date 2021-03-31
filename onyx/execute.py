from onyx.commands import Commands
import beet
from onyx.class_types import Pos, Rot
from onyx.util import Position, Rotation
from onyx.scoreboard import Player
from onyx.dev_util import translate
from onyx.selector import Selector
from onyx.registries import axis, anchor, bossbar_location, dimension, data_type, execute_blocks_mask, source_type
from typing import Callable, Union


class BaseCondition:
    def __init__(self, parent, prefix):
        self.parent = parent
        self.prefix = prefix

    def _add_args(self, type, *args):
        self.parent.output.append(f"{self.prefix} {type} {' '.join(translate(arg) for arg in args)}")

    def block(self, position: Position, value: str):
        self._add_args("block", position, value)
        return self.parent

    def blocks(self, corner_1: Position, corner_2: Position, end_location: Position, mask: execute_blocks_mask):
        self._add_args("blocks", corner_1, corner_2, end_location, mask)
        return self.parent

    def data(self, source_type: source_type, location: Union[str, Position, Selector], path: str):
        self._add_args("data", source_type, location, path)
        return self.parent

    def entity(self, target: Selector):
        self._add_args("entity", target)
        return self.parent

    # TODO predicate types
    def predicate(self, predicate: str):
        self._add_args("predicate", predicate)
        return self.parent

    def score(self, expression):
        self._add_args("score", expression.build()) 
        return self.parent


class If(BaseCondition):
    def __init__(self, parent):
        super().__init__(parent, "if")


class Unless(BaseCondition):
    def __init__(self, parent):
        super().__init__(parent, "unless")


class BaseStore:
    def __init__(self, parent, prefix):
        self.parent = parent
        self.prefix = prefix

    def _add_args(self, type, *args):
        self.parent.output.append(f"store {self.prefix} {type} {' '.join(str(translate(arg)) for arg in args)}")

    def block(self, location: Position, path: str, data_type: data_type, scale: Union[int, float]):
        self._add_args("block", location, path, data_type, scale)
        return self.parent

    # TODO bossbar linking (get namespace from object)
    def bossbar(self, namespace: str, store_location: bossbar_location):
        self._add_args("bossbar", namespace, store_location)
        return self.parent

    def entity(self, targets: Selector, path: str, data_type: data_type, scale: Union[int, float]):
        self._add_args("entity", targets, path, data_type, scale)
        return self.parent

    def score(self, target: Player):
        self._add_args("score", target)
        return self.parent

    def storage(self, location: str, path: str, data_type: data_type, scale: Union[int, float]):
        self._add_args("storage", location, path, data_type, scale)
        return self.parent


class Result(BaseStore):
    def __init__(self, parent):
        super().__init__(parent, "result")


class Success(BaseStore):
    def __init__(self, parent):
        super().__init__(parent, "success")


class Store:
    def __init__(self, parent):
        self.result = Result(parent)
        self.success = Success(parent)


class Execute:
    def __init__(self):
        self.if_ = If(self)
        self.unless = Unless(self)
        self.store = Store(self)

        self.output = []
        self.differentiator = 0

    def __enter__(self):
        # Copy the old function contents and make a new object for the new function
        self.old_function_contents = Commands.function_contents
        Commands.function_contents = []
        self.function_object = beet.Function([])

        # Iterate to get a unique differentiator
        # If you are using more than 65,536 execute statements in one function, you need some serious help and a gamerule command
        for q in range(1, 65536):
            # Stop when it finds an unused number
            if not Commands.active_function + f"/generated{q}" in Commands.pack_object.pack_object.functions:
                self.new_function_path = Commands.active_function + f"/generated{q}"
                self.old_active_function = Commands.active_function
                Commands.active_function = self.new_function_path
                break

        """ 
        for q in range(1, 65536):
            # Stop when it finds an unused number
            if not Commands.active_function + f"/generated{q}" in Commands.pack_object.pack_object.functions:
                # If the function is already in a generated block
                if re.match(".*\/generated\d+$", Commands.active_function):
                    # Remove all numbers at the end
                    self.new_function_path = Commands.active_function[:-get_integer_count_at_string_end(Commands.active_function)] + str(q + 1)
                # If the function is not already in a generated block
                else:
                    self.new_function_path = Commands.active_function + f"/generated{q}"
                self.old_active_function = Commands.active_function
                Commands.active_function = self.new_function_path
                break
        """
        
        # Contents of context manager are run, then __exit__ is called

    def __exit__(self, exception_type, exception_value, traceback):
        self.function_object.lines.extend(Commands.function_contents)
        Commands.pack_object.pack_object[self.new_function_path] = self.function_object
        Commands.function_contents = self.old_function_contents
        Commands.active_function = self.old_active_function
        Commands.push(f"execute {self.build()} run function {self.new_function_path}")

    def run(self, command: Callable):
        return Commands.push(f"execute {self.build()} run {translate(command)}")

    def align(self, axes: Union[axis, tuple]):
        if isinstance(axes, (list, tuple)):
            axes = "".join(translate(axis) for axis in axes)
        else:
            axes = translate(axes)
        self.output.append(f"align {translate(axes)}")
        return self
    
    def anchored(self, anchor: anchor):
        self.output.append(f"anchored {translate(anchor)}")
        return self

    def as_(self, target: Selector):
        self.output.append(f"as {translate(target)}")
        return self

    def at(self, target: Selector):
        self.output.append(f"at {translate(target)}")
        return self

    def as_at(self, target: Selector):
        self.output.append(f"as {translate(target)} at @s")
        return self

    def facing(self, target: Union[Selector, Position], anchor: anchor = anchor.eyes):
        if not isinstance(target, Pos):
            target = f"entity {translate(target)} {translate(anchor)}"
        self.output.append(f"facing {translate(target)}")
        return self

    def in_(self, dimension: dimension):
        self.output.append(f"in {translate(dimension)}")
        return self

    def positioned(self, position: Union[Position, Selector]):
        if not isinstance(position, Pos):
            position = f"as {translate(position)}"
        self.output.append(f"positioned {translate(position)}")
        return self

    def rotated(self, rotation: Union[Rotation, Selector]):
        # It's an entity
        if not isinstance(rotation, Rot):
            rotation = f"as {translate(rotation)}"
        self.output.append(f"rotated {translate(rotation)}")
        return self

    # TODO I need to find schemas for this...
    def build(self):
        return ' '.join(self.output)