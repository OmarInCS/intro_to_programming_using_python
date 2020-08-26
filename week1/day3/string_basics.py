
text = "Welcome to Python"
name = "Omar"
mobile = "0599888921"
email = "omarincs@gmail.com"

print(text[0])
print(text[-1])
print(text[0:7])
print(text[:7])
print(text[-6:])
print(text[:-6])

message = text[:8] * 2 + name
print(message)

print(len(name))
print(text.upper())
print(text.replace("Python", "Java"))
print(text.count("o"))
print(text.startswith("Wel"))
print(mobile.startswith("05"))
print(email.endswith(".com"))
print("@" in email)
print(name.isalpha())
print(mobile.isdigit())
