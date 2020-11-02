
# file = open("words.txt", "r")
#
#
# file.close()

with open("words.txt", "r") as file:
    data = file.readline()
    # data = file.read()
    data = file.readlines()
    print(data)

students = [
    ("Ahmed", 49, 50),
    ("Ali", 39, 43),
    ("Walid", 48, 45)
]

with open("C:\\Users\\OmarKarem\\Desktop\\marks.csv", "w") as file:
    file.write("Name,Semester 1,Semester 2\n")
    for row in students:
        for value in row:
            file.write(str(value) + ",")
        file.write("\n")
