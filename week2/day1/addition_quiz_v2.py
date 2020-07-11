
from random import randint

x = randint(0, 10)
y = randint(0, 10)

print(f"What's {x} + {y} ?")
answer = eval(input("=> "))

while answer == x+y:
    x = randint(0, 10)
    y = randint(0, 10)

    print(f"What's {x} + {y} ?")
    answer = eval(input("=> "))

print("Game over!!")