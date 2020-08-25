### Discord: **https://discord.gg/NcztW9T**
### Documentation: **https://doublefelix.cf/onyx_docs/index.html** 

&nbsp;
# Getting Started
First, make sure you have the package downloaded by running `pip install onyx` in your terminal. Then, make a new file (call it whatever) and at the top, add `from onyx import *` (this includes nbtlib). 

From here, you'll need to define your datapack object. This can be done with `pack = pack(file_path)`. Now you can get started defining functions.

&nbsp;
## Functions
A basic function should look something like this:
```python
from onyx import *
pack = pack(file_path)

main = pack.function("function/path", "function_name")
with main:
    say("Hello, World!")
```
You can make a function run every tick by using `pack.function("function_path", "function_name", loop=True)`.

&nbsp;
## Selectors
Selectors are defined very similar to the normal game, and are done like so:
```python
alive_players_in_arena = selector(at.all_players, tag="alive", y=0, dy=63)
```
Onyx will automatically convert types, so if you don't want to define a selector for something simple, you can just pass in `"@a"` instead of `selector(at.all_players)`.

&nbsp;
## JSON Strings
JSON strings (also known as text-components) have a builder design. They can be chained too, to seperate components with differing elements.
```python
text = json_string().component("Hello, ").component(text="World!", color=color.gold, bold=True, italic=True)
tellraw("@a", text)
```

&nbsp;
# Credits

Language Design:
* [Arcensoth](https://github.com/Arcensoth) (Design Ideas and Feedback, Implementation Ideas)
* the der discohund (Design Ideas, Implementation Ideas)
* [fizzy](https://github.com/vberlier) (Creator of [nbtlib](https://github.com/vberlier/nbtlib), which was used to implement SNBT, and [mudkip](https://github.com/vberlier/mudkip), which was used to generate the docs)
* Not A2 (Design Feedback)
* nphhpn (Feature Suggestions, Design Feedback, Implementation Ideas)
* [PeerHeer](https://github.com/PeerHeer) (Feature Suggestions, Design Ideas and Feedback, Implemetation Assistance)
* [Princess](https://github.com/noglass) (Design Feedback)
* [Ravbug](https://www.ravbug.com) (Design Feedback, Implementation Ideas)
* rx (Feature Suggestions, Design Feedback and Ideas)
* SirBenet (Design Ideas and Feedback, Implementation Ideas)
* TheMrZZ (Design Ideas)
* vdvman1 (Design Feedback, Implementation Assistance, Creator of [Phi](https://github.com/MinecraftPhi/MinecraftPhi-modules), which was almost completely copied for use in the `bitwise` and `rng` libraries)