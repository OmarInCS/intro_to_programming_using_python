
n = eval(input("Enter #students: "))

marks = []
for i in range(n):
    m = eval(input("Enter a mark: "))
    marks.append(m)

best = max(marks)
print("The best Mark:", best)

for x in marks:
    if x > best - 5:
        print(f"{x} => A")
    elif x > best - 10:
        print(f"{x} => B")
    elif x > best - 15:
        print(f"{x} => C")
    else:
        print(f"{x} => F")
