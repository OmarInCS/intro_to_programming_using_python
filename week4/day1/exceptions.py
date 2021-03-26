
try:
    x, y = eval(input("Enter two numbers: "))
    print("Result:", x/y)
# except ZeroDivisionError as ex:
#     print("second number can't be zero")
# except TypeError as ex:
#     print("Enter two numbers")
except Exception as ex:
    print("Recheck your input")

print("-- Good Bye --")
