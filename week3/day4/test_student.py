
from week3.day4.student import Student

s1 = Student("Omar", 23)
s2 = Student("Khaled", 20)

# Student.final_mark = 30
# s2.__mark = 21
s2.set_mark(-21)

print(s1.name, s1.get_grade(), s1.get_pct())
print(s2.name, s2.get_grade(), s2.get_pct())
