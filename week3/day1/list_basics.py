
marks = [23, 15, 25, 17]

print(marks)
print(marks[0])
print(marks[-1])
print(len(marks))

marks.append(20)
print(marks)

marks.insert(0, 12)
print(marks)

marks.remove(15)
print(marks)

marks.pop(0)
print(marks)

marks.sort(reverse=True)
print(marks)

print(13 in marks)
