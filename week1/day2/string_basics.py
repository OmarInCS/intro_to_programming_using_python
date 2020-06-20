
name = "Omar"
mobile = "0599888921"
email = "OmarInCS@gmail.com"

print(len(name))
print(name[0])
print(name[-1])
print(email[:8])
print(email[9:])

print(email.find("@"))
print(mobile.startswith("05"))
print(email.endswith(".com"))
print(mobile.isdigit())
print(name.isalpha())
print(mobile.count("9"))
print("@" in email)
print(email.upper())
print(name.center(20, "-"))