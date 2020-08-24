
from week3.day2.student import Student

s1 = Student("Omar", 23)
s2 = Student("Khalid", 20)

# s1.__mark = 22
s1.set_mark(22)
# Student.final_mark = 30

print(s1.name, s1.get_percentage(), s1.get_grade())
print(s2.name, s2.get_percentage(), s2.get_grade())

