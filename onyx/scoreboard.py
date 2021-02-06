from typing import Union
from onyx.registries import scoreboard_display, scoreboard_trait, scoreboard_render_type
from onyx.dev_util import translate, add_scoreboard
from onyx.commands import Commands
from onyx.text_component import TextComponent


class PlayerOperator:
    def __init__(self, parent, key):
        self.parent = parent
        self.key = key

    def __iadd__(self, value):
        self.parent.__dict__["operator"] = "+="
        return value

    def add(self, value):
        return self.__iadd__(value)

    def __isub__(self, value):
        self.parent.__dict__["operator"] = "-="
        return value

    def subtract(self, value):
        return self.__isub__(value)

    def __imul__(self, value):
        self.parent.__dict__["operator"] = "*="
        return value

    def multiply(self, value):
        return self.__imul__(value)

    def __idiv__(self, value):
        self.parent.__dict__["operator"] = "/="
        return value

    def divide(self, value):
        return self.__idiv__(value)

    def __imod__(self, value):
        self.parent.__dict__["operator"] = "%="
        return value

    def modulo(self, value):
        return self.__imod__(value)

    def swap(self, value):
        self.parent.__dict__["operator"] = "><"
        self.parent.__setattr__(self.key, value)
        return value
 
    def set_if_less(self, value):
        self.parent.__dict__["operator"] = "<"
        return value

    def set_if_greater(self, value):        
        self.parent.__dict__["operator"] = ">"
        return value

    def enable(self):
        Commands.push(f"scoreboard players enable {translate(self.key)} {self.parent.name}")

    def get(self):
        Commands.push(f"scoreboard players get {translate(self.key)} {self.parent.name}")

    def reset(self):
        Commands.push(f"scoreboard players reset {translate(self.key)} {self.parent.name}")


class Scoreboard:
    def __init__(self, name: str, create: bool = False, criteria: str = "dummy", display_name: str = None):
        self.__dict__["name"] = name
        self.__dict__["create"] = create
        self.__dict__["criteria"] = criteria
        self.__dict__["display_name"] = translate(display_name)

        if self.create == True:
            Commands.push(f"scoreboard objectives add {self.name} {self.criteria} {self.display_name}", init=True)

        # self.operator is overwritten if anything except "=" is used
        self.__dict__["operator"] = "="

    def get_name(self):
        return self.name

    def __getattr__(self, key):
        return self.__getitem__(key)

    def __getitem__(self, key):
        return PlayerOperator(self, key)

    def __setattr__(self, key, value):
        return self.__setitem__(key, value)

    def __setitem__(self, key, value):
        if key.startswith("player_"):
            key = key[7:]
        elif key.startswith("_"):
            key = f"#{key[1:]}"
        else:
            key = f"${key}"
        self._multi_operator(key, value, self.operator)

        # Restore the default operator to prepare for the next call
        self.__dict__["operator"] = "="

    def _multi_operator(self, key, value, operator):
        if isinstance(value, int):
            if operator in {"=", "+=", "-="}:
                operator_name = {"=": "set", "+=": "add", "-=": "remove"}[operator]
                Commands.push(f"scoreboard players {operator_name} {translate(key)} {self.name} {value}")
            elif operator in {"*=", "/=", "<", ">"}:
                add_scoreboard("onyx.const")
                Commands.push(f"scoreboard players set ${value} onyx.const {value}", init=True)
                Commands.push(f"scoreboard players operation {translate(key)} {self.name} {operator} ${value} onyx.const")
            elif operator == "><":
                raise ValueError("Cannot swap between player score and integer")
        else:
            if operator in {"=", "+=", "-=", "*=", "/=", "<", ">", "><"}:
                Commands.push(f"scoreboard players operation {translate(key)} {self.name} {operator} {translate(value.key)} {value.parent.name}")
            elif operator == "><":
                Commands.push(f"scoreboard players operation {translate(key)} {self.name} >< {translate(value.key)} {value.parent.name}")

    def delete(self):
        Commands.push(f"scoreboard objectives remove {self.name}")

    def reset(self):
        Commands.push(f"scoreboard players reset * {self.name}")

    def setdisplay(self, display: scoreboard_display):
        Commands.push(f"scoreboard objectives setdisplay {translate(display)} {self.name}")

    def modify(self, trait: scoreboard_trait, value: Union[TextComponent, scoreboard_render_type]):
        Commands.push(f"scoreboard objectives modify {self.name} {translate(trait)} {translate(value)}")

    def create(self, overwrite: bool = False):
        if overwrite == True:
            Commands.push(f"scoreboard objectives remove {self.name}")
        Commands.push(f"scoreboard objectives add {self.name} {self.criteria} {self.display_name}")
