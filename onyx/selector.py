import enum
from typing import Union
from .enums import at, sort, mode
from .handler import Handler, _buildable


class selector(_buildable):
    """Defines a selector

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
    def __init__(self, selector_type: at, advancements: str = None, distance: Union[int, float] = None,
                 dx: Union[int, float] = None, dy: Union[int, float] = None, dz: Union[int, float] = None,
                 gamemode: mode = None, level: int = None, limit: int = None, name: str = None,
                 nbt: str = None, predicate: str = None, scores: str = None, sort: sort = None,
                 tag: str = None, team: str = None, type: str = None, x: int = None, y: int = None,
                 z: int = None, x_rotation: Union[int, float] = None, y_rotation: Union[int, float] = None):

        self._selector_type = selector_type.value
        self._args = {}
        self._change_args(locals())

    def _change_args(self, kwargs):
        for key, arg in kwargs.items():
            # Filter out the args that weren't assigned
            if arg is not None:
                # Skip over the "self" and "selector_type" arguments
                if key in {"self", "selector_type"}:
                    continue
                elif key == "name":
                    self._args[key] = f"'{arg}'"
                # Negated arguments, enum arguments, and any custom arguments are handled here
                else:
                    self._args[key] = Handler._translate(arg)

    # Merge the two dictionaries together, with the new one taking priority.
    def modify(self, selector_type: at, advancements: str = None, distance: Union[int, float] = None,
               dx: Union[int, float] = None, dy: Union[int, float] = None, dz: Union[int, float] = None,
               gamemode: mode = None, level: int = None, limit: int = None, name: str = None,
               nbt: str = None, predicate: str = None, scores: str = None, sort: sort = None,
               tag: str = None, team: str = None, type: str = None, x: int = None, y: int = None,
               z: int = None, x_rotation: Union[int, float] = None, y_rotation: Union[int, float] = None):
        """Modify arguments for an existing selector object.

        Args: See "args" in the docstring of __init__().
        """
        self._args = {**self._args, **locals().items()}
        # Type checking isn't needed since _change_args already provides it
        self._change_args(self._args)

    # Remove an element. Default arguments aren't provided because then they'd have to specify a value
    def remove(self, *args):
        for arg in args:
            del self._args[arg]

    def build(self):
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
