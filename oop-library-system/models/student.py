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

    def return_book(self, book):
        if self.books_borrowed.count(book) == 1:
            book.borrowed = False
            self.books_borrowed.remove(book)
            return True
        else:
            return False
