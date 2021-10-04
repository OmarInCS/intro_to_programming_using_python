
class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_annual_salary(self):
        return self.salary * 12
