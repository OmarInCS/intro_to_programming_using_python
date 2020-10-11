from week5.day2.circle import Circle
from week5.day2.rectangle import Rectangle

r1 = Rectangle(4, 5, "red")
c1 = Circle(3, "green")

r1.print_with_color()
c1.print_with_color()

print(r1.__dict__)
print(r1.__doc__)
print(r1.__class__)
