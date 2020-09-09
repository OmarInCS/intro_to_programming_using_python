
marks = [22, 15, 23, 13]
colors = ["red", "green", "blue"]

print(marks[0])
print(marks[-1])
print(marks[3])
print(max(marks))
print(min(marks))
print(sum(marks) / len(marks))

marks.append(17)
print(marks)

marks.insert(0, 25)
print(marks)

marks[4] = 23
print(marks)

marks.sort()
marks.reverse()
print(marks)

print(marks[0:3])

# marks.remove(22)
marks.pop(3)
print(marks)