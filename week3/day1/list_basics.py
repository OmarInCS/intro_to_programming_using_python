
marks = [23, 12, 25, 15, 20]

print(marks)
print(marks[0])
print(marks[-1])
print(len(marks))

marks.append(18)
print(marks)
marks.insert(0, 13)
print(marks)

marks.remove(12)
print(marks)
marks.pop(2)
print(marks)

marks.sort(reverse=True)
print(marks)

print(marks[:3])
print(18 in marks)
