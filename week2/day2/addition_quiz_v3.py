
from random import randint

x = randint(0, 10)
y = randint(0, 10)
answer = eval(input(f"What's {x} + {y}?\n>> "))

while answer != x+y:
    answer = eval(input(f"Try again, What's {x} + {y}?\n>> "))

print("Correct")
