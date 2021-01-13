
name = "Omar"
email = "omarincs@gmail.com"
mobile = "0599888921"
message = "Welcome to Python"

print(message)
print(len(message))
print(message[0])
print(message[-1])
print(message[0:7])
print(message[:7])
print(message[-6:])

title = message[:8] * 2 + name
print(title)

print(message.upper())
print(message.lower())
print(message.replace("Python", "Java"))
print(message.count("o"))

print(name.isalpha())
print(mobile.isdigit())
print(mobile.startswith("05"))
print(email.endswith(".com"))
print("@" in email)












