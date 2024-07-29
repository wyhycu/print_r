# print_r - PHP's print_r() for python. Or pretty close. 

---
This module does exactly as the title suggests, it dumps python data structures and presents them in ways that emulate PHP's print_r() function.  

This module was the result of serendipity. I cannot take credit as it is a ChaptGPT 4o hallucination. I am choosing to call it a hallucination as I did not prompt explicitly as it to write this module. I was simply asking it questions, but when I began k-shot prompting what I was looking for it pooped out a prototype. I fine-tuned its protype into a few more example, and chose my 3 favorite. 

I am now sharing it with the world in case anyone else hates pprint and similar modules as my as myself and needs something for pattern/shape oriented brains.

I chose an MIT license in honor of the Ruby gem awesome_print, since that example was what help ChatGPT to understand my wishes. 

___
### Example usage:

For the original 'awesome_pretty_print' example:
```python
from print_r import app
app(data_structure_to_dump)
```
For the enhanced 'awesome_pretty_print_colors' example:
```python
from print_r import appc
appc(data_structure_to_dump)
```
And finally, for the full 'php_style_print_r' example:
```python
from print_r import ppr
ppr(data_structure_to_dump)
```