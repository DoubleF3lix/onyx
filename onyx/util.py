from .exception import InvalidPosition
import enum

def Negate(arg):
    if isinstance(arg, enum.Enum): return f"!{str(arg.name)}"
    elif type(arg) is int or type(arg) is float: return f"!{arg}"
    
def Range(min="", max=""):
    return f"{min}..{max}"

def AbsPos(x=0, y=0, z=0):
    if type(x) is int and type(y) is int and type(z) is int:
        return f"~{x or ''} ~{y or ''} ~{z or ''}"

def RelPos(x=0, y=0, z=0):
    if type(x) is int and type(y) is int and type(z) is int:
        return f"~{x or ''} ~{y or ''} ~{z or ''}"

def LocPos(left=0, up=0, forward=0):
    if type(left) is int and type(up) is int and type(forward) is int:
        return f"^{left or ''} ^{up or ''} ^{forward or ''}"