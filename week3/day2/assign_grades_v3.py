
marks = input("Enter all marks: ")
marks = marks.split(" ")
marks = [eval(m) for m in marks]

best = max(marks)
grade_counts = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0}

for m in marks:
    if m >= best - 10:
        print(m, "=> A")
        grade_counts["A"] += 1
    elif m >= best - 20:
        print(m, "=> B")
        grade_counts["B"] += 1
    elif m >= best - 30:
        print(m, "=> C")
        grade_counts["C"] += 1
    elif m >= best - 40:
        print(m, "=> D")
        grade_counts["D"] += 1
    else:
        print(m, "=> F")
        grade_counts["F"] += 1

for grade, count in grade_counts.items():
    print(grade, "=>", count)
