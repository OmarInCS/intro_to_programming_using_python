
# break, continue
# for x in range(1, 11):
#     if x == 5:
#         break
#     print(x, end="\t")
# print()
#
# for x in range(1, 11):
#     if x == 5:
#         continue
#     print(x, end="\t")
# print()

for y in range(1, 11):
    for x in range(1, 11):
        if x == 5 and y == 3:
            continue
        print(x, end="\t")
    print()
