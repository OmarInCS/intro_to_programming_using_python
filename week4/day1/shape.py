
from termcolor import cprint


class Shape:

    def __init__(self, color):
        self.color = color

    def get_area(self):
        pass

    def print_with_color(self):
        cprint(self, self.color)
        cprint(self.get_area(), self.color)

