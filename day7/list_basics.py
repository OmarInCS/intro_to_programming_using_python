
marks = [23, 19, 13, 24]

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

marks.sort(reverse=True)
print(marks)

# marks.remove(23)
# print(marks)
# marks.pop(2)
# print(marks)

print(marks[:3])
print(marks[-3:])

dob = "19-5-1992"
dob = dob.split("-")
print(dob)
dob = " ".join(dob)
print(dob)
