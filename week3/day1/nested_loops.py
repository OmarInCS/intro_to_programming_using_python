
# for y in range(1, 11):
#     for x in range(1, 11):
#         print(x, end="\t")
#     print()


# for y in range(1, 11):
#     for x in range(1, 11):
#         if x == 5 and y == 2:
#             break
#         print(x, end="\t")
#     print()


for y in range(1, 11):
    for x in range(1, 11):
        if x <= y:
            print("X", end="")
            continue
        print(x, end="")
    print()

# print("-" * 20)
# for y in range(1, 11):
#     for x in range(y): # 0,1,2,3,4
#         print("X", end="")
#         # if x == y:
#         #     break
#     print()

print("-" * 20)

for y in range(1, 7):
    for x in range(6, 0, -1):
        if x > y:
            print(" ", end=" ")
            continue
        print(x, end=" ")
    print()


print("-" * 20)

for y in range(1, 7):
    for x in range(1, 7):
        print(x, end=" ")
        if x == y:
            break
    print()
