
n = eval(input("Enter num. of std: "))
final_mark = eval(input("Enter the final mark: "))

for i in range(n):
    mark = eval(input(f"Enter mark of std #{i+1}: "))
    pct = mark / final_mark * 100
    print("Percentage:", pct, "%")

    if pct > 85:
        print("Excellent")
    elif pct > 75:
        print("V. Good")
    elif pct > 65:
        print("Good")
    elif pct >= 50:
        print("Pass")
    else:
        print("Fail")
