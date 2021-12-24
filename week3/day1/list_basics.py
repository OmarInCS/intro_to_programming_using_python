
marks = [23, 10, 22, 17]

print(marks)
print(marks[1])
print(marks[-1])
print(len(marks))

marks.append(25)
print(marks)
marks.insert(0, 15)
print(marks)

# marks.remove(10)
# print(marks)
# marks.pop(0)
# print(marks)

print(10 in marks)
marks.sort()
print(marks)
marks.sort(reverse=True)
print(marks)
print(marks[:3])
print(max(marks))