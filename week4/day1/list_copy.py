
x = [10, 20, 30]
# y = x
# y = x.copy()
y = list(x)
z = [v*10 for v in x]

y[1] += 2

print(x)
print(y)
print(z)