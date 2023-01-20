
try:
    x, y = eval(input("Enter two numbers: "))
    print("Result:", x / y)
# except ZeroDivisionError as ex:
#     print("second number cannot be zero")
# except TypeError as ex:
#     print("must be two numbers")
except Exception as ex:
    print("recheck your input")

print("-- Good Bye --")
