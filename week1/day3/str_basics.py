
name = "Omar"
mobile = "0599888921"
email = "omarincs@gmail.com"
msg = "Welcome to Python"

print(name[0])
print(name[-1])
print(len(name))
print(msg[0:7])
print(msg[:7])
print(msg[-6:])

title = msg[:8] * 2 + name
print(title)

print(msg.upper())
print(msg.lower())
print(msg.replace("Python", "SQL"))

print(email.endswith(".com"))
print(mobile.startswith("05"))
print(email.__contains__("@"))
print("@" in email)

print(mobile.isdigit())
print(name.isalpha())

