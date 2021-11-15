from week4.day1.course import Course

x = Course("Java", 1000)
# y = x
y = Course(x.get_title(), x.get_price())

y.add_student("Ahmed")

print(x)
print(y)

