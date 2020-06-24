
countries = {"sa": "Saudi Arabia", "ae": "Emirates", "eg": "Egypt"}

print(countries)
print(countries["ae"])
countries["ae"] = "Arab Emirates"

print(countries)
countries["pl"] = "Palestine"

print(countries)
print(list(countries.values()))
print(list(countries.keys()))

print("sa" in countries)
print("ye" in countries)

del countries["ae"]

print(countries)

for code, country in countries.items():
    print(f"country {country} has code {code}")

