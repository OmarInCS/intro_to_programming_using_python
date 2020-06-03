
email = input("Enter ur email: ")

idx = email.find("@")

if not "@" in email:
    print("Invalid email")
elif not email[:idx].isalnum():
    print("Invalid email")
elif not email.endswith(".com"):
    print("Invalid email")
else:
    print("Valid email")