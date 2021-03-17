import os
from sqlite3.dbapi2 import connect

from hr_system.model.department import Department

db_path = os.getcwd() + "\\hr.db"
with connect(db_path) as conn:
    cur = conn.cursor()
    sql = "SELECT * FROM departments"
    result = cur.execute(sql).fetchall()
    result = [Department(*row) for row in result]
    print(result)
