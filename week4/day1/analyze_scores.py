
scores = input("Enter scores: ")
scores = scores.split(" ")
scores = [eval(s) for s in scores]

avg = sum(scores) / len(scores)
print("Avg.:", avg)

count = 0
for s in scores:
    if s >= avg:
        count += 1

print("Students above avg.:", count)