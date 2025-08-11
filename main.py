import mysql.connector

# Connect to MySQL
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="isha123",  # Replace with your MySQL root password
    database="library_db"
)

cursor = connection.cursor()

print("✅ Connected to MySQL successfully!")

# Example: Show all books
cursor.execute("SELECT * FROM books")
for row in cursor.fetchall():
    print(row)

# Close connection
cursor.close()
connection.close()
