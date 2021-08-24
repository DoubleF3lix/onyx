import json
import re


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
    return ''.join(
        q.lower().capitalize() if i != 0 else q.lower()
        for i, q in enumerate(
            re.sub("[^a-z0-9 ]", "", text.replace("_", " ").lower()).split(" ")
        )
    )

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
    tmp = [f"{key}={translate(item)}" for key, item in arg.items()]
    return f"{{{', '.join(tmp)}}}"

def translate(obj):
    import enum
    from onyx.class_types import Buildable
    from onyx.scoreboard import Player

    if isinstance(obj, Buildable):
        return obj.build()
    elif isinstance(obj, enum.Enum):
        return obj.value
    elif obj is None:
        return ""
    elif isinstance(obj, Player):
        return str(obj)
    else:
        return obj

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


class TestUnit:
    def __init__(self):
        print()

        self.total_test_count = 0
        self.successful_tests = 0
        self.failed_tests = []

        self.report = []

    def print_report(self):
        print('\n'.join(self.report))
        print(f"Total Tests Passed: {self.successful_tests}/{self.total_test_count}")
        if self.successful_tests < self.total_test_count:
            print("Failed Test Groups:")
            print(''.join(q[:-1] for q in self.failed_tests))
        print()

    def new(self, title, conditions):
        self.report.append(title)

        successes = 0
        status_table = ["X", "✓"]
        status = 0

        largest_condition = max((len(q[0]) + len(q[2])) for q in conditions)

        for condition in conditions:
            if condition[1] == condition[2]:
                successes += 1
                status = 1
            else:
                print(condition[1] + "\n" + condition[2] + "\n")

            report_line = f"{condition[0]} == '{condition[2]}': {' ' * (largest_condition - (len(condition[0]) + len(condition[2])) + 5)} {status_table[status]}"
            if status == 0:
                report_line += f"{' ' * 4}Got Value: '{condition[2]}'"
            self.report.append(report_line)
            status = 0

        self.total_test_count += len(conditions)
        self.successful_tests += successes

        if successes < len(conditions):
            self.failed_tests.append(title)

        self.report.append(f"Tests Passed: {successes}/{len(conditions)}")
        self.report.append("=" * 40)

        return successes
