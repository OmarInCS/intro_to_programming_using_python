
mobile = input("Enter a mobile number: ")

if len(mobile) == 10 and mobile.startswith("05") and mobile.isdigit():
    print("Valid mobile number")
else:
    print("Invalid mobile number")
