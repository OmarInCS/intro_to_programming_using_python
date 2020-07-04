
from week3.day2.student import Student

s1 = Student("Omar", 23)
s2 = Student("Ahmed", 20)

# s1.__mark = 35
s1.set_mark(25)
# Student.final_mark = 30

print(s1.get_pct(), s1.get_grade())
print(s2.get_pct(), s2.get_grade())