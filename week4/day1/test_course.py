from week4.day1.course import Course

c1 = Course("Java", 1000)
c1.add_student("Ahmed")
c1.add_student("Wael")
c1.add_student("Abbas")

print(c1.get_nb_students())
print(c1.get_students())

c1.drop_student("Wael")
print(c1.get_nb_students())
print(c1.get_students())

c2 = Course("Flutter", 1500)
c2 += "Wael"
print(c2.get_students())

print(c1 > c2)
