from random import randint

n = eval(input("Enter the number of questions: "))
score = 0

for i in range(n):
    x = randint(0, 10)
    y = randint(0, 10)
    answer = eval(input(f"What's {x} * {y} ? "))

    if answer == x*y:
        print("Correct Answer")
        score += 1
    else:
        print("Wrong Answer")
    print("-" * 20)

print("Your score:", score, "out of", n)