
x, y, z = eval(input("Enter three marks: "))

avg = (x + y + z) / 3

print("The best mark:", max(x, y, z))
print("The worst mark:", min(x, y, z))
print("The average mark:", round(avg, 2))
