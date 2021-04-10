
from random import randint

number = randint(0, 100)
guess = eval(input("Guess a number btw. 0-100: "))

while guess != number:
    if guess < number:
        print("Go Up")
    else:
        print("Go Down")
    guess = eval(input("new guess: "))

print("You Guess Right!!")
