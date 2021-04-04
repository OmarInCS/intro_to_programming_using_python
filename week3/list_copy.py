
x = [10, 20, 30]
# y = x
# y = list(x)
y = x.copy()
z = [v+3 for v in x]    # list comprehension

# for i in range(3):
#     y[i] += 3
y[0] += 3

print(x)
print(y)
print(z)
