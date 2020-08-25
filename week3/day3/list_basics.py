
marks = [22, 13, 17, 23]
days = ["Sunday", "Monday", "Tuesday"]

print(marks)
print(marks[0])
print(marks[-1])

marks.sort(reverse=True)
print(marks)
marks.append(10)
print(marks)
marks.insert(2, 19)
print(marks)
marks[-2] = 15
print(marks)
print(marks[0:3])
marks.remove(15)
print(marks)
marks.pop(2)
print(marks)

marks_copy = marks.copy()
print(marks_copy)