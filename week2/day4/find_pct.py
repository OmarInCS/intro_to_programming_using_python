
n = eval(input("Enter the num. of std.: "))
final_mark = eval(input("Enter the final mark: "))

for i in range(n):
    mark = eval(input("Enter a mark: "))
    pct = mark / final_mark * 100
    if pct >= 50:
        print("Pass", pct, "%")
    else:
        print("Fail", pct, "%")
