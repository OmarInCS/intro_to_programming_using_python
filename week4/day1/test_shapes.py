from week4.day1.circle import Circle
from week4.day1.rectangle import Rectangle

r1 = Rectangle(4, 5, "blue")
c1 = Circle(3, "red")

r1.print_with_color()
c1.print_with_color()
print(r1.__dict__)