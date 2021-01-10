
plate = input("Enter a plate number: ")
plate = plate.replace(" ", "")

valid_length = len(plate) >= 4 and len(plate) <= 7
valid_part1 = plate[:3].isalpha()
valid_part2 = plate[3:].isdigit()

if valid_length and valid_part1 and valid_part2:
    print("Valid Plate Number")
else:
    print("Invalid Plate Number")
