
n = eval(input("Enter number of students: "))

marks = []
for i in range(n):
    m = eval(input("Enter student mark: "))
    marks.append(m)

avg = sum(marks) / len(marks)
print("Average:", avg)

count = 0
for m in marks:
    if m > avg:
        count += 1

print("students above average: ", count)
