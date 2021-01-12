
password = input("Enter a password: ")

if len(password) < 8:
    print("Invalid Password")
else:
    digits_count = 0
    upper_count = 0
    for letter in password:
        if letter.isdigit():
            digits_count += 1
        elif letter.isupper():
            upper_count += 1

    if digits_count >= 2 and upper_count >= 2:
        print("Valid Password")
    else:
        print("Invalid Password")
