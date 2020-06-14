
marks = [24, 20, 15, 18, 23]
colors = ["red", "green", "blue"]

print(colors[0])
print(colors[-1])
print(len(colors))

colors.append("white")
colors.insert(0, "yellow")
print(colors)
colors.remove("green")
print(colors)
colors.pop(0)
print(colors)

marks.sort()
print(marks)
marks.reverse()
print(marks)

colors.sort()
print(colors)

marks = marks + [10, 25, 17]
print(marks)

marks.sort()
marks.reverse()
print(marks)
print(marks[:3])
print(marks[-3:])

print(23 in marks)
print(13 in marks)

# for i in range(len(marks)):
#     print(marks[i])

from termcolor import colored

for m in marks:
    if m > 20:
        print(colored(m, "green"))
    else:
        print(colored(m, "red"))


