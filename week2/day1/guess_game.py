
from random import randint

number = randint(0, 100)
guess = eval(input("Guess a number btw 0 - 100: "))

while number != guess:
    if guess > number:
        print("Go Down")
    else:
        print("Go Up")

    guess = eval(input(">> "))

print("You Guess Right!!")
