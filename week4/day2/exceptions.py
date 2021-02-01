
try:
    x, y = eval(input("Enter two numbers: "))
    print("Result:", x / y)
# except ZeroDivisionError as ex:
#     print(ex)
# except TypeError as ex:
#     print("enter exactly two integers")
except Exception as ex:
    print("enter exactly two positive integers")
print("--- End ---")
