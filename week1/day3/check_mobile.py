
mobile = input("Enter a mobile number: ")

if len(mobile) == 10 and mobile.startswith("05") and mobile.isdigit():
    print("Valid Mobile Number")
else:
    print("Invalid Mobile Number")
