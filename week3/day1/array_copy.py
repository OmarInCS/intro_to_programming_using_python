
x = [10, 20, 30]
# y = x
# y = x.copy()
y = list(x)
z = [value // 10 for value in x]

x[1] += 3

print(x)
print(y)
print(z)
