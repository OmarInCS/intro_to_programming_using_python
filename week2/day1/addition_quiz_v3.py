from random import randint

correct = 0

for i in range(5):
    x = randint(0, 10)
    y = randint(0, 10)
    answer = eval(input(f"What's {x} + {y} ? "))

    if answer == x+y:
        print("Correct")
        correct += 1
    else:
        print("Wrong")

print("Score:", correct, "out of 5")
