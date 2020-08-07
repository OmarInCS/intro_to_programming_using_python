
from week4.day1.patient import Patient

p1 = Patient("Omar", 65, 1.82)
print("BMI:", p1.get_bmi())
print("Status: ", p1.get_status())

# p2 = Patient(p1.name, p1.weight, p1.height)
p2 = p1

print(p2.get_bmi())

p1.weight += 2

print(p1.get_bmi())
print(p2.get_bmi())