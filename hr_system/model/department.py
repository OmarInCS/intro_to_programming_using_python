from sqlite3 import connect


class Department:

    def __init__(self, dept_id, dept_name, loc_id):
        self.dept_id = dept_id
        self.dept_name = dept_name
        self.loc_id = loc_id

    def __str__(self):
        return self.dept_name

    @staticmethod
    def get_all_depts():
        with connect("C:\\sqlite\\db\\hr.db") as conn:
            cur = conn.cursor()
            stat = "select * from departments"
            data = cur.execute(stat).fetchall()
            data = [Department(*row) for row in data]
            return data

    def save_to_db(self):
        with connect("C:\\sqlite\\db\\hr.db") as conn:
            cur = conn.cursor()
            stat = "insert into departments values (:dept_id, :dept_name, :loc_id)"
            cur.execute(stat, self.__dict__)
            conn.commit()

    def delete_from_db(self):
        with connect("C:\\sqlite\\db\\hr.db") as conn:
            cur = conn.cursor()
            stat = "delete from departments where department_id = :dept_id"
            cur.execute(stat, self.__dict__)
            conn.commit()

