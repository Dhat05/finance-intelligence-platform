import sqlite3

conn = sqlite3.connect("finance.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    email TEXT NOT NULL
)
""")

username = input("Enter username: ")
email = input("Enter email: ")

cursor.execute(
    "INSERT INTO users (username, email) VALUES (?, ?)",
    (username, email)
)

conn.commit()

print("User added successfully!")

conn.close()
