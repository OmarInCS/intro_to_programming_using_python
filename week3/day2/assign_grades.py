
n = eval(input("Enter #students: "))

scores = []
for i in range(n):
    mark = eval(input("Enter a mark: "))
    scores.append(mark)

best = max(scores)

for mark in scores:
    if mark > best - 10:
        print(mark, "=> Excellent")
    elif mark > best - 20:
        print(mark, "=> V. Good")
    elif mark > best - 30:
        print(mark, "=> Good")
    elif mark > best - 40:
        print(mark, "=> Pass")
    else:
        print(mark, "=> Fail")
