
# file = open("words.txt")
#
# file.close()

with open("words.txt") as file:
    # data = file.read()
    data = file.readlines()
    print(data)
    # for w in data:
    #     print(w)

with open("new_file.txt", "a") as file:
    file.write("Welcome to Python\n")
    file.write("Python is Fun\n")