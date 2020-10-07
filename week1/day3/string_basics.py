
name = "Omar"
mobile = "0599888921"
email = "omarincs@gmail.com"
message = "Welcome to Python"

print(message[0])
print(message[-1])
print(len(message))
print(message[0:7])
print(message[:7])
print(message[-6:])

message2 = message[:8] * 2 + name
print(message2)

print(message.upper())
print(message.lower())
print(message.startswith("Wel"))
print(mobile.startswith("05"))
print(email.endswith(".com"))
print("@" in email)

print(name.isalpha())
print(mobile.isdigit())
print(email[0:email.find("@")].isalnum())
print(email.find("@"))

