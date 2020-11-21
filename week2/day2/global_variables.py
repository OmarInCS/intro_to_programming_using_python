
x = 5

def print_x():
    global x
    x = 15
    print(x)

print_x()
print(x)