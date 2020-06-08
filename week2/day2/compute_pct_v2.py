
final_mark = eval(input("Enter the exam final mark: "))
n = eval(input("Enter the number of students: "))
excellent_count = 0

for i in range(1, n+1):
    mark = eval(input("Enter student mark: "))
    pct = mark / final_mark * 100

    print("pct:", pct)

    if pct > 85:
        print("Excellent")
        excellent_count += 1
    elif pct > 75:
        print("V. Good")
    elif pct > 65:
        print("Good")
    elif pct >= 50:
        print("Pass")
    else:
        print("Fail")

print("Excellent count: ", excellent_count)