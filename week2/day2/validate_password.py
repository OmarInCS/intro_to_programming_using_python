
password = input("Enter new password: ")

if len(password) < 8:
    print("Invalid Password")
else:
    upper_count = 0
    digit_count = 0

    for c in password:
        if c.isupper():
            upper_count += 1
        elif c.isdigit():
            digit_count += 1

    if upper_count < 2 or digit_count < 2:
        print("Invalid Password")
    else:
        print("Valid Password")