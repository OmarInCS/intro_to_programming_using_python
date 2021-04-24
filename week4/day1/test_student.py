
from week4.day1.student import Student

s1 = Student("Omar", 23)
s2 = Student("Khalid", 19)

# Student.full_mark = 30
# s1.__mark = 19
s1.set_mark(25)
# print(s1.get_mark())

print(s1.name, s1.get_grade(), s1.get_pct())
print(s2.name, s2.get_grade(), s2.get_pct())