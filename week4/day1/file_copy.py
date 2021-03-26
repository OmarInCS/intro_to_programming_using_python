
file_name = input("Enter a file name: ")
copy_name = input("Enter a copy name: ")

with open(file_name, "r") as file:
    content = file.read()

with open(copy_name, "w") as file:
    file.write(content)
