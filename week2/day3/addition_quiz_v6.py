
from random import randint

score = 0

for i in range(5):
    x = randint(0, 10)
    y = randint(0, 10)

    for j in range(3):
        answer = eval(input(f"{i+1}- What's {x} + {y}?\n>> "))

        if answer == x+y:
            print("Correct Answer")
            score += 1
            break
        else:
            print("Wrong Answer")

    print("-" * 20)

print("Your Score:", score, "out of 5")