
full_mark = eval(input("Enter the exam full mark: "))

pass_count = 0

for i in range(5):
    mark = eval(input("Enter the std. mark: "))
    pct = mark / full_mark * 100
    print("PCT:", pct, "%")
    if pct >= 50:
        print("Pass")
        pass_count += 1
    else:
        print("Fail")

print("number of passing students: ", pass_count)
