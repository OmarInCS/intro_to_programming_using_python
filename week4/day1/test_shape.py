from week4.day1.circle import Circle
from week4.day1.rectangle import Rectangle

r1 = Rectangle(4, 5, "red")
c1 = Circle(3, "blue")
c2 = Circle(3, "blue")

r1.print_with_color()
c1.print_with_color()

print(c1 == c2)