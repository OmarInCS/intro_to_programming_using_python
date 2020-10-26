
file_name = input("Enter a file name: ")

with open(file_name) as file:
    data = file.read()

copy_name = input("Enter the copy name: ")

with open(copy_name, "w") as file:
    file.write(data)
