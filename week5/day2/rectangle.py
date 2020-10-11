from week5.day2.shape import Shape


class Rectangle(Shape):

    def __init__(self, width, length, color):
        Shape.__init__(self, color)
        self.width = width
        self.length = length

    def get_area(self):
        return self.width * self.length
