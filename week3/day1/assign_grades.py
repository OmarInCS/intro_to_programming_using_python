
n = eval(input("Enter the num. of students: "))

marks = []
for i in range(n):
    m = eval(input("Enter std. mark: "))
    marks.append(m)

best = max(marks)

for m in marks:
    if m >= best - 10:
        print(m, "=> A")
    elif m >= best - 20:
        print(m, "=> B")
    elif m >= best - 30:
        print(m, "=> C")
    elif m >= best - 40:
        print(m, "=> D")
    else:
        print(m, "=> F")

