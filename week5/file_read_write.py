
import json

# file = open("words.txt", "r")
#
#
# file.close()

# with open("words.txt", "r") as file:
#     data = file.readline()
#     print(data)
#     # data = file.readlines()
#     data = file.read()
#     print(data)

students = [
    {"name": "Ahmed", "mark": 23},
    {"name": "Said", "mark": 15},
    {"name": "Yasser", "mark": 25},
]

# with open("marks.csv", "w") as file:
#     file.write("Name,Mark\n")
#     for std in students:
#         file.write(std["name"] + ",")
#         file.write(str(std["mark"]) + "\n")


with open("marks.json", "w") as file:
    json.dump(students, file)

with open("marks.json", "r") as file:
    std_data = json.load(file)
    print(std_data)