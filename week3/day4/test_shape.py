
from week3.day4.rectangle import Rectangle
from week3.day4.circle import Circle

c1 = Circle(3, "red")
r1 = Rectangle(4, 5, "green")

c1.print_with_color()
r1.print_with_color()
print(r1.__dict__)
print(r1.__class__)