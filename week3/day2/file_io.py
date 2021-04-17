from random import randint
# file_path = "C:\\Users\\Mr Omar\\Desktop\\Group20210305\\week4\\day1\\words.txt"
# file = open(file_path, "r")
#
# file.close()

with open("words.txt", "r") as file:
    content = file.readline()
    print(content)
    content = file.readline()
    print(content)
    # content = file.readlines()
    # print(content)
    content = file.read()
    print(content)


with open("marks.txt", "w") as file:
    for i in range(5):
        # file.write(str(randint(5, 25)) + "\n")
        print(randint(5, 25), file=file)

