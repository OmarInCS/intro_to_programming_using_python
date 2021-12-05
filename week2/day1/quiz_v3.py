
from random import randint

x = randint(0, 10)
y = randint(0, 10)
answer = eval(input(f"What's {x} * {y} ? "))

while answer != x*y:
    print("Try again")
    answer = eval(input(f"What's {x} * {y} ? "))

print("Correct")
