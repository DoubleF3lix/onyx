from onyx.enums import axis, anchor, dimension
from onyx.selector import selector


# Each method returns self to allow for method chaining
# Method chaining allows execute statements to be reused multiple times
class execute:
    def __init__(self):
        self.output = "execute "

    # execute align
    # Merges multiple enum values into one clump. (axis.x, axis.y) => xy
    def align(self, *args: axis):
        axes = []
        for arg in args:
            if arg.value not in args:
                axes.append(arg.value)
        self.output += f"align {''.join(axes)}"
        return self

    # execute anchored
    def anchored(self, anchor_point: anchor):
        self.output += f"anchored {anchor_point.value} "
        return self

    # execute as
    # Automatically builds the selector
    # "as" is a reserved keyword
    def As(self, entity: selector):
        if not isinstance(entity, selector):
            raise ValueError(f"Expected selector object, got {type(entity)}")
        self.output += f"as {entity.build()} "
        return self

    # execute at
    # Automatically builds the selector
    def at(self, entity: selector):
        if not isinstance(entity, selector):
            raise ValueError(f"Expected selector object, got {type(entity)}")
        self.output += f"at {entity.build()} "
        return self

    # execute as (entity) at (entity)
    # Automatically builds the selector
    def as_at(self, entity: selector):
        if not isinstance(entity, selector):
            raise ValueError(f"Expected selector object, got {type(entity)}")
        self.output += f"as {entity.build()} at @s "
        return self

    # execute facing
    # Automatically builds the selector if "entity" is passed
    # Doesn't allow for "entity" and "pos" to both be passed
    def facing(self, entity: selector = None, pos: tuple = None):
        if entity:
            if pos:
                raise ValueError("You can't provide both an entity and position")
            if not isinstance(entity, selector):
                raise ValueError(f"Expected selector object, got {type(entity)}")
            self.output += f"facing entity {entity.build()} "
        elif pos:
            if not type(pos) is tuple or not len(pos) == 3:
                raise ValueError("'pos' must be a tuple of 3 elements")
            self.output += f"facing {' '.join(pos)} "
        return self

    # execute in
    # "in" is a reserved keyword used for checking lists, tuples, etc.
    def In(self, dimension_name: dimension):
        self.output += f"in minecraft:{dimension_name.value} "
        return self

    # execute positioned
    def positioned(self, pos: tuple):
        if type(pos) is not tuple or len(pos) != 3:
            raise ValueError("'pos' must be a tuple of 3 elements")
        self.output += f"positioned {' '.join(pos)} "
        return self

    # execute rotated
    # Automatically builds the selector if "entity" is passed
    # Doesn't allow for "entity" and "rot" to both be passed
    def rotated(self, entity: selector = None, rot: tuple = None):
        if entity:
            if rot:
                raise ValueError("You can't provide both an entity and rotation values")
            if not isinstance(entity, selector):
                raise ValueError(f"Expected selector object, got {type(entity)}")
            self.output += f"rotated as {entity.build()} "
        elif rot:
            if type(rot) is not tuple or len(rot) != 2:
                raise ValueError("'rot' must be a tuple of 2 values")
            self.output += f"rotated {' '.join(rot)} "
        else:
            raise ValueError("You must specify either an entity or rotation values")
        return self
