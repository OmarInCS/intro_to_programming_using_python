
from random import randint

path = "C:\\Users\\Mr Omar\\Desktop\\words.txt"
# file = open(path)
# file.read()
# file.close()

with open(path) as file:
    data = file.readline().strip()
    print(data)
    data = file.readline().strip()
    print(data)
    # data = file.read()
    # print(data)
    data = file.readlines()
    print(data)


with open("marks.txt", "w") as file:
    for i in range(5):
        m = randint(0, 25)
        # file.write(str(m) + "\n")
        print(m, file=file)