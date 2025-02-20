import sqlite3

# Connect to SQLite database (creates file if not exists)
conn = sqlite3.connect("users.db")
cursor = conn.cursor()

# Create table for storing user data
cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                    id TEXT PRIMARY KEY,
                    name TEXT,
                    email TEXT,
                    dob TEXT,
                    gender TEXT,
                    picture TEXT
                )''')

conn.commit()
conn.close()
print("Database and table setup completed.")
