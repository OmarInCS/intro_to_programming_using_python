
# break, continue

# for y in range(1, 11):
#     for x in range(1, 11):
#         print(x, end="\t")
#     print()
#

# for y in range(1, 11):
#     for x in range(1, 11):
#         if x == 5 and y == 2:
#             break
#         print(x, end="\t")
#     print()

for y in range(1, 11):
    for x in range(1, 11):
        if x == 5 and y == 2:
            print("*", end="\t")
            continue
        print(x, end="\t")
    print()