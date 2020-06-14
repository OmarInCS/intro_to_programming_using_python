
nb_of_students = eval(input("Enter #students: "))

marks = []
for i in range(nb_of_students):
    m = eval(input("Enter student mark: "))
    marks.append(m)

avg = sum(marks) / len(marks)
print("Avg. is:", avg)

count = 0
for m in marks:
    if m > avg:
        count += 1

print("#stdeunts above avg.:", count)