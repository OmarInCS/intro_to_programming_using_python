
file_path = "C:\\Users\\Mr Omar\\Desktop\\words.txt"
# file = open(file_path)
# file.read()
# file.close()

with open(file_path) as file:
    content = file.readline()
    print(content)
    content = file.readline()
    print(content)
    content = file.readlines()
    print(content)
    print(content[1])
    # content = file.read()
    # print(content)

file_path = "C:\\Users\\Mr Omar\\Desktop\\my_data.csv"
with open(file_path, "w") as my_file:
    my_file.write("Ahmed,23\n")
    my_file.write("Wael,17\n")
    my_file.write("Ali,25\n")
