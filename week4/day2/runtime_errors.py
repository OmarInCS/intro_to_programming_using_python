
try:
    x, y = eval(input("Enter two number: "))
    print(x / y)
except ZeroDivisionError as ex:
    print("second number can't be 0")
except ValueError:
    print("enter just two numbers with comma in between")

print("Good Bye")
