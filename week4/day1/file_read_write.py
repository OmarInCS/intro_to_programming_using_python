from random import randint

# file = open("words.txt", "r")
#
#
# file.close()

with open("words.txt", "r") as file:
    data = file.readline()
    print(data)
    data = file.readline()
    print(data)
    # data = file.readlines()
    # print(data)
    data = file.read()
    print(data)


with open("marks.txt", "w") as file:
    for i in range(10):
        # file.write(str(randint(30, 100)) + "\n")
        print(randint(30, 100), file=file)