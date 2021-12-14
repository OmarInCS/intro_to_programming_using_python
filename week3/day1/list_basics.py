
marks = [23, 13, 25, 20]

print(marks[0])
print(marks[3])
print(marks[-1])
print(len(marks))
print(max(marks))
print(sum(marks) / len(marks))

marks.append(19)
print(marks)
marks.insert(0, 17)
print(marks)
# marks.remove(13)
# print(marks)
# marks.pop(0)
# print(marks)
marks.sort()
print(marks)
marks.sort(reverse=True)
print(marks)

print(marks[0:3])
print(13 in marks)