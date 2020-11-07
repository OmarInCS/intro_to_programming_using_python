
from week3.day2.customer import Customer

c1 = Customer("Omar", 65, 1.82)
c2 = Customer("Khaled", 85, 1.75)

print(c1.name, c1.get_status(), c1.get_bmi())
print(c2.name, c2.get_status(), c2.get_bmi())

