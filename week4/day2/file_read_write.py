
# file = open("files/words.txt")
#
#
#
# file.close()

with open("files/words.txt") as file:
    # words = file.readlines()
    # print(words)
    counter = 0
    for word in file:
        if len(word) == 3:
            counter += 1

    print(f"We have {counter} words with length 3")


file_name = input("Enter new file name: ")
marks = [("Ahmed", 23), ("Mohamed", 22),
         ("Hussein", 19)]

with open(f"files/{file_name}.txt", "w") as file:
    for name, mark in marks:
        file.write(f"{name}, {mark}\n")
