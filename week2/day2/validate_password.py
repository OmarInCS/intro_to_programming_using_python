
password = input("Enter a password: ")

if len(password) < 8:
    print("Invalid Password")
else:
    upper_count = 0
    digits_count = 0

    for ch in password:
        if ch.isupper():
            upper_count += 1
        elif ch.isdigit():
            digits_count += 1

    if upper_count < 2 or digits_count < 2:
        print("Invalid Password")
    else:
        print("Valid Password")