
marks = input("Enter all marks: ")
marks = marks.split(" ")
marks = [eval(m) for m in marks]

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
