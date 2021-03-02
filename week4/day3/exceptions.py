
try:
    x, y = eval(input("Enter two integers: "))
    print("Result:", x / y)
# except ZeroDivisionError as ex:
#     print("Number can't be zero")
# except TypeError as ex:
#     print("Enter two numbers")
except Exception as ex:
    print("Plz, recheck your input")
    print(ex)

print("Thank You")
