
# x = 5
# y = x
# y += 3
#
# print(x)
# print(y)

x_lst = [10, 20, 30]
# y_lst = x_lst
# y_lst = list(x_lst)
y_lst = x_lst.copy()
z_lst = [v+2 for v in x_lst]

y_lst[1] += 3

print(x_lst)
print(y_lst)
print(z_lst)



