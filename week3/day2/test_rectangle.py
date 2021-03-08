
from week3.day2.rectangle import Rectangle

w, h = eval(input("Enter width and length: "))
r1 = Rectangle(w, h)
r2 = Rectangle(3, 7)

print("Area:", r1.get_area())
print("Area:", r2.get_area())
