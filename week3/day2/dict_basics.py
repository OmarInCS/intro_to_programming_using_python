
countries = {"sa": "Saudi Arabia",
             "ae": "Arab Emirates",
             "eg": "Egypt"}

print(countries)
print(countries["ae"])
print(len(countries))
countries["eg"] = "Republic of Egypt"
print(countries)
countries["pl"] = "Palestine"
print(countries)
del countries["ae"]
print(countries)
print("ae" in countries)
print("pl" in countries)

for k, v in countries.items():
    print(k, "=>", v)
