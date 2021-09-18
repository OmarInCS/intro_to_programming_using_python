
from week4.day1.course import Course

c1 = Course("Java", 1000)
c1.add_student("Khalid")
c1.add_student("Ali")
c1.add_student("Ahmed")

print(c1.get_students())
print(c1.get_nb_students())

c1.drop_student("Ali")
print(c1.get_students())
print(c1.get_nb_students())

c2 = Course("Python", 1200)
c2 += "Wael"
c2 += "Yasser"
print(c2.get_students())

print(c1 > c2)
print(c1)

