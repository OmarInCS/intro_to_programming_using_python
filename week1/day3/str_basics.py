
name = "Omar"
email = "omarincs@gmail.com"
mobile = "0599888921"
message = "Welcome to Python"

print(message[0])
print(message[-1])
print(message[0:7])
print(message[:7])
print(message[-6:])
print(len(message))

text = message[:8] * 2 + name
print(text)

print(message.upper())
print(message.lower())
print(message.replace("Python", "SQL"))
print(message.startswith("Wel"))
print(mobile.startswith("05"))
print(email.endswith(".com"))
print("@" in email)

print(name.isalpha())
print(name[0].isupper())
print(mobile.isdigit())