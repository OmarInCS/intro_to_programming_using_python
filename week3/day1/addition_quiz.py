
from random import randint

n = eval(input("Enter the number of questions: "))
score = 0

for i in range(1, n+1):
    x = randint(0, 10)
    y = randint(0, 10)

    for j in range(3):
        answer = eval(input(f"{i}) What's {x} * {y} ? "))

        if answer == x*y:
            print("Correct Answer")
            score += 1
            break
        else:
            print("Wrong Answer")

    print("-" * 25)

print("Your score:", score, "out of", n)
