from random import randint

result = 0

for i in range(5):
    x = randint(0, 10)
    y = randint(0, 10)

    answer = eval(input(f"What's {x} + {y} ? "))
    if answer == x+y:
        print("Correct")
        result += 1
    else:
        print("Wrong")

    print("-" * 25)

print("Result:", result, "out of 5")
