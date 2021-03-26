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

file_path = "C:\\Users\\Mr Omar\\Desktop\\numbers.txt"
with open(file_path, "w") as file:
    for i in range(5):
        # file.write(str(randint(0, 50)) + "\n")
        print(randint(0, 50), file=file)
