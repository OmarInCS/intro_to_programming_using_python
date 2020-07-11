
x = [10, 20, 30]
# y = x
# y = list(x)
y = x.copy()
# z = [value / 10 for value in x]
z = [value - 5 for value in x]

y[0] += 2

print(x)
print(y)
print(z)