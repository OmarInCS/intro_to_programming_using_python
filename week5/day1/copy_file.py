
file_name = input("Enter a file name: ")

with open(file_name) as file:
    x = file.read()

with open("copy.txt", "w") as file:
    file.write(x)