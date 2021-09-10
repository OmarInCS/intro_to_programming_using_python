
countries = {
    "sa": "Saudi Arabia",
    "ae": "Arab Emirates",
    "eg": "Egypt"
}

print(countries)
print(countries["sa"])

countries["eg"] = "Republic of Egypt"
print(countries)
# countries["pl"] = "Palstine"
# print(countries)
countries.update({"pl": "Palstine"})
print(countries)

# del countries["ae"]
# print(countries)
countries.pop("ae")
print(countries)

print("ae" in countries)
print("pl" in countries)
print(len(countries))

for k, v in countries.items():
    print(k, v)

print(list(countries.values())[1])