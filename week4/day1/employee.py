
class Employee:

    def __init__(self, name, salary, hire_year):
        self.name = name
        self.salary = salary
        self.hire_year = hire_year

    def get_annual_salary(self):
        return self.salary * 12

    def get_service_period(self):
        return 2020 - self.hire_year

    def calculate_reward(self):
        return self.get_service_period() * self.get_annual_salary() / 2