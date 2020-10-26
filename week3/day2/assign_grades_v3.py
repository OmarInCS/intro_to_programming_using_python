
marks = input("Enter the marks: ")
marks = marks.split(" ")
marks = [eval(m) for m in marks]

best = max(marks)

count_dict = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0}

for m in marks:
    if m >= best - 10:
        print(m, "=> A")
        count_dict["A"] += 1
    elif m > best - 20:
        print(m, "=> B")
        count_dict["B"] += 1
    elif m > best - 30:
        print(m, "=> C")
        count_dict["C"] += 1
    elif m > best - 40:
        print(m, "=> D")
        count_dict["D"] += 1
    else:
        print(m, "=> F")
        count_dict["F"] += 1

for grade, count in count_dict.items():
    print(grade, "=>", count)