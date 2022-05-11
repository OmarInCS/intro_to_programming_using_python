
name = "Omar Karem"
email = "omarincs@gmail.com"
mobile = "0599888921"
message = "Welcome to Python"

print(message[0])
print(message[-1])
print(len(name))
print(message[0:7])
print(message[:7])
print(message[-6:])

title = message[:8] * 2 + name
print(title)

print(message.upper())
print(message.lower())
print(message.replace("Python", "Java"))

print(mobile.startswith("05"))
print(email.endswith(".com"))
print(email.__contains__("@"))
print("@" in email)

print(name.isalpha())
print(mobile.isdigit())
print(name.isalnum())
print(name.replace(" ", "").isalpha())
