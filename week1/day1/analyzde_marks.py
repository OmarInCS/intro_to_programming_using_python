# 0599 888 921
m1, m2, m3 = eval(input("Enter three marks: "))

avg = (m1 + m2 + m3) / 3

print("Average mark:", round(avg, 3))
print("Best mark:", max(m1, m2, m3))
print("Worst mark:", min(m1, m2, m3))
