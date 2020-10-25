from week4.day1.shape import Shape


class Rectangle(Shape):

    def __init__(self, width, length, color):
        super().__init__(color)
        self.width = width
        self.length = length

    def get_area(self):
        return self.width * self.length

    def __repr__(self):
        return f"Rectangle: {self.width}, {self.length}"
