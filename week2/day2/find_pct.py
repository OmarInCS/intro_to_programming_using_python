
n = eval(input("Enter num of students: "))
final_mark = eval(input("Enter the final mark: "))
pass_count = 0

for i in range(n):
    mark = eval(input("Enter a mark: "))
    pct = mark / final_mark * 100

    if pct >= 50:
        print("Pass", pct, "%")
        pass_count += 1
    else:
        print("Fail", pct, "%")

print("The #pass:", pass_count)
print("The #fail:", n - pass_count)
