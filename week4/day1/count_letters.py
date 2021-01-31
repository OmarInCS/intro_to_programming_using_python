
file_name = input("Enter a file name: ")

with open(file_name, "r") as file:
    text = file.read().lower()

count_dict = {}

for letter in text:
    if letter.isalpha():
        if letter in count_dict:
            count_dict[letter] += 1
        else:
            count_dict[letter] = 1

for k, v in count_dict.items():
    print(k, "=>", v)