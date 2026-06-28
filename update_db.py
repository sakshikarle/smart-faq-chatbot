import sqlite3

conn = sqlite3.connect("chatbot.db")
cur = conn.cursor()

try:
    cur.execute("ALTER TABLE chat_history ADD COLUMN time TEXT")
    conn.commit()
    print("Time column added successfully!")
except Exception as e:
    print(e)

conn.close()