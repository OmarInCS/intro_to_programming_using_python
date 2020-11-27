
salaries = [4500, 7000, 5000, 12000]

print(salaries)
print(salaries[0])
print(salaries[-1])
print(salaries[:3])
print(salaries[-3:])
print(len(salaries))
print(max(salaries))
print(min(salaries))
print(sum(salaries) / len(salaries))

salaries.append(3500)
print(salaries)
salaries.insert(0, 6500)
print(salaries)
salaries[1] += 500
print(salaries)
salaries.sort()
print(salaries)

salaries.remove(5000)
print(salaries)
salaries.pop(1)
print(salaries)
