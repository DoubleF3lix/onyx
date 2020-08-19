from typing import Union
from .handler import Handler
from .enums import recipes
from .selector import selector


def _multi_operator(operator, targets, recipe):
    if isinstance(recipe, list):
        for item in recipe:
            Handler._cmds.append(f"recipe {operator} {Handler._translate(targets)} {Handler._translate(item)}")
    else:
        Handler._cmds.append(f"recipe {operator} {Handler._translate(targets)} {Handler._translate(recipe)}")


def give(targets: selector, recipe: Union[recipes, list]):
    """
    Args:
        targets (selector): The players to give the recipe to
        recipe (Union[recipes, list]): The recipe(s) to give
    """
    _multi_operator("give", targets, recipe)


def take(targets: selector, recipe: Union[recipes, list]):
    """
    Args:
        targets (selector): The players to remove the recipe from
        recipe (Union[recipes, list]): The recipe(s) to remove
    """
    _multi_operator("take", targets, recipe)
