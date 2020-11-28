from week3.day2.student import Student

s1 = Student("Omar", 23)
s2 = Student("Belal", 19)

# Student.final_mark = -30
# s2.__mark = 70
s2.set_mark(22)

print(s1.name, s1.get_grade(), s1.get_percentage())
print(s2.name, s2.get_grade(), s2.get_percentage())