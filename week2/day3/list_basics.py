
marks = [23, 13, 20, 10]

print(marks[0])
print(marks[-1])
print(len(marks))
print(max(marks))
print(min(marks))
print(sum(marks) / len(marks))

marks.append(25)
print(marks)
marks.insert(0, 19)
print(marks)
# marks.remove(13)
# print(marks)
# marks.pop(2)
# print(marks)
marks.sort(reverse=True)
print(marks)
print(marks.count(13))
print(13 in marks)
print(marks[:3])
print(marks[-3:])