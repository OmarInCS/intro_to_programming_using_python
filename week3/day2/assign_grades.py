
scores = input("Enter scores: ")
scores = scores.split(" ")
scores = [eval(s) for s in scores]
# print(scores)

best = max(scores)

for i, s in enumerate(scores):
    if s > best - 10:
        print("Student", i, "score", s, "grade A")
    elif s > best - 20:
        print(f"Student {i} score {s} grade B")
    elif s > best - 30:
        print("Student", i, "score", s, "grade C")
    elif s > best - 40:
        print("Student", i, "score", s, "grade D")
    else:
        print("Student", i, "score", s, "grade F")
