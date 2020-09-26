
n = eval(input("Enter num. of students: "))

mark_list = []

for i in range(n):
    mark = eval(input("Enter a mark: "))
    mark_list.append(mark)

best = max(mark_list)

for m in mark_list:
    if m > best - 10:
        print(m, "=> A")
    elif m > best - 20:
        print(m, "=> B")
    elif m > best - 30:
        print(m, "=> C")
    elif m > best - 40:
        print(m, "=> D")
    else:
        print(m, "=> F")
