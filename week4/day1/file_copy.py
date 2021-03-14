
from os.path import isfile

file_name = input("Enter a file name: ")
copy_name = input("Enter the copy file name: ")

while isfile(copy_name):
    choice = input("File exist, want to overwrite? (y/n) ").lower()
    if choice.startswith("n"):
        copy_name = input("Enter the copy file name: ")
    else:
        break

with open(file_name, "r") as file:
    content = file.read()

with open(copy_name, "w") as file:
    file.write(content)

