
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
print(message[:-6])

title = message[:8] * 2 + name
print(title)

print(message.upper())
print(message.lower())
print(message.replace("Python", "SQL"))

print(mobile.startswith("05"))
print(email.endswith(".com"))
print(email.__contains__("@"))
print("@" in email)

print(name.isalpha())
print(mobile.isdigit())



