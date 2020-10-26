
import json

students = [
    {"id": 101, "name": "Ahmed", "mark": 92, "grade": "Excellent"},
    {"id": 102, "name": "Yasser", "mark": 65, "grade": "Good"},
    {"id": 103, "name": "Ali", "mark": 75, "grade": "Good"},
]

with open("students.json", "w") as file:
    json.dump(students, file)


with open("menu_items.json") as file:
    data = json.load(file)
    # print(data["menu_items"][0]["name"])
    for item in data["menu_items"]:
        print(item["name"])
