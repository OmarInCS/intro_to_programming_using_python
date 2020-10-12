
from random import randint

number = randint(0, 100)
guess = eval(input("Guess a number btw 0-100: "))

while number != guess:
    if guess < number:
        guess = eval(input("Go Up\n>> "))
    else:
        guess = eval(input("Go Down\n>> "))

print("You Guess Right!")
