
from week3.day4.course import Course

c1 = Course("SQL")
c1.add_student("Ahmed")
c1.add_student("Walid")
c1.add_student("Ali")
c1.add_student("Fahad")

print(c1.get_students())

c1.drop_student("Walid")
print(c1.get_students())

c2 = Course("Java")
c2.add_student("Walid")
c2 + "Omar"
print(c2.get_students())

print(c1 > c2)
print(c1)
