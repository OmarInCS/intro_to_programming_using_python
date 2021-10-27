
ssn = input("Enter a SSN: ")

if ssn[3] == "-" and ssn[6] == "-" and len(ssn.replace("-", "")) == 9 and ssn.replace("-", "").isdigit():
    print("Valid SSN")
else:
    print("Invalid SSN")
