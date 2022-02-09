
n = eval(input("Enter num. of std.: "))
full_mark = eval(input("Enter exam full mark: "))
pass_count = 0

for i in range(n):
    mark = eval(input("Enter std. mark: "))
    pct = mark / full_mark * 100
    print("PCT:", pct)
    if pct >= 50:
        print("Pass")
        pass_count += 1
    else:
        print("Fail")

print("Pass count:", pass_count)
