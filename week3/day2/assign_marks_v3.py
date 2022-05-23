
marks = input("Enter students marks: ")
marks = marks.split(" ")
marks = [eval(m) for m in marks]
# print(marks)

best = max(marks)
grades_counts = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0}

for m in marks:
    if m >= best - 10:
        print(m, "=> A")
        grades_counts["A"] += 1
    elif m >= best - 20:
        print(m, "=> B")
        grades_counts["B"] += 1
    elif m >= best - 30:
        print(m, "=> C")
        grades_counts["C"] += 1
    elif m >= best - 40:
        print(m, "=> D")
        grades_counts["D"] += 1
    else:
        print(m, "=> F")
        grades_counts["F"] += 1

for g, c in grades_counts.items():
    print(g, "=>", c)