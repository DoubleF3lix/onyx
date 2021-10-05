import json
import onyx
from nbtlib.tag import *


class DataPack(onyx.DataPack):
    def __init__(self):
        super().__init__("Onyx Testing Data Pack")

        self.function("commands:testing/main", self.commands_test)
        self.function("execute:testing/main", self.execute_test)
        self.function("scoreboards:testing/scoreboard_players", self.scoreboard_operators_test)
        self.function("text_components:testing/main", self.text_components_test)

        # TODO add libs (new format)
        #onyx.update_registries()

        self.generate()

    def scoreboard_operators_test(self):
        # Initalize scoreboard
        scoreboard = onyx.scoreboard("name")

        # Initalize the 3 types of players
        real_player = scoreboard.player("player_realplayer")
        hidden_player = scoreboard.player("_hiddenplayer")
        fake_player = scoreboard.player("fakeplayer")

        # Initalize operators
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

        # Test string conversion
        assert str(real_player) == "realplayer name"
        assert str(hidden_player) == "#hiddenplayer name"
        assert str(fake_player) == "$fakeplayer name"

        assert set_value == "scoreboard players set $fakeplayer name 8"
        assert set_value_player == "scoreboard players operation $fakeplayer name = $fakeplayer name"
        assert add_value == "scoreboard players add $fakeplayer name 8"
        assert add_value_player == "scoreboard players operation $fakeplayer name += $fakeplayer name"
        assert subtract_value == "scoreboard players remove $fakeplayer name 8"
        assert subtract_value_player == "scoreboard players operation $fakeplayer name -= $fakeplayer name"
        assert multiply_value == "scoreboard players operation $fakeplayer name *= $8 onyx.const"
        assert multiply_value_player == "scoreboard players operation $fakeplayer name *= $fakeplayer name"
        assert divide_value == "scoreboard players operation $fakeplayer name /= $8 onyx.const"
        assert divide_value_player == "scoreboard players operation $fakeplayer name /= $fakeplayer name"
        assert modulo_value == "scoreboard players operation $fakeplayer name %= $8 onyx.const"
        assert modulo_value_player == "scoreboard players operation $fakeplayer name %= $fakeplayer name"
        assert swap_value == "scoreboard players operation $fakeplayer name >< $fakeplayer name"
        assert set_if_less_value == "scoreboard players operation $fakeplayer name < $8 onyx.const"
        assert set_if_less_value_player == "scoreboard players operation $fakeplayer name < $fakeplayer name"
        assert set_if_greater_value == "scoreboard players operation $fakeplayer name > $8 onyx.const"
        assert set_if_greater_value_player == "scoreboard players operation $fakeplayer name > $fakeplayer name"
        assert enable_value == "scoreboard players enable $fakeplayer name"
        assert get_value == "scoreboard players get $fakeplayer name"
        assert reset_value == "scoreboard players reset $fakeplayer name"

    def text_components_test(self):
        main_component = onyx.text_component().part(
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
            extra=[
                onyx.text_component().part(text="extra_component", color="#328128"),
                onyx.text_component().part(text="extra_component2", color="#518923")
            ],
            color=onyx.color.blue,
            font="minecraft:default",
            bold=True,
            italic=True,
            underlined=True,
            strikethrough=True,
            obfuscated=False,
            insertion="Hello!"
        )

        click_event_component = onyx.text_component().part(
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

        hover_event_component = onyx.text_component().part(
            text="Hover over me to show text\n",
            hover_event=onyx.HoverEvent(onyx.hover_event_action.show_text, text="Hello")
        ).part(
            text="Hover over me to show an item with NBT\n",
            hover_event=onyx.HoverEvent(onyx.hover_event_action.show_item, item_id="minecraft:light_blue_glazed_terracotta")
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

        index_component = onyx.text_component().part(
            text="Part1"
        ).part(
            text="Part2"
        ).part(
            text="Part3"
        )

        dict_component = onyx.text_component().part(
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
                "extra": [onyx.text_component().part(text="extra_component", color="#328128")],
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

        assert main_component.build() == """["", {"text": "pls", "translate": "translate:string", "with": ["monkey", "ape"], "score": {"objective": "objective", "name": "player", "value": 30}, "selector": "@a", "keybind": "key.advancements", "nbt": "NBT.Path", "interpret": true, "block": "3 ~ 17", "entity": "@a", "storage": "storage:location", "extra": [[{"text": "extra_component", "color": "#328128"}], [{"text": "extra_component2", "color": "#518923"}]], "color": "blue", "font": "minecraft:default", "bold": true, "italic": true, "underlined": true, "strikethrough": true, "insertion": "Hello!"}]"""
        assert click_event_component.build() == """["", {"text": "Click me to change page\\n", "clickEvent": {"action": "change_page", "value": "3"}}, {"text": "Click me to copy to clipboard\\n", "clickEvent": {"action": "copy_to_clipboard", "value": "This is what is in your clipboard"}}, {"text": "Click me to open URL\\n", "clickEvent": {"action": "open_url", "value": "https://doublef3lix.github.io"}}, {"text": "Click me to run command\\n", "clickEvent": {"action": "run_command", "value": "/say Hello"}}, {"text": "Click me to suggest command", "clickEvent": {"action": "suggest_command", "value": "/say Hello"}}]"""
        assert hover_event_component.build() == """["", {"text": "Hover over me to show text\\n", "hoverEvent": {"action": "show_text", "contents": "Hello"}}, {"text": "Hover over me to show an item with NBT\\n", "hoverEvent": {"action": "show_item", "contents": {"id": "minecraft:light_blue_glazed_terracotta", "count": 1}}}, {"text": "Hover over me to show an item with NBT", "hoverEvent": {"action": "show_item", "contents": {"id": "minecraft:netherite_chestplate", "count": 1, "tag": "{display: {Name: '{\\"text\\": \\"Hi\\"}'}}"}}}]"""
        assert index_component[1] == """{"text": "Part2"}"""
        assert dict_component.build() == """["", {"text": "pls", "translate": "translate:string", "with": ["monkey", "ape"], "score": {"objective": "objective", "name": "player", "value": 30}, "selector": "@a", "keybind": "key.advancements", "nbt": "NBT.Path", "interpret": true, "block": "3 ~ 17", "entity": "@a", "storage": "storage:location", "extra": [[{"text": "extra_component", "color": "#328128"}]], "color": "blue", "font": "minecraft:default", "bold": true, "italic": true, "underlined": true, "strikethrough": true, "insertion": "Hello!"}]"""

    def execute_test(self):
        # These functions have to be checked for manually
        onyx.commands.say("before function1")
        with onyx.execute().as_at("@s"):
            onyx.commands.say("function1")

            with onyx.execute().as_at("@s"):
                onyx.commands.say("in function1, function2")

        with onyx.execute().as_at("@s"):
            onyx.commands.say("function3")
        onyx.commands.say("after function3")

        # unless isn't tested since it uses the exact same system as if, so if if works, unless does too
        if_block_cmd = onyx.execute().if_.block("~ ~ ~", "minecraft:stone").build()
        if_blocks_cmd = onyx.execute().if_.blocks("~ ~ ~", "~ ~1 ~", "~ ~ ~1", onyx.execute_blocks_mask.all).build()
        if_data_cmd = onyx.execute().if_.data(onyx.source_type.block, "~ ~ ~", "Path").build()
        if_entity_cmd = onyx.execute().if_.entity("@a").build()
        if_predicate_cmd = onyx.execute().if_.predicate("namespace:predicate").build()
        
        dummy_scoreboard = onyx.scoreboard("objective")
        dummy_player1 = dummy_scoreboard.player("player1")
        dummy_player2 = dummy_scoreboard.player("player2")
        if_score_eq_cmd = onyx.execute().if_.score(dummy_player1 == dummy_player2).build()
        if_score_gt_eq_cmd = onyx.execute().if_.score(dummy_player1 >= dummy_player2).build()
        if_score_gt_cmd = onyx.execute().if_.score(dummy_player1 > dummy_player2).build()
        if_score_lt_eq_cmd = onyx.execute().if_.score(dummy_player1 <= dummy_player2).build()
        if_score_lt_cmd = onyx.execute().if_.score(dummy_player1 < dummy_player2).build()
        if_score_matches_cmd = onyx.execute().if_.score(dummy_player1 == onyx.Range(7, 18)).build()

        # success store isn't tested since it uses the exact same system as result store, so if result store works, success does too
        store_result_block_cmd = onyx.execute().store.result.block("~ ~ ~", "Path", onyx.data_type.byte, 0.1).build()
        store_result_bossbar_cmd = onyx.execute().store.result.bossbar("minecraft:bossbar", onyx.bossbar_location.max).build()
        store_result_entity_cmd = onyx.execute().store.result.entity("@s", "Path", onyx.data_type.byte, 0.1).build()
        store_result_score_cmd = onyx.execute().store.result.score(onyx.scoreboard("objective").player("player")).build()
        store_result_storage_cmd = onyx.execute().store.result.storage("storage:namespace", "Path", onyx.data_type.byte, 0.1).build()

        rest_param_cmd = onyx.execute(
        ).align(onyx.axis.x
        ).align([onyx.axis.x, onyx.axis.y]
        ).anchored(onyx.anchor.eyes
        ).as_("@a"
        ).at("@s"
        ).as_at("@s"
        ).facing(onyx.AbsPos(3, 4, 5)
        ).facing("@s", onyx.anchor.feet
        ).positioned(onyx.AbsPos(3, 4, 5)
        ).positioned("@s"
        ).rotated(onyx.AbsRot(6, 7)
        ).rotated("@s"
        ).build()

        assert if_block_cmd == "if block ~ ~ ~ minecraft:stone"
        assert if_blocks_cmd == "if blocks ~ ~ ~ ~ ~1 ~ ~ ~ ~1 all"
        assert if_data_cmd == "if data block ~ ~ ~ Path"
        assert if_entity_cmd == "if entity @a"
        assert if_predicate_cmd == "if predicate namespace:predicate"
        assert if_score_eq_cmd == "if score $player1 objective = $player2 objective"
        assert if_score_gt_eq_cmd == "if score $player1 objective >= $player2 objective"
        assert if_score_gt_cmd == "if score $player1 objective > $player2 objective"
        assert if_score_lt_eq_cmd == "if score $player1 objective <= $player2 objective"
        assert if_score_lt_cmd == "if score $player1 objective < $player2 objective"
        assert if_score_matches_cmd == "if score $player1 objective matches 7..18"
        assert store_result_block_cmd == "store result block ~ ~ ~ Path byte 0.1"
        assert store_result_bossbar_cmd == "store result bossbar minecraft:bossbar max"
        assert store_result_entity_cmd == "store result entity @s Path byte 0.1"
        assert store_result_score_cmd == "store result score $player objective"
        assert store_result_storage_cmd == "store result storage storage:namespace Path byte 0.1"
        assert rest_param_cmd == "align x align xy anchored eyes as @a at @s as @s at @s facing 3 4 5 facing entity @s feet positioned 3 4 5 positioned as @s rotated 6 7 rotated as @s"
        
    def commands_test(self):
        clear_cmd = onyx.commands.clear("@a", onyx.item.anvil, 64)
        difficulty_cmd = onyx.commands.difficulty(onyx.difficulty.easy)
        gamemode_cmd = onyx.commands.gamemode(onyx.gamemode.creative, "@a")
        say_cmd = onyx.commands.say("Dummy")
        tellraw_cmd = onyx.commands.tellraw("@a", onyx.text_component().part(text="Dummy"))

        assert clear_cmd == "clear @a minecraft:anvil 64"
        assert difficulty_cmd == "difficulty easy"
        assert gamemode_cmd == "gamemode creative @a"
        assert say_cmd == "say Dummy"
        assert tellraw_cmd == """tellraw @a ["", {"text": "Dummy"}]"""


DataPack()
