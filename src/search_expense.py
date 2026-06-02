import sqlite3

conn = sqlite3.connect("finance.db")
cursor = conn.cursor()

category = input("Enter category to search: ")

cursor.execute(
    "SELECT * FROM expenses WHERE category = ?",
    (category,)
)

rows = cursor.fetchall()

if rows:
    print("\nExpenses Found:\n")
    for row in rows:
        print(row)
else:
    print("No expenses found.")

conn.close()
