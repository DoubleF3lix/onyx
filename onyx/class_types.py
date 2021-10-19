class Buildable:
    ...


class Particle:
    ...


class Stringable:
    ...


class Vector3:
    """
    Vector3 - Represents a group of 3 numbers

    Args:
        prefix (str): A string that is inserted before every value
        x (int): First value
        y (int): Second value
        z (int): Third value
    """

    def __init__(self, prefix: str, x: int, y: int, z: int) -> None:
        self.prefix = prefix
        self.x = x
        self.y = y
        self.z = z

    def build(self) -> str:
        """
        build

        Returns:
            str: The Vector3 as a string
        """
        return f"{self.prefix}{self.x} {self.prefix}{self.y} {self.prefix}{self.z}"


class Vector2:
    """
    Vector3 - Represents a group of 2 numbers

    Args:
        prefix (str): A string that is inserted before every value
        x (int): First value
        y (int): Second value
    """

    def __init__(self, prefix: str, x: int, y: int) -> None:
        self.prefix = prefix
        self.x = x
        self.y = y

    def build(self) -> str:
        """
        build

        Returns:
            str: The Vector2 as a string
        """
        return f"{self.prefix}{self.x} {self.prefix}{self.y}"
