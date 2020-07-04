
x = 5   # global variable


def my_func():
    global x

    x = 10  # local variable
    print(x)


my_func()
print(x)
