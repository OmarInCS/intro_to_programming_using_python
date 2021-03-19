
marks_lst = input("Enter all marks: ")
marks_lst = marks_lst.split(" ")
marks_lst = [eval(m) for m in marks_lst]

best = max(marks_lst)
for m in marks_lst:
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
