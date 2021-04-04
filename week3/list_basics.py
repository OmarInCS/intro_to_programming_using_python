
marks = [19, 23, 13, 21]

print(marks)
print(marks[0])
print(marks[-1])
print(len(marks))
print(max(marks))

marks.append(15)
print(marks)
marks.insert(0, 17)
print(marks)
marks.insert(1, 50)
print(marks)

marks.remove(50)
print(marks)
marks.pop(3)
print(marks)

marks.sort(reverse=True)
print(marks)
