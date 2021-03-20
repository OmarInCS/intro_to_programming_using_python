
from week3.day2.course import Course

c1 = Course("Python")
c1.add_student("Khaled")
c1.add_student("Ali")
c1.add_student("Omar")

print(c1.get_students())

c1.drop_student("Ali")
print(c1.get_students())
print(c1.get_nb_students())

c2 = Course("Java")
c2.add_student("Saud")
c2 + "Walid"

print(c1 > c2)
print(c2)