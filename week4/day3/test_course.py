from week4.day3.course import Course

c1 = Course("Java", 1000)
c2 = Course("Python", 1200)

c1.add_student("Ali")
c1.add_student("Wael")
c1.add_student("Fahad")
c1 += "Adel"

print(c1.get_nb_students())
print(c1.get_students())

c1.drop_student("Wael")
print(c1.get_nb_students())
print(c1.get_students())

print(c1 > c2)
c1.price = -1200
# c1.set_price(-1200)
# print(c1.get_price())
print(c1.price)

