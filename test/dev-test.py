import json

import onyx
from nbtlib.tag import *
from onyx.dev_util import TestUnit


class DataPack(onyx.DataPack):
    def __init__(self):
        self.test_unit = TestUnit()

        super().__init__("Onyx Testing Data Pack")

        self.function("scoreboards:testing/scoreboard_players", self.scoreboard_operators_test)
        self.function("text_components:testing/main", self.text_components_test)
        self.function("commands:testing/main", self.commands_test)

        self.test_unit.print_report()

        self.generate()

    def scoreboard_operators_test(self):
        # Initalize scoreboard
        scoreboard = onyx.scoreboard("name")

        # Initalize the 3 types of players
        real_player = scoreboard.player("player_realplayer")
        hidden_player = scoreboard.player("_hiddenplayer")
        fake_player = scoreboard.player("fakeplayer")

        # Check the string representation is valid
        self.test_unit.new("Scoreboard Players Stringify Test:", [
            ("str(real_player)", str(real_player), 'realplayer name'),
            ("str(hidden_player)", str(hidden_player), '#hiddenplayer name'),
            ("str(fake_player)", str(fake_player), '$fakeplayer name')
        ])

        set_value = fake_player.set(8)
        set_value_player = fake_player.set(fake_player)
        add_value = fake_player.add(8)
        add_value_player = fake_player.add(fake_player)
        subtract_value = fake_player.subtract(8)
        subtract_value_player = fake_player.subtract(fake_player)
        multiply_value = fake_player.multiply(8)
        multiply_value_player = fake_player.multiply(fake_player)
        divide_value = fake_player.divide(8)
        divide_value_player = fake_player.divide(fake_player)
        modulo_value = fake_player.modulo(8)
        modulo_value_player = fake_player.modulo(fake_player)
        swap_value = fake_player.swap(fake_player)
        set_if_less_value = fake_player.set_if_less(8)
        set_if_less_value_player = fake_player.set_if_less(fake_player)
        set_if_greater_value = fake_player.set_if_greater(8)
        set_if_greater_value_player = fake_player.set_if_greater(fake_player)
        enable_value = fake_player.enable()
        get_value = fake_player.get()
        reset_value = fake_player.reset()

        self.test_unit.new("Scoreboard Players Operation Test:", [
            ("set_value", set_value, 'scoreboard players set $fakeplayer name 8'),
            ("set_value_player", set_value_player, 'scoreboard players operation $fakeplayer name = $fakeplayer name'),
            ("add_value", add_value, 'scoreboard players add $fakeplayer name 8'),
            ("add_value_player", add_value_player, 'scoreboard players operation $fakeplayer name += $fakeplayer name'),
            ("subtract_value", subtract_value, 'scoreboard players remove $fakeplayer name 8'),
            ("subtract_value_player", subtract_value_player, 'scoreboard players operation $fakeplayer name -= $fakeplayer name'),
            ("multiply_value", multiply_value, 'scoreboard players operation $fakeplayer name *= $8 onyx.const'),
            ("multiply_value_player", multiply_value_player, 'scoreboard players operation $fakeplayer name *= $fakeplayer name'),
            ("divide_value", divide_value, 'scoreboard players operation $fakeplayer name /= $8 onyx.const'),
            ("divide_value_player", divide_value_player, 'scoreboard players operation $fakeplayer name /= $fakeplayer name'),
            ("modulo_value", modulo_value, 'scoreboard players operation $fakeplayer name %= $8 onyx.const'),
            ("modulo_value_player", modulo_value_player, 'scoreboard players operation $fakeplayer name %= $fakeplayer name'),
            ("swap_value", swap_value, 'scoreboard players operation $fakeplayer name >< $fakeplayer name'),
            ("set_if_less_value", set_if_less_value, 'scoreboard players operation $fakeplayer name < $8 onyx.const'),
            ("set_if_less_value_player", set_if_less_value_player, 'scoreboard players operation $fakeplayer name < $fakeplayer name'),
            ("set_if_greater_value", set_if_greater_value, 'scoreboard players operation $fakeplayer name > $8 onyx.const'),
            ("set_if_greater_value_player", set_if_greater_value_player, 'scoreboard players operation $fakeplayer name > $fakeplayer name'),
            ("enable_value", enable_value, 'scoreboard players enable $fakeplayer name'),
            ("get_value", get_value, 'scoreboard players get $fakeplayer name'),
            ("reset_value", reset_value, 'scoreboard players reset $fakeplayer name')
        ])

    def text_components_test(self):
        main_component = onyx.TextComponent().part(
            text="pls",
            translate="translate:string",
            with_=["monkey", "ape"],
            score={
                "objective": "objective",
                "name": "player",  # Use "*" for viewing player
                "value": 30
            },
            selector=onyx.selector(onyx.selector_type.all_players),
            keybind=onyx.keybind.advancements,
            nbt="NBT.Path",
            interpret=True,
            block=(3, "~", "17"),
            entity="@a",
            storage="storage:location",
            extra=onyx.TextComponent().part(text="extra_component", color="#328128"),
            color=onyx.color.blue,
            font="minecraft:default",
            bold=True,
            italic=True,
            underlined=True,
            strikethrough=True,
            obfuscated=False,
            insertion="Hello!"
        )

        click_event_component = onyx.TextComponent().part(
            text="Click me to change page\n",
            click_event=onyx.ClickEvent(
                onyx.click_event_action.change_page, "3")
        ).part(
            text="Click me to copy to clipboard\n",
            click_event=onyx.ClickEvent(
                onyx.click_event_action.copy_to_clipboard, "This is what is in your clipboard")
        ).part(
            text="Click me to open URL\n",
            click_event=onyx.ClickEvent(
                onyx.click_event_action.open_url, "https://doublef3lix.github.io")
        ).part(
            text="Click me to run command\n",
            click_event=onyx.ClickEvent(
                onyx.click_event_action.run_command, "/say Hello"),
        ).part(
            text="Click me to suggest command",
            click_event=onyx.ClickEvent(
                onyx.click_event_action.suggest_command, "/say Hello")
        )

        hover_event_component = onyx.TextComponent().part(
            text="Hover over me to show text\n",
            hover_event=onyx.HoverEvent(
                onyx.hover_event_action.show_text, text="Hello")
        ).part(
            text="Hover over me to show an item with NBT\n",
            hover_event=onyx.HoverEvent(
                onyx.hover_event_action.show_item, item_id="minecraft:light_blue_glazed_terracotta")
        ).part(
            text="Hover over me to show an item with NBT",
            hover_event=onyx.HoverEvent(
                onyx.hover_event_action.show_item,
                item_id="minecraft:netherite_chestplate",
                item_tags={
                    "display": Compound({
                        "Name": String(
                            json.dumps({
                                "text": "Hi"
                            })
                        )
                    })
                }
            )
        )

        index_component = onyx.TextComponent().part(
            text="Part1"
        ).part(
            text="Part2"
        ).part(
            text="Part3"
        )

        dict_component = onyx.TextComponent().part(
            dict = {
                "text": "pls",
                "translate": "translate:string",
                "with_": ["monkey", "ape"],
                "score": {
                    "objective": "objective",
                    "name": "player",  # Use "*" for viewing player
                    "value": 30
                },
                "selector": onyx.selector(onyx.selector_type.all_players),
                "keybind": onyx.keybind.advancements,
                "nbt": "NBT.Path",
                "interpret": True,
                "block": (3, "~", "17"),
                "entity": "@a",
                "storage": "storage:location",
                "extra": onyx.TextComponent().part(text="extra_component", color="#328128"),
                "color": onyx.color.blue,
                "font": "minecraft:default",
                "bold": True,
                "italic": True,
                "underlined": True,
                "strikethrough": True,
                "obfuscated": False,
                "insertion": "Hello!"
            }
        )

        self.test_unit.new("Text-Components Test:", [
            ("main_component.build()", main_component.build(), """["", {"text": "pls", "translate": "translate:string", "with_": ["monkey", "ape"], "score": {"objective": "objective", "name": "player", "value": 30}, "selector": "@a", "keybind": "advancements", "nbt": "NBT.Path", "interpret": true, "block": [3, "~", "17"], "entity": "@a", "storage": "storage:location", "extra": [{"text": "extra_component", "color": "#328128"}], "color": "blue", "font": "minecraft:default", "bold": true, "italic": true, "underlined": true, "strikethrough": true, "obfuscated": false, "insertion": "Hello!"}]"""),
            ("click_event_component.build()", click_event_component.build(), """["", {"text": "Click me to change page\\n", "clickEvent": {"action": "change_page", "value": "3"}}, {"text": "Click me to copy to clipboard\\n", "clickEvent": {"action": "copy_to_clipboard", "value": "This is what is in your clipboard"}}, {"text": "Click me to open URL\\n", "clickEvent": {"action": "open_url", "value": "https://doublef3lix.github.io"}}, {"text": "Click me to run command\\n", "clickEvent": {"action": "run_command", "value": "/say Hello"}}, {"text": "Click me to suggest command", "clickEvent": {"action": "suggest_command", "value": "/say Hello"}}]"""),
            ("hover_event_component.build()", hover_event_component.build(), """["", {"text": "Hover over me to show text\\n", "hoverEvent": {"action": "show_text", "contents": "Hello"}}, {"text": "Hover over me to show an item with NBT\\n", "hoverEvent": {"action": "show_item", "contents": {"id": "minecraft:light_blue_glazed_terracotta", "count": 1}}}, {"text": "Hover over me to show an item with NBT", "hoverEvent": {"action": "show_item", "contents": {"id": "minecraft:netherite_chestplate", "count": 1, "tag": "{display: {Name: '{\\"text\\": \\"Hi\\"}'}}"}}}]"""),
            ("index_component[1]", index_component[1], """{"text": "Part2"}"""),
            ("dict_component.build()", dict_component.build(), """["", {"text": "pls", "translate": "translate:string", "with_": ["monkey", "ape"], "score": {"objective": "objective", "name": "player", "value": 30}, "selector": "@a", "keybind": "advancements", "nbt": "NBT.Path", "interpret": true, "block": [3, "~", "17"], "entity": "@a", "storage": "storage:location", "extra": [{"text": "extra_component", "color": "#328128"}], "color": "blue", "font": "minecraft:default", "bold": true, "italic": true, "underlined": true, "strikethrough": true, "obfuscated": false, "insertion": "Hello!"}]""")
        ])

    def commands_test(self):
        gamemode_cmd = onyx.commands.gamemode(onyx.gamemode.creative, "@a")
        tellraw_cmd = onyx.commands.tellraw("@a", onyx.TextComponent().part(text="Dummy"))

        self.test_unit.new("Commands Test:", [
            ("gamemode_cmd", gamemode_cmd, """gamemode creative @a"""),
            ("tellraw_cmd", tellraw_cmd, """tellraw @a ["", {"text": "Dummy"}]""")
        ])


DataPack()