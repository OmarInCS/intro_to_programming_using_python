
from week3.day3.student import Student

s1 = Student("Omar", 23)
s2 = Student("Ahmed", 19)

# s1.mark = 24
s1.set_mark(27)
# Student.final_mark = 30

print(s1.name, s1.get_pct(), s1.get_grade())
print(s2.name, s2.get_pct(), s2.get_grade())