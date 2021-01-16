
x = [10, 20, 30, 40, 50, 60]
# y = x
# y = list(x)
y = x.copy()
z = [v*10 for v in x if v > 30] # list comprehension
# z = []
# for v in x:
#     z.append(v*10)

y[0] += 2

print(x)
print(y)
print(z)
