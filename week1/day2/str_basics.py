
name = "Om2r"
email = "omarincs@gmail.com"
mobile = "0599 888 921"
message = "Welcome to Python"

print(message[0])
print(message[-1])
print(message[0:7])
print(message[:7])
print(message[-6:])
print(message)
print(len(message))

print(message.upper())
print(message.replace("Python", "Java"))

title = message[:8] * 2 + name
print(title)

print(mobile.startswith("05"))
print(email.endswith(".com"))
print("@" in email)
print(email.__contains__("@"))

print(name.istitle())
print(name.isalpha())
print(name.isalnum())
print(mobile.isdigit())