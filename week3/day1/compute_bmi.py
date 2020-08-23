
from week3.day1.patient import Patient

name, w, h = eval(input("Enter name, weight, height: "))

p1 = Patient(name, w, h)
print(p1.name)
print(p1.get_bmi())
print(p1.get_status())
print("-" * 20)

p2 = Patient("Khaled", 69, 1.7)
print(p2.name)
print(p2.get_bmi())
print(p2.get_status())
