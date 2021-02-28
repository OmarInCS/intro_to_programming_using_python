
from week4.day1.course import Course

c1 = Course("Python")
c1.add_student("Yasser")
c1.add_student("AboSara")
c1.add_student("Asmaa")
c1.add_student("Obai")

print(c1.get_nb_of_students())
print(c1.get_students())

c1.drop_student("Obai")

print(c1.get_nb_of_students())
print(c1.get_students())

c2 = Course("SQL")
c2.add_student("Wael")
c2.add_student("Said")
c2 + "Omar"

print(c1 > c2)
print(c2.get_students())
print(c2)