
from random import randint

number = randint(0, 100)
guess = eval(input("Enter a num. btw 0-100: "))

while guess != number:
    if guess < number:
        print("Go up")
    else:
        print("Go down")
    guess = eval(input(">> "))

print("You Guess Right!")
