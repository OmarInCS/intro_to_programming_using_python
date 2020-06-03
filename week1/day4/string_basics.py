
name = "Omar"
mobile = "0599888921"
text = "Welcome to Python"

print(name)
print(len(name))
print(name[0])
print(name[-1])
print(text[0:7])
print(text[:7])
print(text[11:])
print(text[-6:])

print(text.upper())
print(text.replace("Python", "Java"))
print(text.replace("o", "0"))
print(text.count("o"))

print(mobile.startswith("05"))
print(mobile.endswith("05"))
print(mobile.isdigit())
print(name.isalpha())

email = "omarin@gmail.com"

print(email.find("@"))
print(email[0:email.find("@")])

print("@" in email)