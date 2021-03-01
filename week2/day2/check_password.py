
password = input("Enter a password: ")

if len(password) < 8:
    print("Weak Password")
else:
    digit_count = 0
    upper_count = 0

    for letter in password:
        if letter.isdigit():
            digit_count += 1
        elif letter.isupper():
            upper_count += 1

    if digit_count < 2 or upper_count < 2:
        print("Weak Password")
    else:
        print("Strong Password")


