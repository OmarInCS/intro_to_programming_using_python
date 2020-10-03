
from week4.day2.student import Student

s1 = Student("Omar", 23)
s2 = Student("Khaled", 17)

# Student.final_mark += 5
# s2.__mark = 15
s2.set_mark(-15)

print(s1.name, s1.get_pct(), s1.get_grade())
print(s2.name, s2.get_pct(), s2.get_grade())
