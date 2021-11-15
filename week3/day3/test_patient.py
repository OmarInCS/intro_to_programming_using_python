
from week3.day3.patient import Patient

name = input("Enter a name: ")
w, h = eval(input("Enter weight and height: "))

p1 = Patient(name, w, h)
p2 = Patient("Khalid", 85, 175)

print(p1.name, p1.get_status(), p1.get_bmi())
print(p2.name, p2.get_status(), p2.get_bmi())

