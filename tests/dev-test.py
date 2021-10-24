import json
import os

import onyx
from nbtlib.tag import *


class DataPack(onyx.DataPack):
    def __init__(self):
        super().__init__("Onyx Testing Data Pack")

        self.q = self.function("testing:blank", print)
        self.function("testing:commands", self.commands_test)
        self.function("testing:misc", self.misc_test)
        self.function("testing:execute", self.execute_test)
        self.function("testing:scoreboard_operators", self.scoreboard_operators_test)
        self.function("testing:text_components", self.text_components_test)

        self.function(
            "testing:direct_string_insertion",
            "say Hello, World!\nsay This is a function!",
        )
        self.function("testing:indirect_string_insertion", self.write_string)

        self.generate(print_generation_time=True)

        self.after_file_check()

    def write_string(self):
        return """
        say Hello, World!
        say This is a function!
        """

    def after_file_check(self):
        src = os.path.join(
            os.path.dirname(os.path.dirname(onyx.__file__)),
            "Onyx Testing Data Pack",
        )
        with open(
            os.path.join(src, "pack.mcmeta"),
            "r",
        ) as infile:
            assert (
                infile.read()
                == """{\n  "pack": {\n    "pack_format": 7,\n    "description": "Data Pack"\n  }\n}\n"""
            )

        with open(
            os.path.join(src, "data", "testing", "functions", "commands.mcfunction"),
            "r",
        ) as infile:
            assert (
                infile.read()
                == """advancement revoke @a everything\nadvancement revoke @a from fake:advancement\nadvancement grant @a through fake:advancement\nattribute @s minecraft:generic.armor modifier add 1-1-1-1-1 modifier_name 3 multiply\nattribute @s minecraft:generic.armor base set 3\nattribute @s minecraft:generic.armor modifier value get 1-1-1-1-1 3\nattribute @s minecraft:generic.armor modifier remove 1-1-1-1-1\nclear @a minecraft:anvil 64\nclone 0 0 0 1 1 1 2 2 2 filtered minecraft:acacia_button[facing=east]{NBT: 1b} move\ndefaultgamemode adventure\ndifficulty easy\nenchant @s minecraft:aqua_affinity 1\nenchant @s minecraft:aqua_affinity 3\nenchant @s minecraft:binding_curse 1\nfill 0 0 0 1 1 1 minecraft:acacia_sapling replace minecraft:acacia_planks\ngamemode creative @a\ngamerule announceAdvancements true\ngive @s minecraft:stone{CustomModelData: 1b, display: {Lore: [\'["", {"text": "line1"}]\']}} 3\nhelp\nhelp help\nkill @s\nexecute as @e[type=pig] run data merge entity @s {Health:0.0f,DeathTime:19s,DeathLootTable:"minecraft:empty"}\nlist\nlist uuids\nlocate bastion_remnant\nlocatebiome minecraft:badlands\nme is tired of writing tests and documentation\nmsg @a hiya\nparticle minecraft:crit 0 0 0 3 2 1 1.5 12 normal @a\nparticle minecraft:dust 10 11 12 5 0 0 0 3 2 1 1.5 12 force @a\nparticle minecraft:block minecraft:bedrock 0 0 0 3 2 1 1.5 12 force @a\nparticle minecraft:item minecraft:birch_sign 0 0 0 3 2 1 1.5 12 force @a\nparticle minecraft:ambient_entity_effect 0 0 0 128 19 12 64 0 normal @s\nparticle minecraft:bubble 0 0 0 3 0 0 2 0 force @a\nparticle minecraft:note 0 0 0 0.56 0 0 17 0 force @p\nplaysound minecraft:ambient.basalt_deltas.additions master @a 0 255 0 2147483647 2\nsay Dummy\nseed\nsetblock 5 5 5 minecraft:acacia_slab destroy\nsetworldspawn 0 64 0 160\nspawnpoint @a 0 64 0 36\ngamemode spectator @s\nspectate @e[type=cow,limit=1] @s\nspreadplayers 16 16 12 20 under 74 true @a\nstopsound @r * minecraft:block.ancient_debris.break\nsummon minecraft:cat 0 255 0 {Health: 34.0f}\nteammsg I am very much on your team :)\nteleport @a 0 256 0\nteleport @a @s\nteleport @e 0 0 0\ntellraw @a ["", {"text": "Dummy"}]\nweather clear 40\nbossbar list\nbossbar get namespace:bossbar_id max\nbossbar remove namespace:bossbar_id\nbossbar set namespace:bossbar_id value 12\neffect clear @s minecraft:absorption\neffect clear @s minecraft:absorption\neffect clear @s minecraft:water_breathing\neffect give @s minecraft:absorption 30 1 true\ndata get entity @s path\ndata merge storage storage:namespace {Wow: "NBT"}\ndata modify entity @s path insert 1 from entity @s path\ndata remove entity @s path\ndatapack disable onyx_testing_data_pack\ndatapack enable onyx_testing_data_pack after onyx_testing_data_pack\ndatapack list\ndebug function testing:blank\ndebug start\ndebug stop\nexperience add @s 7 levels\nexperience add @a -2147483647 levels\nexperience query @s points\nexperience set @s 8 points\nforceload add 1 1 1 1\nforceload query 1 1\nforceload remove 1 1 2 2\nforceload remove all\nitem modify entity @s path item:modifier\nitem replace entity @s path from entity @s path\nloot give @s fish minecraft:empty 1 1 1\nloot insert 3 3 3 kill @s\nloot replace entity @s container.0 mine 3 3 3 mainhand\nloot spawn 0 0 0 loot minecraft:empty\nperf start\nperf stop\nrecipe give @a *\nrecipe take @a *\nschedule clear testing:blank\nschedule function testing:blank 21d append\nscoreboard players list @a[tag=amonguslol]\nscoreboard players reset @a\nscoreboard objectives list\ntag @a add ivebeenwritingtestsfor2hourspleasehelpme\ntag @a list\ntag @a remove itswildhowlongyoucanmaketagsimeanthisisabsurdlikeicouldputtheentirescriptofhalmetinthisbabyandnothingwouldstopmeisntthatgloriousithoughtsobutalsowhyintheheckwouldanyoneevermakeatagthislonglikethisiscompletelybonkersbutitsprettyhilariousthatyoucanevendothisiknowtheyremovedthelimitsforscoreboardobjectivesandteamnameswhichisamazingbecausescoreboardobjectivescanactuallycontainalotofinformationlikenamespaceentitypurposeetcbutwhyonearthwouldyouneedatagthislongimeanitskindofinsanebutstillfunnyanywaymomsaiddinnerisreadywerehavingpotatosoupsoimgonnagohaveanicedaythankssigneddoublefelix\nteam add writingsomethingthismonotonehasbrokenme\nteam empty likeitsnotlikethisisntuseful\nteam join buttheresnothingnewitsjusttestaftertest @a\nteam leave @a\nteam list\nteam modify team collisionRule never\nteam remove nevergonnagiveyouupnevergonnaletyoudown\ntime add 3000\ntime query daytime\ntime set 288000\ntitle @a actionbar ["", {"text": "I really should\'ve just done \'import onyx.commands as _\', but oh well..."}]\ntitle @a clear\ntitle @a reset\ntitle @a subtitle "too lazy to make an object lol"\ntitle @a times 0 0 0\ntitle @a title "you\'ll never see this because of instant times"\ntrigger name add 3\ntrigger youllneverseeitcoming set 3\nworldborder add 30 1\nworldborder center 12 12\nworldborder damage amount 3\nworldborder damage buffer 19\nworldborder get\nworldborder set 12 19\nworldborder warning distance 12\nworldborder warning time 9\n"""
            )

        with open(
            os.path.join(src, "data", "testing", "functions", "execute.mcfunction"), "r"
        ) as infile:
            assert (
                infile.read()
                == """say before function1\nexecute as @s at @s run function testing:execute/generated1\nexecute as @s at @s run function testing:execute/generated2\nsay after function3\nsay Hello\nexecute as @a at @s run say Hello\n"""
            )

        with open(
            os.path.join(
                src, "data", "testing", "functions", "scoreboard_operators.mcfunction"
            ),
            "r",
        ) as infile:
            assert (
                infile.read()
                == """scoreboard players set $fakeplayer name 8\nscoreboard players operation $fakeplayer name = $fakeplayer name\nscoreboard players add $fakeplayer name 8\nscoreboard players operation $fakeplayer name += $fakeplayer name\nscoreboard players remove $fakeplayer name 8\nscoreboard players operation $fakeplayer name -= $fakeplayer name\nscoreboard players operation $fakeplayer name *= $8 onyx.const\nscoreboard players operation $fakeplayer name *= $fakeplayer name\nscoreboard players operation $fakeplayer name /= $8 onyx.const\nscoreboard players operation $fakeplayer name /= $fakeplayer name\nscoreboard players operation $fakeplayer name %= $8 onyx.const\nscoreboard players operation $fakeplayer name %= $fakeplayer name\nscoreboard players operation $fakeplayer name >< $fakeplayer name\nscoreboard players operation $fakeplayer name < $8 onyx.const\nscoreboard players operation $fakeplayer name < $fakeplayer name\nscoreboard players operation $fakeplayer name > $8 onyx.const\nscoreboard players operation $fakeplayer name > $fakeplayer name\nscoreboard players enable $fakeplayer name\nscoreboard players get $fakeplayer name\nscoreboard players reset $fakeplayer name\n"""
            )

        with open(
            os.path.join(
                src,
                "data",
                "testing",
                "functions",
                "direct_string_insertion.mcfunction",
            ),
            "r",
        ) as infile:
            assert infile.read() == "say Hello, World!\nsay This is a function!\n"

        with open(
            os.path.join(
                src,
                "data",
                "testing",
                "functions",
                "indirect_string_insertion.mcfunction",
            ),
            "r",
        ) as infile:
            assert infile.read() == "say Hello, World!\nsay This is a function!\n"

        with open(
            os.path.join(src, "data", "testing", "advancements", "advancement.json"),
            "r",
        ) as infile:
            assert infile.read() == "{}\n"

    def misc_test(self):
        assert str(self) == "onyx_testing_data_pack"
        self.advancement("testing:advancement", {})

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

        assert str(real_player) == "realplayer name"
        assert str(hidden_player) == "#hiddenplayer name"
        assert str(fake_player) == "$fakeplayer name"

        assert set_value == "scoreboard players set $fakeplayer name 8"
        assert (
            set_value_player
            == "scoreboard players operation $fakeplayer name = $fakeplayer name"
        )
        assert add_value == "scoreboard players add $fakeplayer name 8"
        assert (
            add_value_player
            == "scoreboard players operation $fakeplayer name += $fakeplayer name"
        )
        assert subtract_value == "scoreboard players remove $fakeplayer name 8"
        assert (
            subtract_value_player
            == "scoreboard players operation $fakeplayer name -= $fakeplayer name"
        )
        assert (
            multiply_value
            == "scoreboard players operation $fakeplayer name *= $8 onyx.const"
        )
        assert (
            multiply_value_player
            == "scoreboard players operation $fakeplayer name *= $fakeplayer name"
        )
        assert (
            divide_value
            == "scoreboard players operation $fakeplayer name /= $8 onyx.const"
        )
        assert (
            divide_value_player
            == "scoreboard players operation $fakeplayer name /= $fakeplayer name"
        )
        assert (
            modulo_value
            == "scoreboard players operation $fakeplayer name %= $8 onyx.const"
        )
        assert (
            modulo_value_player
            == "scoreboard players operation $fakeplayer name %= $fakeplayer name"
        )
        assert (
            swap_value
            == "scoreboard players operation $fakeplayer name >< $fakeplayer name"
        )
        assert (
            set_if_less_value
            == "scoreboard players operation $fakeplayer name < $8 onyx.const"
        )
        assert (
            set_if_less_value_player
            == "scoreboard players operation $fakeplayer name < $fakeplayer name"
        )
        assert (
            set_if_greater_value
            == "scoreboard players operation $fakeplayer name > $8 onyx.const"
        )
        assert (
            set_if_greater_value_player
            == "scoreboard players operation $fakeplayer name > $fakeplayer name"
        )
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
                "value": 30,
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
                onyx.text_component().part(text="extra_component2", color="#518923"),
            ],
            color=onyx.color.blue,
            font="minecraft:default",
            bold=True,
            italic=True,
            underlined=True,
            strikethrough=True,
            obfuscated=False,
            insertion="Hello!",
        )

        click_event_component = (
            onyx.text_component()
            .part(
                text="Click me to change page\n",
                click_event=onyx.ClickEvent(onyx.click_event_action.change_page, "3"),
            )
            .part(
                text="Click me to copy to clipboard\n",
                click_event=onyx.ClickEvent(
                    onyx.click_event_action.copy_to_clipboard,
                    "This is what is in your clipboard",
                ),
            )
            .part(
                text="Click me to open URL\n",
                click_event=onyx.ClickEvent(
                    onyx.click_event_action.open_url, "https://doublef3lix.github.io"
                ),
            )
            .part(
                text="Click me to run command\n",
                click_event=onyx.ClickEvent(
                    onyx.click_event_action.run_command, "/say Hello"
                ),
            )
            .part(
                text="Click me to suggest command",
                click_event=onyx.ClickEvent(
                    onyx.click_event_action.suggest_command, "/say Hello"
                ),
            )
        )

        hover_event_component = (
            onyx.text_component()
            .part(
                text="Hover over me to show text\n",
                hover_event=onyx.HoverEvent(
                    onyx.hover_event_action.show_text, text="Hello"
                ),
            )
            .part(
                text="Hover over me to show an item with NBT\n",
                hover_event=onyx.HoverEvent(
                    onyx.hover_event_action.show_item,
                    item_id="minecraft:light_blue_glazed_terracotta",
                ),
            )
            .part(
                text="Hover over me to show an item with NBT",
                hover_event=onyx.HoverEvent(
                    onyx.hover_event_action.show_item,
                    item_id="minecraft:netherite_chestplate",
                    item_tags=Compound(
                        {
                            "display": Compound(
                                {"Name": String(json.dumps({"text": "Hi"}))}
                            )
                        }
                    ),
                ),
            )
        )

        index_component = (
            onyx.text_component()
            .part(text="Part1")
            .part(text="Part2")
            .part(text="Part3")
        )

        dict_component = onyx.text_component().part(
            dict={
                "text": "pls",
                "translate": "translate:string",
                "with_": ["monkey", "ape"],
                "score": {
                    "objective": "objective",
                    "name": "player",  # Use "*" for viewing player
                    "value": 30,
                },
                "selector": onyx.selector(onyx.selector_type.all_players),
                "keybind": onyx.keybind.advancements,
                "nbt": "NBT.Path",
                "interpret": True,
                "block": (3, "~", "17"),
                "entity": "@a",
                "storage": "storage:location",
                "extra": [
                    onyx.text_component().part(text="extra_component", color="#328128")
                ],
                "color": onyx.color.blue,
                "font": "minecraft:default",
                "bold": True,
                "italic": True,
                "underlined": True,
                "strikethrough": True,
                "obfuscated": False,
                "insertion": "Hello!",
            }
        )

        assert (
            main_component.build()
            == """["", {"text": "pls", "translate": "translate:string", "with": ["monkey", "ape"], "score": {"objective": "objective", "name": "player", "value": 30}, "selector": "@a", "keybind": "key.advancements", "nbt": "NBT.Path", "interpret": true, "block": "3 ~ 17", "entity": "@a", "storage": "storage:location", "extra": [[{"text": "extra_component", "color": "#328128"}], [{"text": "extra_component2", "color": "#518923"}]], "color": "blue", "font": "minecraft:default", "bold": true, "italic": true, "underlined": true, "strikethrough": true, "insertion": "Hello!"}]"""
        )
        assert (
            click_event_component.build()
            == """["", {"text": "Click me to change page\\n", "clickEvent": {"action": "change_page", "value": "3"}}, {"text": "Click me to copy to clipboard\\n", "clickEvent": {"action": "copy_to_clipboard", "value": "This is what is in your clipboard"}}, {"text": "Click me to open URL\\n", "clickEvent": {"action": "open_url", "value": "https://doublef3lix.github.io"}}, {"text": "Click me to run command\\n", "clickEvent": {"action": "run_command", "value": "/say Hello"}}, {"text": "Click me to suggest command", "clickEvent": {"action": "suggest_command", "value": "/say Hello"}}]"""
        )
        assert (
            hover_event_component.build()
            == """["", {"text": "Hover over me to show text\\n", "hoverEvent": {"action": "show_text", "contents": "Hello"}}, {"text": "Hover over me to show an item with NBT\\n", "hoverEvent": {"action": "show_item", "contents": {"id": "minecraft:light_blue_glazed_terracotta", "count": 1}}}, {"text": "Hover over me to show an item with NBT", "hoverEvent": {"action": "show_item", "contents": {"id": "minecraft:netherite_chestplate", "count": 1, "tag": "{display: {Name: '{\\"text\\": \\"Hi\\"}'}}"}}}]"""
        )
        assert index_component[1] == """{"text": "Part2"}"""
        assert (
            dict_component.build()
            == """["", {"text": "pls", "translate": "translate:string", "with": ["monkey", "ape"], "score": {"objective": "objective", "name": "player", "value": 30}, "selector": "@a", "keybind": "key.advancements", "nbt": "NBT.Path", "interpret": true, "block": "3 ~ 17", "entity": "@a", "storage": "storage:location", "extra": [[{"text": "extra_component", "color": "#328128"}]], "color": "blue", "font": "minecraft:default", "bold": true, "italic": true, "underlined": true, "strikethrough": true, "insertion": "Hello!"}]"""
        )

    def execute_test(self):
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
        if_blocks_cmd = (
            onyx.execute().if_.blocks("~ ~ ~", "~ ~1 ~", "~ ~ ~1", False).build()
        )
        if_data_cmd = (
            onyx.execute()
            .if_.data(onyx.DataSource(onyx.source_type.block, "~ ~ ~", "Path"))
            .build()
        )
        if_entity_cmd = onyx.execute().if_.entity("@a").build()
        if_predicate_cmd = onyx.execute().if_.predicate("namespace:predicate").build()

        dummy_scoreboard = onyx.scoreboard("objective")
        dummy_player1 = dummy_scoreboard.player("player1")
        dummy_player2 = dummy_scoreboard.player("player2")
        if_score_eq_cmd = (
            onyx.execute().if_.score(dummy_player1 == dummy_player2).build()
        )
        if_score_gt_eq_cmd = (
            onyx.execute().if_.score(dummy_player1 >= dummy_player2).build()
        )
        if_score_gt_cmd = (
            onyx.execute().if_.score(dummy_player1 > dummy_player2).build()
        )
        if_score_lt_eq_cmd = (
            onyx.execute().if_.score(dummy_player1 <= dummy_player2).build()
        )
        if_score_lt_cmd = (
            onyx.execute().if_.score(dummy_player1 < dummy_player2).build()
        )
        if_score_matches_cmd = (
            onyx.execute().if_.score(dummy_player1 == onyx.Range(7, 18)).build()
        )

        # success store isn't tested since it uses the exact same system as result store, so if result store works, success does too
        store_result_block_cmd = (
            onyx.execute()
            .store.result.block(
                onyx.StoreTarget("~ ~ ~", "Path", onyx.data_type.byte, 0.1)
            )
            .build()
        )
        q = onyx.bossbar("bossbar")
        store_result_bossbar_cmd = (
            onyx.execute()
            .store.result.bossbar(onyx.StoreTarget(q, onyx.bossbar_location.max))
            .build()
        )
        store_result_bossbar_cmd2 = (
            onyx.execute()
            .store.result.bossbar(
                onyx.StoreTarget("minecraft:bossbar", onyx.bossbar_location.max)
            )
            .build()
        )
        store_result_entity_cmd = (
            onyx.execute()
            .store.result.entity(
                onyx.StoreTarget("@s", "Path", onyx.data_type.byte, 0.1)
            )
            .build()
        )
        store_result_score_cmd = (
            onyx.execute().store.result.score(dummy_player1).build()
        )
        store_result_storage_cmd = (
            onyx.execute()
            .store.result.storage(
                onyx.StoreTarget("storage:namespace", "Path", onyx.data_type.byte, 0.1)
            )
            .build()
        )

        rest_param_cmd = (
            onyx.execute()
            .align(onyx.axis.x)
            .align([onyx.axis.x, onyx.axis.y])
            .anchored(onyx.anchor.eyes)
            .as_("@a")
            .at("@s")
            .as_at("@s")
            .facing(onyx.AbsPos(3, 4, 5))
            .facing("@s", onyx.anchor.feet)
            .positioned(onyx.AbsPos(3, 4, 5))
            .positioned("@s")
            .rotated(onyx.AbsRot(6, 7))
            .rotated("@s")
            .build()
        )

        manual_context_cmd = onyx.execute(context="as @a at @s").run(
            onyx.commands.say("Hello")
        )

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
        assert store_result_bossbar_cmd2 == "store result bossbar minecraft:bossbar max"
        assert store_result_entity_cmd == "store result entity @s Path byte 0.1"
        assert store_result_score_cmd == "store result score $player1 objective"
        assert (
            store_result_storage_cmd
            == "store result storage storage:namespace Path byte 0.1"
        )
        assert (
            rest_param_cmd
            == "align x align xy anchored eyes as @a at @s as @s at @s facing 3 4 5 facing entity @s feet positioned 3 4 5 positioned as @s rotated 6 7 rotated as @s"
        )
        assert manual_context_cmd == "execute as @a at @s run say Hello"

    def commands_test(self):
        advancement_command1 = onyx.commands.advancement(
            True, "@a", onyx.advancement_mode.everything
        )
        advancement_command2 = onyx.commands.advancement(
            True, "@a", onyx.advancement_mode.from_, "fake:advancement"
        )
        advancement_command3 = onyx.commands.advancement(
            False, "@a", onyx.advancement_mode.through, "fake:advancement"
        )
        attribute_modifier = onyx.AttributeModifier(
            "modifier_name",
            3,
            onyx.attribute_modifier_mode.multiply,
            uuid_override="1-1-1-1-1",
        )
        attribute_command1 = onyx.commands.attribute(
            "@s",
            onyx.attribute.armor,
            onyx.attribute_mode.add_modifier,
            modifier=attribute_modifier,
        )
        attribute_command2 = onyx.commands.attribute(
            "@s", onyx.attribute.armor, onyx.attribute_mode.set_base, base_value=3
        )
        attribute_command3 = onyx.commands.attribute(
            "@s",
            onyx.attribute.armor,
            onyx.attribute_mode.get_modifier,
            attribute_modifier,
            scale=3,
        )
        attribute_command4 = onyx.commands.attribute(
            "@s",
            onyx.attribute.armor,
            onyx.attribute_mode.remove_modifier,
            attribute_modifier,
        )
        clear_cmd = onyx.commands.clear("@a", onyx.item.anvil, 64)
        # Also tests onyx.Block
        clone_cmd = onyx.commands.clone(
            onyx.AbsPos(0, 0, 0),
            onyx.AbsPos(1, 1, 1),
            onyx.AbsPos(2, 2, 2),
            onyx.clone_mask_mode.filtered,
            filter=onyx.Block(
                onyx.block.acacia_button, {"facing": "east"}, Compound({"NBT": Byte(1)})
            ),
            clone_mode=onyx.clone_mode.move,
        )
        defaultgamemode_cmd = onyx.commands.defaultgamemode(onyx.gamemode.adventure)
        difficulty_cmd = onyx.commands.difficulty(onyx.difficulty.easy)
        enchant_cmd1 = onyx.commands.enchant("@s", onyx.enchantment.aqua_affinity, 1)
        enchant_cmd2 = onyx.commands.enchant(
            "@s", {onyx.enchantment.aqua_affinity: 3, onyx.enchantment.binding_curse: 1}
        )
        fill_cmd = onyx.commands.fill(
            onyx.AbsPos(0, 0, 0),
            onyx.AbsPos(1, 1, 1),
            onyx.block.acacia_sapling,
            onyx.fill_mode.replace,
            onyx.block.acacia_planks,
        )
        gamemode_cmd = onyx.commands.gamemode(onyx.gamemode.creative, "@a")
        gamerule_cmd = onyx.commands.gamerule(onyx.gamerule.announceAdvancements, True)
        # Also tests onyx.Item
        give_cmd = onyx.commands.give(
            "@s",
            onyx.Item(
                "minecraft:stone",
                onyx.text_component().part(text="wow"),
                lore=[onyx.text_component().part(text="line1")],
                tags=Compound({"CustomModelData": Byte(1)}),
            ),
            3,
        )
        help_cmd1 = onyx.commands.help()
        help_cmd2 = onyx.commands.help("help")
        kill_cmd1 = onyx.commands.kill("@s")
        kill_cmd2 = onyx.commands.kill("@e[type=pig]", clean_kill=True)
        list_cmd1 = onyx.commands.list()
        list_cmd2 = onyx.commands.list(True)
        locate_cmd = onyx.commands.locate(onyx.structure.bastion_remnant)
        locatebiome_cmd = onyx.commands.locatebiome(onyx.biome.badlands)
        me_cmd = onyx.commands.me("is tired of writing tests and documentation")
        msg_cmd = onyx.commands.msg("@a", "hiya")
        particle_cmd1 = onyx.commands.particle(
            onyx.ParticleNormal(
                onyx.particle.crit, onyx.AbsPos(0, 0, 0), (3, 2, 1), 1.5, 12
            ),
            False,
            "@a",
        )
        particle_cmd2 = onyx.commands.particle(
            onyx.ParticleNormal(
                onyx.particle.dust,
                onyx.AbsPos(0, 0, 0),
                (3, 2, 1),
                1.5,
                12,
                (10, 11, 12, 5),
            ),
            True,
            "@a",
        )
        particle_cmd2 = onyx.commands.particle(
            onyx.ParticleNormal(
                onyx.particle.block,
                onyx.AbsPos(0, 0, 0),
                (3, 2, 1),
                1.5,
                12,
                onyx.block.bedrock,
            ),
            True,
            "@a",
        )
        particle_cmd3 = onyx.commands.particle(
            onyx.ParticleNormal(
                onyx.particle.item,
                onyx.AbsPos(0, 0, 0),
                (3, 2, 1),
                1.5,
                12,
                onyx.item.birch_sign,
            ),
            True,
            "@a",
        )
        particle_cmd4 = onyx.commands.particle(
            onyx.ParticleEntityEffectModified(
                onyx.particle.ambient_entity_effect,
                onyx.AbsPos(0, 0, 0),
                (128, 19, 12),
                64,
            ),
            False,
            "@s",
        )
        particle_cmd5 = onyx.commands.particle(
            onyx.ParticleMotion(
                onyx.particle.bubble, onyx.AbsPos(0, 0, 0), (3, 0, 0), 2
            ),
            True,
            "@a",
        )
        particle_cmd6 = onyx.commands.particle(
            onyx.ParticleNoteModified(onyx.AbsPos(0, 0, 0), 0.56, 17), True, "@p"
        )
        playsound_cmd = onyx.commands.playsound(
            "minecraft:ambient.basalt_deltas.additions",
            onyx.sound_channel.master,
            "@a",
            onyx.AbsPos(0, 255, 0),
            2147483647,
            2,
        )
        say_cmd = onyx.commands.say("Dummy")
        seed_cmd = onyx.commands.seed()
        setblock_cmd = onyx.commands.setblock(
            onyx.AbsPos(5, 5, 5), onyx.block.acacia_slab, onyx.setblock_mode.destroy
        )
        setworldspawn_cmd = onyx.commands.setworldspawn(onyx.AbsPos(0, 64, 0), 160)
        spawnpoint_cmd = onyx.commands.spawnpoint("@a", onyx.AbsPos(0, 64, 0), 36)
        spectate_cmd = onyx.commands.spectate(
            "@e[type=cow,limit=1]", put_in_gamemode=True
        )
        spreadplayers_cmd = onyx.commands.spreadplayers(
            onyx.AbsPos2D(16, 16), 12, 20, True, "@a", under=74
        )
        stopsound_cmd = onyx.commands.stopsound(
            "@r", onyx.sound_channel.any, "minecraft:block.ancient_debris.break"
        )
        summon_cmd = onyx.commands.summon(
            onyx.entity.cat, onyx.AbsPos(0, 255, 0), Compound({"Health": Float(34)})
        )
        teammsg_cmd = onyx.commands.teammsg("I am very much on your team :)")
        teleport_cmd1 = onyx.commands.teleport(
            "@a",
            onyx.AbsPos(0, 256, 0),
            facing=onyx.selector(onyx.selector_type.selected_entity),
        )
        teleport_cmd2 = onyx.commands.teleport(
            "@a", "@s", facing=onyx.AbsPos(0, 256, 0)
        )
        teleport_cmd3 = onyx.commands.teleport("@e", onyx.AbsPos(0, 0, 0))
        tellraw_cmd = onyx.commands.tellraw(
            "@a", onyx.text_component().part(text="Dummy")
        )
        weather_cmd = onyx.commands.weather(onyx.weather_type.clear, 40)

        bossbar_list_cmd = onyx.commands.bossbar.list()
        bossbar_obj = onyx.bossbar("namespace:bossbar_id", create=True)
        assert str(bossbar_obj) == "namespace:bossbar_id"
        assert (
            bossbar_obj.get(onyx.bossbar_query.max_value)
            == "bossbar get namespace:bossbar_id max"
        )
        assert bossbar_obj.remove() == "bossbar remove namespace:bossbar_id"
        assert bossbar_obj.set_value(12) == "bossbar set namespace:bossbar_id value 12"

        effect_clear_cmd1 = onyx.commands.effect.clear("@s", onyx.effect.absorption)
        effect_clear_cmd2 = onyx.commands.effect.clear(
            "@s", [onyx.effect.absorption, onyx.effect.water_breathing]
        )
        effect_give_cmd = onyx.commands.effect.give(
            "@s", onyx.effect.absorption, 30, 1, True
        )

        data_source_pathed = onyx.DataSource(onyx.source_type.entity, "@s", "path")
        data_get_cmd = onyx.commands.data.get(data_source_pathed)
        data_merge_cmd = onyx.commands.data.merge(
            onyx.DataSource(onyx.source_type.storage, "storage:namespace"),
            Compound({"Wow": String("NBT")}),
        )
        data_modify_cmd = onyx.commands.data.modify(
            data_source_pathed, onyx.data_operator.insert, data_source_pathed, 1
        )
        data_remove_cmd = onyx.commands.data.remove(data_source_pathed)

        datapack_disable_cmd = onyx.commands.datapack.disable(self)
        datapack_enable_cmd = onyx.commands.datapack.enable(
            self, onyx.datapack_enable_mode.after, self
        )
        datapack_list_cmd = onyx.commands.datapack.list()

        debug_function_cmd = onyx.commands.debug.function(self.q)
        debug_start_cmd = onyx.commands.debug.start()
        debug_stop_cmd = onyx.commands.debug.stop()

        experience_add_cmd = onyx.commands.experience.add("@s", "7L")
        experience_clear_cmd = onyx.commands.experience.clear("@a")
        experience_query_cmd = onyx.commands.experience.query(
            "@s", onyx.experience_type.points
        )
        experience_set_cmd = onyx.commands.experience.set(
            "@s", 8, onyx.experience_type.points
        )

        forceload_add_cmd = onyx.commands.forceload.add(onyx.AbsPos2D(1, 1))
        forceload_query_cmd = onyx.commands.forceload.query(onyx.AbsPos2D(1, 1))
        forceload_remove_cmd = onyx.commands.forceload.remove(
            onyx.AbsPos2D(1, 1), onyx.AbsPos2D(2, 2)
        )
        forceload_remove_all_cmd = onyx.commands.forceload.remove_all()

        item_modify_cmd = onyx.commands.item.modify(data_source_pathed, "item:modifier")
        item_replace_cmd = onyx.commands.item.replace(
            data_source_pathed, data_source_pathed
        )

        loot_give_cmd = onyx.commands.loot.give(
            "@s", loot_table="minecraft:empty", block=onyx.AbsPos(1, 1, 1)
        )  # fish
        loot_insert_cmd = onyx.commands.loot.insert(
            onyx.AbsPos(3, 3, 3), killed_entity="@s"
        )  # kill
        loot_replace_cmd = onyx.commands.loot.replace(
            onyx.DataSource(onyx.source_type.entity, "@s", onyx.slot.container_0),
            block=onyx.AbsPos(3, 3, 3),
            broken_with=onyx.hand.mainhand,
        )  # mine
        loot_spawn_cmd = onyx.commands.loot.spawn(
            onyx.AbsPos(0, 0, 0), loot_table="minecraft:empty"
        )

        perf_start_cmd = onyx.commands.perf.start()
        perf_stop_cmd = onyx.commands.perf.stop()

        recipe_give_cmd = onyx.commands.recipe.give("@a", onyx.recipe.all)
        recipe_take_cmd = onyx.commands.recipe.take("@a", onyx.recipe.all)

        schedule_clear_cmd = onyx.commands.schedule.clear(self.q)
        schedule_function_cmd = onyx.commands.schedule.function(
            self.q, "3w", onyx.schedule_mode.append
        )

        scoreboard_list_player_scores_cmd = onyx.commands.scoreboard.list_player_scores(
            "@a[tag=amonguslol]"
        )
        scoreboard_reset_player_scores_cmd = (
            onyx.commands.scoreboard.reset_player_scores("@a")
        )
        scoreboard_list_objectives_cmd = onyx.commands.scoreboard.list_objectives()

        tag_add_cmd = onyx.commands.tag.add(
            "@a", "ivebeenwritingtestsfor2hourspleasehelpme"
        )
        tag_list_cmd = onyx.commands.tag.list("@a")
        tag_remove_cmd = onyx.commands.tag.remove(
            "@a",
            "itswildhowlongyoucanmaketagsimeanthisisabsurdlikeicouldputtheentirescriptofhalmetinthisbabyandnothingwouldstopmeisntthatgloriousithoughtsobutalsowhyintheheckwouldanyoneevermakeatagthislonglikethisiscompletelybonkersbutitsprettyhilariousthatyoucanevendothisiknowtheyremovedthelimitsforscoreboardobjectivesandteamnameswhichisamazingbecausescoreboardobjectivescanactuallycontainalotofinformationlikenamespaceentitypurposeetcbutwhyonearthwouldyouneedatagthislongimeanitskindofinsanebutstillfunnyanywaymomsaiddinnerisreadywerehavingpotatosoupsoimgonnagohaveanicedaythankssigneddoublefelix",
        )

        team_add_cmd = onyx.commands.team.add("writingsomethingthismonotonehasbrokenme")
        team_empty_cmd = onyx.commands.team.empty("likeitsnotlikethisisntuseful")
        team_join_cmd = onyx.commands.team.join(
            "buttheresnothingnewitsjusttestaftertest", "@a"
        )
        team_leave_cmd = onyx.commands.team.leave("@a")
        team_list_cmd = onyx.commands.team.list()
        team_modify_cmd = onyx.commands.team.modify(
            "team", onyx.team_attribute.collision_rule, onyx.collision_rule.never
        )
        team_remove_cmd = onyx.commands.team.remove(
            "nevergonnagiveyouupnevergonnaletyoudown"
        )

        time_add_cmd = onyx.commands.time.add("3h")
        time_query_cmd = onyx.commands.time.query(
            onyx.time_query.daytime
        )  # Okay, but like have you ever used molang? The conversion is absurd. Why didn't they just make it a float? I wrote up some data here: https://gist.github.com/DoubleF3lix/a03afde0a979dfa41e8525ee92f12ca5. Shameless plug, but I wrote both things so who cares. Shoutouts to Sprunkles and SirLich.
        time_set_cmd = onyx.commands.time.set("12d")

        title_actionbar_cmd = onyx.commands.title.actionbar(
            "@a",
            onyx.text_component().part(
                text="I really should've just done 'import onyx.commands as _', but oh well..."
            ),
        )
        title_clear_cmd = onyx.commands.title.clear("@a")
        title_reset_cmd = onyx.commands.title.reset("@a")
        title_subtitle_cmd = onyx.commands.title.subtitle(
            "@a", '"too lazy to make an object lol"'
        )
        title_times_cmd = onyx.commands.title.times("@a", 0, 0, 0)
        title_title_cmd = onyx.commands.title.title(
            "@a", '"you\'ll never see this because of instant times"'
        )

        trigger_add_cmd = onyx.commands.trigger.add(onyx.scoreboard("name"), 3)
        trigger_set_cmd = onyx.commands.trigger.set(
            onyx.scoreboard("youllneverseeitcoming"), 3
        )

        worldborder_add_cmd = onyx.commands.worldborder.add(30, 1)
        worldborder_center_cmd = onyx.commands.worldborder.center(onyx.AbsPos2D(12, 12))
        worldborder_damage_cmd1 = onyx.commands.worldborder.damage(per_block=3)
        worldborder_damage_cmd2 = onyx.commands.worldborder.damage(buffer_distance=19)
        worldborder_get_cmd = onyx.commands.worldborder.get()
        worldborder_set_cmd = onyx.commands.worldborder.set(12, 19)
        worldborder_warning_cmd = onyx.commands.worldborder.warning(distance=12, time=9)

        assert advancement_command1 == "advancement revoke @a everything"
        assert advancement_command2 == "advancement revoke @a from fake:advancement"
        assert advancement_command3 == "advancement grant @a through fake:advancement"
        assert (
            attribute_command1
            == "attribute @s minecraft:generic.armor modifier add 1-1-1-1-1 modifier_name 3 multiply"
        )
        assert attribute_command2 == "attribute @s minecraft:generic.armor base set 3"
        assert (
            attribute_command3
            == "attribute @s minecraft:generic.armor modifier value get 1-1-1-1-1 3"
        )
        assert (
            attribute_command4
            == "attribute @s minecraft:generic.armor modifier remove 1-1-1-1-1"
        )
        assert clear_cmd == "clear @a minecraft:anvil 64"
        assert (
            clone_cmd
            == "clone 0 0 0 1 1 1 2 2 2 filtered minecraft:acacia_button[facing=east]{NBT: 1b} move"
        )
        assert defaultgamemode_cmd == "defaultgamemode adventure"
        assert difficulty_cmd == "difficulty easy"
        assert enchant_cmd1 == "enchant @s minecraft:aqua_affinity 1"
        assert enchant_cmd2 == [
            "enchant @s minecraft:aqua_affinity 3",
            "enchant @s minecraft:binding_curse 1",
        ]
        assert (
            fill_cmd
            == "fill 0 0 0 1 1 1 minecraft:acacia_sapling replace minecraft:acacia_planks"
        )
        assert gamemode_cmd == "gamemode creative @a"
        assert gamerule_cmd == "gamerule announceAdvancements true"
        assert (
            give_cmd
            == """give @s minecraft:stone{CustomModelData: 1b, display: {Lore: ['["", {"text": "line1"}]']}} 3"""
        )
        assert help_cmd1 == "help"
        assert help_cmd2 == "help help"
        assert kill_cmd1 == "kill @s"
        assert (
            kill_cmd2
            == """execute as @e[type=pig] run data merge entity @s {Health:0.0f,DeathTime:19s,DeathLootTable:"minecraft:empty"}"""
        )
        assert list_cmd1 == "list"
        assert list_cmd2 == "list uuids"
        assert locate_cmd == "locate bastion_remnant"
        assert locatebiome_cmd == "locatebiome minecraft:badlands"
        assert me_cmd == "me is tired of writing tests and documentation"
        assert msg_cmd == "msg @a hiya"
        assert particle_cmd1 == "particle minecraft:crit 0 0 0 3 2 1 1.5 12 normal @a"
        assert (
            particle_cmd2
            == "particle minecraft:block minecraft:bedrock 0 0 0 3 2 1 1.5 12 force @a"
        )
        assert (
            particle_cmd3
            == "particle minecraft:item minecraft:birch_sign 0 0 0 3 2 1 1.5 12 force @a"
        )
        assert (
            particle_cmd4
            == "particle minecraft:ambient_entity_effect 0 0 0 128 19 12 64 0 normal @s"
        )
        assert particle_cmd5 == "particle minecraft:bubble 0 0 0 3 0 0 2 0 force @a"
        assert particle_cmd6 == "particle minecraft:note 0 0 0 0.56 0 0 17 0 force @p"
        assert (
            playsound_cmd
            == "playsound minecraft:ambient.basalt_deltas.additions master @a 0 255 0 2147483647 2"
        )
        assert say_cmd == "say Dummy"
        assert seed_cmd == "seed"
        assert setblock_cmd == "setblock 5 5 5 minecraft:acacia_slab destroy"
        assert setworldspawn_cmd == "setworldspawn 0 64 0 160"
        assert spawnpoint_cmd == "spawnpoint @a 0 64 0 36"
        assert spectate_cmd == "spectate @e[type=cow,limit=1] @s"
        assert spreadplayers_cmd == "spreadplayers 16 16 12 20 under 74 true @a"
        assert stopsound_cmd == "stopsound @r * minecraft:block.ancient_debris.break"
        assert summon_cmd == "summon minecraft:cat 0 255 0 {Health: 34.0f}"
        assert teammsg_cmd == "teammsg I am very much on your team :)"
        assert teleport_cmd1 == "teleport @a 0 256 0 facing entity @s"
        assert teleport_cmd2 == "teleport @a @s facing 0 256 0"
        assert teleport_cmd3 == "teleport @e 0 0 0"
        assert tellraw_cmd == """tellraw @a ["", {"text": "Dummy"}]"""
        assert weather_cmd == "weather clear 40"

        assert bossbar_list_cmd == "bossbar list"

        assert effect_clear_cmd1 == "effect clear @s minecraft:absorption"
        assert effect_clear_cmd2 == [
            "effect clear @s minecraft:absorption",
            "effect clear @s minecraft:water_breathing",
        ]
        assert effect_give_cmd == "effect give @s minecraft:absorption 30 1 true"

        assert data_get_cmd == "data get entity @s path"
        assert data_merge_cmd == """data merge storage storage:namespace {Wow: "NBT"}"""
        assert (
            data_modify_cmd == "data modify entity @s path insert 1 from entity @s path"
        )
        assert data_remove_cmd == "data remove entity @s path"

        assert datapack_disable_cmd == "datapack disable onyx_testing_data_pack"
        assert (
            datapack_enable_cmd
            == "datapack enable onyx_testing_data_pack after onyx_testing_data_pack"
        )
        assert datapack_list_cmd == "datapack list"

        assert debug_function_cmd == "debug function testing:blank"
        assert debug_start_cmd == "debug start"
        assert debug_stop_cmd == "debug stop"

        assert experience_add_cmd == "experience add @s 7 levels"
        assert experience_clear_cmd == "experience add @a -2147483647 levels"
        assert experience_query_cmd == "experience query @s points"
        assert experience_set_cmd == "experience set @s 8 points"

        assert forceload_add_cmd == "forceload add 1 1 1 1"
        assert forceload_query_cmd == "forceload query 1 1"
        assert forceload_remove_cmd == "forceload remove 1 1 2 2"
        assert forceload_remove_all_cmd == "forceload remove all"

        assert item_modify_cmd == "item modify entity @s path item:modifier"
        assert item_replace_cmd == "item replace entity @s path from entity @s path"

        assert loot_give_cmd == "loot give @s fish minecraft:empty 1 1 1"
        assert loot_insert_cmd == "loot insert 3 3 3 kill @s"
        assert (
            loot_replace_cmd == "loot replace entity @s container.0 mine 3 3 3 mainhand"
        )
        assert loot_spawn_cmd == "loot spawn 0 0 0 loot minecraft:empty"

        assert perf_start_cmd == "perf start"
        assert perf_stop_cmd == "perf stop"

        assert recipe_give_cmd == "recipe give @a *"
        assert recipe_take_cmd == "recipe take @a *"

        assert schedule_clear_cmd == "schedule clear testing:blank"
        assert schedule_function_cmd == "schedule function testing:blank 21d append"

        assert (
            scoreboard_list_player_scores_cmd
            == "scoreboard players list @a[tag=amonguslol]"
        )
        assert scoreboard_reset_player_scores_cmd == "scoreboard players reset @a"
        assert scoreboard_list_objectives_cmd == "scoreboard objectives list"
        assert tag_add_cmd == "tag @a add ivebeenwritingtestsfor2hourspleasehelpme"
        assert tag_list_cmd == "tag @a list"
        assert (
            tag_remove_cmd
            == "tag @a remove itswildhowlongyoucanmaketagsimeanthisisabsurdlikeicouldputtheentirescriptofhalmetinthisbabyandnothingwouldstopmeisntthatgloriousithoughtsobutalsowhyintheheckwouldanyoneevermakeatagthislonglikethisiscompletelybonkersbutitsprettyhilariousthatyoucanevendothisiknowtheyremovedthelimitsforscoreboardobjectivesandteamnameswhichisamazingbecausescoreboardobjectivescanactuallycontainalotofinformationlikenamespaceentitypurposeetcbutwhyonearthwouldyouneedatagthislongimeanitskindofinsanebutstillfunnyanywaymomsaiddinnerisreadywerehavingpotatosoupsoimgonnagohaveanicedaythankssigneddoublefelix"
        )

        assert team_add_cmd == "team add writingsomethingthismonotonehasbrokenme"
        assert team_empty_cmd == "team empty likeitsnotlikethisisntuseful"
        assert team_join_cmd == "team join buttheresnothingnewitsjusttestaftertest @a"
        assert team_leave_cmd == "team leave @a"
        assert team_list_cmd == "team list"
        assert team_modify_cmd == "team modify team collisionRule never"
        assert team_remove_cmd == "team remove nevergonnagiveyouupnevergonnaletyoudown"

        assert time_add_cmd == "time add 3000"
        assert time_query_cmd == "time query daytime"
        assert time_set_cmd == "time set 288000"

        assert (
            title_actionbar_cmd
            == """title @a actionbar ["", {"text": "I really should've just done 'import onyx.commands as _', but oh well..."}]"""
        )
        assert title_clear_cmd == "title @a clear"
        assert title_reset_cmd == "title @a reset"
        assert (
            title_subtitle_cmd
            == """title @a subtitle "too lazy to make an object lol\""""
        )
        assert title_times_cmd == "title @a times 0 0 0"
        assert (
            title_title_cmd
            == """title @a title "you'll never see this because of instant times\""""
        )

        assert trigger_add_cmd == "trigger name add 3"
        assert trigger_set_cmd == "trigger youllneverseeitcoming set 3"

        assert worldborder_add_cmd == "worldborder add 30 1"
        assert worldborder_center_cmd == "worldborder center 12 12"
        assert worldborder_damage_cmd1 == ["worldborder damage amount 3"]
        assert worldborder_damage_cmd2 == ["worldborder damage buffer 19"]
        assert worldborder_get_cmd == "worldborder get"
        assert worldborder_set_cmd == "worldborder set 12 19"
        assert worldborder_warning_cmd == [
            "worldborder warning distance 12",
            "worldborder warning time 9",
        ]


DataPack()
