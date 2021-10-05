class Buildable: ...
class Particle: ...


class Vector3:
    def __init__(self, prefix, x, y, z):
        self.prefix = prefix
        self.x = x
        self.y = y
        self.z = z

    def build(self):
        # Single number passed
        if self.y is None and self.z is None:
            return f"{self.prefix}{self.x}"
        else:
            return f"{self.prefix}{self.x} {self.prefix}{self.y} {self.prefix}{self.z}"


class Vector2:
    def __init__(self, prefix, x, y):
        self.prefix = prefix
        self.x = x
        self.y = y

    def build(self):
        # Single number passed
        if self.y is None:
            return f"{self.prefix}{self.x}"
        else:
            return f"{self.prefix}{self.x} {self.prefix}{self.y}"
