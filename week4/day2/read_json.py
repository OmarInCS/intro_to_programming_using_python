
import json

file_path = "C:\\Users\\OmarKarem\\SemicolonGD\\Python\\resources\\video_links_20200809.json"

with open(file_path) as file:
    data = json.load(file)
    for session in data:
        print(session["Topic"])