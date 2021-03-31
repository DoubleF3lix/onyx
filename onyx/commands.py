from onyx.text_component import TextComponent
from onyx.selector import Selector
from onyx.dev_util import translate
from onyx.registries import gamemode


class Scoreboard:
    @staticmethod
    def list_player_scores(target: Selector):
        return Commands.push(f"scoreboard players list {translate(target)}")

    @staticmethod
    def reset_player_scores(target: Selector):
        return Commands.push(f"scoreboard players reset {translate(target)}")

    @staticmethod
    def list_objectives():
        return Commands.push("scoreboard objectives list")


class Commands:
    def __init__(self, pack_object):
        Commands.function_contents = []
        Commands.pack_object = pack_object
        Commands.added_scoreboards = []
        Commands.init_commands = []
        Commands.active_function = None

        Commands.scoreboard = Scoreboard()

    @staticmethod
    def push(command, init=False):
        if isinstance(command, list):
            command = "\n".join(command)
        if init == False:
            Commands.function_contents.append(command)
            return command
        else:
            if command not in Commands.init_commands:
                Commands.pack_object.init_contents.append(command)
                Commands.init_commands.append(command)

    @staticmethod
    def say(text: str):
        return Commands.push(f"say {text}")

    @staticmethod
    def gamemode(mode: gamemode, players: Selector):
        return Commands.push(f"gamemode {translate(mode)} {translate(players)}")

    @staticmethod
    def tellraw(players: Selector, text: TextComponent):
        return Commands.push(f"tellraw {translate(players)} {translate(text)}")
