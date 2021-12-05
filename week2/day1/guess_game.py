
from random import randint

number = randint(0, 100)
guess = eval(input("Enter a number btw 0-100: "))

while guess != number:
    if guess > number:
        print("Go Down")
    else:
        print("Go Up")
    guess = eval(input("Enter a new guess: "))

print("You guessed right!!")

