
x, y = eval(input("Enter two integers: "))

gcd = 1
for div in range(2, x + 1):
    if x % div == 0 and y % div == 0:
        gcd = div

print("GCD:", gcd)
