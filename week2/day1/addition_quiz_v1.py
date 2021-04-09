
from random import randint

x = randint(0, 10)
y = randint(0, 10)

print("What's", x, "+", y, "?")
answer = eval(input("ans: "))

while answer == x+y:
    x = randint(0, 10)
    y = randint(0, 10)

    print("What's", x, "+", y, "?")
    answer = eval(input("ans: "))

print("Game Over!!")
