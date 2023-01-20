from week4.day1.patient import Patient

p1 = Patient("Omar", 72, 182)
p2 = Patient("Khalid", 72, 170)

print(p1.name, p1.get_status(), p1.get_bmi())
print(p2.name, p2.get_status(), p2.get_bmi())
