
from week3.day3.course import Course
from week3.day3.student import Student

c1 = Course("Python")
print(c1.get_nb_of_students())

c1.add_student(Student("Mohannad", 23))
c1.add_student(Student("Saleh", 20))
c1.add_student(Student("Omar", 13))

print(c1.get_students())
print(c1.get_nb_of_students())

c1.drop_student("Omar")

print(c1.get_students())
print(c1.get_nb_of_students())
