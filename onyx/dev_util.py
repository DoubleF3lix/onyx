import re
import json

def convert_mcfunction_path(mcfunction_path):
    path = mcfunction_path.split(":")
    namespace = path[0]
    namespace_removed_path = path[1].split("/")

    return {
        "namespace": namespace,
        "path": '/'.join(namespace_removed_path[:-1]),
        "name": namespace_removed_path[-1]
    }

def snakify(text):
    output = []
    split_text = text.split(" ")
    for part in split_text:
        part = re.sub(r'[^A-Za-z_]', '', part)
        output.append(part.lower())

    return '_'.join(output)

def dict_to_advancement_selector(arg):
    # {"thing/1": {"thing/12": True}, "thing/2": False}
    tmp = []
    for key, item in arg.items():
        if isinstance(item, bool):
            tmp.append(f"{key}={json.dumps(item)}")   
        # Assume type is dictionary
        else:
            # Grab only the first key and its value (stored in a tuple, key is 0, value is 1)
            first_dict_pair = list(item.items())[0]
            tmp.append(f"{key}={{{first_dict_pair[0]}={json.dumps(first_dict_pair[1])}}}")

    return f"{{{', '.join(tmp)}}}"

def dict_to_score_selector(arg):
    # {scoreboardObj1: 3, scoreboardObj2: 4}
    tmp = []
    for key, item in arg.items():
        tmp.append(f"{key}={translate(item)}")   

    return f"{{{', '.join(tmp)}}}"

def translate(obj):
    from onyx.class_types import Buildable
    import enum

    if isinstance(obj, Buildable):
        return obj.build()
    elif isinstance(obj, enum.Enum):
        return obj.value
    elif obj is None:
        return ""
    else:
        return obj
