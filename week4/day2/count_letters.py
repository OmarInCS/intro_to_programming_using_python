
file_name = input("Enter a file name: ")
with open(file_name) as file:
    text = file.read().lower()

count_dict = {}

for letter in text:
    if letter.isalpha():
        if letter in count_dict:
            count_dict[letter] += 1
        else:
            count_dict[letter] = 1


lst = count_dict.items()
lst = sorted(lst, key=lambda e: e[1], reverse=True)


for letter, count in lst:
    print(letter, "appeared", count, "times")