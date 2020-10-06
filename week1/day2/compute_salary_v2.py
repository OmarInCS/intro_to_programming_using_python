
salary = eval(input("Enter ur salary: "))
annual_salary = salary * 12
print("Annual Salary:", annual_salary)

if salary > 12000:
    print("High Salary")
elif salary > 4000:
    print("Normal Salary")
else:
    print("Low Salary")
