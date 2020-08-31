
final_mark = eval(input("Enter final Mark: "))
count = 0

for i in range(5):
    mark = eval(input(f"Enter a mark: "))
    pct = mark / final_mark * 100
    print("Percentage: ", pct)
    if pct > 85:
        print("Excellent")
        count += 1
    elif pct > 75:
        print("V. Good")
    elif pct > 65:
        print("Good")
    elif pct >= 50:
        print("Pass")
    else:
        print("Fail")

    print("-" * 30)

print("Excellent students are:", count)
