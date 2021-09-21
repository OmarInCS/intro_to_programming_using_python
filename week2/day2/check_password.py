
password = input("Enter a new password: ")

if len(password) < 8:
    print("Weak password")
else:
    digit_count = 0
    upper_count = 0

    for ch in password:
        if ch.isupper():
            upper_count += 1
        elif ch.isdigit():
            digit_count += 1

    if digit_count < 2 or upper_count < 2:
        print("Weak password")
    else:
        print("Strong password")
