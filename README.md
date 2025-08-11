# 📚 Library Management System (Python + MySQL)

A simple **Library Management System** built using **Python** and **MySQL**, allowing you to:
- Add new books
- View all books
- Delete books from the library

---

## 🚀 Features
- **Add Book** → Save book details (Title, Author, Year) in MySQL
- **View Books** → Display all stored books in a tabular format
- **Delete Book** → Remove books by their ID
- Interactive menu for easy navigation

---

## 🛠️ Tech Stack
- **Python 3**
- **MySQL**
- **mysql-connector-python** library

---

## 📦 Installation & Setup

1. **Clone this repository**
```bash
git clone https://github.com/YourUsername/library_system.git
cd library_system
**install dependencies**
pip install mysql-connector-python
**setup mysql database**
CREATE DATABASE library;
USE library;

CREATE TABLE books (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    author VARCHAR(255) NOT NULL,
    year INT
);
**run the program**
python library_system.py
**license**
This project is licensed under the MIT License - see the https://chatgpt.com/c/LICENSE file for details.
