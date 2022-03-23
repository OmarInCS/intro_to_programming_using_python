from random import randint

number = randint(0, 100)
guess = eval(input("Guess a num. btw 0-100: "))

while guess != number:
    if guess < number:
        print("Go up")
    else:
        print("Go down")
    guess = eval(input("New guess: "))

print("You Guessed Right!")
