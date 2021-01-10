
from string import punctuation

name = "Omar"
email = "omar@gmail.com"
mobile = "0599888921"
message = "Welcome to Python"

print(len(name))
print(name[0])
print(name[-1])
print(message[0:7])
print(message[:7])
print(message[-6:])

text = message[:8] * 2 + name
print(text)

print(text.upper())
print(text[:3].upper() + text[3:])
print(text.lower())
print(message.replace("Python", "Java"))
print(message.startswith("Wel"))
print(mobile.startswith("05"))
print(email.endswith(".com"))
print("@" in email)

print(name.isalpha())
print(mobile.isdigit())

print("?" in punctuation)