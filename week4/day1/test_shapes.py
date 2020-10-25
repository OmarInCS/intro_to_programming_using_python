
from week4.day1.rectangle import Rectangle
from week4.day1.circle import Circle

c1 = Circle(3, "red")
r1 = Rectangle(4, 5, "blue")
r2 = Rectangle(4, 5, "blue")

c1.print_with_color()
r1.print_with_color()

print(r1.__dict__)
print(c1 == r1)
print(r2 == r1)
