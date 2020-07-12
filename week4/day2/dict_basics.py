
countries = {"sa": "Saudi Arabia",
             "ae": "Arab Emirates",
             "eg": "Egypt"}

print(countries)
print(countries["eg"])
countries["eg"] = "Egypt Republic"
countries["pl"] = "Palestine"

print(countries)

del countries["eg"]
print(countries)
print("eg" in countries)

# for code in countries:
#     print(code)

for country in countries.values():
    print(country)

for code, country in countries.items():
    print(code, country)