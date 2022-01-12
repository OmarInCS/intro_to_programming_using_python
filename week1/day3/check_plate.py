
plate = input("Enter a plate number: ")

if len(plate) >= 4 and len(plate) <= 7 and plate[:3].isalpha() and plate[3:].isdigit():
    print("Valid Plate number")
else:
    print("Invalid Plate number")
