
# A => m >= best - 10
# B => m >= best - 20
# c => m >= best - 30
# D => m >= best - 40
# F => else

num_of_students = eval(input("Enter the number of students: "))
marks = []

for i in range(num_of_students):
    m = eval(input("Enter the mark: "))
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


