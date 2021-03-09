from sqlite3.dbapi2 import connect
import os
from week4.day3.department import Department

db_path = f"{os.getcwd()}\\hr.db"

with connect(db_path) as conn:
    cur = conn.cursor()
    sql = "SELECT * FROM departments"
    result = cur.execute(sql).fetchall()
    result = [Department(*row) for row in result]
    print(result)
