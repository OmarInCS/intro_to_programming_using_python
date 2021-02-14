from random import randint

x = randint(0, 10)
y = randint(0, 10)

answer = eval(input(f"What's {x} + {y} ? "))

while answer == x+y:
    print("Correct")
    x = randint(0, 10)
    y = randint(0, 10)
    answer = eval(input(f"What's {x} + {y} ? "))

print("Game Over!!")
