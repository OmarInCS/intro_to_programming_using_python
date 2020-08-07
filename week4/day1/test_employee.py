
from week4.day1.employee import Employee

e1 = Employee("Khaled", 5000, 2018)
e2 = Employee("Ahmed", 8000, 2018)
e3 = Employee("Eslam", 4000, 2015)

print("Annual Salary", e1.get_annual_salary())
print("Reward:", e1.calculate_reward())