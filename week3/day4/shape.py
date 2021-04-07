
from termcolor import cprint

class Shape:

    def __init__(self, color):
        self.color = color

    def print_with_color(self):
        cprint(self, self.color)
