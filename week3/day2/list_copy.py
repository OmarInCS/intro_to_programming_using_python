
x = [10, 20, 30]
# y = x
# y = list(x)
y = x.copy()
# z = [m + 2 for m in x] # list comprehension
z = [m * 10 for m in x]

y[1] += 3

print(x)
print(y)
print(z)