
from random import randint

with open("words.txt") as file:
    data = file.readline()
    print(data)
    data = file.readline()
    print(data)
    # data = file.read()
    # print(data)
    data = file.readlines()
    print(data)

with open("story.txt", "a") as file:
    for i in range(10):
        idx = randint(0, len(data))
        file.write(data[idx])

    file.write("oooo")
    file.write("Ahmed\n")
    file.write("Wael\n")

