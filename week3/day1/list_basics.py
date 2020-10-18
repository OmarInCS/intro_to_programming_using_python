
marks = [20, 15, 23, 10]
print(marks)
print(marks[0])
print(marks[-1])

print(len(marks))
print(max(marks))
print(min(marks))
print(sum(marks) / len(marks))

marks.sort()
print(marks)
marks.append(25)
print(marks)
marks.insert(0, 5)
print(marks)
marks[0] = 7
print(marks)
# marks.remove(7)
# print(marks)
# marks.pop(-1)
# print(marks)

print(marks[:3])
print(marks[-3:])

for m in marks:
    print(m)