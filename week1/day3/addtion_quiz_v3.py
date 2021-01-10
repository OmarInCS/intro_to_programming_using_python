
from random import randint

n = eval(input("How many question? "))

for i in range(n):
    x = randint(0, 10)
    y = randint(0, 10)
    answer = eval(input(f"What's {x} + {y} ? "))

    if answer == x+y:
        print("Correct")
    else:
        print("Wrong")

    print("-" * 20)
