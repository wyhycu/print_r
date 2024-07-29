from print_r import app
from print_r import appc
from print_r import ppr

complex_data = {
    "name": "John Doe",
    "age": 30,
    "children": [
        {
            "name": "Jane Doe",
            "age": 10,
            "hobbies": ["drawing", "reading"]
        },
        {
            "name": "Jim Doe",
            "age": 7,
            "hobbies": ["soccer", "video games"]
        }
    ],
    "address": {
        "street": "123 Main St",
        "city": "Anytown",
        "postal_code": "12345",
        "coordinates": {
            "latitude": 40.7128,
            "longitude": -74.0060
        }
    },
    "employment": {
        "current": {
            "position": "Software Engineer",
            "company": "TechCorp",
            "years": 5,
            "projects": [
                {"name": "Project A", "duration": "2 years"},
                {"name": "Project B", "duration": "1 year"},
                {"name": "Project C", "duration": "2 years"}
            ]
        },
        "previous": [
            {"position": "Junior Developer", "company": "DevInc", "years": 2},
            {"position": "Intern", "company": "StartUp", "years": 1}
        ]
    },
    "favorites": {
        "colors": ["blue", "green", "red"],
        "foods": ["pizza", "ice cream", "salad"]
    }
}

print("awesome_pretty_print example:\n")
app(complex_data)
print("\n")
print("awesome_pretty_print_colors example:\n")
appc(complex_data)
print("\n")
print("php_style_print_r example:\n")
ppr(complex_data)
print("\n")