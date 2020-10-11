
from termcolor import cprint

class Shape(object):

    def __init__(self, color):
        self.color = color

    def print_with_color(self):
        cprint(self, self.color)

    def __repr__(self):
        return f"Area: {self.get_area()}"