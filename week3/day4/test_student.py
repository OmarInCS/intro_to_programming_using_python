from week3.day4.student import Student

s1 = Student("Omar", 23)
s2 = Student("Wael", 19)

Student.full_mark = 30
# s1.__mark = -30
s1.set_mark(30)

print(s1.get_name(), s1.get_grade(), s1.get_percentage())
print(s2.get_name(), s2.get_grade(), s2.get_percentage())
