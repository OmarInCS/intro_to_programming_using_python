
marks = (23, 19, 13, 24)

print(marks[0])
print(marks[-1])

print(len(marks))
print(max(marks))

countries = {"sa": "Saudi Arabia",
             "ae": "Arab Emirates",
             "eg": "Egypt"}

print(countries["sa"])
print(countries)
countries["eg"] = "Republic of Egypt"
print(countries)
countries["pl"] = "Palestine"
print(countries)
del countries["ae"]
print(countries)

print("ae" in countries)
print("pl" in countries)
print(len(countries))

for k, v in countries.items():
    print(k, "=>", v)
