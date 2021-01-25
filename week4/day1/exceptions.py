
try:
    x, y = eval(input("Enter two number: "))
    print("Result:", x / y)
except Exception as ex:
    print(ex)
# except ZeroDivisionError as ex:
#     print(ex)
# except NameError as ex:
#     print("Plz, enter number")

print("--- End ---")