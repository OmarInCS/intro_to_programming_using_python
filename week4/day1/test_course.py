
from week4.day1.course import Course

c1 = Course("Java")
c1.add_student("Ali")
c1.add_student("Walid")
c1.add_student("Fahad")

print(c1.get_students())
print(c1.get_nb_of_students())

c1.drop_student("Walid")

print(c1.get_students())
print(c1.get_nb_of_students())

c2 = Course("Python")
c2.add_student("Sultan")

print(c1 > c2)
c1 + "Hussein"
print(c1.get_students())

print(c1)