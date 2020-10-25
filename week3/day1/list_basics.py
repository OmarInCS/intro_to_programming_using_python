
marks = [20, 13, 18, 23]
print(marks)
print(marks[0])
print(marks[-1])
print(len(marks))

marks.append(22)
print(marks)
marks.insert(0, 15)
print(marks)
marks.sort()
marks.reverse()
print(marks)

# marks.remove(20)
# print(marks)
# marks.pop(2)
# print(marks)

print(marks[:3])
print(marks[-3:])

print(20 in marks)