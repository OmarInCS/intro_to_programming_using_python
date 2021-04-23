
name = "Omar Karem"
email = "omarincs@gmail.net"
mobile = "0599888921"
message = "Welcome to Python"

print(message[0])
print(message[-1])
print(message[0:7])
print(message[:7])
print(message[-6:])
print(len(name))

print(message.upper())
print(message.lower())
print(name.upper())

title = message[:8] * 2 + name
print(title)

print(message.replace("Python", "Java"))
print(message.startswith("we"))
print(mobile.startswith("05"))
print(email.endswith(".com"))

print(mobile.isdigit())
print(name.replace(" ", "").isalpha())