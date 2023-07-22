from pyfiglet import Figlet
from termcolor import colored
from colorama import init

# Initialize colorama
init()

# For the intro
intro = Figlet(font='big')

# Just coloring for fun
def color(text, color='yellow'):
    return colored(text, color, attrs=["bold"])
