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
        db_path = "D:\\Abadnet\\Python\\Group20220109\\week5\\day1\\hr.db"
        with connect(db_path) as conn:
            cur = conn.cursor()
            sql = "SELECT * FROM departments"
            result = cur.execute(sql).fetchall()
            result = [Department(*row) for row in result]
            return result
