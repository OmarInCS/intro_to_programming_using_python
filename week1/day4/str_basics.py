
name = "Omar Karem"
email = "OmarInCS@gmail.com"
mobile = "0599888921"
msg = "Welcome to Python"

print(msg[0])
print(msg[-1])
print(len(msg))
print(msg[0:7])
print(msg[:7])
print(msg[-6:])

title = msg[:8] * 2 + name
print(title)

print(msg.upper())
print(msg.lower())
print(msg.replace("Python", "Java"))

print(mobile.startswith("05"))
print(email.endswith(".com"))
print(email.__contains__("@"))
print("@" in email)

print(mobile.isdigit())
print(name.replace(" ", "").isalpha())

