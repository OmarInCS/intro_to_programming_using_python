from week4.day2.circle import Circle
from week4.day2.rectangle import Rectangle

r1 = Rectangle(4, 5, "blue")
c1 = Circle(3, "red")
c2 = Circle(3, "green")

r1.print_with_color()
c1.print_with_color()

print(r1.__class__)
print(r1.__dict__)
print(r1 == c1)
print(c2 == c1)
