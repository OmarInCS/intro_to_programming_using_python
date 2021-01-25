
countries = {"sa": "Saudi Arabia",
             "ae": "Arab Emirates",
             "eg": "Egypt"}

print(countries)
print(countries.values())
print(countries.keys())
print(countries["sa"])
countries["eg"] = "Republic of Egypt"
print(countries)

countries["pl"] = "Palestine"
print(countries)

del countries["ae"]
print(countries)

print("ae" in countries)
print("Palestine" in countries.values())

for k, v in countries.items():
    print(k, v)
