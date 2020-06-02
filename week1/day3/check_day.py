
day = eval(input("Enter a day number: "))

if day >= 1 and day <= 5:
    print("Work-day")
elif day == 6 or day == 7:
    print("off-day")
else:
    print("Invalid Day Number")

