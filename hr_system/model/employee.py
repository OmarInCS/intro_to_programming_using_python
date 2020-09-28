from sqlite3 import connect


class Employee:

    def __init__(self, emp_id, emp_name, email, hire_date, job_id, salary, dept_id):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.email = email
        self.hire_date = hire_date
        self.job_id = job_id
        self.salary = salary
        self.dept_id = dept_id

    def __repr__(self):
        return self.emp_name

    @staticmethod
    def get_all_emps():
        db_path = "C:\\Users\\OmarKarem\\SemicolonGD\\Python\\intro_to_python_programming\\week4\\day4\\hr.db"

        with connect(db_path) as conn:
            cur = conn.cursor()
            command = "select employee_id, last_name, email, hire_date, job_id, salary, department_id from employees"
            result = cur.execute(command).fetchall()
            result = [Employee(*row) for row in result]

            return result

    def save_to_db(self):
        db_path = "C:\\Users\\OmarKarem\\SemicolonGD\\Python\\intro_to_python_programming\\week4\\day4\\hr.db"

        with connect(db_path) as conn:
            cur = conn.cursor()
            command = "insert into employees (employee_id, last_name, email, hire_date, job_id, salary, department_id) " \
                      "values (:emp_id, :emp_name, :email, :hire_date, :job_id, :salary, :dept_id)"
            cur.execute(command, self.__dict__)

            conn.commit()

    def delete_from_db(self):
        db_path = "C:\\Users\\OmarKarem\\SemicolonGD\\Python\\intro_to_python_programming\\week4\\day4\\hr.db"

        with connect(db_path) as conn:
            cur = conn.cursor()
            command = "delete from employees where employee_id = :emp_id"
            cur.execute(command, self.__dict__)

            conn.commit()