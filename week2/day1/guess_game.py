
from random import randint

number = randint(0, 100)
guess = eval(input("Guess a number btw 0-100: "))

while number != guess:
    if number > guess:
        guess = eval(input("Guess a greater number: "))
    else:
        guess = eval(input("Guess a smaller number: "))

print("You guess right!")