
try:
    x, y = eval(input("Enter two integers: "))
    print(x / y)
# except ZeroDivisionError as ex:
#     print("Zero is not allowed")
# except TypeError as ex:
#     print("two numbers are required")
except Exception as ex:
    print("Recheck your input")

print("Thank You!")
