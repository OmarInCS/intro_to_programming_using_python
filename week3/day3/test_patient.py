
from week3.day3.patient import Patient

p1 = Patient("Omar", 68, 182)
p2 = Patient("Khalid", 75, 175)

print(p1.name, p1.get_status(), p1.get_bmi())
print(p2.name, p2.get_status(), p2.get_bmi())
