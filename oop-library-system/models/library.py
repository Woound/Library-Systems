from colorama import Fore, Style


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

    def get_book(self, id):
        for book in self.books:
            if book.id == id:
                return book

    def get_all_books(self):
        return self.books

    def get_available_book(self, index):
        available_books = self.available_books()
        return available_books[index]

    def get_students(self):
        return self.students

    def available_books(self):
        available_books = []
        for book in self.books:
            if not book.is_borrowed():
                available_books.append(book)
        return available_books

    def display_books(self):
        book_counter = 1
        for book in self.available_books():
            print(
                f"{book_counter}) {Fore.LIGHTCYAN_EX}'{book.title}' {Style.RESET_ALL} - by {book.author}\n"
            )
            book_counter += 1
