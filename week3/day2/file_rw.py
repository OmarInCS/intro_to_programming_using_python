
from random import randint

file_path = "C:\\Users\\Mr Omar\\Desktop\\words.txt"
# file = open(file_path, "r")
#
# file.close()

with open(file_path, "r") as file:
    data = file.readline()
    print(data)
    data = file.readline()
    print(data)
    # data = file.readlines()
    # print(data)
    data = file.read()
    print(data)

with open("marks.txt", "w") as file:
    for i in range(5):
        x = randint(0, 10)
        file.write(str(x) + "\n")
