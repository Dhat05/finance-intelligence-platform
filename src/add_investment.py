import sqlite3

conn = sqlite3.connect("finance.db")
cursor = conn.cursor()

user_id = int(input("Enter User ID: "))
investment_type = input("Enter Investment Type: ")
amount = float(input("Enter Investment Amount: "))

cursor.execute(
    "INSERT INTO investments (user_id, investment_type, amount) VALUES (?, ?, ?)",
    (user_id, investment_type, amount)
)

conn.commit()

print("Investment added successfully!")

conn.close()
