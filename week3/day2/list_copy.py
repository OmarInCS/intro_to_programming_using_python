
x = [10, 20, 30]
# y = x
# y = list(x)
y = x.copy()
z = [v+2 for v in x]

y[1] += 3

print(x)
print(y)
print(z)
