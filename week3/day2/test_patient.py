
from week3.day2.patient import Patient

p1 = Patient("Omar", 65, 1.82)
p2 = Patient("Khaled", 85, 1.72)
# p3 = p2
p3 = p2.copy()

p3.weight = 120

print(p1.name, p1.get_status(), p1.get_bmi())
print(p2.name, p2.get_status(), p2.get_bmi())
