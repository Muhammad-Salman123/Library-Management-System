# Library Management System

class Library:
    """A simple Library class to manage books."""

    def __init__(self, name: str):
        """Initialize the library with a name and an empty book list."""
        self.name = name
        self.books = []

    def display_books(self):
        """Display all available books in the library."""
        if not self.books:
            print("\nNo books available in the library.\n")
        else:
            print(f"\nBooks available in {self.name}:")
            for i, book in enumerate(self.books, 1):
                print(f"{i}. {book}")
            print()

    def add_book(self, book: str):
        """Add a book to the library."""
        self.books.append(book)
        print(f"\n'{book}' has been added to the library.\n")

    def borrow_book(self, book: str):
        """Borrow a book if it exists, otherwise show a message."""
        if book in self.books:
            self.books.remove(book)
            print(f"\nYou have borrowed '{book}'. Please return it on time.\n")
        else:
            print(f"\nSorry, '{book}' is not available right now.\n")

    def return_book(self, book: str):
        """Return a book to the library."""
        self.books.append(book)
        print(f"\nThank you for returning '{book}'.\n")


def main():
    """Main program loop for the Library Management System."""
    library = Library("City Library")

    while True:
        print("===== Library Management System =====")
        print("1. Display available books")
        print("2. Add a book")
        print("3. Borrow a book")
        print("4. Return a book")
        print("5. Exit")

        try:
            choice = int(input("Enter your choice (1-5): "))
        except ValueError:
            print("\nInvalid input! Please enter a number.\n")
            continue

        if choice == 1:
            library.display_books()
        elif choice == 2:
            book = input("Enter the book name to add: ").strip()
            if book:
                library.add_book(book)
            else:
                print("\nBook name cannot be empty.\n")
        elif choice == 3:
            book = input("Enter the book name to borrow: ").strip()
            if book:
                library.borrow_book(book)
            else:
                print("\nBook name cannot be empty.\n")
        elif choice == 4:
            book = input("Enter the book name to return: ").strip()
            if book:
                library.return_book(book)
            else:
                print("\nBook name cannot be empty.\n")
        elif choice == 5:
            print("\nThank you for using the Library Management System. Goodbye!\n")
            break
        else:
            print("\nInvalid choice! Please select between 1-5.\n")


if __name__ == "__main__":
    main()