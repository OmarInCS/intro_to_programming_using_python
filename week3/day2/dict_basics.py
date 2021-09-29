
countries = {
    "sa": "Saudi Arabia",
    "ae": "Arab Emirates",
    "eg": "Egypt"
}

print(countries)
# print(countries["ae"])
print(countries.get("ae"))

# countries["eg"] = "Republic of Egypt"
countries.update({"eg": "Republic of Egypt"})
print(countries)

# countries["pl"] = "Palstine"
countries.update({"pl": "Palstine"})
print(countries)

# del countries["ae"]
countries.pop("ae")
print(countries)

print("ae" in countries)
print("pl" in countries)

for k, v in countries.items():
    print(k, v)
