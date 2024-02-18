from book import Book

class Library:
    def __init__(self, filename="library.txt"):
        self.filename = filename
        self.books = self.load_books()

    def load_books(self):
        try:
            with open(self.filename, 'r') as file:
                books = []
                for line in file:
                    title, author, quantity, available_quantity = line.strip().split(',')
                    books.append(Book(title, author, int(quantity)))
                return books
        except FileNotFoundError:
            return []
        
    def save_books(self):
        with open(self.filename, 'w') as file:
            for book in self.books:
                file.write(f"{book.title},{book.author},{book.quantity},{book.available_quantity}\n")

    def add_books(self, title, author, quantity=1):
        for book in self.books:
            if book.title.lower() == title.lower() and book.author.lower() == author.lower():
                book.quantity += quantity
                book.available_quantity += quantity
                break
        else:
            self.books.append(Book(title, author, quantity))
        self.save_books()

    def display_books(self, filename="library.txt"):
        print("Available Books:")
        for book in self.books:
            print(f"{book.title} by {book.author} - Available: {book.available_quantity}/{book.quantity}")

    def borrow_books(self, title):
        for book in self.books:
            if book.title.lower() == title.lower() and book.available_quantity > 0:
                book.available_quantity -= 1
                self.save_books()
                print(f"You have borrowed {book.title}")
                return
        print("Sorry, the book is either not availale or doesn't exist.")

    def return_books(self, title):
        for book in self.books:
            if book.title.lower() == title.lower() and book.available_quantity < book.quantity:
                book.available_quantity += 1
                self.save_books()
                print(f"Thank you for returning {book.title}")
                return
        print("This book was not borrowed from this library.")