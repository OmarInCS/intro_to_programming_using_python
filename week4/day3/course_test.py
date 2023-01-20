from week4.day3.course import Course

c1 = Course("Java", 1200)
c2 = Course("SQL", 1000)

c1.add_student("Ahmed")
c1.add_student("Wael")
c1.add_student("Ali")
c1 + "Abbass"

print(c1.get_students())
print(c1.get_nb_students())

c1.drop_student("Wael")
print(c1.get_students())
print(c1.get_nb_students())


print(c1 > c2)
print(c1)


# a1.deposit(500)
# a1 + 500
# a1 - 500