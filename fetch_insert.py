import requests
import sqlite3
import random
import string

# Function to generate a random alphanumeric ID
def generate_id():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=8))

# Fetch user data from API
def fetch_and_insert():
    response = requests.get("https://randomuser.me/api")  # Fetch data
    if response.status_code == 200:
        data = response.json()["results"][0]  # Extract user data

        # Extract required fields
        user_id = generate_id()
        name = f"{data['name']['first']} {data['name']['last']}"
        email = data["email"]
        dob = data["dob"]["date"].split("T")[0]  # Extract only the date
        gender = data["gender"]
        picture = data["picture"]["large"]

        # Insert into database
        conn = sqlite3.connect("users.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (id, name, email, dob, gender, picture) VALUES (?, ?, ?, ?, ?, ?)",
                       (user_id, name, email, dob, gender, picture))
        conn.commit()
        conn.close()

        print(f"User {name} inserted successfully!")
    else:
        print("Failed to fetch data.")

# Run the function
fetch_and_insert()
