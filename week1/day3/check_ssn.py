
ssn = input("Enter a SSN: ")

if len(ssn) != 11:
    print("Invalid SSN")
elif ssn[3] != "-" or ssn[6] != "-":
    print("Invalid SSN")
elif not ssn.replace("-", "").isdigit():
    print("Invalid SSN")
else:
    print("Valid SSN")
