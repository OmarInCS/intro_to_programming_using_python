
n1, n2, n3 = eval(input("Enter three numbers: "))

print("The best: ", max(n1, n2, n3))
print("The worest: ", min(n1, n2, n3))
avg = (n1 + n2 + n3) / 3

print("The Average: ", round(avg, 2))