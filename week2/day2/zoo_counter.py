
count = eval(input("How many Person? "))
total = 0

for i in range(count):
    age = eval(input(f"Enter age of Person {i+1}: "))
    if age >= 3 and age < 15:
        total += 15
    elif age >= 15 and age < 61:
        total += 25
    elif age >= 61:
        total += 20

print("Total Cost:", total, "SAR")