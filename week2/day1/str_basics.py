
name = "Omar"
email = "omarincs@gmail.com"
mobile = "059888921"
msg = "Welcome to Python"

print(msg[0])
print(msg[-1])
print(msg[0:7])
print(msg[:7])
print(msg[-6:])
print(len(msg))

title = msg[:8] * 2 + name
print(title)

print(msg.upper())
print(msg.lower())
print(msg.replace("Python", "Java"))
print(msg.find("@"))
print(email.find("@"))

print(email.endswith(".com"))
print(mobile.startswith("05"))
print("@" in email)
print(email.__contains__("@"))
print(name.isalpha())
print(mobile.isdigit())
