
from week4.day1.course import Course
from week4.day1.student import Student


c1 = Course("Python")
c1.add_student(Student("Ahmed", 23))
c1.add_student(Student("Mohamed", 20))
c1.add_student(Student("Ali", 15))

print(c1.get_students())

c1.drop_student("Ali")
print(c1.get_students())
print(c1.get_nb_of_students())

print(c1)
