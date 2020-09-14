

marks = input("Enter student marks: ").split(" ")
marks = [eval(m) for m in marks]

best = max(marks)

grades = {"A": [], "B": [], "C": [],
          "D": [], "F": []}

for m in marks:
    if m >= best - 10:
        grades["A"].append(m)
    elif m >= best - 20:
        grades["B"].append(m)
    elif m >= best - 30:
        grades["C"].append(m)
    elif m >= best - 40:
        grades["D"].append(m)
    else:
        grades["F"].append(m)

for gr, mr in grades.items():
    print(gr, "=>", mr)
