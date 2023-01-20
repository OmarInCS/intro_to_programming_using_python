from week4.day1.room import Room

w, l = eval(input("Enter room width and length: "))
r1 = Room(w, l)
print("Area:", r1.get_area())

r2 = Room(3, 7)
print("Area:", r2.get_area())


