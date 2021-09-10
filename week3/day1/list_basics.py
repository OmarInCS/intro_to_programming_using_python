
marks = [23, 17, 24, 13]
print(marks)
print(marks[0])
print(marks[-1])
print(marks[:2])
print(len(marks))

marks.append(25)
print(marks)
marks.insert(0, 10)
print(marks)
marks[0] = 15
print(marks)

marks.remove(17)
print(marks)
marks.pop(3)
print(marks)

marks.sort(reverse=True)
print(marks)
print(17 in marks)



