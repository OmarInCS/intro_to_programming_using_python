from week3.day4.student import Student

s1 = Student("Ali", 23)
s2 = Student("Wael", 19)

Student.full_mark = 30
# s2.mark = 30
s2.set_mark(-30)

print(s1.name, s1.get_percentage(), s1.get_grade())
print(s2.name, s2.get_percentage(), s2.get_grade())