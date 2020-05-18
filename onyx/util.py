from .exception import InvalidPosition
import enum

def Negate(arg):
    if isinstance(arg, enum.Enum): return f"!{str(arg.name)}"
    elif isinstance(arg, (int, float)): return f"!{arg}"
    
def Range(min="", max=""):
    return f"{min}..{max}"

# Thanks for Vorniy for shortening down the if statements
def abs_pos(x, y, z):
    if not all(isinstance(arg, (int, float)) for arg in [x, y, z]):
        raise InvalidPosition("You must supply 3 numbers")
    return (f"{x}", f"{y}", f"{z}")

def rel_pos(x, y, z):
    if not all(isinstance(arg, (int, float)) for arg in [x, y ,z]):
        raise InvalidPosition("You must supply 3 numbers")
    return (f"~{x or ''}", f"~{y or ''}", f"~{z or ''}")

def loc_pos(left, up, forward):
    if not all(isinstance(arg, (int, float)) for arg in [left, up, forward]):
        raise InvalidPosition("You must supply 3 numbers")
    return (f"^{left or ''}", f"^{up or ''}", f"^{forward or ''}")

def abs_rot(y_rot, x_rot):
    if not all(isinstance(arg, (int, float)) for arg in [y_rot, x_rot]):
        raise InvalidPosition("You must supply 2 numbers")
    return (f"{y_rot}", f"{x_rot}")

def rel_rot(y_rot, x_rot):
    if not all(isinstance(arg, (int, float)) for arg in [y_rot, x_rot]):
        raise InvalidPosition("You must supply 2 numbers")
    return (f"~{y_rot}", f"~{x_rot}")  