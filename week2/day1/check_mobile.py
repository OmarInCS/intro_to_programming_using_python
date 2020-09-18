
mobile = input("Enter mobile number: ")

if len(mobile) == 10 and mobile.startswith("05") and mobile.isdigit():
    print("Valid Mobile Number")
else:
    print("Invalid Mobile Number")


if len(mobile) != 10:
    print("Invalid Mobile Number")
elif not mobile.startswith("05"):
    print("Invalid Mobile Number")
elif not mobile.isdigit():
    print("Invalid Mobile Number")
else:
    print("Valid Mobile Number")