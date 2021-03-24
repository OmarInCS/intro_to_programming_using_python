# 0599888921
m1, m2, m3 = eval(input("Enter three marks: "))

avg = (m1 + m2 + m3) / 3

print("The average:", round(avg, 2))
print("The best:", max(m1, m2, m3))
print("The worst:", min(m1, m2, m3))
