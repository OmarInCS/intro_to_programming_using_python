
from week3.day1.patient import Patient

p1 = Patient("Omar", 65, 1.82)
p2 = Patient("Khaled", 75, 1.72)

print(p1.name, p1.get_status(), p1.get_bmi())
print(p2.name, p2.get_status(), p2.get_bmi())
