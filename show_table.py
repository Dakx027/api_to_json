from prettytable import PrettyTable
import sqlite3
from datetime import datetime

# Function to display data in table format
def show_records():
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users ORDER BY dob")  # Sort by DOB
    records = cursor.fetchall()
    conn.close()

    table = PrettyTable(["ID", "Name", "Email", "DOB", "Age", "Gender", "Picture"])
    total_records = len(records)

    for record in records:
        user_id, name, email, dob, gender, picture = record
        age = datetime.now().year - int(dob.split("-")[0])  # Calculate age
        table.add_row([user_id, name, email, dob, age, gender, picture])

    print(table)
    print(f"\nTotal Records: {total_records}")

# Run the function
show_records()

