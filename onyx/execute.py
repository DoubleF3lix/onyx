from typing import Union

import beet

import onyx.storage
from onyx.class_types import Buildable, Vector2, Vector3
from onyx.commands import Commands
from onyx.dev_util import translate
from onyx.pack_manager import Function
from onyx.registries import anchor, axis, dimension
from onyx.scoreboard import Expression, Player
from onyx.selector import Selector
from onyx.util import DataSource, StoreTarget


class BaseCondition:
    """
    BaseCondition - ``execute if`` and ``execute unless`` commands

    Args:
        parent (Execute): The ``Execute`` object
        prefix (str): ``if`` or ``unless``
    """

    def __init__(self, parent: "Execute", prefix: str) -> None:
        self.parent = parent
        self.prefix = prefix

    def _add_args(self, type: str, *args) -> None:
        """
        _add_args - Private method. Do not use. Adds a full ``if`` or ``unless`` subcommand to the parent object.

        Args:
            type (str): The type of subcommand to add (block, blocks, entity, etc.)
            *args: Any extra arguments to be added to the subcommand
        """
        self.parent.output.append(
            f"{self.prefix} {type} {' '.join(translate(arg) for arg in args)}"
        )

    def block(self, position: Vector3, value: str) -> "Execute":
        """
        block - Checks if a block is of a certain type

        Args:
            position (Vector3): The position to check
            value (str): The block to check at the position

        Returns:
            Execute: The parent object
        """
        self._add_args("block", position, value)
        return self.parent

    def blocks(
        self,
        corner_1: Vector3,
        corner_2: Vector3,
        end_location: Vector3,
        mask: bool = False,
    ) -> "Execute":
        """
        blocks - Checks the status of a selection of blocks

        Args:
            corner_1 (Vector3): The first corner of the selection
            corner_2 (Vector3): The second corner of the selection
            end_location (Vector3): The first corner of the area being checked
            mask (bool): Whether or not air should be ignored in the selection

        Returns:
            Execute: The parent object
        """
        self._add_args(
            "blocks", corner_1, corner_2, end_location, "masked" if mask else "all"
        )
        return self.parent

    def data(self, source: DataSource) -> "Execute":
        """
        data - Checks if a data path exists

        Args:
            source (DataSource): The data source to check

        Returns:
            Execute: The parent object
        """
        self._add_args("data", source)
        return self.parent

    def entity(self, target: Selector) -> "Execute":
        """
        entity - Checks if an entity exists

        Args:
            target (Selector): The entity to check

        Returns:
            Execute: The parent object
        """
        self._add_args("entity", target)
        return self.parent

    def predicate(self, predicate: Union["Predicate", str]) -> "Execute":
        """
        predicate - Checks if a predicate is true

        Args:
            predicate (Union[Predicate, str]): The predicate to check

        Returns:
            Execute: The parent object
        """
        self._add_args("predicate", predicate)
        return self.parent

    def score(self, expression: Expression) -> "Execute":
        """
        score - Checks if a score matches criteria

        Args:
            expression (Expression): The expression to check. Created by using a conditional operator on a ``Player`` object.

        Returns:
            Execute: The parent object
        """
        self._add_args("score", expression)
        return self.parent


class If(BaseCondition):
    """
    If - Provides synactic sugar for ``execute if`` commands

    Args:
        parent (Execute): The ``Execute`` object
    """

    def __init__(self, parent: "Execute") -> None:
        super().__init__(parent, "if")


class Unless(BaseCondition):
    """
    Unless - Provides synactic sugar for ``execute unless`` commands

    Args:
        parent (Execute): The ``Execute`` object
    """

    def __init__(self, parent: "Execute") -> None:
        super().__init__(parent, "unless")


