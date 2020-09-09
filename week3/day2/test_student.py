
from week3.day2.student import Student

s1 = Student("Omar", 23)
s2 = Student("Khaled", 19)

Student.final_mark = 30
# s2.__mark = -20
s2.set_mark(-23)

print(s1.name, s1.get_pct(), s1.get_grade())
print(s2.name, s2.get_pct(), s2.get_grade())
