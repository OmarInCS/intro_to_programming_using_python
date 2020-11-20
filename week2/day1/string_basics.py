
text = "Welcome to Python"
name = "Omar"
email = "omarincs@gmail.com"
mobile = "0599888921"

print(text[0])
print(text[-1])
print(text[0:7])
print(text[:7])
print(text[-6:])
print(len(text))

print(text.upper())
print(text.lower())
print(text.replace("Python", "Java"))
print(text.startswith("We"))
print(mobile.startswith("05"))
print(email.endswith(".com"))
print("@" in email)

print(name.isalpha())
print(mobile.isdigit())
