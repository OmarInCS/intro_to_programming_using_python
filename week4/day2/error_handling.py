
try:
    x, y = eval(input("Enter two numbers: "))
    print("result:", x / y)
# except ZeroDivisionError as ex:
#     print("division by zero not allowed")
# except TypeError as ex:
#     print("Enter two numbers")
except Exception as ex:
    print("review your input")
    print(ex)

print("-- Good Bye --")
