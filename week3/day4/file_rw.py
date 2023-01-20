from random import randint

file_path = "C:\\Users\\Mr Omar\\Desktop\\words.txt"
# file = open(file_path)
# file.read()
# file.close()

with open(file_path) as file:
    data = file.readline()
    print(data)
    data = file.readline()
    print(data)
    # data = file.readlines()
    # print(data)
    data = file.read()
    print(data)

file_path2 = "marks.txt"
with open(file_path2, "w") as file:
    for i in range(10):
        x = randint(0, 100)
        # file.write(str(x) + "\n")
        print(x, file=file)
