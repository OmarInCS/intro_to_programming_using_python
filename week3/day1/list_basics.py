
marks = [19, 23, 13, 24]

print(marks)
print(marks[0])
print(marks[-1])
print(len(marks))

marks.append(21)
print(marks)
marks.insert(0, 12)
print(marks)
marks[0] = 22
print(marks)

marks.sort(reverse=True)
print(marks)

print(marks[:3])
print(marks[-3:])

marks.remove(13)
print(marks)
marks.pop(0)
print(marks)