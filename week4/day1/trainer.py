from week4.day1.employee import Employee


class Trainer(Employee):

    def __init__(self, name, salary):
        Employee.__init__(self, name, salary)
        # super().__init__(name, salary)
        self.overtime = 0

    def get_total_salary(self):
        return self.salary + self.salary / 30 / 8 * self.overtime

    def __str__(self):
        return f"Trainer: {self.name}"
