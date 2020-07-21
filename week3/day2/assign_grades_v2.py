
scores = input("Enter scores: ").split(" ")
scores = [eval(s) for s in scores]

best = max(scores)

counts = {"Excellent": 0, "V. Good": 0, "Good": 0, "Pass": 0, "Fail": 0}

for mark in scores:
    if mark > best - 10:
        print(mark, "=> Excellent")
        counts["Excellent"] += 1
    elif mark > best - 20:
        print(mark, "=> V. Good")
        counts["V. Good"] += 1
    elif mark > best - 30:
        print(mark, "=> Good")
        counts["Good"] += 1
    elif mark > best - 40:
        print(mark, "=> Pass")
        counts["Pass"] += 1
    else:
        print(mark, "=> Fail")
        counts["Fail"] += 1


for grade, count in counts.items():
    print(grade, ":", count)