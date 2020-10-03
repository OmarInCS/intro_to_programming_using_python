
mark_list = input("Enter scores: ")
mark_list = mark_list.split(" ")
mark_list = [eval(m) for m in mark_list]
# print(mark_list)

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
