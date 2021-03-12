from random import randint

score = 0

for i in range(5):
    x = randint(0, 10)
    y = randint(0, 10)

    answer = eval(input(f"What's {x} + {y} ? "))
    if answer == x+y:
        print("Correct Answer")
        score += 1
    else:
        print("Wrong Answer")

print("Score is:", score, "out of 5")
print(f"Score is: {score} out of 5")
