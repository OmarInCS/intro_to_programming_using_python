from random import randint
# file = open("words.txt", mode="r")
#
# file.close()

with open("words.txt", mode="r") as file:
    data = file.readline()
    print(data)
    data = file.readline()
    print(data)
    # data = file.read()
    # print(data)
    data = file.readlines()
    print(data)

with open("marks.txt", mode="w") as file:
    for i in range(5):
        m = randint(50, 100)
        # file.write(str(m) + "\n")
        print(m, file=file)
