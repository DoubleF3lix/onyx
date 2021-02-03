from onyx.class_types import Buildable


class Range(Buildable):
    def __init__(self, min: int = None, max: int = None):
        self.min = min
        self.max = max

    def build(self):
        return f"{self.min or ''}..{self.max or ''}"