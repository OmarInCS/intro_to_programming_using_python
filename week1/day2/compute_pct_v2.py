
mark = eval(input("Enter a mark: "))
final_mark = eval(input("Enter the final mark: "))
pct = mark / final_mark * 100

print("Your Percentage: ", pct)

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
