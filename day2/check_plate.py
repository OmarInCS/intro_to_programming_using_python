
plate = input("Enter a plate number: ")

if len(plate) < 4 or len(plate) > 7:
    print("Invalid Plate Number!!")
elif not plate[:3].isalpha():
    print("Invalid Plate Number!!")
elif not plate[3:].isdigit():
    print("Invalid Plate Number!!")
else:
    print("Valid Plate Number")

