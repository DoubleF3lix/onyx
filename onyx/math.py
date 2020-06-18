import inspect
from typing import Union
import math
from .handler import Handler
from .enum import lib


def rand_int(lower_bound: int = None, upper_bound: int = None):
    """rand_int - Generates a random number within the bounds set. If 'lower_bound' or 'upper_bound' are not specified, it defaults to 0 or 2147483647 respectively.

    Args:
        lower_bound (int, optional): The minimum value that should be set. Defaults to None.
        upper_bound (int, optional): The maximum value that should be set. Defaults to None.
    """
    if isinstance(lower_bound, float):
        lower_bound = math.floor(lower_bound)
    if isinstance(upper_bound, float):
        upper_bound = math.floor(upper_bound)

    Handler._load_lib(lib.rng)
    Handler._add_to_init("scoreboard objectives add onyx.rng dummy")

    if lower_bound:
        Handler._write(inspect.stack()[1][3], f"scoreboard players set $lower_bound onyx.rng {lower_bound}")
        if not upper_bound:
            Handler._write(inspect.stack()[1][3], f"scoreboard players set $upper_bound onyx.rng 2147483647")
    if upper_bound:
        Handler._write(inspect.stack()[1][3], f"scoreboard players set $upper_bound onyx.rng {upper_bound}")
        if not lower_bound:
            Handler._write(inspect.stack()[1][3], f"scoreboard players set $lower_bound onyx.rng 0")

    if lower_bound or upper_bound:
        Handler._write(inspect.stack()[1][3], f"function {Handler._datapack_name}:lib/rng/range")
        return f"function {Handler._datapack_name}:lib/rng/range"
    else:
        Handler._write(inspect.stack()[1][3], f"function {Handler._datapack_name}:lib/rng/no_range")
        return f"function {Handler._datapack_name}:lib/rng/no_range"


def sin(theta: Union[int, float]):
    """sin - Calculate the sine of an angle in degrees. Outputs to a scale of 10,000 (0.0197 => 197)

    Args:
        theta (int or float): The angle to calculate.
    """

    Handler._load_lib(lib.math)

    Handler._add_to_init("scoreboard objectives add onyx.math dummy")
    Handler._write(inspect.stack()[1][3], [
        f"scoreboard players set $input onyx.math {math.floor(theta * 10)}",
        f"function {Handler._datapack_name}:lib/math/sin/main"

    ])
    return f"function {Handler._datapack_name}:lib/math/sine/main"


def cos(theta: Union[int, float]):
    """cos - Calculate the cosine of an angle in degrees. Outputs to a scale of 10,000 (0.0197 => 197)

    Args:
        theta (int or float): The angle to calculate.
    """

    Handler._load_lib(lib.math)
    Handler._add_to_init("scoreboard objectives add onyx.math dummy")

    Handler._write(inspect.stack()[1][3], [
        f"scoreboard players set $input onyx.math {math.floor(theta * 10)}",
        f"function {Handler._datapack_name}:lib/math/cos/main"
    ])
    return f"function {Handler._datapack_name}:lib/math/cosine/main"


def tan(theta: Union[int, float]):
    """tan - Calculate the tangent of an angle in degrees. Outputs to a scale of 1. (1.0105 => 1)

    Args:
        theta (int or float): The angle to calculate.
    """

    Handler._load_lib(lib.math)
    Handler._add_to_init("scoreboard objectives add onyx.math dummy")

    Handler._write(inspect.stack()[1][3], [
        f"scoreboard players set $input onyx.math {math.floor(theta * 10)}",
        f"function {Handler._datapack_name}:lib/math/tan/main"
    ])
    return f"function {Handler._datapack_name}:lib/math/tangent/main"


def asin(ratio: Union[int, float]):
    """atan - Calculate the inverse sine. Outputs to a scale of 1000. (-0.001 => -1)

    Args:
        ratio (Union[int, float]): The ratio to calculate. Limited from -1 to 1.
    """

    if ratio < 1 or ratio > -1:
        raise ValueError("'ratio' must be between -1 and 1")

    Handler._load_lib(lib.math)
    Handler._add_to_init("scoreboard objectives add onyx.math dummy")

    Handler._write(inspect.stack()[1][3], [
        f"scoreboard players set $input onyx.math {math.floor(ratio * 10)}",
        f"function {Handler._datapack_name}:lib/math/asin/main"
    ])
    return f"function {Handler._datapack_name}:lib/math/asin/main"


def acos(ratio: Union[int, float]):
    """atan - Calculate the cosine sine. Outputs to a scale of 1000. (-0.001 => -1)

    Args:
        ratio (Union[int, float]): The ratio to calculate. Limited from -1 to 1.
    """

    if ratio < 1 or ratio > -1:
        raise ValueError("'ratio' must be between -1 and 1")

    Handler._load_lib(lib.math)
    Handler._add_to_init("scoreboard objectives add onyx.math dummy")

    Handler._write(inspect.stack()[1][3], [
        f"scoreboard players set $input onyx.math {math.floor(ratio * 10)}",
        f"function {Handler._datapack_name}:lib/math/acos/main"
    ])
    return f"function {Handler._datapack_name}:lib/math/acos/main"


def atan(ratio: Union[int, float]):
    """atan - Calculate the inverse tangent. Outputs to a scale of 1000. (-0.001 => -1)

    Args:
        ratio (Union[int, float]): The ratio to calculate. Limited from -1 to 1.
    """

    if ratio <= -1 or ratio >= 1:
        raise ValueError("'ratio' must be between -1 and 1")

    Handler._load_lib(lib.math)
    Handler._add_to_init("scoreboard objectives add onyx.math dummy")

    Handler._write(inspect.stack()[1][3], [
        f"scoreboard players set $input onyx.math {math.floor(ratio * 10)}",
        f"function {Handler._datapack_name}:lib/math/atan/main"
    ])
    return f"function {Handler._datapack_name}:lib/math/atan/main"
