

marks = input("Enter student marks: ").split(" ")
marks = [eval(m) for m in marks]

best = max(marks)

grades = {"A": 0, "B": 0, "C": 0,
          "D": 0, "F": 0}

for m in marks:
    if m >= best - 10:
        grades["A"] += 1
    elif m >= best - 20:
        grades["B"] += 1
    elif m >= best - 30:
        grades["C"] += 1
    elif m >= best - 40:
        grades["D"] += 1
    else:
        grades["F"] += 1

with open("report.txt", "w") as file:
    for gr, mr in grades.items():
        print(gr, "=>", mr)

        file.write(f"{gr} => {mr}\n")
