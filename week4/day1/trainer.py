from week4.day1.employee import Employee


class Trainer(Employee):

    def __init__(self, emp_id, emp_name, salary):
        Employee.__init__(self, emp_id, emp_name, salary)
        self.overtime = 0

    def get_total_salary(self):
        return self.salary + self.overtime
