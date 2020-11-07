
from week3.day2.room import Room

w, l = eval(input("Enter the room width and length: "))
r1 = Room(w, l)
print("Area:", r1.get_area())
