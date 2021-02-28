
marks = [23, 13, 19, 24]

print(marks)
print(marks[0])
print(marks[-1])
print(len(marks))
print(max(marks))

marks.append(21)
print(marks)
marks.insert(0, 10)
print(marks)
marks[0] = 15
print(marks)

# marks.remove(13)
# print(marks)
# marks.pop(2)
# print(marks)

marks.sort(reverse=True)
print(marks)

print(marks[:3])
print(marks[-3:])