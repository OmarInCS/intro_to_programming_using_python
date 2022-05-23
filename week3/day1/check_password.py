
password = input("Enter a new password: ")

if len(password) < 8:
    print("Weak password")
else:
    upper_count = 0
    digit_count = 0

    for char in password:
        if char.isupper():
            upper_count += 1
        elif char.isdigit():
            digit_count += 1

    if upper_count < 2 or digit_count < 2:
        print("Weak Password")
    else:
        print("Strong Password")
