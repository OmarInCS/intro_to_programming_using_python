
from week3.day3.student import Student

# n, m = eval(input("Enter name and mark: "))
# s1 = Student(n, m)
s1 = Student("Omar", 23)
s2 = Student("Khaled", 19)

# Student.final_mark = 30
# s2.__mark = 25
s2.set_mark(-25)

print(s1.name, s1.get_grade(), s1.get_pct())
print(s2.name, s2.get_grade(), s2.get_pct())
