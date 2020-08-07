from random import randint

# file = open("words.txt")
#
#
# file.close()

with open("words.txt") as file:
    data = file.readlines()
    # data = file.read()
    # data = file.readline()
    print(type(data))
    print(data)

    # for line in file:
    #     print(line)

with open("scores.txt", "w") as file:
    for i in range(5):
        file.write(str(randint(20, 30)) + "\n")