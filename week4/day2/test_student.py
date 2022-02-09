
from week4.day2.student import Student

s1 = Student("Ahmed", 23)
s2 = Student("Wael", 19)

Student.full_mark = 30
# s2.mark = 25
s2.set_mark(25)

# print(s2.get_mark())
print(s1.name, s1.get_grade(), s1.get_percent())
print(s2.name, s2.get_grade(), s2.get_percent())
