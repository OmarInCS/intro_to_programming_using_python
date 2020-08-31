
file_path = "C:\\Users\\OmarKarem\\Desktop\\words.txt"
# file = open(file_path)
#
#
#
# file.close()

with open("words.txt") as file:
    # data = file.read()
    data = file.readlines()
    # data = file.readline()
    # for x in file:
    #     print(x)

countries = {"sa": "Saudi Arabia",
             "ae": "Arab Emirates",
             "eg": "Egypt"}

file_path = "C:\\Users\\OmarKarem\\Desktop\\countries.csv"

with open(file_path, "w") as file:
    for code, country in countries.items():
        # file.write(code)
        # file.write(",")
        # file.write(country)
        # file.write("\n")
        file.write(f"{code},{country}\n")
