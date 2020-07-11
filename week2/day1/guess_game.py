
from random import randint

number = randint(0, 100)
guess = eval(input("Guess a number btw 0-100: "))

while number != guess:
    if guess < number:
        guess = eval(input("Go up\n=> "))
    else:
        guess = eval(input("Go down\n=> "))

print("You Guess Right")
