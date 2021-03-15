
try:
    x, y = eval(input("Enter two integers: "))
    print(x / y)
# except ZeroDivisionError as ex:
#     print("Cannot divide by zero")
# except TypeError as ex:
#     print("Two inputs are required")
except Exception as ex:
    print("Plz, recheck your input")

print("--- Good Bye ---")
