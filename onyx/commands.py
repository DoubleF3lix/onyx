from onyx.selector import Selector
from onyx.dev_util import translate
from onyx.registries import gamemode


class Scoreboard:
    @staticmethod
    def list_player_scores(target: Selector):
        Commands.push(f"scoreboard players list {translate(target)}")

    @staticmethod
    def reset_player_scores(target: Selector):
        Commands.push(f"scoreboard players reset {translate(target)}")

    @staticmethod
    def list_objectives():
        Commands.push("scoreboard objectives list")


class Commands:
    def __init__(self, pack_object):
        Commands.function_contents = []
        Commands.pack_object = pack_object
        Commands.added_scoreboards = []

        Commands.scoreboard = Scoreboard()

    @staticmethod
    def push(command: str, init: bool = False):
        if init == False:
            Commands.function_contents.append(command)
        else:
            Commands.pack_object.init_contents.append(command)

    @staticmethod
    def say(text: str):
        Commands.push(f"say {text}")

    @staticmethod
    def gamemode(mode: gamemode, players: Selector):
        Commands.push(f"gamemode {translate(mode)} {translate(players)}")
