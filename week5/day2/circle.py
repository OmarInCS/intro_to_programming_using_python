from week5.day2.shape import Shape


class Circle(Shape):

    def __init__(self, radius, color):
        Shape.__init__(self, color)
        self.radius = radius

    def get_area(self):
        return 3.14 * self.radius ** 2