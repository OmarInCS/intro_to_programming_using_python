
n = eval(input("Enter the number of students: "))
final_mark = eval(input("Enter the final mark: "))

for i in range(n):
    mark = eval(input("Enter the std. mark: "))
    pct = mark / final_mark * 100
    print(f"The percentage: {pct}%")
    if pct >= 50:
        print("Pass")
    else:
        print("Fail")
