
from week3.day1.patient import Patient

p1 = Patient("Omar", 65, 182)
p2 = Patient("Khaled", 85, 175)

print(p1.name, p1.get_status(), p1.get_bmi())
print(p2.name, p2.get_status(), p2.get_bmi())
