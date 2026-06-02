import sqlite3

conn = sqlite3.connect("finance.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM income")

rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()

