from random import randint

number = randint(0, 100)
answer = eval(input("Guess a num. btw 0-100: "))

while answer != number:
    if answer < number:
        print("Go Up")
    else:
        print("Go Down")
    answer = eval(input("new guess: "))

print("You Guessed Right!!")
