
x = [10, 20, 30]
# y = x
# y = list(x)
y = x.copy()
z = [i*10 for i in x]

x[1] += 2

print(x)
print(y)
print(z)
