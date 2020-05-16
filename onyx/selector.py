from .exception import InvalidSelector
import enum

class Selector:
    def __init__(self, selector_type, **kwargs):
        self._selector_type = selector_type.value
        self._args = {}
        self._change_args(kwargs)

    def _change_args(self, kwargs):
        for key, value in kwargs.items():
            if key in {"advancements", "nbt", "predicate", "scores", "tag", "team", "type"}: 
                self._args[key] = value
            elif key in {"distance", "limit"}: 
                if (type(value) is int or type(value) is float) and value > 0: 
                    self._args[key] = value
                else: 
                    raise InvalidSelector(f"'{key}' must be an int greater than 0")
            elif key in {"dx", "dz", "dy"}: 
                if type(value) is int: 
                    self._args[key] = value
                else: 
                    raise InvalidSelector(f"'{key}' must be an int")
            elif isinstance(value, enum.Enum): 
                self._args[key] = value.name
            elif isinstance(value, str) and value.startswith("!"): 
                    self._args[key] = value
            elif key == "level":
                if type(value) is int and value >= 0: 
                    self._args["level"] = value
                else: 
                    raise InvalidSelector("'level' must be an int greater than or equal to 0")
            elif key == "name": 
                self._args[key] = f"'{value}'"
            elif key in {"x", "y", "z", "x_rotation", "y_rotation"}:
                if (type(value) is int or type(value) is float): 
                    self._args[key] = value
                else: 
                    raise InvalidSelector(f"{key} must be an int")
            else:
                raise InvalidSelector(f"Unknown value: '{key}''")

    def modify(self, **kwargs):
        self._args = {**self._args, **kwargs}
        self._change_args(self._args)

    def remove(self, *args):
        for arg in args:
            del self._args[arg]

    def build(self):
        _selector_args = []
        for key, value in self._args.items():
            _selector_args.append(f"{key}={value}")
        selector = f"{self._selector_type}[{', '.join(_selector_args)}]"
        return selector