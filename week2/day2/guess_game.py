
from random import randint

number = randint(0, 100)

guess = eval(input("Guess a num. btw 0-100: "))

while number != guess:
    if guess > number:
        guess = eval(input("Go Down: "))
    else:
        guess = eval(input("Go Up: "))

print("You Guess Right!")
