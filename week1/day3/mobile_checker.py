
mobile = input("Enter your mobile number: ")

if len(mobile) != 10:
    print("Invalid Mobile Number")
elif not mobile.startswith("05"):
    print("Invalid Mobile Number")
elif not mobile.isdigit():
    print("Invalid Mobile Number")
else:
    print("Valid Mobile Number")