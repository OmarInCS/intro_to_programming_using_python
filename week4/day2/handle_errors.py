
try:
    x, y = eval(input("Enter two numbers: "))
    print("Result:", x / y)
# except ZeroDivisionError as ex:
#     print("Cannot divide by zero")
# except TypeError as ex:
#     print("should enter two numbers")
except Exception as ex:
    print("Recheck your input")

print("-- Good Bye --")

