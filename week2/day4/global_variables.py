
x = 5


def my_func():
    global x
    x = 15
    print(x)


my_func()
print(x)