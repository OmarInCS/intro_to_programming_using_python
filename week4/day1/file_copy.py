
file_name = input("Enter a file name: ")

with open(file_name) as file:
    content = file.read()

copy_name = input("Enter a copy name: ")

with open(copy_name, "w") as file:
    file.write(content)
