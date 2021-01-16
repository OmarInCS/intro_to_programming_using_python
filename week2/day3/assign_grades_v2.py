
marks = input("Enter student marks: ")
marks = marks.split(" ")
marks = [eval(m) for m in marks]

best = max(marks)

for i, m in enumerate(marks):
    if m >= best - 10:
        print(f"Student #{i+1}, mark {m}, has grade A")
    elif m >= best - 20:
        print(f"Student #{i + 1}, mark {m}, has grade B")
    elif m >= best - 30:
        print(f"Student #{i + 1}, mark {m}, has grade C")
    elif m >= best - 40:
        print(f"Student #{i + 1}, mark {m}, has grade D")
    else:
        print(f"Student #{i + 1}, mark {m}, has grade F")