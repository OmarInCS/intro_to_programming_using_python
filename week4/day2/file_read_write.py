
# file = open("words.txt")
#
#
# file.close()


with open("words.txt", "r") as file:
    data = file.readline()
    data = file.readline()
    # data = file.read()
    data = file.readlines()
    print(data)

employees = ["Ahmed", "Walid", "Fahad", "Sara"]

with open("employees.csv", "w") as file:
    for emp in employees:
        file.write(emp + "\n")


employees = [
    {"id": 101, "name": "Ahmed", "salary": 6000},
    {"id": 102, "name": "Mohammed", "salary": 7000},
    {"id": 103, "name": "Walid", "salary": 15000}
]

# print(employees[1]["name"])

import json

with open("employees.json", "w") as file:
    json.dump(employees, file)

with open("categories.json", "r") as file:
    categories = json.load(file)

    print(categories[0])

