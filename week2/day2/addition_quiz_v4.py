
from random import randint

score = 0

for i in range(1, 6):
    x = randint(0, 10)
    y = randint(0, 10)

    print(i, ") What's", x, "+", y, "?")
    answer = eval(input("ans: "))

    if answer == x+y:
        print("Correct Answer")
        score += 1
    else:
        print("Wrong Answer")

print("your score:", score, "out of 5")