
from termcolor import colored

nb_of_students = eval(input("Enter the #students: "))

marks = []
for i in range(nb_of_students):
    m = eval(input("Enter student mark: "))
    marks.append(m)

best = max(marks)

print("The best mark:", best)

for m in marks:
    if m > best - 10:
        print(m, colored("Excellent", "green"))
    elif m > best - 20:
        print(m, colored("V. Good", "green"))
    elif m > best - 30:
        print(m, colored("Good", "yellow"))
    elif m > best - 40:
        print(m, colored("Pass", "yellow"))
    else:
        print(m, colored("Fail", "red"))