
# A => m >= best - 10
# B => m >= best - 20
# c => m >= best - 30
# D => m >= best - 40
# F => else

marks = input("Enter all marks: ")
marks = marks.split(" ")
marks = [eval(m) for m in marks]

best = max(marks)

grades_count = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0}

for m in marks:
    if m >= best - 10:
        print(m, "=> A")
        grades_count["A"] += 1
    elif m >= best - 20:
        print(m, "=> B")
        grades_count["B"] += 1
    elif m >= best - 30:
        print(m, "=> C")
        grades_count["C"] += 1
    elif m >= best - 40:
        print(m, "=> D")
        grades_count["D"] += 1
    else:
        print(m, "=> F")
        grades_count["F"] += 1

print("-" * 20)
for k, v in grades_count.items():
    print(k, "=>", v)

# A => 2
# B => 2
# C => 2
# D => 1
# F => 0
