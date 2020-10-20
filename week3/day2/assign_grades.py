

marks = input("Enter all marks: ").split(" ")
marks = [eval(m) for m in marks]
# print(marks)

best = max(marks)
grades_dict = {"A": [], "B": [], "C": [], "D": [], "F": []}

for i, m in enumerate(marks):
    if m > best - 10:
        print("Student ", i, ":", m, "=> A")
        grades_dict["A"].append(m)
    elif m > best - 20:
        print("Student ", i, ":", m, "=> B")
        grades_dict["B"].append(m)
    elif m > best - 30:
        print("Student ", i, ":", m, "=> C")
        grades_dict["C"].append(m)
    elif m > best - 40:
        print("Student ", i, ":", m, "=> D")
        grades_dict["D"].append(m)
    else:
        print("Student ", i, ":", m, "=> F")
        grades_dict["F"].append(m)


for g, marks in grades_dict.items():
    print(g, ":", marks)

