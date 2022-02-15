
salary = eval(input("Enter your salary: "))
annual_salary = salary * 12
print("Annual Salary:", annual_salary, "SAR")

if salary > 12000:
    print("High Salary")
elif salary > 6000:
    print("Normal Salary")
elif salary > 3000:
    print("Low Salary")
else:
    print("Very Low Salary")

