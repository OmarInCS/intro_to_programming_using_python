
class Employee:

    def __init__(self, emp_id, emp_name, salary):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.salary = salary

    def get_total_salary(self) -> int:
        pass

    def get_annual_salary(self):
        return self.get_total_salary() * 12
