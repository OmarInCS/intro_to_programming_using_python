
password = input("Enter a new password: ")

if len(password) < 8:
    print("Invalid Password")
else:
    digit_count = 0
    upper_count = 0

    for c in password:
        if c.isdigit():
            digit_count += 1
        elif c.isupper():
            upper_count += 1

    if digit_count < 2 or upper_count < 2:
        print("Invalid Password")
    else:
        print("Valid Password")
