from week4.day4.employee import Employee


class Trainer(Employee):

    def __init__(self, emp_id, emp_name, salary, overtime):
        Employee.__init__(self, emp_id, emp_name, salary)
        self.overtime = overtime

    def get_total_salary(self):
        return self.salary + self.overtime

