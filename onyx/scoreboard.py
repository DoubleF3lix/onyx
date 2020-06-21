from .handler import Handler
from .selector import Selector


def add_objective(name, critera, display):
    if not isinstance(display, Selector):
        Handler._warn("display is not a selector object. Consider using the selector builder to avoid errors.")
    Handler._write()
