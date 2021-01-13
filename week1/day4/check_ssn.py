
ssn = input("Enter SSN: ")

if len(ssn) == 11 and ssn[3] == "-" and ssn[6] == "-" and ssn.replace("-", "").isdigit():
    print("Valid SSN")
else:
    print("Invalid SSN")
