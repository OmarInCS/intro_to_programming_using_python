
# def print_1_100(n):
#     print(n)
#     if n == 100: return
#     print_1_100(n + 1)
#
#
# print_1_100(1)

# from random import randint
# rand_list = []
# for i in range(20):
#     num = randint(1, 50)
#     while num in rand_list:
#         num = randint(1, 50)
#
#     rand_list.append(num)
#
# print(rand_list)

units_list = [500, 100, 50, 20, 10, 5, 1, 0.5, 0.25, 0.1]
money = 400
output = ""

for unit in units_list:
    while money >= unit:
        money -= unit
        output += f"{unit} + "

output += f"{round(money, 2)}"

print(output)
print(eval(output))