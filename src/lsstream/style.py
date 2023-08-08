from pyfiglet import Figlet
from termcolor import colored
from colorama import init

# Initialize colorama
init()

# For the intro
intro = Figlet(font='big')

# Just coloring for fun
def color(text, color='green', attrs=None):
    default_attrs = ['bold']
    if attrs:
        default_attrs.extend(attrs)
    return colored(text, color, attrs=default_attrs)
