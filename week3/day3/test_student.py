
from week3.day3.student import Student

s1 = Student("Ahmed", 22)
s2 = Student("Belal", 25)

# s1.__mark = 27
s1.set_mark(24)
# Student.final_mark = 30

print(s1.name, s1.get_grade(), s1.get_pct())
print(s2.name, s2.get_grade(), s2.get_pct())