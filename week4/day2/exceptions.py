
try:
    x, y = eval(input("Enter two numbers: "))
    print(x / y)
except Exception as ex:
    print(ex)
# except ZeroDivisionError as ex:
#     print("1)", ex)
# except ValueError as ex:
#     print("2)", ex)

print("-- End --")
