
marks = [23, 13, 24, 19]

print(marks)
print(marks[0])
print(marks[-1])
print(len(marks))
print(max(marks))

marks.append(17)
print(marks)
marks.insert(0, 25)
print(marks)

# marks.remove(13)
# print(marks)
# marks.pop(3)
# print(marks)

marks.sort(reverse=True)
print(marks)
print(marks[:3])
print(marks[-3:])
print(19 in marks)
