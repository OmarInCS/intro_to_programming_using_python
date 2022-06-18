
day = eval(input("Enter a day number: "))

# if day == 7 or day >= 1 and day <= 4:
if day == 7 or 1 <= day <= 4:
    print("Work-day")
elif day == 5 or day == 6:
    print("Off-day")
else:
    print("Invalid day number")
