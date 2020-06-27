
n = eval(input("Enter the group size: "))
total = 0

for i in range(n):
    age = eval(input("Enter the person age: "))
    if age > 65:
        total += 14
    elif age > 12:
        total += 23
    elif age > 2:
        total += 17

print("Total Cost:", total, "SAR")