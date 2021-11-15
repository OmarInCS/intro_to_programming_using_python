from random import randint

file_path = "C:\\Users\\Mr Omar\\Desktop\\words.txt"
# file = open(file_path, "r")
#
# file.close()

with open(file_path, "r") as file:
    content = file.readline()
    print(content)
    content = file.readline()
    print(content)
    # content = file.read()
    # print(content)
    content = file.readlines()
    print(content)


file_name = "marks.txt"
with open(file_name, "w") as file:
    for i in range(5):
        x = randint(0, 25)
        # file.write(str(x) + "\n")
        print(x, file=file)

