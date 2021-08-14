
countries = {
    "sa": "Saudi Arabia",
    "ae": "Arab Emirates",
    "eg": "Egypt"
}

print(countries)
print(len(countries))
print(countries["sa"])
countries["eg"] = "Republic of Egypt"
print(countries)
# countries["pl"] = "Palstine"
countries.update({"pl": "Palstine"})
print(countries)

# del countries["ae"]
countries.pop("ae")
print(countries)

keys = list(countries.keys())
values = list(countries.values())
print(keys)
print(values)

print("ae" in countries)
print("pl" in countries)

for k, v in countries.items():
    print(k, v)
