
from week3.day3.rectangle import Rectangle

w, l = eval(input("Enter width and length: "))
r1 = Rectangle(w, l)

print("Area:", r1.get_area())

r2 = Rectangle(7, 3)
print("Area:", r2.get_area())