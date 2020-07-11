
scores = input("Enter scores: ")
scores = scores.split(" ")
scores = [eval(s) for s in scores]

best = max(scores)

for s in scores:
    if s >= best - 10:
        print(s, "Grade A")
    elif s >= best - 20:
        print(s, "Grade B")
    elif s >= best - 30:
        print(s, "Grade C")
    elif s >= best - 40:
        print(s, "Grade D")
    else:
        print(s, "Grade F")
