
text = "Welcome to Python"
name = "Omar"
mobile = "0599888921"
email = "omarincs@gmail.com"

print(text[0])
print(text[-1])
print(len(text))
print(text[0:7])
print(text[:7])
print(text[-6:])

message = text[:8] * 2 + name
print(message)

print(text.upper())
print(text.lower())
print(mobile.startswith("05"))
print(email.endswith(".net"))
print("@" in email)
print(message.replace("Omar", "Sultan"))
print(name.isalpha())
print(mobile.isdigit())