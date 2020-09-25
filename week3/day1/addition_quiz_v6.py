
from random import randint

for i in range(5):
    x = randint(0, 10)
    y = randint(0, 10)

    for j in range(3):
        answer = eval(input(f"What's {x} + {y}? "))
        if answer == x+y:
            print("Correct")
            break
        else:
            print("Wrong")

    print("-" * 20)
