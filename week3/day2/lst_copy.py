
x_lst = [10, 20, 30]
# y_lst = x_lst
# y_lst = list(x_lst)
y_lst = x_lst.copy()
z_lst = [x+3 for x in x_lst]  # list comprehension

y_lst[0] += 3

print(x_lst)
print(y_lst)
print(z_lst)
