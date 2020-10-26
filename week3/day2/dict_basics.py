
countries = {"sa": "Saudi Arabia",
             "ae": "Arab Emirates",
             "eg": "Egypt"}

print(countries)
print(countries["ae"])
countries["eg"] = "Republic of Egypt"
print(countries)
countries["pl"] = "Palastine"
print(countries)

print("ae" in countries)
del countries["ae"]
print("ae" in countries)
print(countries)

print(countries.keys())
print(countries.values())

for code, country in countries.items():
    print(code, country)
