n = eval(input("Enter num. of students: "))

marks = []
for i in range(n):
    m = eval(input("Enter a mark: "))
    marks.append(m)

avg = sum(marks) / n

count = 0
for m in marks:
    if m > avg:
        count += 1

print("Average:", avg)
print("#above Average:", count)
