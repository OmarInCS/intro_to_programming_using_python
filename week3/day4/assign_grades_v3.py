
import json

file_name = input("Enter a file name: ")
with open(file_name) as file:
    marks = file.readlines()
    marks = [eval(m) for m in marks]
print(marks)

best = max(marks)
grades_count = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0}

for m in marks:
    if m >= best - 10:
        grades_count["A"] += 1
    elif m >= best - 20:
        grades_count["B"] += 1
    elif m >= best - 30:
        grades_count["C"] += 1
    elif m >= best - 40:
        grades_count["D"] += 1
    else:
        grades_count["F"] += 1

# with open("report.txt", "w") as file:
#     for g, c in grades_count.items():
#         print(g, "=>", c, file=file)

with open("report.json", "w") as file:
    json.dump(grades_count, file)
