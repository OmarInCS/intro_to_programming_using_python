
n = eval(input("Enter number of students: "))

marks = []
for i in range(n):
    m = eval(input("Enter student mark: "))
    marks.append(m)

best = max(marks)

for m in marks:
    if m >= best - 10:
        print(m, "=> Excellent")
    elif m >= best - 20:
        print(m, "=> V. Good")
    elif m >= best - 30:
        print(m, "=> Good")
    elif m >= best - 40:
        print(m, "=> Pass")
    else:
        print(m, "=> Fail")
