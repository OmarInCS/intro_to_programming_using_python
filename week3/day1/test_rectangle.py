
from week3.day1.rectangle import Rectangle

w, l = eval(input("Enter width and length: "))
r1 = Rectangle(w, l)
area = r1.get_area()
print("Area:", area)

r2 = Rectangle(3, 7)
print("Area:", r2.get_area())
