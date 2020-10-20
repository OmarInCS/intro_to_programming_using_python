
marks = input("Enter all marks: ").split(" ")
marks = [eval(m) for m in marks]

avg = sum(marks) / len(marks)

print("Avg.:", avg)

count = 0
for m in marks:
    if m > avg:
        count += 1

print("Above average:", count)
