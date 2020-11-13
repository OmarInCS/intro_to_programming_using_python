
from week4.day1.student import Student

s1 = Student("Ahmed", 23)
s2 = Student("Walid", 19)

# s2.__mark = 210
s2.set_mark(21)
# Student.final_mark = 30

print(s1.get_grade(), s1.get_percentage())
print(s2.get_grade(), s2.get_percentage())
