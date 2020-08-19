from .handler import Handler
from .selector import selector


def add(targets: selector, tag_name: str):
    """
    Args:
        targets (selector): The targets to add the tag to
        tag_name (str): The name of the tag
    """
    Handler._cmds.append(f"tag {Handler._translate(targets)} add {Handler._translate(tag_name)}")


def remove(targets: selector, tag_name: str):
    """
    Args:
        targets (selector): The targets to remove the tag from
        tag_name (str): The name of the tag
    """
    Handler._cmds.append(f"tag {Handler._translate(targets)} remove {Handler._translate(tag_name)}")


def list(targets: selector):
    """Returns the number of tags
    Args:
        targets (selector): The targets to get the tag list from
    """
    Handler._cmds.append(f"tag {Handler._translate(targets)} list")