class BaseStore:
    """
    BaseStore - ``execute store result`` and ``execute store success`` commands

    Args:
        parent (Execute): The ``Execute`` object
        prefix (str): ``result`` or ``success``
    """

    def __init__(self, parent: "Execute", prefix: str) -> None:
        self.parent = parent
        self.prefix = prefix

    def _add_args(self, type: str, source: StoreTarget) -> None:
        """
        _add_args - Private method. Do not use. Adds a full ``store result`` or ``store success`` subcommand to the parent object.

        Args:
            type (str): ``block``, ``bossbar``, ``entity``, ``score``, or ``storage``
            source (StoreTarget): The data location to store the data in
        """
        self.parent.output.append(f"store {self.prefix} {type} {translate(source)}")

    def block(self, source: StoreTarget) -> "Execute":
        """
        block - Stores data in a block

        Args:
            source (StoreTarget): The data location to store the data in

        Returns:
            Execute: The parent object
        """
        self._add_args("block", source)
        return self.parent

    def bossbar(self, source: StoreTarget) -> "Execute":
        """
        bossbar - Stores data in a bossbar

        Args:
            source (StoreTarget): The data location to store the data in

        Returns:
            Execute: The parent object
        """
        self._add_args("bossbar", source)
        return self.parent

    def entity(self, source: StoreTarget) -> "Execute":
        """
        entity - Stores data in a entity

        Args:
            source (StoreTarget): The data location to store the data in

        Returns:
            Execute: The parent object
        """
        self._add_args("entity", source)
        return self.parent

    def score(self, target: Player) -> "Execute":
        """
        score - Stores data in a scoreboard player

        Args:
            source (StoreTarget): The data location to store the data in

        Returns:
            Execute: The parent object
        """
        self._add_args("score", target)
        return self.parent

    def storage(self, source: StoreTarget) -> "Execute":
        """
        storage - Stores data in storage

        Args:
            source (StoreTarget): The data location to store the data in

        Returns:
            Execute: The parent object
        """
        self._add_args("storage", source)
        return self.parent


class Result(BaseStore):
    """
    Result - Provides synactic sugar for ``execute store result`` commands

    Args:
        parent (Execute): The ``Execute`` object
    """

    def __init__(self, parent):
        super().__init__(parent, "result")


class Success(BaseStore):
    """
    Success - Provides synactic sugar for ``execute store success`` commands

    Args:
        parent (Execute): The ``Execute`` object
    """

    def __init__(self, parent):
        super().__init__(parent, "success")


class Store:
    """
    Store - Provides synactic sugar for ``execute store`` commands. Only purpose is to provide a delimeter between ``execute`` and ``result`` or ``success`.

    Args:
        parent (Execute): The ``Execute`` object
    """

    def __init__(self, parent):
        self.result = Result(parent)
        self.success = Success(parent)


