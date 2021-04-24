# 1) password 8 char or more
# 2) at least 2 upper letters
# 3) at least 2 digits

# Ahmed123, 20AhmeD20

password = input("Enter a password: ")

if len(password) < 8:
    print("Weak Password")
else:
    upper_count = 0
    digit_count = 0
    for c in password:
        if c.isupper():
            upper_count += 1
        elif c.isdigit():
            digit_count += 1

    if upper_count < 2 or digit_count < 2:
        print("Weak Password")
    else:
        print("Strong Password")

