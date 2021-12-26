from random import randint

file_path = "C:\\Users\\Mr Omar\\Desktop\\words.txt"
# file = open(file_path)
# file.read()
# file.close()
with open(file_path) as file:
    content = file.readline()
    print(content)
    content = file.readline()
    print(content)
    # content = file.readlines()
    # print(content)
    content = file.read()
    print(content)

with open("numbers.txt", "w") as file:
    for i in range(50):
        x = randint(0, 100)
        # file.write(str(x) + "\n")
        print(x, file=file)
