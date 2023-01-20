
countries = {
    "sa": "Saudi Arabia",
    "ae": "Arab Emirates",
    "eg": "Egypt"
}

print(countries)
print(countries["ae"])
print(len(countries))

countries["pl"] = "Palstine"
print(countries)
countries["eg"] = "Republic of Egypt"
print(countries)
print(len(countries))
del countries["ae"]
print(countries)

for k, v in countries.items():
    print(k, v)
