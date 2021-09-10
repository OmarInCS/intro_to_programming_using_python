
marks = input("Enter all marks: ")
marks = marks.split(" ")
marks = [eval(m) for m in marks]

best = max(marks)
grades_map = {"A": [], "B": [], "C": [], "D": [], "F": []}

for m in marks:
    if m >= best - 10:
        print(m, "=> A")
        grades_map["A"].append(m)
    elif m >= best - 20:
        print(m, "=> B")
        grades_map["B"].append(m)
    elif m >= best - 30:
        print(m, "=> C")
        grades_map["C"].append(m)
    elif m >= best - 40:
        print(m, "=> D")
        grades_map["D"].append(m)
    else:
        print(m, "=> F")
        grades_map["F"].append(m)

for grade, marks in grades_map.items():
    print(grade, "=>", marks)
