
src_name = input("Enter a file name: ")
copy_name = input("Enter the copy name: ")

with open(src_name, "r") as file:
    text = file.read()

with open(copy_name, "w") as file:
    file.write(text)
