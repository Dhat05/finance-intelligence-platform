import sqlite3

conn = sqlite3.connect("finance.db")
cursor = conn.cursor()

cursor.execute(
    "SELECT amount, category FROM expenses ORDER BY amount DESC"
)

rows = cursor.fetchall()

print("\nTop Expenses:\n")

for row in rows:
    print(row)

conn.close()
