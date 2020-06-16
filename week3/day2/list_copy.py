
x = [10, 20, 30]
# y = x
# y = list(x)
y = x.copy()
z = [v*10 for v in x]   # comprehension list

y[1] += 2

print(x)
print(y)
print(z)
