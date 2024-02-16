from book import Book

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author, quantity=1):
        book = Book(title, author, quantity)
        self.books.append(book)

    def display_books(self):
        print("Available Books:")
        for book in self.books:
            print(f"{book.title} by {book.author} - Available: {book.available_quantity}/{book.quantity}")

    def borrow_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower() and book.available_quantity > 0:
                book.available_quantity -= 1
                print(f"You have borrowed {book.title}")
                return
        print("Sorry, the book is either not availale or doesn't exist.")

    def return_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower() and book.available_quantity < book.quantity:
                book.available_quantity += 1
                print(f"Thank you for returning {book.title}")
                return
        print("This book was not borrowed from this library.")