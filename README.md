# Onyx
A python library to create minecraft data packs

## Documentation
You can view the documentation [here](https://doublef3lix.github.io/onyx/index.html).

## Getting Started
First, install the package with `pip install onyx-mclib`.
Next, create a python script and import onyx. It is also recommended you import all of `nbtlib.tag` like so: `from nbtlib.tag import *`.

Here's a sample script to get you started:
```python
import onyx

class MyPack(onyx.DataPack):
    def __init__(self):
        super().__init__("My data pack name")

        self.function("namespace:function", self.function_obj)

        self.generate()

    def function_obj(self):
        onyx.commands.say("Hello, World!")

MyPack()
```

## Credits
* [fizzy/vberlier](https://github.com/vberlier) - Creator of [nbtlib](https://github.com/vberlier/nbtlib), [beet](https://github.com/mcbeet/beet), and [mudkip](https://github.com/vberlier/mudkip), helped walk me through using GitHub actions
* Arcensoth, rx, vdvman1 - Library design help
* Jayfin, Lue, lolad/lolgeny, MulverineX, Speedy2025 - Motivating me to work on this project after nearly abandoning it
* You - For using this (hopefully, heh)
