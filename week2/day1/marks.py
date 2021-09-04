
n = eval(input("Entre num of students: "))
full_mark = eval(input("Enter exam full mark: "))

for i in range(n):
    mark = eval(input("Enter std. mark: "))
    pct = mark / full_mark * 100
    print("PCT:", pct)
    if pct >= 50:
        print("Pass")
    else:
        print("Fail")

