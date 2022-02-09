from sqlite3 import connect

from week5.day1.department import Department

db_path = "D:\\Abadnet\\Python\\Group20220109\\week5\\day1\\hr.db"
with connect(db_path) as conn:
    cur = conn.cursor()
    sql = "SELECT * FROM departments"
    result = cur.execute(sql).fetchall()
    result = [Department(*row) for row in result]
    print(result)
