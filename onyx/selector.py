from .enum import at, sort, mode
import enum
from typing import Union


class Selector:
    # I used default arguments instead of **kwargs because then I'd need to use overloading for auto-complete and it's just a mess
    def __init__(self, selector_type: at, advancements: str = None, distance: Union[int, float] = None,
                 dx: Union[int, float] = None, dy: Union[int, float] = None, dz: Union[int, float] = None,
                 gamemode: mode = None, level: int = None, limit: int = None, name: str = None,
                 nbt: str = None, predicate: str = None, scores: str = None, sort: sort = None,
                 tag: str = None, team: str = None, type: str = None, x: int = None, y: int = None,
                 z: int = None, x_rotation: Union[int, float] = None, y_rotation: Union[int, float] = None):
        """__init__ - Initalizes the selector object.

        Args:
            selector_type (at): The selector type (@a, @p, etc.).
            advancements (str, optional): Defaults to None.
            distance (Union[int, float], optional): Defaults to None.
            dx (Union[int, float], optional): Defaults to None.
            dy (Union[int, float], optional): Defaults to None.
            dz (Union[int, float], optional): Defaults to None.
            gamemode (mode, optional): Defaults to None.
            level (int, optional): Defaults to None.
            limit (int, optional): Defaults to None.
            name (str, optional): Defaults to None.
            nbt (str, optional): Defaults to None.
            predicate (str, optional): Defaults to None.
            scores (str, optional): Defaults to None.
            sort (sort, optional): Defaults to None.
            tag (str, optional): Defaults to None.
            team (str, optional): Defaults to None.
            type (str, optional): Defaults to None.
            x (int, optional): Defaults to None.
            y (int, optional): Defaults to None.
            z (int, optional): Defaults to None.
            x_rotation (Union[int, float], optional): Defaults to None.
            y_rotation (Union[int, float], optional): Defaults to None.
        """
        self._selector_type = selector_type.value
        self._args = {}
        self._change_args(locals())

    def _change_args(self, kwargs):
        """_change_args - Change the class arguments. Used internally by __init__() and modify()

        Args:
            kwargs (dict): See "args" in the docstring of __init__().

        Raises:
            ValueError: Raised if the argument isn't the right type.
        """
        for key, arg in kwargs.items():
            # Filter out the args that weren't assigned
            if arg is not None:
                # Skip over the "self" and "selector_type" arguments
                if key in {"self", "selector_type"}:
                    continue

                # Everything below is just type checking. I won't comment it since it's pretty straightforward.
                elif key in {"advancements", "nbt", "predicate", "scores", "tag", "team", "type"}:
                    if not isinstance(key, (str, tuple)):
                        raise ValueError(f"Expected string for '{key}', got {type(key)}")
                    self._args[key] = arg

                elif key in {"distance", "limit"}:
                    if isinstance(arg, (int, float)) and arg > 0:
                        self._args[key] = arg
                    else:
                        raise ValueError(f"Expected integer greater than or equal to 0 for '{key}', got {type(key)} with value {arg}")

                elif key in {"dx", "dz", "dy"}:
                    if isinstance(arg, int):
                        self._args[key] = arg
                    else:
                        raise ValueError(f"Expected integer for '{key}', got {type(key)}")

                elif isinstance(arg, enum.Enum):
                    self._args[key] = arg.value

                # Negated values
                elif isinstance(arg, str) and arg.startswith("!"):
                    self._args[key] = arg

                # This wasn't merged with the distance and limit type checking due to level being allowed to be 0.
                elif key == "level":
                    if isinstance(arg, int) and arg >= 0:
                        self._args["level"] = arg
                    else:
                        raise ValueError(f"Expected integer greater than or equal to 0 for 'level', got {type(key)} with value {arg}")

                elif key == "name":
                    self._args[key] = f"'{arg}'"

                elif key in {"x", "y", "z", "x_rotation", "y_rotation"}:
                    if isinstance(arg, (int, float)):
                        self._args[key] = arg
                    else:
                        raise ValueError(f"Expected integer for '{key}', got {type(key)}")
                # An else condition here is not needed since providing anything outside of the default arguments throws an error

    # Merge the two dictionaries together, with the new one taking priority.
    def modify(self, selector_type: at, advancements: str = None, distance: Union[int, float] = None,
               dx: Union[int, float] = None, dy: Union[int, float] = None, dz: Union[int, float] = None,
               gamemode: mode = None, level: int = None, limit: int = None, name: str = None,
               nbt: str = None, predicate: str = None, scores: str = None, sort: sort = None,
               tag: str = None, team: str = None, type: str = None, x: int = None, y: int = None,
               z: int = None, x_rotation: Union[int, float] = None, y_rotation: Union[int, float] = None):
        """modify - Modify arguments for an existing selector object.

        Args: See "args" in the docstring of __init__().
        """
        self._args = {**self._args, **locals().items()}
        # Type checking isn't needed since _change_args already provides it
        self._change_args(self._args)

    # Remove an element. Default arguments aren't provided because then they'd have to specify a value
    def remove(self, *args):
        for arg in args:
            del self._args[arg]

    # Builds the argument dictionary into a string
    # This method is automatically called by things like execute, but it's not marked as private in case the user wants to use it for some other purpose.
    def build(self):
        """build - Returns the selector object as a built string.

        Returns:
            str: The built selector.
        """
        _selector_args = []
        for key, value in self._args.items():
            if isinstance(value, str):
                _selector_args.append(f"{key}={value}")
            elif isinstance(value, tuple):
                for arg in value:
                    _selector_args.append(f"{key}={arg}")

        # Don't include "[]" if no arguments were provided
        if len(_selector_args) > 0:
            return f"{self._selector_type}[{', '.join(_selector_args)}]"
        return f"{self._selector_type}"
