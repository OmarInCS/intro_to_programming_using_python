
salaries = input("Enter all salaries: ")
salaries = salaries.split(",")
salaries = [eval(s) for s in salaries]
# print(salaries)

avg = sum(salaries) / len(salaries)
print("Avg.:", avg)

count = 0
for s in salaries:
    if s > avg:
        count += 1

print("Above Avg.:", count)