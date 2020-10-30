
text = "Welcome to Python"
mobile = "0599888921"
email = "omarincs@gmail.com"
name = "Omar"

print(text[0])
print(len(text))
print(text[-1])
print(text[16])
print(text[0:7])
print(text[:7])
print(text[:8])
print(text[-6:])

message = text[:8] * 2 + name
print(message)

print(text.upper())
print(text.lower())
print(text.replace("Python", "Java"))
print(text.startswith("Wel"))
print(mobile.startswith("05"))
print(email.endswith(".com"))
print("@" in email)
print(name.isalpha())
print(mobile.isdigit())
