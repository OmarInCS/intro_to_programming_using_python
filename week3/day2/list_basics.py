
marks = [23, 17, 25, 13]

print(marks)
print(marks[0])
print(marks[-1])
print(len(marks))

marks.append(21)
print(marks)
marks.insert(0, 15)
print(marks)

marks.remove(13)
print(marks)
marks.pop(0)
print(marks)

marks.sort(reverse=True)
print(marks)
print(21 in marks)
