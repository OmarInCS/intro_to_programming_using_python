
n = eval(input("Enter #employees: "))

salaries = []
for i in range(n):
    salary = eval(input("Enter a salary: "))
    salaries.append(salary)

avg = sum(salaries) / n
print("Avg is:", avg)

count = 0
for salary in salaries:
    if salary > avg:
        count += 1

print("#employees above avg.:", count)
