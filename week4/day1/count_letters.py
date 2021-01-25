
import json

file_name = input("Enter a file name: ")
count_dict = {}

with open(file_name, "r") as file:
    text = file.read().lower()

for letter in text:
    if letter.isalpha():
        if letter in count_dict:
            count_dict[letter] += 1
        else:
            count_dict[letter] = 1

with open("result.txt", "w") as file:
    for letter, count in count_dict.items():
        print(letter, "=>", count, file=file)


# with open("result.json", "w") as file:
#     json.dump(count_dict, file)


# with open("result.json", "r") as file:
#     data = json.load(file)
#     print()