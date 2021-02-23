
from random import randint

n = eval(input("Enter number of questions: "))
score = 0

for i in range(n):
    x = randint(0, 10)
    y = randint(0, 10)

    for j in range(3):
        answer = eval(input(f"What's {x} + {y} ? "))

        if answer == x+y:
            print("Correct")
            score += 1
            break
        else:
            print("Wrong")

    print("-" * 20)

print("Score:", score, "out of", n)

