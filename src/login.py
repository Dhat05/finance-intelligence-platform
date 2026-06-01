import sqlite3

username = input("Enter username: ")

conn = sqlite3.connect("finance.db")
cursor = conn.cursor()

cursor.execute(
    "SELECT * FROM users WHERE username=?",
    (username,)
)

user = cursor.fetchone()

if user:
    print("Login Successful!")
else:
    print("User Not Found!")

conn.close()
