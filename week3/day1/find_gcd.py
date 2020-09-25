
x, y = eval(input("Enter two numbers: "))

gcd = 1
for div in range(2, min(x, y) + 1):
    if x % div == 0 and y % div == 0:
        gcd = div

print("GCD is:", gcd)
