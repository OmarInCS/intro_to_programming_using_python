
try:
    x, y = eval(input("Enter two numbers: "))
    z = x / y
    print(z)
except Exception as ex:
    print(ex)
# except ZeroDivisionError as ex:
#     print(ex)
# except TypeError as ex:
#     print("too few inputs")

print("--- End ---")
