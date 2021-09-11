from week3.day2.student import Student

s1 = Student("Omar", 23)
s2 = Student("Khalid", 20)

# Student.full_mark = 30
# s2.__mark = -25
s2.set_mark(-25)

print(s1.get_name(), s1.find_grade(), s1.calc_pct())
print(s2.get_name(), s2.find_grade(), s2.calc_pct())