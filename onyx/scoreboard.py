from typing import Union
from onyx.registries import scoreboard_display, scoreboard_trait, scoreboard_render_type
from onyx.dev_util import translate, add_scoreboard, convert_scoreboard_player_name
from onyx.commands import Commands
from onyx.text_component import TextComponent


class Player:
    def __init__(self, parent, name):
        self.parent = parent
        self.name = convert_scoreboard_player_name(name)

    def set(self, value):
        self.parent.operator = "="
        return self.parent.handle_operator(self.name, value)

    def __imatmul__(self, value):
        return self.set(value)

    def __str__(self):
        return f"{self.name} {self.parent.name}"

    def __iadd__(self, value):
        return self.add(value)

    def add(self, value):
        self.parent.operator = "+="
        return self.parent.handle_operator(self.name, value)

    def __isub__(self, value):
        return self.subtract(value)

    def subtract(self, value):
        self.parent.operator = "-="
        return self.parent.handle_operator(self.name, value)

    def __imul__(self, value):
        return self.multiply(value)

    def multiply(self, value):
        self.parent.operator = "*="
        return self.parent.handle_operator(self.name, value)

    def __idiv__(self, value):
        return self.divide(value)

    def divide(self, value):
        self.parent.operator = "/="
        return self.parent.handle_operator(self.name, value)

    def __imod__(self, value):
        return self.modulo(value)

    def modulo(self, value):
        self.parent.operator = "%="
        return self.parent.handle_operator(self.name, value)

    def swap(self, value):
        self.parent.operator = "><"
        return self.parent.handle_operator(self.name, value)
 
    def set_if_less(self, value):
        self.parent.operator = "<"
        return self.parent.handle_operator(self.name, value)

    def set_if_greater(self, value):    
        self.parent.operator = ">"
        return self.parent.handle_operator(self.name, value)

    def enable(self):
        return Commands.push(f"scoreboard players enable {translate(self.name)} {self.parent.name}")

    def get(self):
        return Commands.push(f"scoreboard players get {translate(self.name)} {self.parent.name}")

    def reset(self):
        return Commands.push(f"scoreboard players reset {translate(self.name)} {self.parent.name}")


class Scoreboard:
    def __init__(self, name: str, create: bool = False, criteria: str = "dummy", display_name: str = None):
        self.name = name
        self.create = create
        self.criteria = criteria
        self.display_name = translate(display_name)

        if self.create == True:
            Commands.push(f"scoreboard objectives add {self.name} {self.criteria} {self.display_name}", init=True)

        # self.operator is overwritten if anything except "=" is used
        self.operator = "="

        # Used to keep track of existing players to de-dupe stuff
        self.players = {}

    def player(self, name: str):
        if name not in self.players:
            self.players[name] = Player(self, name)
        return self.players[name]

    def get_name(self):
        return self.name

    def handle_operator(self, name, value):
        if isinstance(value, int):
            if self.operator in {"=", "+=", "-="}:
                operator_name = {"=": "set", "+=": "add", "-=": "remove"}[self.operator]
                return Commands.push(f"scoreboard players {operator_name} {translate(name)} {self.name} {value}")
            elif self.operator in {"*=", "/=", "%=",  "<", ">"}:
                add_scoreboard("onyx.const"),
                Commands.push(f"scoreboard players set ${value} onyx.const {value}", init=True),
                return Commands.push(f"scoreboard players operation {translate(name)} {self.name} {self.operator} ${value} onyx.const")
            elif self.operator == "><":
                raise ValueError("Cannot swap between player score and integer")
        else:
            if self.operator in {"=", "+=", "-=", "*=", "/=", "%=", "<", ">", "><"}:
                return Commands.push(f"scoreboard players operation {translate(name)} {self.name} {self.operator} {value.name} {value.parent.name}")

        self.operator = "="

    def delete(self):
        return Commands.push(f"scoreboard objectives remove {self.name}")

    def reset(self):
        return Commands.push(f"scoreboard players reset * {self.name}")

    def setdisplay(self, display: scoreboard_display):
        return Commands.push(f"scoreboard objectives setdisplay {translate(display)} {self.name}")

    def modify(self, trait: scoreboard_trait, value: Union[TextComponent, scoreboard_render_type]):
        return Commands.push(f"scoreboard objectives modify {self.name} {translate(trait)} {translate(value)}")

    def create(self, overwrite: bool = False):
        q = []
        if overwrite == True:
            q.append(Commands.push(f"scoreboard objectives remove {self.name}"))
        q.append(Commands.push(f"scoreboard objectives add {self.name} {self.criteria} {self.display_name}"))
        return q
