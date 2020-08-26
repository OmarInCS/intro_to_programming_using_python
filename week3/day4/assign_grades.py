
# n = eval(input("Enter number of students: "))
#
# marks = []
# for i in range(n):
#     m = eval(input(f"Enter mark {i+1}: "))
#     marks.append(m)

marks = input("Enter student marks: ")
marks = marks.split(" ")
marks = [eval(m) for m in marks]
# print(marks)

best = max(marks)

marks.sort(reverse=True)

for i, m in enumerate(marks):
    if m >= best - 10:
        print(f"Student {i}, {m} => A")
    elif m >= best - 20:
        print(f"Student {i}, {m} => B")
    elif m >= best - 30:
        print(f"Student {i}, {m} => C")
    elif m >= best - 40:
        print(f"Student {i}, {m} => D")
    else:
        print(f"Student {i}, {m} => F")

