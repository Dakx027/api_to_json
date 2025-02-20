import json
import sqlite3

# Connect to database
conn = sqlite3.connect("users.db")
cursor = conn.cursor()

# Fetch all records
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()

# Convert to JSON format
columns = [desc[0] for desc in cursor.description]
data = [dict(zip(columns, row)) for row in rows]

# Add total rows count
data_json = {"records": data, "totalRows": len(rows)}

# Print the JSON output
print(json.dumps(data_json, indent=4))

# Close the connection
conn.close()
