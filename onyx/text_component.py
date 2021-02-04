import random
from onyx.class_types import Buildable


class TextComponent(Buildable):
    # Verify the hack works
    def build(self): 
        print(random.randint(3000, 301201))
