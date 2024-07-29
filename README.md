## print_r - PHP's print_r() for python. Or pretty close. 

---
This module does exactly as the title suggests, it dumps Python data structures and presents them in ways that emulate PHP's print_r() function.

This module was the result of serendipity. I cannot take credit as it is a ChaptGPT 4o hallucination. I am choosing to call it a hallucination as I did not prompt explicitly as it to write this module. I was simply asking it questions, but when I began k-shot prompting what I was looking for it pooped out a prototype. I fine-tuned its prototype into a few more examples and chose my 3 favorites.

I am now sharing it with the world in case anyone else hates pprint and similar modules as much as myself and needs something for pattern/shape-oriented brains.

I chose an MIT license in honor of the Ruby gem awesome_print, since that example was what helped ChatGPT to understand my wishes.

You will need colorama for this. 
```
pip install colorama
```

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
An example of ppr() output: 
```ruby
(
    'name' => 'John Doe'
    'age' => 30
    'children' =>     (
        [0] =>         (
            'name' => 'Jane Doe'
            'age' => 10
            'hobbies' =>             (
                [0] => 'drawing'
                [1] => 'reading'
            )
        )
        [1] =>         (
            'name' => 'Jim Doe'
            'age' => 7
            'hobbies' =>             (
                [0] => 'soccer'
                [1] => 'video games'
            )
        )
    )
    'address' =>     (
        'street' => '123 Main St'
        'city' => 'Anytown'
        'postal_code' => '12345'
        'coordinates' =>         (
            'latitude' => 40.7128
            'longitude' => -74.006
        )
    )
    'employment' =>     (
        'current' =>         (
            'position' => 'Software Engineer'
            'company' => 'TechCorp'
            'years' => 5
            'projects' =>             (
                [0] =>                 (
                    'name' => 'Project A'
                    'duration' => '2 years'
                )
                [1] =>                 (
                    'name' => 'Project B'
                    'duration' => '1 year'
                )
                [2] =>                 (
                    'name' => 'Project C'
                    'duration' => '2 years'
                )
            )
        )
        'previous' =>         (
            [0] =>             (
                'position' => 'Junior Developer'
                'company' => 'DevInc'
                'years' => 2
            )
            [1] =>             (
                'position' => 'Intern'
                'company' => 'StartUp'
                'years' => 1
            )
        )
    )
    'favorites' =>     (
        'colors' =>         (
            [0] => 'blue'
            [1] => 'green'
            [2] => 'red'
        )
        'foods' =>         (
            [0] => 'pizza'
            [1] => 'ice cream'
            [2] => 'salad'
        )
    )
)
```