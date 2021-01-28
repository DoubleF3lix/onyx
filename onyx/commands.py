import onyx.registries

class Commands:
    def __init__(self):
        Commands.function_contents = []

    @staticmethod
    def push(command: str):
        Commands.function_contents.append(command)

    @staticmethod
    def say(text: str):
        Commands.push(f"say {text}")

    @staticmethod
    def gamemode(mode: onyx.registries.difficulty, players: onyx.selector.Selector):
        Commands.push(f"")