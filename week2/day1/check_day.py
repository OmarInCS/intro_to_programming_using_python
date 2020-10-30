
day = eval(input("Enter day number: "))

# if day >= 1 and day <= 5:
if 1 <= day <= 5:
    print("Work-day")
elif day == 6 or day == 7:
    print("Off-day")
else:
    print("Invalid Day number")
