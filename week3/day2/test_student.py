
from week3.day2.student import Student

s1 = Student("Ahmed", 25)
s2 = Student("Fahad", 15)

# Student.final_mark = 30
# s2.__mark = 20
s2.set_mark(20)

print(s1.name, s1.get_grade(), s1.get_pct())
print(s2.name, s2.get_grade(), s2.get_pct())