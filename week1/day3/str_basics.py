
name = "Omar"
email = "omarincs@gmail.com"
mobile = "0599888921"
message = "Welcome to Python"

print(name[0])
print(name[-1])
print(len(name))
print(message[0:7])
print(message[:7])
print(message[-6:])

title = message[:8] * 2 + name
print(title)

print(name[:2].upper() + name[2:].lower())
print(name.upper())
print(name.lower())
print(message.replace("Python", "Swift"))

print(email.endswith(".com") or email.endswith(".net"))
print(mobile.startswith("05"))
print(email.__contains__("@"))
print("@" in email)

print(name.isalpha())
print(mobile.isdigit())