class Execute(Buildable):
    """
    Execute - Represents an ``execute`` command

    Args:
        context (str, optional): Context can be provided manually if you don't want to construct it with method chaining. Do not include the ``execute`` keyword. Example: ``"if entity @s"``. Defaults to None.
    """

    def __init__(self, context: str = None) -> None:
        self.if_ = If(self)
        self.unless = Unless(self)
        self.store = Store(self)

        self.context = context

        self.output = []
        self.differentiator = 0

    def __enter__(self) -> "Execute":
        """
        __enter__ - Called when a context manager is opened
        """
        # Copy the old function contents and make a new object for the new function
        self.old_function_contents = Commands.function_contents
        Commands.function_contents = []
        self.function_object = beet.Function([])

        # Iterate to get a unique differentiator
        # If you are using more than 65,536 execute statements in one function, you need some serious help and a gamerule command
        for q in range(1, 65536):
            # Stop when it finds an unused number
            if (
                Commands.active_function + f"/generated{q}"
                not in onyx.storage.cpo.pack_object.functions
            ):
                self.new_function_path = Commands.active_function + f"/generated{q}"
                self.old_active_function = Commands.active_function
                Commands.active_function = self.new_function_path
                break

        # Contents of context manager are run, then __exit__ is called

    def __exit__(self, exception_type, exception_value, traceback) -> None:
        """
        __exit__ - Called when a context manager is closed

        Args:
            exception_type: Parameter required for context managers. Unused.
            exception_value: Parameter required for context managers. Unused.
            traceback: Parameter required for context managers. Unused.
        """
        self.function_object.lines.extend(Commands.function_contents)
        onyx.storage.cpo.pack_object[self.new_function_path] = self.function_object
        Commands.function_contents = self.old_function_contents
        Commands.active_function = self.old_active_function

        Commands.push(
            f"execute {self.context or translate(self)} run function {self.new_function_path}"
        )

    def run(self, command: Union[Function, str]) -> str:
        """
        run - Runs a command in the context specified by the ``Execute`` object

        Args:
            command (Union[Function, str]): The command to be run

        Returns:
            str: Returns an execute command. Does not return ``self`` as no more method chaining should be done after this.
        """
        return Commands.push(
            f"execute {self.context or translate(self)} run {translate(command)}"
        )

    def align(self, axes: Union[axis, tuple]) -> "Execute":
        """
        align - Aligns on the specified axes

        Args:
            axes (Union[axis, tuple]): The axes to align the command on. You can specify a single axis, or multiple axes in a list or tuple.

        Returns:
            self: The current object
        """
        if isinstance(axes, (list, tuple)):
            axes = "".join(translate(axis) for axis in axes)
        else:
            axes = translate(axes)
        self.output.append(f"align {translate(axes)}")
        return self

    def anchored(self, anchor: anchor) -> "Execute":
        """
        anchored - Anchors on the eyes or feet of an entity

        Args:
            anchor (anchor): The anchor to be used

        Returns:
            self: The current object
        """
        self.output.append(f"anchored {translate(anchor)}")
        return self

    def as_(self, targets: Selector) -> "Execute":
        """
        as_ - Executes as the specified entity/entities

        Args:
            targets (Selector): The entity/entities to execute as

        Returns:
            self: The current object
        """
        self.output.append(f"as {translate(targets)}")
        return self

    def at(self, targets: Selector) -> "Execute":
        """
        at - Executes at the specified entity/entities

        Args:
            targets (Selector): The entity/entities to execute at

        Returns:
            self: The current object
        """
        self.output.append(f"at {translate(targets)}")
        return self

    def as_at(self, targets: Selector) -> "Execute":
        """
        as_at - Executes as AND at the specified entity/entities. Turns into ``as <entity> at @s``.

        Args:
            targets (Selector): The entity/entities to execute as and at

        Returns:
            self: The current object
        """
        self.output.append(f"as {translate(targets)} at @s")
        return self

    def facing(
        self, target: Union[Selector, Vector3], anchor: anchor = anchor.eyes
    ) -> "Execute":
        """
        facing - Executes facing the specified entity or location

        Args:
            target (Union[Selector, Vector3]): The entity or location to face
            anchor (anchor, optional): The anchor to use (eyes, feet). Defaults to ``anchor.eyes``.

        Returns:
            self: The current object
        """
        if not isinstance(target, Vector3):
            target = f"entity {translate(target)} {translate(anchor)}"
        self.output.append(f"facing {translate(target)}")
        return self

    def in_(self, dimension: dimension) -> "Execute":
        """
        in_ - Executes in a dimension

        Args:
            dimension (dimension): The dimension to execute in

        Returns:
            self: The current object
        """
        self.output.append(f"in {translate(dimension)}")
        return self

    def _positioned_or_rotated(
        self,
        location: Union[Vector3, Vector2, Selector],
        type: Union[Vector3, Vector2],
        prefix: str,
    ) -> "Execute":
        """
        _positioned_or_rotated - Private method used by ``positioned`` and ``rotated`` to reduce duplicated code

        Args:
            location (Union[Vector3, Vector2, Selector]): The location to position/rotate to
            type (Union[Vector3, Vector2]): The type of location to position/rotate to. Used for checking if ``as`` should be used.
            prefix (str): The prefix to use for the command

        Returns:
            self: The current object
        """
        if not isinstance(location, type):
            location = f"as {translate(location)}"
        self.output.append(f"{prefix}{translate(location)}")
        return self

    def positioned(self, position: Union[Vector3, Selector]) -> "Execute":
        """
        positioned - Changes the position of the execution context

        Args:
            position (Union[Vector3, Selector]): The location to execute at

        Returns:
            self: The current object
        """
        return self._positioned_or_rotated(position, Vector3, "positioned ")

    def rotated(self, rotation: Union[Vector2, Selector]) -> "Execute":
        """
        rotated - Changes the rotation of the execution context

        Args:
            rotation (Union[Vector2, Selector]): The rotation/entity to execute at

        Returns:
            self: The current object
        """
        return self._positioned_or_rotated(rotation, Vector2, "rotated ")

    def build(self) -> str:
        """
        build

        Returns:
            str: The full execute chain as a string
        """
        return " ".join(self.output)
