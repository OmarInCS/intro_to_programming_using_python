
# file = open("words.txt", "r")
#
#
#
# file.close()
from random import randint

with open("words.txt", "r") as file:
    data = file.readline()
    print(data)
    data = file.readline()
    print(data)
    # data = file.readlines()
    # print(data)
    data = file.read()
    print(data)

with open("questions.txt", "w") as file:

    for i in range(1, 6):
        x = randint(0, 10)
        y = randint(0, 10)
        # file.write(f"What's {x} + {y} ? .......\n\n")
        print(f"{i}) What's {x} + {y} ? .......\n", file=file)
