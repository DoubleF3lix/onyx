from onyx.pack_manager import *
from onyx.commands import Commands as commands
from onyx.selector import Selector as selector
from onyx.util import *
from onyx.scoreboard import Scoreboard as scoreboard
from onyx.registries import *

# I'm so sorry... (but also this is really cool and I'm kind of proud and ashamed at the same time. Proumed or ashoud or prashamed, I don't know, figure it out yourself ¯\_(ツ)_/¯)
class BadHack:
    @property
    def component(self):
        import onyx
        return onyx.text_component.TextComponent()
text_component = BadHack().component