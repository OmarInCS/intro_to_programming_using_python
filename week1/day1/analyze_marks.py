
m1, m2, m3 = eval(input("Enter three marks: "))

avg = (m1 + m2 + m3) / 3

print("Average mark:", round(avg, 2))
print("The Best mark:", max(m1, m2, m3))
print("The Worst mark:", min(m1, m2, m3))
