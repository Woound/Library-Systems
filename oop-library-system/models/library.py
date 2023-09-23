class Library:
    def __init__(self):
        self.books = []  # List of Book objects
        self.students = []

    def add_book(self, book):
        self.books.append(book)

    def add_books(self, books):
        for book in books:
            self.books.append(book)

    def add_student(self, student):
        self.students.append(student)

    def add_students(self, students):
        for student in students:
            self.students.append(student)

    def get_book(self, index):
        return self.books[index]

    def get_students(self):
        return self.students

    def display_books(self):
        for idx, book in enumerate(self.books, start=1):
            # Only displaying the books that are currently available to borrow, to avoid clutter.
            if not book.is_borrowed():
                print(
                    f'{idx}. {book.title} by {book.author} - {"Available" if not book.is_borrowed() else "Borrowed"}'
                )
