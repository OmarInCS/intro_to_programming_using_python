
text = "Welcome to Python"
name = "Omar"
mobile = "0599888921"
email = "omarincs@gmail.com"

print(text[0])
print(len(text))
print(text[16])
print(text[-1])
# print(text[20])
print(text[0:7])
print(text[:7])
print(text[-6:])

print(text[:8] * 2 + name)

print(text.upper())
print(text.lower())
print(text.replace("Python", "Java"))
print(mobile.startswith("05"))
print(email.endswith(".com") or email.endswith(".net"))
print("@" in email)

print(mobile.isdigit())
print(name.isalpha())