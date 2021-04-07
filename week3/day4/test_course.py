
from week3.day4.course import Course

c1 = Course("Python", 6)
c1.add_student("Ahmed")
c1.add_student("Ali")
c1.add_student("Yasser")
c1.add_student("Abbas")

print(c1.get_nb_students())
print(c1.get_students())

c1.drop_student("Ali")
print(c1.get_nb_students())
print(c1.get_students())

c2 = Course("Java", 4)
c2.add_student("Ali")
c2 + "Wael"
print(c2.get_students())

print(c1 > c2)
