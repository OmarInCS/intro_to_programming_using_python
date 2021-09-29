
file_name = input("Enter a file name: ")

counts = {}
with open(file_name) as file:
    content = file.read().lower()

for letter in content:
    if letter.isalpha():
        if letter in counts:
            counts[letter] += 1
        else:
            counts[letter] = 1

for letter, count in counts.items():
    print(letter, "=>", count)
