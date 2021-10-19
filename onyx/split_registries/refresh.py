import onyx
import os
import requests
import json


class NoInternetError(Exception): ...


def check_internet_connection():
    try:
        # If cloudflare is down then half the internet is already broken anyway and a connection to the internet means nothing
        requests.get("https://1.1.1.1")
    except requests.ConnectionError:
        raise NoInternetError

def create_registry(name, url):
    registry_output = ["import enum\n\n\n", f"class {name}(enum.Enum):\n", f"\t\"\"\"\n\t{name}\n\n"]
    values = requests.get(url).json()["values"]

    for item in values:
        registry_output.append(f"\t* {item.replace('minecraft:', '').replace('/', '_')}\n")
    registry_output.append("\t\"\"\"\n")

    for item in values:
        registry_output.append(f"\t{item.replace('minecraft:', '').replace('/', '_')} = \"{item}\"\n")

    with open(f"{os.path.dirname(onyx.split_registries.__file__)}{os.sep}{name}.py", "w") as registry:
        registry.write(''.join(registry_output))

def create_registry_from_literal(name, location):
    registry_output = ["import enum\n\n\n", f"class {name}(enum.Enum):\n", f"\t\"\"\"{name}\n\n"]
    values = requests.get("https://raw.githubusercontent.com/Arcensoth/mcdata/master/generated/reports/commands.json").json()["children"][location]["children"]

    for item in values:
        registry_output.append(f"\t* {item.replace('minecraft:', '').replace('/', '_')}\n")
    registry_output.append("\t\"\"\"\n")

    for item in values:
        registry_output.append(f"\t{item} = \"{item}\"\n")

    with open(f"{os.path.dirname(onyx.split_registries.__file__)}{os.sep}{name}.py", "w") as registry:
        registry.write(''.join(registry_output))

# Will likely break things, for dev use only
def update_registries(): 
    try:
        check_internet_connection()

        create_registry("biome", "https://raw.githubusercontent.com/Arcensoth/mcdata/master/processed/reports/biomes/data.json")
        create_registry("block", "https://raw.githubusercontent.com/Arcensoth/mcdata/master/processed/reports/registries/block/data.min.json")
        create_registry("block_tag", "https://raw.githubusercontent.com/Arcensoth/mcdata/master/processed/data/minecraft/tags/blocks/data.json")
        create_registry("effect", "https://raw.githubusercontent.com/Arcensoth/mcdata/master/processed/reports/registries/mob_effect/data.json")
        create_registry("enchantment", "https://raw.githubusercontent.com/Arcensoth/mcdata/master/processed/reports/registries/enchantment/data.min.json")
        create_registry("entity", "https://raw.githubusercontent.com/Arcensoth/mcdata/master/processed/reports/registries/entity_type/data.json")
        create_registry("entity_tag", "https://raw.githubusercontent.com/Arcensoth/mcdata/master/processed/data/minecraft/tags/entity_types/data.json")
        create_registry_from_literal("gamerule", "gamerule")
        create_registry("item", "https://raw.githubusercontent.com/Arcensoth/mcdata/master/processed/reports/registries/item/data.min.json")
        create_registry("item_tag", "https://raw.githubusercontent.com/Arcensoth/mcdata/master/processed/data/minecraft/tags/items/data.json")
        create_registry("particle", "https://raw.githubusercontent.com/Arcensoth/mcdata/master/processed/reports/registries/particle_type/data.min.json")
        create_registry("recipe", "https://raw.githubusercontent.com/Arcensoth/mcdata/master/processed/data/minecraft/recipes/data.json")
        create_registry_from_literal("structure", "locate")

        print("Successfully updated registries\n")

    except NoInternetError:
        print(f"There was a problem when updating the registries.\nYou are not connected to the internet. Note that this can false trigger if Cloudflare is down.\n")
    except PermissionError:
        print(f"There was a problem when updating the registries.\nThe registry files could not be written to.\n")
    except json.JSONDecodeError:
        print(f"There was a problem when updating the registries.\nThe format of the mcdata repository data has been changed and the data cannot be read.\n")
    except requests.Timeout:
        print(f"There was a problem when updating the registries.\nThe connection to the mcdata repository timed out.\n")
    except requests.ConnectionError:
        print(f"There was a problem when updating the registries.\nA connection to the mcdata repository could not be made.\n")
    except requests.InvalidURL:
        print(f"There was a problem when updating the registries.\nThe protocol for URLs has been changed and half of the internet is broken.\n")
