
plate = input("Enter plate number: ")

if len(plate) >= 4 and len(plate) <= 7 and plate[:3].isalpha() and plate[3:].isdigit():
    print("Valid")
else:
    print("Invalid")
