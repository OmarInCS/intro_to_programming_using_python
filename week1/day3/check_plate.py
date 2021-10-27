
plate = input("Enter a plate number: ")

if 4 <= len(plate) <= 7 and plate[:3].isalpha() and plate[3:].isdigit():
    print("Valid plate number")
else:
    print("Invalid plate number")

