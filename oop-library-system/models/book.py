class Book:
    def __init__(self, id, title, author, publisher):
        self.title = title
        self.id = id
        self.author = author
        self.publisher = publisher
        self.borrowed = False
        self.borrower = None

    def is_borrowed(self):
        return self.borrowed

    def borrow(self, studentID):
        if not self.borrowed:
            self.borrowed = True
            self.borrower = studentID
            return True
        else:
            return False

    def info(self):
        info_message = f"Book name: {self.title}\nAuthor: {self.author}\nPublisher: {self.publisher}\nAvailable to borrow: {not self.borrowed}"
        return info_message
