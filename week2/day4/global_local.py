
x = 5

def do_some_thing():
    global x
    x = 13
    print(x)


do_some_thing()
print(x)
