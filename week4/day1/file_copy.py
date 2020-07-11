
src_name = input("Enter source file name: ")
new_name = input("Enter new file name: ")

with open(src_name) as file:
    data = file.read()

with open(new_name, "w") as file:
    file.write(data)
