
salaries = input("Enter emps. salaries: ")
salaries = salaries.split(" ")
salaries = [eval(s) for s in salaries]

avg = sum(salaries) / len(salaries)
print(avg)

level_count = {"high": 0, "normal": 0, "low": 0}

count= 0
for s in salaries:

    if s >= 12000:
        level_count["high"] += 1
    elif s >= 6000:
        level_count["normal"] += 1
    else:
        level_count["low"] += 1

    if s >= avg:
        count +=1
print(count)

for l, c in level_count.items():
    print(l, "=>", c)
