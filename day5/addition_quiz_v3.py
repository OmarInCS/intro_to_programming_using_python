
from random import randint

n = eval(input("Enter the num. of questions: "))
score = 0
for i in range(n):
    x = randint(0, 10)
    y = randint(0, 10)

    print("What's", x, "+", y, "?")
    answer = eval(input("ans: "))

    if answer == x+y:
        print("Correct")
        score += 1
    else:
        print("Wrong")

print("Your score:", score, "out of", n)
