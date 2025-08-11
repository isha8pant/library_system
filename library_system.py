import mysql.connector

# Connect to MySQL
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="isha123",  # replace with your MySQL password
    database="library"
)
cursor = connection.cursor()

def add_book():
    title = input("Enter book title: ")
    author = input("Enter author name: ")
    year = input("Enter year of publication: ")

    query = "INSERT INTO books (title, author, year) VALUES (%s, %s, %s)"
    cursor.execute(query, (title, author, year))
    connection.commit()
    print("✅ Book added successfully!")

def view_books():
    cursor.execute("SELECT * FROM books")
    rows = cursor.fetchall()
    print("\n--- Library Books ---")
    for row in rows:
        print(row)

def delete_book():
    book_id = input("Enter book ID to delete: ")
    query = "DELETE FROM books WHERE id = %s"
    cursor.execute(query, (book_id,))
    connection.commit()
    print("🗑 Book deleted successfully!")

while True:
    print("\n===== 📚 Library Management System =====")
    print("1. Add Book")
    print("2. View Books")
    print("3. Delete Book")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_book()
    elif choice == "2":
        view_books()
    elif choice == "3":
        delete_book()
    elif choice == "4":
        break
    else:
        print("❌ Invalid choice! Please try again.")

cursor.close()
connection.close()
