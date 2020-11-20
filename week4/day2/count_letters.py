
file_name = input("Enter a file name: ")

with open(file_name) as file:
    data = file.read().lower()

count_dict = {}
for letter in data:
    if letter.isalpha():
        if letter in count_dict:
            count_dict[letter] += 1
        else:
            count_dict[letter] = 1

for letter, count in count_dict.items():
    print(letter, "appears", count, "times")