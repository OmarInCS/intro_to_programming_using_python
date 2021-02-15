
from random import randint

score = 0
q_number = eval(input("Enter #questions: "))

for i in range(q_number):
    x = randint(0, 10)
    y = randint(0, 10)
    answer = eval(input(f"What's {x} + {y} ? "))
    if answer == x+y:
        print("Correct")
        score += 1
    else:
        print("Wrong")

    print("-" * 20)

print("Your score:", score, "out of", q_number)
