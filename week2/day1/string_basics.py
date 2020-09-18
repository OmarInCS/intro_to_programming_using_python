
name = "Omar"
email = "omarincs@gmail.com"
mobile = "0599888921"
text = "Welcome to Python"

print(text[0])
print(text[-1])
print(len(text))
print(text[0:7])
print(text[:7])
print(text[-6:])

print("@" in email)
print("@" in mobile)

text2 = text[:8] * 2 + name
print(text2)

print(text.upper())
print(text.lower())
text = text.replace("Python", "PHP")
print(text)
print(mobile.startswith("05"))
print(email.endswith(".com"))
print(mobile.isdigit())
print(name.isalpha())
