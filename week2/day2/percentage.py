
n = eval(input("Enter number of students: "))
final_mark = eval(input("Enter the final Mark: "))

for i in range(n):
    mark = eval(input("Enter student mark: "))
    pct = mark / final_mark * 100
    print("Percentage:", pct)

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
