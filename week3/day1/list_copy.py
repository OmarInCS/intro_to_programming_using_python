
x = [10, 20, 30]
# y = x
# y = list(x)
y = x.copy()
z = [v/10 for v in x]

y[0] += 3

print(x)
print(y)
print(z)

