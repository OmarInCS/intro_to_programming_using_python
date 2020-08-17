
password = input("Enter a password: ")

if len(password) < 8:
    print("Invalid Password")
else:
    count_upper = 0
    count_digit = 0

    for letter in password:
        if letter.isupper():
            count_upper += 1
        elif letter.isdigit():
            count_digit += 1

    if count_digit < 2 or count_upper < 2:
        print("Invalid Password")
    else:
        print("Valid Password")
