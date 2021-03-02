
from random import randint

# file = open("words.txt", "r")
#
#
# file.close()

file_path = "C:\\Users\\OmarKarem\\Desktop\\words.txt"

with open(file_path, "r") as file:
    data = file.readline()
    print(data)
    data = file.readline()
    print(data)
    # data = file.readlines()
    # print(data)
    data = file.read()
    print(data)

    # data = file.readline()
    # while data != "":
    #     print(data.strip())
    #     more = input()
    #     data = file.readline()

with open("numbers.txt", "w") as file:
    for i in range(5):
        num = randint(0, 100)
        # file.write(str(num) + "\n")
        print(num, file=file)
