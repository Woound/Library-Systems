class Library:
    def __init__(self):
        self.books = []  # List of Book objects

    def add_book(self, book):
        self.books.append(book)

    def add_books(self, books):
        for book in books:
            self.books.append(book)

    def display_books(self):
        for idx, book in enumerate(self.books, start=1):
            print(
                f'{idx}. {book.title} by {book.author} - {"Available" if not book.is_borrowed() else "Borrowed"}'
            )
