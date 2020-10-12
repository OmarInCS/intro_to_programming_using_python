
n = eval(input("Enter number of students: "))
final_mark = eval(input("Enter final mark: "))

excellent_count = 0

for i in range(n):
    mark = eval(input("Enter a mark: "))
    pct = mark / final_mark * 100
    print("PCT:", pct)

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

print("Excellent Count: ", excellent_count)