
# file = open("words.txt")
#
#
# file.close()

with open("words.txt") as file:
    # data = file.read()
    data = file.readline()
    print(data)
    data = file.readlines()
    print(data)

countries = {"sa": "Saudi Arabia",
             "ae": "Arab Emirates",
             "eg": "Egypt"}

with open("C:\\Users\\OmarKarem\\Desktop\\data.csv", "w") as file:
    file.write("Code, Country\n")
    for code, country in countries.items():
        file.write(f"{code}, {country}\n")
