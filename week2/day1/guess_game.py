
from random import randint

number = randint(0, 100)
guess = eval(input("Guess a number btw 0-100: "))

while guess != number:
    if guess > number:
        guess = eval(input("Guess a smaller number: "))
    else:
        guess = eval(input("Guess a greater number: "))

print("You Guess Right!!")
