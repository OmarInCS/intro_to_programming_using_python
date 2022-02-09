
class Rectangle:

    def __init__(self, width, length):
        self.width = width
        self.length = length

    def get_area(self):
        return self.width * self.length

    # def get_status(self):
    #     bmi = self.get_area()
    #     if