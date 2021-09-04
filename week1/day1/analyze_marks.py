
m1, m2, m3 = eval(input("Enter three marks: "))

avg = (m1 + m2 + m3) / 3

print("The Average:", round(avg, 2))
print("The Best:", max(m1, m2, m3))
print("The Worst:", min(m1, m2, m3))
