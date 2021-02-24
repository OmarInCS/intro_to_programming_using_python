
name = "Omar"
email = "omarincs@gmail.com"
mobile = "0599888921"
text = "Welcome to Python"

print(text[0])
print(text[-1])
print(text[0:7])
print(text[:7])
print(text[-6:])

title = text[:8] * 2 + name
print(title)

print(len(text))
print(text.upper())
print(text.lower())
print(text.replace("Python", "SQL"))

print(text.startswith("Welcome"))
print(mobile.startswith("05"))
print(email.endswith(".com"))
print("@" in email)
print(name.isalpha())
print(mobile.isdigit())
