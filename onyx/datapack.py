import inspect
from .handler import Handler
from .enum import position

def disable(datapack_name:str):
    if not isinstance(datapack_name, str):
        raise ValueError(f"Expected string for 'datapack_name', got {type(datapack_name)}")
    Handler._write(inspect.stack()[1][3], f"datapack disable \"file/{datapack_name}\"")

def enable(datapack_name:str, datapack_pos:position=None, relative_to:str=None):
    if not isinstance(datapack_name, str):
        raise ValueError(f"Expected string for 'datapack_name', got {type(datapack_name)}")
    if datapack_pos:
        if datapack_pos.value in {"before", "after"}:
            if not relative_to:
                Handler._warn("Specified 'datapack_pos' but not 'relative_to' so it was ignored")
                Handler._write(inspect.stack()[1][3], f"datapack enable \"file/{datapack_name}\"") 
                 # Stop running the function so the below statements don't run
                return 0
            else:
                if not isinstance(relative_to, str):
                    raise ValueError(f"Expected string for 'relative_to', got {type(relative_to)}")
                Handler._write(inspect.stack()[1][3], f"datapack enable \"file/{datapack_name}\" {datapack_pos.value} \"file/{relative_to}\"")
                # Stop running the function so the below statements don't run
                return 0
    
        Handler._write(inspect.stack()[1][3], f"datapack enable \"file/{datapack_name}\" {datapack_pos.value}")
        # Stop running the function so the below statements don't run
        return 0
    Handler._write(inspect.stack()[1][3], f"datapack enable \"file/{datapack_name}\"") 