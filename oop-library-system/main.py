import time
from colorama import Fore, Style

from models.book import Book
from models.student import Student
from models.library import Library

library = Library()


def setup():
    student1 = Student(1, "Alice", "alicewonderland@gmail.com")
    student2 = Student(2, "Bob", "bobthebuilder@gmail.com")

    book1 = Book(1, "1984", "George Orwell", "Penguin")
    book2 = Book(2, "To Kill a Mockingbird", "Harper Lee", "HarperCollins")
    book3 = Book(3, "Pride and Prejudice", "Jane Austen", "Chiltern Publishing Limited")
    book4 = Book(4, "The Catcher in the Rye", "J.D. Salinger", "Little, Brown")

    books = [book1, book2, book3, book4]

    library.add_books(books)


def main():
    setup()
    user_choice = ""
    options = ["Borrow a book", "Return a book", "Find a book"]

    print(f"\n{Fore.GREEN}Welcome to the Student Library!{Style.RESET_ALL}\n")
    time.sleep(1)

    input_message = "What would you like to do?\n"

    for index, option in enumerate(options):
        input_message += f"{index+1}) {option}\n"

    # Starts a while loop that continues as long as the user's choice is not one of the valid choices.
    while user_choice not in map(str, range(1, len(options) + 1)):
        user_choice = input(input_message)

    # Borrowing process
    if user_choice == "1":
        time.sleep(2)
        handle_borrow_book()

    # # Returning process
    # elif user_choice == "2":
    #     handle_return_book()

    # # Looking-up process
    # elif user_choice == "3":
    #     handle_find_book()


def handle_borrow_book():
    print(
        f"\n{Fore.MAGENTA}These are the books you can currently borrow:{Style.RESET_ALL}"
    )
    library.display_books()

    while True:
        book_choice = input(
            "\nPlease enter the index of the book you would like to order: "
        )
        if 0 < int(book_choice) <= len(library.books):
            print("Good")
            break


if __name__ == "__main__":
    main()
