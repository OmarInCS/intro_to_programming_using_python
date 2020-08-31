
from random import randint

score = 0

for i in range(5):
    x = randint(0, 10)
    y = randint(0, 10)
    answer = eval(input(f"{i+1}- What's {x} + {y} ? "))

    if answer == x+y:
        print("Correct")
        score += 1
    else:
        print("Wrong")

print("Your score is:", score)