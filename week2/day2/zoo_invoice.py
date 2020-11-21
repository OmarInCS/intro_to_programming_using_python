
while True:
    n = eval(input("How many persons? "))
    cost = 0

    for i in range(n):
        age = eval(input("Enter the age: "))
        if age >= 3 and age <= 12:
            cost += 14
        elif age >= 13 and age <= 64:
            cost += 20
        elif age >= 65:
            cost += 18

    print("The total cost:", cost, "SAR")
    print("-" * 30)
    exit = input("Want to exit (y/n)? ")
    if exit == "y":
        break

