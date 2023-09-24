import time
from colorama import Fore, Style

from models.book import Book
from models.student import Student
from models.library import Library

library = Library()


def setup():
    student1 = Student(1, "Alice", "alicewonderland@gmail.com")
    student2 = Student(2, "Bob", "bob@gmail.com")

    book1 = Book(1, "1984", "George Orwell", "Penguin")
    book2 = Book(2, "To Kill a Mockingbird", "Harper Lee", "HarperCollins")
    book3 = Book(3, "Pride and Prejudice", "Jane Austen", "Chiltern Publishing Limited")
    book4 = Book(4, "The Catcher in the Rye", "J.D. Salinger", "Little, Brown")

    books = [book1, book2, book3, book4]
    students = [student1, student2]

    library.add_books(books)
    library.add_students(students)


# Set up outside of main to prevent duplicates.
setup()


def main():
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

    # Returning process
    elif user_choice == "2":
        handle_return_book()

    # Looking-up process
    elif user_choice == "3":
        handle_find_book()


def handle_borrow_book():
    print(
        f"\n{Fore.MAGENTA}These are the books you can currently borrow:{Style.RESET_ALL}\n"
    )

    # Display the list of books available in the library
    library.display_books()

    while True:
        # Try-catch block in case user attempts to enter a value other than an integer.
        try:
            book_choice = input(
                "\nPlease enter the index of the book you would like to borrow: "
            )
            if 0 < int(book_choice) <= len(library.available_books()):
                students = library.get_students()
                student_id = input("Enter your student id: ")
                student_email = input("Enter your student email to confirm: ")
                for student in students:
                    if (
                        student.student_id == int(student_id)
                        and student.email == student_email
                    ):
                        book = library.get_available_book(int(book_choice) - 1)
                        student.borrow_book(book)
                        # print(f"\n{book.info()}\n")
                        time.sleep(2)
                        print(
                            f"\n{Fore.LIGHTYELLOW_EX}Succesfully borrowed! Redirecting to the main menu...{Style.RESET_ALL}"
                        )
                        # print(student.books_borrowed)
                        time.sleep(3)
                        # Redirecting to main menu
                        main()
                print(
                    f"\n{Fore.RED}Invalid! Student not found, please try again.{Style.RESET_ALL}"
                )
                break
            else:
                print(
                    f"\n{Fore.RED}Option does not exist, please check again.{Style.RESET_ALL}"
                )
                continue

        except ValueError:
            print(
                f"\n{Fore.RED}Invalid value, please enter an integer!{Style.RESET_ALL}"
            )


def handle_return_book():
    time.sleep(2)
    students = library.get_students()
    while True:
        try:
            student_id = input("Enter your student id: ")
            student_email = input("Enter your student email to confirm: ")
            time.sleep(2)

            print(
                f"{Fore.LIGHTGREEN_EX}\nList of your borrowed books: {Style.RESET_ALL}"
            )
            for student in students:
                if (
                    student.student_id == int(student_id)
                    and student.email == student_email
                ):
                    student.borrowed_list(library)
                    book_to_return = input(
                        "Enter the index of the book you would like to return: "
                    )
                    if student.books_borrowed.count(int(book_to_return)) == 1:
                        if student.return_book(int(book_to_return), library):
                            time.sleep(2)
                            print(
                                f"\n{Fore.LIGHTMAGENTA_EX}Your book has succesfully been returned. Thank you!{Style.RESET_ALL}"
                            )
                            time.sleep(1)
                            main()
                    else:
                        print(
                            f"{Fore.RED}Incorrect option, or, you do not own this book.{Style.RESET_ALL}"
                        )
                    break

        except ValueError:
            print(
                f"\n{Fore.RED}Invalid value, please enter an integer!{Style.RESET_ALL}"
            )


def handle_find_book():
    books = library.get_all_books()
    found = False
    while True:
        try:
            book_to_find = input(
                "Please enter the name of the book you would like to find: "
            )
            time.sleep(1)
            for book in books:
                if book.title.lower() == book_to_find.lower():
                    found = True
                    print(f"\n{Fore.YELLOW}Book Details:{Style.RESET_ALL}")
                    print(f"\n{Fore.LIGHTGREEN_EX}{book.info()}{Style.RESET_ALL}")
                    time.sleep(2)
                    carry_on = input("\nWould you like to find another book? (y/n): ")
                    if carry_on.lower() == "y":
                        break
                    else:
                        time.sleep(1)
                        print(
                            f"{Fore.LIGHTBLUE_EX}Redirecting to main menu...{Style.RESET_ALL}"
                        )
                        time.sleep(2)
                        main()
            if not found:
                time.sleep(1)
                print(f"\n{Fore.RED}Book not found, please try again.{Style.RESET_ALL}")
        except ValueError:
            print(f"\n{Fore.RED}Invalid value!{Style.RESET_ALL}")


if __name__ == "__main__":
    main()
