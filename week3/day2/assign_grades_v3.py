
marks = input("Enter all marks: ")
marks = marks.split(" ")
marks = [eval(m) for m in marks]

grade_counts = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0}

for m in marks:
    if m > 85:
        grade_counts["A"] += 1
    elif m > 75:
        grade_counts["B"] += 1
    elif m > 65:
        grade_counts["C"] += 1
    elif m >= 50:
        grade_counts["D"] += 1
    else:
        grade_counts["F"] += 1

for g, c in grade_counts.items():
    print(g, "=>", c)
