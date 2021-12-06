
n = eval(input("Enter num. of visitors: "))
total = 0

for i in range(n):
    age = eval(input("Enter visitor age: "))
    if age > 50:
        total += 12
    elif age > 23:
        total += 15
    elif age > 2:
        total += 10

print("Total cost:", total)
