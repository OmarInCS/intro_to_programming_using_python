
from termcolor import cprint


class Shape:

    def __init__(self, color):
        self.color = color

    def print_with_color(self):
        cprint(self, self.color)

    def get_area(self):
        pass

    def __eq__(self, other):
        return self.get_area() == other.get_area()
