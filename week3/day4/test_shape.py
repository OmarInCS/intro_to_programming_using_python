
from week3.day4.rectangle import Rectangle
from week3.day4.circle import Circle

r1 = Rectangle(4, 5, "blue")
c1 = Circle(5, "red")

r1.print_with_color()
c1.print_with_color()

print(r1.__dict__)
