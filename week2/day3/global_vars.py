
x = 15

def do_something():
    global x
    x = 5
    print(x)


do_something()
print(x)