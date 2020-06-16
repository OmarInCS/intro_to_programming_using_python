

from week3.day3.patient import Patient

p1 = Patient("Omar", 65, 1.82)
p2 = Patient("Ahmed", 70, 1.69)

print(p1.name, p1.get_bmi(), p1.get_status())
print(p2.name, p2.get_bmi(), p2.get_status())

