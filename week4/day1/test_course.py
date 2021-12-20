
from week4.day1.course import Course

c1 = Course("Java", 1200)
c1.add_student("Ahmed")
c1.add_student("Wael")
c1.add_student("Saad")

print(c1.get_nb_students())
print(c1.get_students())

c1.drop_student("Wael")

print(c1.get_nb_students())
print(c1.get_students())

c2 = Course("SQL", 1000)
c2.add_student("Wael")
c2 + "Ali"
print(c2.get_students())

print(c1 > c2)
print(c1)
