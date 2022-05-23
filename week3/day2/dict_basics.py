
countries = {
    "sa": "Saudi Arabia",
    "ae": "Arab Emirates",
    "eg": "Egypt"
}

print(countries)
print(countries["ae"])
print(len(countries))

# countries["eg"] = "Republic of Egypt"
# print(countries)
# countries["pl"] = "Palstine"
# print(countries)
# del countries["ae"]
# print(countries)

countries.update({"eg": "Republic of Egypt"})
print(countries)
countries.update({"pl": "Palstine"})
print(countries)
countries.pop("ae")
print(countries)

print("pl" in countries)

for k, v in countries.items():
    print(k, "=>", v)
