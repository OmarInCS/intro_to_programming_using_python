
countries = {
    "sa": "Saudi Arabia",
    "ae": "Arab Emirates",
    "eg": "Egypt"
}

print(countries)
# print(countries["ae"])
# countries["eg"] = "Republic of Egypt"
# print(countries)
# countries["pl"] = "Palstine"
# print(countries)
# del countries["ae"]
# print(countries)
print(len(countries))
print("ae" in countries)

print(countries.get("ae"))
countries.update({"eg": "Republic of Egypt"})
print(countries)
countries.update({"pl": "Palstine"})
print(countries)
countries.pop("ae")
print(countries)

print(list(countries.keys()))
print(list(countries.values()))

for k, v in countries.items():
    print(k, "=>", v)
