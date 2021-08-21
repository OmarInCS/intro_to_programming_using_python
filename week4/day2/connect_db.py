
from sqlite3 import connect
import os

from week4.day2.department import Department

db_path = os.getcwd() + "\\hr.db"
with connect(db_path) as conn:
    cur = conn.cursor()
    sql = "SELECT * FROM departments"
    cur.execute(sql)
    result = cur.fetchall()
    result = [Department(*row) for row in result]
    print(result)



