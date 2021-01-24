
x = [10, 20, 30]
# y = x
# y = list(x)
y = x.copy()
z = [v*10 for v in x]
# z = []
# for v in x:
#     z.append(v * 10)

y[0] += 3

print(x)
print(y)
print(z)