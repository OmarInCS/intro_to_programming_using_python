import os
from sqlite3 import connect


class Department:

    def __init__(self, dept_id, dept_name, loc_id):
        self.dept_id = dept_id
        self.dept_name = dept_name
        self.loc_id = loc_id

    def __repr__(self):
        return self.dept_name

    @staticmethod
    def get_all_depts():
        basedir = os.path.abspath(os.path.dirname(__file__))
        with connect(f"{basedir}\\hr.db") as conn:
            cur = conn.cursor()
            sql = "SELECT * FROM departments"
            result = cur.execute(sql).fetchall()
            result = [Department(*row) for row in result]

            return result

    def save_to_db(self):
        basedir = os.path.abspath(os.path.dirname(__file__))
        with connect(f"{basedir}\\hr.db") as conn:
            cur = conn.cursor()
            sql = "INSERT INTO departments VALUES (:dept_id, :dept_name, :loc_id)"
            cur.execute(sql, self.__dict__)
            conn.commit()

    def delete_from_db(self):
        basedir = os.path.abspath(os.path.dirname(__file__))
        with connect(f"{basedir}\\hr.db") as conn:
            cur = conn.cursor()
            sql = "DELETE FROM departments WHERE department_id = :dept_id"
            cur.execute(sql, self.__dict__)
            conn.commit()