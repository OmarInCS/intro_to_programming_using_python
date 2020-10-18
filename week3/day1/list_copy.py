
x = [10, 20, 30]
# y = x
# y = list(x)
y = x.copy()
z = [v + 2 for v in y] # comprehension list

y[1] += 2

print(x)
print(y)
print(z)

marks = [23, 20, 17, 13]
pct = [m / 25 * 100 for m in marks]
print(pct)
