from week3.day4.shape import Shape


class Circle(Shape):

    def __init__(self, radius, color):
        super().__init__(color)
        self.radius = radius

    def get_area(self):
        return 3.14 * self.radius ** 2

    def __str__(self):
        return f"Circle: {self.get_area()}"