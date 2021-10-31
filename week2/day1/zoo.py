
info = input("Enter person age (or exit): ")
total = 0

while info != "exit":
    if info.isdigit():
        age = eval(info)
        if age > 50:
            total += 10
        elif age > 20:
            total += 15
        elif age > 2:
            total += 5

    info = input("Enter person age (or exit): ")

print("Total cost:", total, "SAR")
