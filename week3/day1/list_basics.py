
marks = [23, 10, 17, 24]

print(marks)
print(marks[0])
print(marks[-1])
print(len(marks))
print(max(marks))
print(sum(marks) / len(marks))

marks.append(15)
print(marks)

marks.insert(0, 25)
print(marks)

# marks.remove(10)
# print(marks)
#
# # marks.pop(2)
# # print(marks)
#
# del marks[2]
# print(marks)

marks.sort()
marks.reverse()
print(marks)