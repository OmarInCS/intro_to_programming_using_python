
x = 5

def do_something():
    global x
    x = 15
    print(x)

do_something()
print(x)
