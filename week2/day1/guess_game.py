
from random import randint

number = randint(0, 100)
guess = eval(input("Guess num. btw. 0-100: "))

while guess != number:
    if guess > number:
        guess = eval(input("Go Down\n>> "))
    else:
        guess = eval(input("Go Up\n>> "))

print("You Guess Right!!")
