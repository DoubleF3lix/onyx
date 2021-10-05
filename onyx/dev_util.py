import json
import re
import nbtlib


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
    return "_".join(re.sub(r'[^a-zA-Z0-9_]', '', q.lower()) for q in text.split(" "))

def camelify(text):
    return ''.join(q.lower().capitalize() if i != 0 else q.lower() for i, q in enumerate(re.sub("[^a-z0-9 ]", "", text.replace("_", " ").lower()).split(" ")))

def dict_to_advancement_selector(arg):
    # {"thing/1": {"thing/12": True}, "thing/2": False}
    q = []
    for key, item in arg.items():
        if isinstance(item, bool):
            q.append(f"{key}={json.dumps(item)}")   
        # Assume type is dictionary
        else:
            # Grab only the first key and its value (stored in a tuple, key is 0, value is 1)
            first_dict_pair = list(item.items())[0]
            q.append(f"{key}={{{first_dict_pair[0]}={json.dumps(first_dict_pair[1])}}}")

    return f"{{{', '.join(q)}}}"

def dict_to_score_selector(arg):
    # {scoreboardObj1: 3, scoreboardObj2: 4}
    q = [f"{key}={translate(item)}" for key, item in arg.items()]
    return f"{{{', '.join(q)}}}"

def translate(obj, json_dump_elements=False, normalize_boolean=False):
    import enum
    from onyx.class_types import Buildable
    from onyx.scoreboard import Player

    if isinstance(obj, Buildable):
        return obj.build()
    elif isinstance(obj, enum.Enum):
        return obj.value
    elif isinstance(obj, (list, tuple)):
        if json_dump_elements == True:
            return [json.dumps(translate(element)) for element in obj]
        else:
            return " ".join(str(translate(element)) for element in obj)
    elif obj is None:
        return ""
    elif isinstance(obj, Player):
        return str(obj)
    elif isinstance(obj, bool) and normalize_boolean == True:
        return json.dumps(obj)
    elif isinstance(obj, nbtlib.Base):
        return obj.snbt()
    else:
        return obj

def convert_experience_amount(amount):
    xp_type = "levels"
    if isinstance(amount, str):
        amount = amount.lower()
        if amount.endswith("p"):
            xp_type = "points"
        if not amount.isdigit():
            amount = amount[:-1]
    return (amount, xp_type)

def add_scoreboard(objective, criteria="dummy"):
    from onyx.commands import Commands

    if objective not in Commands.added_scoreboards:
        Commands.added_scoreboards.append(objective)
        return Commands.push(f"scoreboard objectives add {objective} {criteria}", init=True)

def convert_scoreboard_player_name(name):
    from onyx.scoreboard import Player

    if isinstance(name, Player):
        name = name.name

    if isinstance(name, str):
        if name.startswith("player_"):
            name = name[7:]
        elif name.startswith("_"):
            name = f"#{name[1:]}"
        else:
            name = f"${name}"
    return translate(name)

def get_integer_count_at_string_end(string):
    string = str(string)[::-1]
    for char_index in range(len(string)):
        if not string[char_index].isdigit():
            return char_index

def dict_to_block_state(dict):
    return f"[{','.join([f'{key}={value}' for key, value in dict.items()])}]"

def convert_time(string):
    if isinstance(string, int):
        return f"{string}t"
    elif string.endswith("m"):
        return f"{int(string[:-1]) * 60}s"
    elif string.endswith("h"):
        return f"{int(string[:-1]) * 3600}s"
    elif string.endswith("m"):
        return f"{int(string[:-1]) * 30}d"
    else:
        return string
