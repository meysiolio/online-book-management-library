from book import Book

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author):
        book = Book(title, author)
        self.books.append(book)

    def display_books(self):
        print("Available Books:")
        for book in self.books:
            if book.available:
                print(f"{book.title} by {book.author}")

    def borrow_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower() and book.available:
                book.available = False
                print(f"You have borrowed {book.title}")
                return
        print("Sorry, the book is either not availale or doesn't exist.")

    def return_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower() and not book.available:
                book.available = True
                print(f"Thank you for returning {book.title}")
                return
        print("This book was not borrowed from this library.")