from week3.day4.course import Course

c1 = Course("SQL")
c1.add_student("Ahmed")
c1.add_student("Ali")
c1.add_student("Walid")

print(c1.get_students())
print(c1.get_nb_of_students())

c1.drop_student("Ali")

print(c1.get_students())
print(c1.get_nb_of_students())
