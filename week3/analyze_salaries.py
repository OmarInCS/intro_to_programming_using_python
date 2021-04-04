
n = eval(input("Enter num. of emps.: "))
salaries = []

for i in range(n):
    s = eval(input("Enter a salary: "))
    salaries.append(s)

avg = sum(salaries) / len(salaries)
print("Avg.:", avg)

count = 0
for s in salaries:
    if s > avg:
        count += 1

print("Above Avg.:", count)
