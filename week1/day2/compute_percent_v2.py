
mark = eval(input("Enter your mark: "))
full_mark = eval(input("Enter exam full mark: "))

pct = mark / full_mark * 100
print("Percent:", pct, "%")

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
