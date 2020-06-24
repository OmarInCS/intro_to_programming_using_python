
import json
import csv

with open("files/menu_items.json") as file:
    data = json.load(file)
    # print(type(data))
    for item in data["menu_items"]:
        if item["price_small"] != None and item["price_small"] < 5:
            print(item["name"], "=>", item["price_small"])


countries = [
    {"name": "Saudi Arabia", "capital": "Riyadh", "pop": 35},
    {"name": "Egypt", "capital": "Cairo", "pop": 100}
]

with open("files/countries.json", "w") as file:
    json.dump(countries, file)

with open("files/countries.csv", "w", newline="") as file:
    writer = csv.DictWriter(file, ["name", "capital", "pop"])
    writer.writeheader()
    writer.writerows(countries)

