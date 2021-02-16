
m1, m2, m3 = eval(input("Enter three marks: "))

avg = (m1 + m2 + m3) / 3

print("The best mark:", max(m1, m2, m3))
print("The worst mark:", min(m1, m2, m3))
print("The average mark:", round(avg, 2))