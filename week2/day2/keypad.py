
text = input("Enter a text: ")
text = text.upper()

for char in text:
    if char in "QZ":
        print(1, end="")
    elif char in "ABC":
        print(2, end="")
    elif char in "DEF":
        print(3, end="")
    elif char in "GHI":
        print(4, end="")
    elif char in "JKL":
        print(5, end="")
    elif char in "MNO":
        print(6, end="")
    elif char in "PRS":
        print(7, end="")
    elif char in "TUV":
        print(8, end="")
    elif char in "WXY":
        print(9, end="")
