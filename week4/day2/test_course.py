from week4.day2.course import Course

c1 = Course("SQL", 1000)
c1.add_student("Baraa")
c1.add_student("Asmaa")
c1.add_student("Khalid")
print(c1.get_students())

c1.drop_student("Khalid")
print(c1.get_students())

c2 = Course("Java", 1200)
c2.add_student("Khalid")
c2 += "Belal"
print(c2.get_students())

print(c1 > c2)
