
from sqlite3 import connect

from week4.day3.department import Department

db_path = "C:\\Users\\OmarKarem\\SemicolonGD\\Python\\Group20210207\\week4\\day3\\hr.db"
with connect(db_path) as conn:
    cur = conn.cursor()
    sql = "SELECT * FROM departments"
    result = cur.execute(sql).fetchall()
    result = [Department(*row) for row in result]
    print(result)
