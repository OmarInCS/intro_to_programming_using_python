
from week3.day3.student import Student

s1 = Student("Omar", 23)
s2 = s1
# s2 = Student(s1.name, s1.get_mark())

s2.set_mark(20)

print(s1.get_pct())
print(s2.get_pct())