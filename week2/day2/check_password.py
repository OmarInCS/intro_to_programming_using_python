
from string import punctuation

password = input("Enter a password: ")

if len(password) < 8:
    print("Weak password")
else:
    digit_count = 0
    upper_count = 0
    has_punct = False

    for ch in password:
        if ch.isdigit():
            digit_count += 1
        elif ch.isupper():
            upper_count += 1
        elif ch in punctuation:
            has_punct = True

    if digit_count < 2 or upper_count < 2 or has_punct == True:
        print("Weak password")
    else:
        print("Strong Password!!")