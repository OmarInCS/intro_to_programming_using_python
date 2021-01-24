
marks = [23, 19, 21, 13]

print(marks)
print(marks[0])
print(marks[-1])
print(len(marks))
print(max(marks))
print(min(marks))
print(sum(marks) / len(marks))

marks.append(17)
print(marks)

marks.insert(0, 25)
print(marks)

# marks.remove(13)
# print(marks)

# marks.pop(4)
# print(marks)

marks.sort()
print(marks)

print(marks[-3:])
print(marks[:3])

marks = marks + [15, 22]
print(marks)

print(marks * 3)