
try:
    x, y = eval(input("Enter two integers: "))
    print("Result:", x / y)
# except ZeroDivisionError as ex:
#     print("second number cannot be zero")
# except TypeError as ex:
#     print("make sure to enter two numbers")
except Exception as ex:
    print("Recheck your input")

print("-- Good Bye --")
