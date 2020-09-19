
from random import randint

score = 0

for i in range(5):
    x = randint(0, 10)
    y = randint(0, 10)
    answer = eval(input(f"What's {x} + {y}?\n>> "))

    if answer == x+y:
        print("Correct")
        score += 1
    else:
        print("Wrong")

    print("-" * 20)

print("Your score is:", score, "out of 5")