
try:
    x, y = eval(input("Enter two integers: "))
    result = x / y
    print("Result:", result)
# except ZeroDivisionError:
#     print("2nd num. can't be zero")
# except TypeError:
#     print("two numbers are required")
except Exception as ex:
    print("plz, check your input")
    print(ex)

print("--- Good Bye ---")
