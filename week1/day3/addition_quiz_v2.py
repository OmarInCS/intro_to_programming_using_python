from random import randint

score = 0
x = randint(0, 10)
y = randint(0, 10)

answer = eval(input(f"What's {x} + {y} ? "))

while answer == x+y:
    score += 1
    x = randint(0, 10)
    y = randint(0, 10)
    answer = eval(input(f"What's {x} + {y} ? "))

print("Game Over!")
print("Score:", score)

