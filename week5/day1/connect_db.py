
from sqlite3 import connect

from week5.day1.department import Department

db_path = "C:\\Users\\OmarKarem\\SemicolonGD\\Python\\intro_to_python_programming\\week5\\day1\\hr.db"

with connect(db_path) as conn:
    cur = conn.cursor()
    sql = "select * from departments"
    result = cur.execute(sql).fetchall()
    result = [Department(*row) for row in result]
    print(result)
