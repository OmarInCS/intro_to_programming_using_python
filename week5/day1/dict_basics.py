
countries = {"sa": "Saudi Arabia",
             "ae": "Arab Emirates",
             "eg": "Egypt"}

print(countries)
print(countries["sa"])
countries["eg"] = "Arab Republic of Egypt"
print(countries)
countries["pl"] = "Palastina"
print(countries)
del countries["ae"]
print(countries)

for code, country in countries.items():
    print(code, country)

