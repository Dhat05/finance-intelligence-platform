import sqlite3

conn = sqlite3.connect("finance.db")
cursor = conn.cursor()

user_id = int(input("Enter User ID: "))
amount = float(input("Enter Expense Amount: "))
category = input("Enter Category: ")

cursor.execute(
    "INSERT INTO expenses (user_id, amount, category) VALUES (?, ?, ?)",
    (user_id, amount, category)
)

conn.commit()

print("Expense added successfully!")

conn.close()
