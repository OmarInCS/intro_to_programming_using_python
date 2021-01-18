
text = input("Enter a text: ").lower()

for char in text:
    if char in "abc":
        print(2, end="")
    elif char in "def":
        print(3, end="")
    elif char in "ghi":
        print(4, end="")
    elif char in "jkl":
        print(5, end="")
    elif char in "mno":
        print(6, end="")
    elif char in "pqrs":
        print(7, end="")
    elif char in "tuv":
        print(8, end="")
    elif char in "wxyz":
        print(9, end="")
    else:
        print(char, end="")