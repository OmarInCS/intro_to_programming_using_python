
from os.path import isfile

old_file_name = input("Enter a file name: ")
copy_file_name = input("Enter the copy name: ")

if isfile(old_file_name):
    with open(old_file_name) as file:
        data = file.read()

    with open(copy_file_name, "w") as file:
        file.write(data)