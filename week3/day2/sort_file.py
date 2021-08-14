
file_name = input("Enter a file name: ")

with open(file_name, mode="r") as file:
    data = file.readlines()
    data.sort()

with open(file_name.replace(".txt", "-sorted.txt"), mode="w") as file:
    for word in data:
        file.write(word)

print("File created!!")
