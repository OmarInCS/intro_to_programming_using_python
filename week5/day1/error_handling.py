
try:
    x, y = eval(input("Enter two numbers: "))
    print("Result:", x / y)
# except ZeroDivisionError as ex:
#     print("second number can't be zero")
# except TypeError as ex:
#     print("must have two inputs")
except Exception as ex:
    print("recheck your inputs")

print("-- Good Bye --")
