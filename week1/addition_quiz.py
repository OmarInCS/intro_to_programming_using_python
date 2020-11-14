
from random import randint

x = randint(0, 10)
y = randint(0, 10)

# print("What's", x, "+", y, "?")
# print(f"What's {x} + {y} ? ")

answer = eval(input(f"What's {x} + {y} ? "))

if answer == x+y:
    print("Correct")
else:
    print("Wrong")
