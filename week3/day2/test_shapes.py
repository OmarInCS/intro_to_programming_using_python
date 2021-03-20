
from week3.day2.rectangle import Rectangle
from week3.day2.circle import Circle

r1 = Rectangle(4, 5, "red")
c1 = Circle(3, "green")

r1.print_with_color()
c1.print_with_color()
print(r1.__dict__)
print(r1.__class__)
