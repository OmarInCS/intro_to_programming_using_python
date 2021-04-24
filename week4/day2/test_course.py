
from week4.day2.course import Course

c1 = Course("Java")
c1.add_student("Hesham")
c1.add_student("Abdallah")
c1.add_student("Yasser")

print(c1.get_students())
print(c1.get_nb_of_students())

c1.drop_student("Abdallah")
print(c1.get_students())
print(c1.get_nb_of_students())

c2 = Course("C#")
c3 = Course("Python")
c2.add_student("Abdallah")
c2 += "Mohamed"
print(c2.get_students())

print(c1 > c2)
print(c3 > c2)
print(c3 > c2 > c1)
print(c1)

