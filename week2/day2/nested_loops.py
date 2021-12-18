
# for y in range(1, 11):
#     for x in range(1, 11):
#         print(x, end="\t")
#     print()

# break, continue

# for y in range(1, 11):
#     for x in range(1, 11):
#         if y == 3 and x == 5:
#             break
#         print(x, end="\t")
#     print()

for y in range(1, 11):
    for x in range(1, 11):
        if y == x:
            print("X", end="\t")
            continue
        print(x, end="\t")
    print()
