
file_name = input("Enter a file name: ")

with open(file_name, "r") as file:
    text = file.read()

letters_count = {}

for letter in text:
    if letter.isalpha():
        if letter in letters_count:
            letters_count[letter] += 1
        else:
            letters_count[letter] = 1

for letter, count in letters_count.items():
    print(letter, "appeared", count, "times")
