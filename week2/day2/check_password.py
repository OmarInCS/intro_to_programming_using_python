
password = input("Enter a password: ")

if len(password) < 8:
    print("Weak Password")
else:
    upper_count = 0
    digit_count = 0

    for letter in password:
        if letter.isupper():
            upper_count += 1
        elif letter.isdigit():
            digit_count += 1

    if upper_count < 2 or digit_count < 2:
        print("Weak Password")
    else:
        print("Strong Password")
