
from week3.day1.patient import Patient

name = input("Enter name: ")
w, h = eval(input("Enter weight and height: "))
p1 = Patient(name, w, h)

print(p1.name, p1.get_status(), p1.get_bmi())

p2 = Patient("Khaled", 70, 1.7)
print(p2.name, p2.get_status(), p2.get_bmi())