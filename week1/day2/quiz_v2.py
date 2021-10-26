from random import randint

x = randint(0, 10)
y = randint(0, 10)

answer = eval(input(f"What's {x} * {y} ? "))

# if answer == x*y:
#     print("Correct")
# else:
#     print("Wrong")

print("Correct" if answer == x*y else "Wrong")