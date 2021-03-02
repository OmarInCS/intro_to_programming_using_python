
file_name = input("Enter a file name: ")
with open(file_name, "r") as file:
    text = file.read().lower()

dict_count = {}
for letter in text:
    if letter.isalpha():
        if letter in dict_count:
            dict_count[letter] += 1
        else:
            dict_count[letter] = 1

for letter, count in dict_count.items():
    print(letter, ">>", count)

