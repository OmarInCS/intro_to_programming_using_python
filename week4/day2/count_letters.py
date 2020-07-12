
file_name = input("Enter file name: ")
with open(file_name) as file:
    text = file.read().lower()

count_dict = {}
for letter in text:
    if letter in count_dict:
        count_dict[letter] += 1
    elif letter.isalpha():
        count_dict[letter] = 1


for letter, count in count_dict.items():
    print(letter, "appears", count, "times")