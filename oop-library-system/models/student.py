from colorama import Fore, Style


class Student:
    def __init__(self, student_id, name, email):
        self.student_id = student_id
        self.name = name
        self.email = email
        self.books_borrowed = []

    def borrow_book(self, book):
        if book.borrow(self.student_id):
            self.books_borrowed.append(book.id)
            return True
        else:
            return False

    def return_book(self, book_id, library):
        if self.books_borrowed.count(book_id) == 1:
            for book in self.books_borrowed:
                book = library.get_book(book_id)
                book.borrowed = False
                self.books_borrowed.remove(book_id)
                return True
        else:
            return False

    def borrowed_list(self, library):
        book_counter = 1
        for book_id in self.books_borrowed:
            book = library.get_book(book_id)
            if book == None:
                return None
            print(
                f"{book_counter}) {Fore.LIGHTCYAN_EX}'{book.title}' {Style.RESET_ALL} - by {book.author}\n"
            )
            book_counter += 1
