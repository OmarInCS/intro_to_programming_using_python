
# file = open("C:\\Users\\OmarKarem\\Desktop\\words.txt")
#
#
# file.close()

# file_path = "C:\\Users\\OmarKarem\\Desktop\\words.txt"

with open("words.txt") as file:
    # data = file.read()
    # data = file.readlines()
    data = file.readline()
    print(data)

