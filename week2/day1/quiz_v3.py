
from random import randint

n = eval(input("How many questions? "))
score = 0

for i in range(n):
    x = randint(0, 10)
    y = randint(0, 10)
    answer = eval(input(f"What's {x} * {y} ? "))

    if answer == x*y:
        print("Correct")
        score += 1
    else:
        print("Wrong")

print("Your score is:", score, "out of", n)