
ssn = input("Enter your SSN: ")

if len(ssn) != 11:
    print("Invalid SSN")
elif ssn[3] != "-" or ssn[6] != "-":
    print("Invalid SSN")
elif not ssn.replace("-", "").isdigit():
    print("Invalid SSN")
else:
    print("Valid SSN")


# if len(ssn) == 11 \
#         and ssn[3] == "-" \
#         and ssn[6] == "-" \
#         and ssn.replace("-", "").isdigit():
#     print("Valid")
# else:
#     print("Invalid")
#