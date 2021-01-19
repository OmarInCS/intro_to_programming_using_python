from random import randint

result = 0
n = eval(input("Enter number of questions: "))

for i in range(n):
    x = randint(0, 10)
    y = randint(0, 10)
    for j in range(3):
        answer = eval(input(f"What's {x} + {y} ? "))

        if answer == x+y:
            print("Correct")
            result += 1
            break
        else:
            print("Wrong")

    print("-" * 20)

print("Result:", result, "out of", n)