
from week3.day2.rectangle import Rectangle

w, l = eval(input("Enter width and length: "))
r1 = Rectangle(w, l)
print(r1.get_area())

r2 = Rectangle(7, 3)
print(r2.get_area())
