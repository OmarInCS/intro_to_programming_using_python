
from week4.day1.course import Course

c1 = Course("Python")
c2 = Course("Java")

c1.add_student("Abdullah")
c1.add_student("Essam")
c1.add_student("Mohamed")
c1.add_student("Omar")

print(c1.get_students())
print(c1.get_nb_of_students())

c1.drop_student("Omar")

print(c1.get_students())
print(c1.get_nb_of_students())
