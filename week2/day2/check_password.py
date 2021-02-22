
password = input("Enter new password: ")

if len(password) < 8:
    print("Weak password")
else:
    digit_count = 0
    upper_count = 0

    for letter in password:
        if letter.isdigit():
            digit_count += 1
        elif letter.isupper():
            upper_count += 1

    if digit_count >= 2 and upper_count >= 2:
        print("Strong password")
    else:
        print("Weak password")