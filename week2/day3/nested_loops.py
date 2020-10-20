# break, continue
# for y in range(1, 11):
#     for x in range(1, 11):
#         print(x, end=" ")
#     print()

# for y in range(1, 11):
#     for x in range(1, 11):
#         if x == 5 and y == 2:
#             break
#         print(x, end=" ")
#     print()

# for y in range(1, 11):
#     for x in range(1, 11):
#         if x == 5 and y == 2:
#             print("X", end=" ")
#             continue
#         print(x, end=" ")
#     print()

for y in range(1, 11):
    for x in range(1, 11):
        if x == y:
            print("X", end=" ")
            continue
        print(x, end=" ")
    print()