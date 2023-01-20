
name = "Omar"
email = "omarincs@gmail.com"
mobile = "0599888921"
message = "Welcome to Python"

print(name[0])
print(name[1])
print(name[-1])
print(len(name))
print(message[0:7])
print(message[:7])
print(message[8:10])
print(message[-6:])

print(message.upper())
print(message.lower())
print(message.replace("Python", "Java"))

print(mobile.startswith("05"))
print(email.endswith(".sa"))
print(email.__contains__("@"))
print("@" in email)

print(name.isalpha())
print(mobile.isdigit())
