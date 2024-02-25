import sqlite3
from book import Book

class Library:
    def __init__(self, db_name="library.db"):
        self.db_name = db_name
        self.connection = None
        try:
            self.connection = sqlite3.connect(self.db_name)
            self.create_table()
        except sqlite3.Error as e:
            print(f"Error connecting to database: {e}")

    def __del__(self):
        if self.connection:
            self.connection.close()

    def create_table(self):
        try:
            query = '''CREATE TABLE IF NOT EXISTS books (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            title TEXT,
                            author TEXT,
                            quantity INTEGER,
                            available_quantity INTEGER
                        )'''
            self.connection.execute(query)
            self.connection.commit()
        except sqlite3.Error as e:
            print(f"Error creating table: {e}")

    def add_books(self, title, author, quantity=1):
        try:
            query = '''INSERT INTO books(title, author, quantity, available_quantity)
                        VALUES (?, ?, ?, ?)'''
            self.connection.execute(query, (title, author, quantity, quantity))
            self.connection.commit()
        except sqlite3.Error as e:
            print(f"Error adding books: {e}")

    def display_books(self):
        try:
            query = "SELECT title, author, quantity, available_quantity FROM books"
            cursor = self.connection.execute(query)
            print("Available Books:")
            for row in cursor:
                title, author, quantity, available_quantity = row
                print(f"{title} by {author} - Available: {available_quantity}/{quantity}")
        except sqlite3.Error as e:
            print(f"Error loading books: {e}")
            
    def borrow_books(self, title):
        try:
            query = "SELECT id, available_quantity FROM books WHERE title = ?"
            cursor = self.connection.execute(query,(title,))
            row = cursor.fetchone()
            if row:
                book_id, available_quantity = row
                if available_quantity > 0:
                    available_quantity -= 1
                    query = "UPDATE books SET available_quantity = ? WHERE id = ?"
                    self.connection.execute(query, (available_quantity, book_id))
                    self.connection.commit()
                    print(f"You have borrowed {title}")
                else:
                    print("Sorry, the book is not available.")
            else:
                print("Sorry, the book doesn't exist.")
        except sqlite3.Error as e:
            print(f"Error borrowing books: {e}")

    def return_books(self, title):
        try:
            query = "SELECT id, available_quantity, quantity FROM books WHERE title = ?"
            cursor = self.connection.execute(query,(title,))
            row = cursor.fetchone()
            if row:
                book_id, available_quantity, total_quantity = row
                if available_quantity < total_quantity:
                    available_quantity += 1
                    query = "UPDATE books SET available_quantity = ? WHERE id = ?"
                    self.connection.execute(query, (available_quantity,book_id))
                    self.connection.commit()
                    print(f"Thank you for returning {title}")
                else:
                    print("This book was not borrowed from this library.")
            else:
                print("Sorry, the book doesn't exist.")
        except sqlite3.Error as e:
            print(f"Error returning books: {e}")