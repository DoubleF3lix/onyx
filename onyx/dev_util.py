import re
import onyx.selector

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

def translate(obj):
    if isinstance(obj, onyx.selector.Selector):
        return obj.build()