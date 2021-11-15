from week3.day4.student import Student

s1 = Student("Omar", 23)
s2 = Student("Khalid", 20)

Student.full_mark = 30
# s2.__mark = 30
s2.set_mark(30)

print(s1.name, s1.find_grade(), s1.calc_percentage())
print(s2.name, s2.find_grade(), s2.calc_percentage())
print(s2.get_mark())
