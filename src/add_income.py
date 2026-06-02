import sqlite3

conn = sqlite3.connect("finance.db")
cursor = conn.cursor()

user_id = int(input("Enter User ID: "))
amount = float(input("Enter Income Amount: "))

cursor.execute(
    "INSERT INTO income (user_id, amount) VALUES (?, ?)",
    (user_id, amount)
)

conn.commit()

print("Income added successfully!")

conn.close()
