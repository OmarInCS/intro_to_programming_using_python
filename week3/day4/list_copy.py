
x = [10, 20, 30]
# y = x
# y = list(x)
y = x.copy()
z = [value / 2 for value in x]

print("x:", x)
print("y:", y)
print("z:", z)

y[1] += 3

print("x:", x)
print("y:", y)
