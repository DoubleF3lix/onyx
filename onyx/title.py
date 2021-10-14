from .handler import Handler
from .selector import selector
from .json_string import json_string


def actionbar(targets: selector, text: json_string):
    """
    Args:
        targets (selector): The players to display the text to
        text (json_string): The text to display
    """
    Handler._cmds.append(f"title {Handler._translate(targets)} actionbar {Handler._translate(text)}")


def clear(targets: selector = "@a"):
    """Clears the title and subtitle

    Args:
        targets (selector, optional): The players to clear of title of. Defaults to "@a".
    """
    Handler._cmds.append(f"title {Handler._translate(targets)} clear")


def reset(targets: selector):
    """Clears the subtitle and resets the times

    Args:
        targets (selector): The players to reset the subtitle of
    """
    Handler._cmds.append(f"title {Handler._translate(targets)} reset")


def subtitle(targets: selector, text: json_string, titleless: bool = False):
    """
    Args:
        targets (selector): The players to display the text to
        text (json_string): The text to display
        titleless (bool, optional): Whether or not a title is planned to exist. Automatically creates a blank title. Defaults to False.
    """
    if titleless:
        Handler._cmds.append(f"title {Handler._translate(targets)} title \"\"")
    Handler._cmds.append(f"title {Handler._translate(targets)} subtitle {Handler._translate(text)}")


def times(targets: selector, fade_in: int, stay: int, fade_out: int):
    """
    Args:
        targets (selector): The players to modify the times of
        fade_in (int): How long it takes the text to show up
        stay (int): How long the text stays
        fade_out (int): How long it takes for the text to disappear
    """
    Handler._translate(f"title {Handler._translate(targets)} {Handler._translate(fade_in)} {Handler._translate(stay)} {Handler._translate(fade_out)}")


def title(targets: selector, text: json_string):
    """
    Args:
        targets (selector): The players to display the text to
        text (json_string): The text to display
    """
    Handler._cmds.append(f"title {Handler._translate(targets)} title {Handler._translate(text)}")
