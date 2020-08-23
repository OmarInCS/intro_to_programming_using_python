
from week3.day1.rectangle import Rectangle

w, h = eval(input("Enter width and length: "))
r1 = Rectangle(w, h)
print("Area:", r1.get_area())

r2 = Rectangle(3, 7)
print("Area:", r2.get_area())
