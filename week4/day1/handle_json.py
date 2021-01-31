
import json

with open("menu_items.json", "r") as file:
    data = json.load(file)

for item in data["menu_items"]:
    print(item["name"])

emps_list = [
    {"emp_id": 101, "emp_name": "Steven", "salary": 7000},
    {"emp_id": 102, "emp_name": "Walid", "salary": 4500},
    {"emp_id": 103, "emp_name": "Sarah", "salary": 17000},
]

with open("emps.json", "w") as file:
    json.dump(emps_list, file)
