# print_r.py

# basic awesome pretty print
from colorama import Fore, Style, init

def awesome_pretty_print(obj, indent=0):
    spacing = '    '
    if isinstance(obj, dict):
        print(' ' * indent + '{')
        for key, value in obj.items():
            print(' ' * (indent + 4) + repr(key) + ' => ', end='')
            awesome_pretty_print(value, indent + 4)
        print(' ' * indent + '}')
    elif isinstance(obj, list):
        print(' ' * indent + '[')
        for index, value in enumerate(obj):
            print(' ' * (indent + 4) + f'[{index}] => ', end='')
            awesome_pretty_print(value, indent + 4)
        print(' ' * indent + ']')
    else:
        print(repr(obj))

def app(obj):
    awesome_pretty_print(obj)

# awesome pretty print with colors
init(autoreset=True)

def awesome_pretty_print_colors(obj, indent=0):
    spacing = '    '
    if isinstance(obj, dict):
        print(' ' * indent + '{')
        for key, value in obj.items():
            print(' ' * (indent + 4) + Fore.CYAN + repr(key) + Style.RESET_ALL + ' => ', end='')
            awesome_pretty_print_colors(value, indent + 4)  
        print(' ' * indent + '}')
    elif isinstance(obj, list):
        print(' ' * indent + '[')
        for index, value in enumerate(obj):
            print(' ' * (indent + 4) + Fore.YELLOW + f'[{index}]' + Style.RESET_ALL + ' => ', end='')
            awesome_pretty_print_colors(value, indent + 4) 
        print(' ' * indent + ']')
    else:
        print(Fore.GREEN + repr(obj) + Style.RESET_ALL)

def appc(obj):
    awesome_pretty_print_colors(obj)  

# PHP style print_r with colors
def php_style_print_r(obj, indent=0):
    spacing = '    '
    if isinstance(obj, dict):
        print(' ' * indent + '(')
        for key, value in obj.items():
            print(' ' * (indent + 4) + Fore.CYAN + repr(key) + Style.RESET_ALL + ' => ', end='')
            php_style_print_r(value, indent + 4) 
        print(' ' * indent + ')')
    elif isinstance(obj, list):
        print(' ' * indent + '(')
        for index, value in enumerate(obj):
            print(' ' * (indent + 4) + Fore.YELLOW + f'[{index}]' + Style.RESET_ALL + ' => ', end='')
            php_style_print_r(value, indent + 4)  
        print(' ' * indent + ')')
    else:
        print(Fore.GREEN + repr(obj) + Style.RESET_ALL)

def ppr(obj):
    php_style_print_r(obj)

# Python style print_r with colors with logic to handle python objects better
def python_style_print_r(obj, indent=0):
    spacing = '    '
    if isinstance(obj, dict):
        print(' ' * indent + '(')
        for key, value in obj.items():
            print(' ' * (indent + 4) + Fore.CYAN + repr(key) + Style.RESET_ALL + ' => ', end='')
            python_style_print_r(value, indent + 4)
        print(' ' * indent + ')')
    elif isinstance(obj, list):
        print(' ' * indent + '(')
        for index, value in enumerate(obj):
            print(' ' * (indent + 4) + Fore.YELLOW + f'[{index}]' + Style.RESET_ALL + ' => ', end='')
            python_style_print_r(value, indent + 4)
        print(' ' * indent + ')')
    elif hasattr(obj, '__dict__'):
        print(' ' * indent + obj.__class__.__name__ + ' {')
        for key, value in vars(obj).items():
            print(' ' * (indent + 4) + Fore.CYAN + repr(key) + Style.RESET_ALL + ' => ', end='')
            python_style_print_r(value, indent + 4)
        print(' ' * indent + '}')
    else:
        print(Fore.GREEN + repr(obj) + Style.RESET_ALL)

def pypr(obj):
    python_style_print_r(obj)