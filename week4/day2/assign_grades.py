
marks = input("Enter student marks: ")
marks = marks.split(" ")
marks = [eval(m) for m in marks]

best = max(marks)

marks.sort(reverse=True)

counts = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0}

for i, m in enumerate(marks):
    if m >= best - 10:
        print(f"Student {i}, {m} => A")
        counts["A"] += 1
    elif m >= best - 20:
        print(f"Student {i}, {m} => B")
        counts["B"] += 1
    elif m >= best - 30:
        print(f"Student {i}, {m} => C")
        counts["C"] += 1
    elif m >= best - 40:
        print(f"Student {i}, {m} => D")
        counts["D"] += 1
    else:
        print(f"Student {i}, {m} => F")
        counts["F"] += 1

print("-" * 30)
for grade, count in counts.items():
    print(grade, "number of students:", count)
