
name = "Omar"
email = "OmarInCS@gmail.com"
mobile = "0599888921"
message = "Welcome to Python"

print(message)
print(message[0])
print(message[-1])
print(message[0:7])
print(message[:7])
print(message[-6:])

title = message[:8] * 2 + name
print(title)

print(message.replace("Python", "Java"))
print(email.endswith(".com"))
print(mobile.startswith("05"))
print("@" in email)

print(name.isalpha())
print(mobile.isdigit())