
from sqlite3 import connect

from week4.day4.department import Department

db_path = "C:\\Users\\OmarKarem\\SemicolonGD\\Python\\intro_to_python_programming\\week4\\day4\\hr.db"

with connect(db_path) as conn:
    cur = conn.cursor()
    command = "select * from departments"
    result = cur.execute(command).fetchall()
    result = [Department(*row) for row in result]
    print(result)
