
password = input("Enter a new password: ")

if len(password) < 8:
    print("Weak password")
else:
    digit_count = 0
    upper_count = 0

    # for i in range(len(password)):
    #     if password[i].isdigit()
    for letter in password:
        if letter.isdigit():
            digit_count += 1
        elif letter.isupper():
            upper_count += 1

    if digit_count < 2 or upper_count < 2:
        print("Weak password")
    else:
        print("Strong password")
