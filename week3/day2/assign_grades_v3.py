

marks = input("Enter all marks: ").split(" ")
marks = [eval(m) for m in marks]
# print(marks)

best = max(marks)
grades_dict = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0}

for i, m in enumerate(marks):
    if m >= best - 10:
        print("Student ", i, ":", m, "=> A")
        grades_dict["A"] += 1
    elif m >= best - 20:
        print("Student ", i, ":", m, "=> B")
        grades_dict["B"] += 1
    elif m >= best - 30:
        print("Student ", i, ":", m, "=> C")
        grades_dict["C"] += 1
    elif m >= best - 40:
        print("Student ", i, ":", m, "=> D")
        grades_dict["D"] += 1
    else:
        print("Student ", i, ":", m, "=> F")
        grades_dict["F"] += 1


for g, marks in grades_dict.items():
    print(g, ":", marks)

