
marks = [19, 23, 25, 13]

print(marks)
print(len(marks))
print(marks[0])
print(marks[-1])

marks.append(15)
print(marks)

marks.insert(0, 17)
print(marks)

# marks.remove(13)
# print(marks)

# marks.pop(2)
# print(marks)

marks.sort(reverse=True)
print(marks)

print(13 in marks)
print(marks[:3])
