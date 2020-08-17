
text = "Welcome to Python"
name = "omar"
mobile = "0599888921"
email = "omarincs@gmail.com"

print(text[0])
print(text[-1])
print(text[0:7])
print(text[:7])
print(text[-6:])
print(len(text))

print(text.upper())
print(text.lower())
print(text.index("c"))
print(text.count("o"))
print(text.replace("Python", "Java"))

print(mobile.isdigit())
print(name.isalpha())
print(text.isalpha())
print(text.endswith("Python"))
print(mobile.startswith("05"))
print("@" in email)
