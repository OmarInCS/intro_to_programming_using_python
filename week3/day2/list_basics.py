
marks = [23, 20, 10, 22]
colors = ["red", "green", "blue"]

print(len(marks))
print(marks[0])
print(marks[-1])

print(max(marks))
print(min(marks))
print(sum(marks) / len(marks))

marks.append(19)
print(marks)

marks.insert(2, 13)
print(marks)

marks.remove(13)
print(marks)

marks.pop(2)
print(marks)

marks.extend([21, 18, 13, 10])
print(marks)

marks.sort()
print(marks)

marks.reverse()
print(marks)

print(marks[:3])
print(marks[-3:])

# for i in range(len(marks)):
#     print(marks[i])

for x in marks:
    print(x)


