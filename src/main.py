from library import Library

def main():
    library = Library()

    while True:
        print("\nWelcome to the Online Library System")
        print("1. Add a Book")
        print("2. Display Available Books")
        print("3. Borrow a Book")
        print("4. Return a Book")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter author name: ")
            quantity = int(input("Enter quantity of books: "))
            library.add_books(title, author, quantity)
            print("Book(s) added successfully!")

        elif choice == '2':
            library.display_books()

        elif choice == '3':
            title = input("Enter the title of the book you want to borrow: ")
            library.borrow_books(title)

        elif choice == '4':
            title = input("Enter the title of the book you want to return: ")
            library.return_books(title)

        elif choice == '5':
            print("Thank you for using the online Library System. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()