
from week4.patient import Patient

# n = input("Enter a name: ")
# w, h = eval(input("Enter weight and height: "))
# p1 = Patient(n, w, h)
p1 = Patient("Omar", 65, 182)
p2 = Patient("Khalid", 75, 175)
# p3 = p2
p3 = Patient(p2.name, p2.weight, p2.height)

p3.weight += 10

print(p1.name, p1.get_status(), p1.get_bmi())
print(p2.name, p2.get_status(), p2.get_bmi())
print(p3.name, p3.get_status(), p3.get_bmi())
