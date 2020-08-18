
from random import randint

score = 0

for i in range(1, 6):
    x = randint(0, 10)
    y = randint(0, 10)

    for t in range(1, 4):

        answer = eval(input(f"{i}- What's {x} + {y} ?\n>> "))

        if answer == x+y:
            print("Correct")
            score += 1
            break
        else:
            print("Wrong")

    print("-" * 30)

print("Your Score is:", score, "out of 5")