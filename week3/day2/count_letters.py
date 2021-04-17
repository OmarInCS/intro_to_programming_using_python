
file_name = input("Enter a file name: ")

with open(file_name, "r") as file:
    text = file.read().upper()

count_letters = {}
for char in text:
    if char.isalpha():
        if char in count_letters:
            count_letters[char] += 1
        else:
            count_letters[char] = 1

for char, count in count_letters.items():
    print(char, "=>", count)