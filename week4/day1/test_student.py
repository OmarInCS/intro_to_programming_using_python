
from week4.day1.student import Student

s1 = Student("Omar", 25)
s2 = Student("Ahmed", 23)

Student.final_mark = 30
# s1.mark = 30
# s2.__mark = 37
s1.set_mark(30)
s2.set_mark(37)

print(s1.get_pct(), s1.get_status())
print(s2.get_pct(), s2.get_status())
