
countries = {"sa": "Saudi Arabia",
             "ae": "Arab Emirates",
             "eg": "Egypt"}

print(countries)
print(countries["ae"])
countries["eg"] = "Republic of Egypt"
print(countries)
countries["pl"] = "Palestine"
print(countries)
del countries["ae"]
print(countries)
print(len(countries))
print("sa" in countries)

print(countries.keys())
print(countries.values())
print(countries.items())


# for code in countries:
#     print(code, countries[code])

for code, country in countries.items():
    print(code, country)
