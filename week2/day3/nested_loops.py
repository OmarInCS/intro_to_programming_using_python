# break, continue
# for y in range(1, 11):
#     for x in range(1, 11):
#         print(x, end="\t")
#     print()

# for y in range(1, 11):
#     for x in range(1, 11):
#         if x == 5 and y == 3:
#             break
#         print(x, end="\t")
#     print()

# for y in range(1, 11):
#     for x in range(1, 11):
#         if x == 5 and y == 3:
#             print("#", end="\t")
#             continue
#         print(x, end="\t")
#     print()

for y in range(1, 11):
    for x in range(1, 11):
        if x == y or x + y == 11:
            print("#", end="\t")
            break
        print(x, end="\t")
    print()