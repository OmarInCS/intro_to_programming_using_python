
text = input("Enter a text: ").lower()

print("code: ", end="")
for letter in text:
    if letter in "abc":
        print(2, end="")
    elif letter in "def":
        print(3, end="")
    elif letter in "ghi":
        print(4, end="")
    elif letter in "jkl":
        print(5, end="")
    elif letter in "mno":
        print(6, end="")
    elif letter in "pqrs":
        print(7, end="")
    elif letter in "tuv":
        print(8, end="")
    elif letter in "wxyz":
        print(9, end="")
    else:
        print(letter, end="")
